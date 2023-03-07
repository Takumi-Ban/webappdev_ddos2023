## 環境構築
### venvによる仮想環境構築
```
## プロジェクトディレクトリの作成
## 任意のディレクトリ以下に作業ディレクトリを作成
$ mkdir [dirname]

## pyenvによるPythonのインストール
$ pyenv install 3.9.13 # 3.8以降ならなんでもOK、3.9.13で動作確認済

## venvによる仮想環境作成
$ python -m venv venv # venvという名前の仮想環境が作成される

## 仮想環境の有効化
$ source venv/bin/activate

## 仮想環境の無効化
$ deactivate
```
- 以下必ず仮想環境が`有効化`された状態で実行する
### 使用するライブラリのインストール
```
$ pip install flask
$ pip install sqlalchemy
```