# slack-ml-audio

## Slack APIによるプログラミング　機械学習への応用編

Slack APIチュートリアル「NodeJSとSlack APIによるいまどきのネットワークプログラミング」の応用編として機械学習向けにアプリを公開する。

### 音声を認識する

音声ファイルをアップロードして、その内容をテキストとしてSlackに投稿する。

#### ffmpegを配置する

ffmpegは、動画や音声の変換、編集、ストリーミングなど、マルチメディア処理を行うためのオープンソースのソフトウェアであり、コマンドラインツールとして提供されている。

- ffmpeg公式サイト[https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)からWindowsアイコンをクリックし「Windows builds by BtbN」を選択する。
  - Windows向けの圧縮ファイルをダウンロードし、解凍する。
  - binフォルダーにあるffmpeg.exeとDLLファイル全てを本アプリのサブフォルダーspeechに配置する。

#### 必要なパッケージをインストールする

コマンドライン上で次のコマンドを起動し、依存するPythonパッケージをインストールする。

```bash
pip install -r requirements.txt
```

#### 環境変数を設定する

本アプリを起動するには環境変数の設定が必要である。env.tplファイルを環境変数設定ファイル.envとしてコピーし、以下の環境変数を定義する。

```bash
copy env.tpl .env
```

|  変数名  |  説明  |
| ---- | ---- |
|  SLACK_BOT_TOKEN  | Botユーザーとして関連付けられたトークン。対象Slackワークスペースのアプリ設定 > [OAuth & Permissions] > [Bot User OAuth Token]から取得する。xoxb-で始まる文字列。 |
|  SLACK_APP_TOKEN  | 全ての組織を横断できるアプリレベルトークン。対象Slackワークスペースのアプリ設定 > [Basic Information] > [App-Level Tokens]から取得する。xapp-で始まる文字列。 |
|  SLACK_USER_TOKEN  | アプリをインストールまたは認証したユーザーに成り代わってAPIを呼び出すことができるトークン。対象Slackワークスペースのアプリ設定 > [OAuth & Permissions] > [User OAuth Token]から取得する。xoxp-で始まる文字列。 |
|  LOCAL_FOLDER  | Slackにアップロードしたファイルを暫定的に保存するローカルフォルダーの名前 |

#### 音声ファイルからテキストを抽出する

- Google Speech Recognitionを用いて音声ファイルからテキストを抽出する
- 起動方法

```bash
python recognize_speech.py
```

- Slack入力欄の「＋」アイコンで、音声データファイル（MP3あるいはWAV形式）をアップロードする。
- Slack画面に音声の内容がテキストとして表示されることを確認する。

### 更新履歴

- 2025-06-16 dotenvを利用
- 2023-12-12 ffmpegの配置について記述
- 2023-02-01 初版
