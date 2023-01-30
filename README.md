# slack-ml-audio

## Slack APIによるプログラミング　機械学習への応用編

Slack APIチュートリアル「NodeJSとSlack APIによるいまどきのネットワークプログラミング」の応用編として機械学習向けにアプリを公開する。

### 音声を認識する

音声ファイルをアップロードして、その内容をテキストとしてSlackに投稿する。

#### 必要なライブラリをインストールする

>$ pip install -r requirements.txt

#### 環境変数を設定する

- ファイルenv.tpl内のSLACK_BOT_TOKEN、SLACK_APP_TOKEN、SLACK_USER_TOKENに該当するトークン文字列を設定する
- env.tplをenv.batに名前を変え、バッチを実行する
  >$ ren env.tpl env.bat
  >
  >$ env.bat

#### 音声ファイルからテキストを抽出する

- Google Speech Recognitionを用いて音声ファイルからテキストを抽出する
- 起動方法
  >$ python recognize_speech.py

- 音声データファイル（MP3あるいはWAV形式）をアップロードする
- Slack画面に音声の内容がテキストとして表示されることを確認する
