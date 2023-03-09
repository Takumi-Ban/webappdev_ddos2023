## 制作するもの
### メモ帳アプリ
- 機能
    - メモ書き込み機能
    - メモ編集機能
    - メモ削除機能
- 実装
    - Web技術: HTML, Bootstrap, JavaScript
    - 言語: Python
    - DB: SQLite3


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
- 有効化されると先頭に`(venv)`と表示される
    - `(venv) arm64:~/Development/ddos2023_webapp`
### 使用するライブラリのインストール
```
$ pip install flask
$ pip install sqlalchemy
```

- `pip freeze`でインストール済みのライブラリ一覧を表示できる
```
$ pip freeze
click==8.1.3
Flask==2.2.3
importlib-metadata==6.0.0
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.2
SQLAlchemy==2.0.5.post1
typing-extensions==4.5.0
Werkzeug==2.2.3
zipp==3.15.0
```

- VScodeを起動
```
$ code .
```

## ファイル構成
- `app.py`: 
- `main.py`
- `db.py`:
- `initdb.py`

## 作成手順
1. Webページの作成(HTML, Bootstrap)
2. Pythonでアプリ部分を作成

## Webページの作成
- HTML(HyperTextMarkupLanguage)によって記述
- CSS, JavaScriptで装飾したり動きをつけることも可能
- 今回はCSSを自力で書かずに`Bootstrap`というフレームワークを使用
- HTMLファイルは`./templates/`以下に保存

### メイン画面の作成
