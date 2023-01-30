#!/usr/bin/env python
# coding: utf-8
#
# [FILE] extract.py
#
# [DESCRIPTION]
#   Google Speech Recognitionを使って音声ファイルからテキストを抽出する
#
# [NOTES]
#  必要なソフトウェア
#  $ pip install SpeechRecognition
#
import speech_recognition as sr

#
# [FUNCTION] extract_text()
#
# [DESCRIPTION]
#  WAV形式の音声ファイルからテキストを抽出する
#
# [INPUTS]
#  wav_file - WAV形式音声ファイル
#
# [OUTPUTS]
#   {error: <エラーメッセージ>, text: <認識されたテキスト>}
#
# [NOTES]
#
def extract_text(wav_file):
    output = {}
    output['error'] = ''
    output['text']  = ''

    # wav_fileが指定されていない場合
    if wav_file == None or wav_file == '':
        output['error'] = 'WAVファイルが指定されていません'
        return output
               
    # WAVファイルの内容を認識する
    r = sr.Recognizer()
    try:
        with sr.AudioFile(wav_file) as source:
            audio = r.record(source)
        text = r.recognize_google(audio, language='ja-JP')
        print(text)
        output['text'] = text
    except Exception as e:
        output['error'] = e
        print(e)

    return output

#
# END OF FILE
#