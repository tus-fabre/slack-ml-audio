#!/usr/bin/env python
# coding: utf-8
#
# [FILE] recognize_speech.py
#
# [DESCRIPTION]
#  オーディオファイルからテキストを抽出するSlackアプリトップファイル
#
# [NOTES]
#  利用する音声認識技術はGoogle Speech Recognition
#  https://pypi.org/project/SpeechRecognition/
#

import os, sys
from pathlib import Path
import requests
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from speech.audio_util import convert_mp3
from speech.extract import extract_text

# BOTトークンからアプリを初期化する
bot_token = os.environ.get("SLACK_BOT_TOKEN")
if bot_token == None:
    print("環境変数が設定されていません")
    sys.exit()
app = App(token=bot_token)

# アプリトークン
app_token = os.environ["SLACK_APP_TOKEN"]
# ユーザートークン：ファイルの内容を取得するため用いる
user_token = os.environ.get("SLACK_USER_TOKEN")
# ローカルフォルダー
local_folder = os.environ.get("LOCAL_FOLDER")

#
# [EVENT] message
#
# [DESCRIPTION]
#  次のメッセージを受信したときのリスナー関数
#   Unhandled request ({'type': 'event_callback', 'event': {'type': 'message', 'subtype': 'file_share'}})
#
@app.event("message")
def handle_message_events(body, logger):
    logger.info(body)

#
# [EVENT] file_shared
#
# [DESCRIPTION]
#  ファイルを共有したときに起動するリスナー関数
#
# [NOTES]
#  対応可能なファイルタイプ：wav/mp3
#
@app.event("file_shared")
def file_shared(payload, client, ack, say):
    ack()
    
    # アップロードしたファイルのIDを取得する
    file_id = payload.get('file').get('id')
    
    # ファイル情報を取得する
    file_info = client.files_info(file = file_id).get('file')
    url = file_info.get('url_private')
    file_type = file_info.get('filetype')

    file_name = local_folder + "/" + file_info.get('title')
    mp3_path = None
    if file_type == 'mp3':
        mp3_path = file_name
        wav_path = file_name.replace(".mp3", ".wav")
    elif file_type == 'wav':
        wav_path = file_name
    else:
        say(f"サポートしていないファイル形式です： {file_type}")
        return

    # ファイルの内容を取得する
    resp = requests.get(url, headers={'Authorization': 'Bearer %s' % user_token})
    
    # ローカルフォルダーにファイルを一時的に保存する
    save_file = Path(file_name)
    save_file.write_bytes(resp.content)
    if mp3_path != None:
        print("[MP3 FILE] " + mp3_path)
    print("[WAV FILE] " + wav_path)

    # MP3形式からWAV形式に変換する
    converted = convert_mp3(mp3_path, wav_path)
    
    # WAVファイルから内容をテキストとして抽出する
    output = extract_text(wav_path)
    # ファイルからテキストを抽出できたら、メッセージ欄に送信する
    if output['error'] != '':
        say("ERROR: " + output['error'])
    elif output['text'] != '':
        say(output['text'])
    
    # ファイルを削除する
    if converted == True:
        os.remove(wav_path) 
    os.remove(file_name) 
   
#
# Start the Slack app
#
if __name__ == "__main__":
    print('⚡️Audio App starts...')
    SocketModeHandler(app, app_token).start()

#
# END OF FILE
#