#!/usr/bin/env python
# coding: utf-8
#
# [FILE] audio_util.py
#
# [DESCRIPTION]
#   音声ファイルに関するユーティリティ関数を定義する
#
# [NOTES]
#  必要なソフトウェア
#  ffmpeg - https://ffmpeg.org/からインストール
#
import subprocess

#
# [FUNCTION] convert_mp3()
#
# [DESCRIPTION]
#  MP3ファイルをWAVファイルに変換する
#
# [INPUTS]
#  mp3_file - MP3形式の入力音声ファイル名
#  wav_file - WAV形式の出力音声ファイル名
#
# [OUTPUTS]
#  true  - MP3からWAVへ変換された
#  false - MP3からWAVへ変換されなかった、MP3あるいはWAVファイルが指定されていない
#
# [NOTES]
#
def convert_mp3(mp3_file, wav_file):
    converted = False

    # mp3_fileが指定されていない場合
    if mp3_file == None or mp3_file == '':
        return converted
    
    # wav_fileが指定されていない場合
    if wav_file == None or wav_file == '':
        return converted
        
    # ffmpeg.exeを使ってMP3ファイルをWAVファイルに変換する
    if mp3_file != None:
        cmd = ["speech/ffmpeg.exe", "-i", mp3_file, wav_file]
        subprocess.call(cmd)
        converted = True

    return converted

#
# END OF FILE
#