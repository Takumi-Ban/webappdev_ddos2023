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
```shell
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
```shell
$ pip install flask
$ pip install sqlalchemy
```

- `pip freeze`でインストール済みのライブラリ一覧を表示できる
```shell
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
```shell
$ code .
```

## ファイル構成
- `app.py`
- `db.py`
- `initdb.py`

## 作成手順
1. Webページの作成(HTML, Bootstrap)
2. Pythonでアプリ部分を作成
---
## Webページの作成
- HTML(HyperTextMarkupLanguage)によって記述
- CSS, JavaScriptで装飾したり動きをつけることも可能
- 今回はCSSを自力で書かずに`Bootstrap`というフレームワークを使用
- HTMLファイルは`./templates/`以下に保存

### 各種ページの作成
- HTMLの記法については省略
- 配布のHTMLファイルを参照・穴埋め形式で進める
---
## Flaskの基礎
### 以下はすべて`app.py`に記述
- モジュールの読み込み
```python
from flask import Flask
```
- おまじない
```python
app = Flask(__name__)
```
- ルーティングの作成
    - ルーティングとはURLに対してどのような処理を行うかを紐付けること
    - 例
        - `/hello`というURLにアクセスされたら`Hello World!`という文字列を返す
        - `/login`というURLにアクセスされたら`ログイン処理`を行い結果を返す
    - Flaskでは`route`関数によってルーティングを定義する
```python
@app.route('/') # / というURLを定義・ / にアクセスするとindex関数が実行される
def index():
    return
```
- おまじない2
    - `debug=True`: プログラムを書き換えてもサーバを再起動することなく変更を反映できる
    - `port=5050`: 5050番ポートで実行(defaultは5000番)
```python
if __name__ == '__main__':
    app.run(debug=True, port=5050))
```
- いままで記述したものをまとめる(`app.py`)
```python
from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return

if __name__ == '__main__':
    app.run(debug=True, port=5050))
```

- サーバの起動
```shell
$ python app.py
```
- ブラウザから`http://127.0.0.1:5050` or `http://localhost:5050`にアクセス
- 正常に動作するとこうなる
    - 赤文字でWARNINGがでるがまずは焦らずに読んでみよう
    - 「これは開発用のサーバだから本番環境では使わないでね。本番環境にはかわりにWSGIサーバを使ってね。」と書いてあるだけ
```shell
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5050
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: ***-***-***
```
- 何も表示されないWebアプリを作成することができた
    - せっかくなのでなにか表示させてみよう
    - `index関数`の戻り値に文字列を指定する
```python
@app.route('/')
def index():
    return "Hello World!"
```
- ブラウザで更新ボタンを押してみると、`Hello World!`と表示された
---
### HTMLファイルを表示する
- モジュールの読み込み
```python
from flask import Flask, render_template
```
- HTMLファイルを配置
    - `app.py`と同階層にある`templates`ディレクトリ以下にHTMLファイルを配置
- `app.py`の書き換え
    - 実行される関数の戻り値に`render_template`を使用する
    ```python
    @app.route('/')
    def index():
        return render_template('hello.html')
    ```
- ブラウザで更新ボタンを押してみると、`hello.html`が表示される

### 表示する内容を動的に変化させる
- これらはJinjaというテンプレートによって実現される
- HTMLファイル内に`{{}}`で変数を囲って記述する
```html
<!doctype html>
<html lang="ja">
  <head>
    <title>練習</title>
  </head>
  <body>
    <h1>こんにちは</h1>
    <p>今日の天気は{{ weather }}です。</p>
  </body>
</html>
```
- サーバ側から表示する内容を渡してあげる
- `render_template`の第2引数に変数を指定すればOK
```python
@app.route('/')
def index():
    weather = '晴れ'
    return render_template('hello.html', weather = weather)
```
- リストを渡してリストのインデックスを指定することもできる
```python
@app.route('/')
def index():
    weathers = ['晴れ', '曇り', '雨', '雪']
    return render_template('hello.html', weather = weathers)
```
- リストの2番目の要素を指定(インデックス1)
```html
<!doctype html>
<html lang="ja">
  <head>
    <title>練習</title>
  </head>
  <body>
    <h1>こんにちは</h1>
    <p>今日の天気は{{ weather.1 }}です。</p>
  </body>
</html>
```
- 繰り返し処理によってすべての要素を表示させることもできる
    - Pythonに近いfor文を記述することができる
    - for文を`{% %}`で囲い、ループ終了地点に`{% endfor %}`と記す
```html
<!doctype html>
<html lang="ja">
  <head>
    <title>練習</title>
  </head>
  <body>
    <h1>こんにちは</h1>
    {% for w in weathers %}
    <p>今日の天気は{{ w }}です。</p>
    {% endfor %}
  </body>
</html>
```
- 辞書を表示することもできる
    - `{{ 変数名.キー }}`で値を表示できる
```python
@app.route('/')
def index():
    info = {'city':'Tokyo', 'weather':'sunny'}
    return render_template('hello.html', info = info)
```
```html
<!doctype html>
<html lang="ja">
  <head>
    <title>練習</title>
  </head>
  <body>
    <h1>こんにちは</h1>
    <p>今日の{{ info.city }}の天気は{{ info.sunny }}です。</p>
  </body>
</html>
```
- 変数の値によって表示する内容を変化させることもできる
```html
{% if 条件式 %}
条件を満たしたときの表示内容
{% elif 条件式 %}
条件を満たしたときの表示内容
{% else %}
条件をいずれも満たさなかったときの表示内容
{% endif %}
```
```python
@app.route('/')
def index():
    result = 10 - 8
    return render_template('hello.html', result = result)
```
```html
<!doctype html>
<html lang="ja">
  <head>
    <title>練習</title>
  </head>
  <body>
    <h1>計算結果</h1>
    {% if result > 0 %}
    <p>答えは正の数です</p>
    {% elif result < 0 %}
    <p>答えは負の数です</p>
    {% else %}
    <p>答えは0です</p>
    {% endif %}
  </body>
</html>
```
### HTTPリクエストメソッドごとに処理を分ける
- HTTPリクエストメソッド
    - GET: 情報を検索したり取得するときに使用するメソッド(冪等性がある)
    - POST: 登録・更新などデータが更新される可能性があるときに使用するメソッド(冪等性がない)
    - ※冪等性(べきとうせい): 何度同じ処理を実行しても同じ結果を得られる性質
- `route()`関数の第2引数で許可するメソッドを指定する(defaultはGETのみ)
- 条件分岐で処理をわける
```python
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else: # -> if request.method == 'POST':と同値
        # 何かしらの登録処理・表示・計算処理など
        result = 'hogehoge'
        return render_template('index.html', result = result)
```
- 許可するHTTPメソッドごとに関数を分ける
```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def post_index():
    # 何かしらの登録処理・表示・計算処理など
    result = 'hogehoge'
    return render_template('index.html', result = result)
```
---
## サーバサイドの作成
### データベースの準備(`dbsetting.py`に記述)
- `SQLAlchemy`
    - Pythonでよく利用されるORM(Object Relational Mapper)の1つ
    - PythonのクラスとDBのテーブルを1対1で対応させて、クラスのメソッド経由でデータの取得・変更等が可能
    - 様々なRDBMSに対応しており、RDBMSを変えてもプログラムを流用可能
    - SQLを記述せずにデータの取得・挿入・変更・削除などの基本操作が可能

- データベースの準備の流れ
1. どのDBにどのように接続するかを設定(この設定を`エンジン`と呼ぶ)
2. マッピング・セッションの生成
3. 生成されたセッションによってDBを操作

- モジュールの読み込み
```python
from sqlalchemy import create_engine # エンジンの生成
from sqlalchemy.orm import scoped_session, sessionmaker # セッションの生成
from sqlalchemy.orm import declarative_base # ベースクラスの生成
```
- データベースの指定
    - SQLite3を使用
    - 指定した`.db`ファイル・`.sqlite`ファイルが存在しない場合は自動で作成される
```python
dbname = 'memo' # 接続するDB名
DB = f'sqlite:///{dbname}.sqlite?charset=utf8mb4'
```
- 参考: PostgreSQLを使用する場合
    - 別途接続対象となるDBが作成し以下を記述
```python
username = 'postgres' # 任意のusername
password = 'postgres' # 対応するpassword
host = 'localhost'
port = '5432'
dbname = 'memoapp' # 任意のDB名

DB = f'postgresql://{username}:{password}@{host}:{port}/{dbname}'
```

 - エンジンの生成
 ```python
Engine = create_engine(
    DB,
    echo=False # 実行されたSQLを表示しない
)
Base = declarative_base()
 ```

 - セッションの生成
 ```python
session = scoped_session(
    sessionmaker(
        autocommit = False,
	    autoflush = False,
	    bind = Engine
    )
)
 ```

 - ベースモデルの生成
 ```python
Base = declarative_base()
Base.query = session.query_property()
 ```
- `dbsetting.py`の全体
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm import declarative_base

dbname = 'memo'
DB = f'sqlite:///{dbname}.sqlite?charset=utf8mb4'

Engine = create_engine(
    DB,
    echo=False
)
Base = declarative_base()

session = scoped_session(
    sessionmaker(
        autocommit = False,
	    autoflush = False,
	    bind = Engine
    )
)

Base = declarative_base()
Base.query = session.query_property()
```

### データベースのテーブル定義(`initdb.py`に記述)
- モジュールの読み込み
```python
from sqlalchemy import Column, Integer, String, DateTime # 使用するデータ型
from dbsetting import Engine # dbsetting.pyで生成されたエンジン
from dbsetting import Base # dbsetting.pyで生成されたベースモデル
```

- 作成したいテーブルのイメージ

| column | id | title | detail | created_at |
| :---: | :---: | :---: | :---: | :---: |
| type | Integer | String(30) | String(140) | DateTime |

- テーブルの定義
    - `id`: 整数型・主キー(primary-key)に指定・autoincrement(連番で自動挿入)・nullを許可しない
    - `title`: 文字列型(30文字まで)・nullを許可しない
    - `detail`: 文字列型(140文字まで)・nullを許可しない
    - `created_at`: 日付時刻型・nullを許可しない
```python
class Memo(Base):
    __tablename__ = 'memo'
    __table_args__ = {
        'comment': 'メモ内容のマスターテーブル'
    }

    id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column('title', String(30), nullable=False)
    detail = Column('content', String(140), nullable=False)
    created_at = Column('created_at', DateTime, nullable=False)
```
- おまじない3
```python
if __name__ == '__main__':
    Base.metadata.create_all(bind=Engine)
```

- 複数のテーブルを作成したい場合は続けて別のクラスを定義すればよい

- `initdb.py`の全体
```python
from sqlalchemy import Column, Integer, String, DateTime
from dbsetting import Engine
from dbsetting import Base

class Memo(Base):
    __tablename__ = 'memo'
    __table_args__ = {
        'comment': 'メモ内容のマスターテーブル'
    }

    id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column('title', String(30), nullable=False)
    detail = Column('content', String(140), nullable=False)
    created_at = Column('created_at', DateTime, nullable=False)

if __name__ == '__main__':
    Base.metadata.create_all(bind=Engine)
```

### アプリのメイン処理(`app.py`)に記述
- モジュールの読み込みとおまじない
```python
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from sqlalchemy import desc
from initdb import Memo # initdb.pyで作成したやつ
from dbsetting import session, Engine # dbsetting.pyで作成したやつ

app = Flask(__name__)
```

#### トップページ(ルートページ)の作成
- トップページにはメモのタイトルを一覧で表示 -> DBからデータを取得・反映したHTMLファイルを生成
    - データベースから`created_at DESC`降順にデータを取得 -> `session.query(Memo).order_by(desc(Memo.created_at)).all()`
    - 右のSQLと同値 -> `SELECT * FROM memo ORDER BY created_at DESC;`
- メモの詳細表示・新規作成・編集・削除ボタンを配置
```python
@app.route('/')
def index():
    contents = session.query(Memo).order_by(desc(Memo.created_at)).all()
    session.close() # セッションを終了
    return render_template('index.html', [あなうめ]) 
```
- `index.html`に記述
     - `aタグ`の`href属性`に`url_for('関数名')`を指定することで、クリック時に指定の関数を実行
```html
<!doctype html>
<html lang="ja">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <title>はじめてのWebアプリ</title>
  </head>
  <body>
    <div class="container">
        <div class="row">
            <div class="col-12">
                <h1 class="text-info">すごいアプリケーション</h1>
                <a href="[あなうめ]" class="btn btn-info">メモを追加</a>
                [あなうめ]
                <h4>[あなうめ]: [あなうめ]</h4>
                <p>作成日時: [あなうめ]</p>
                <hr>
                [あなうめ]
            </div>
        </div>
    </div>
    <!-- Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
  </body>
</html>
```
- おまじない(`app.py`に追記)
```python
if __name__ == '__main__':
    app.run(debug=True, port=5050)
```

- `app.py`の全体
```python
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from initdb import Memo
from dbsetting import session, Engine
from sqlalchemy import desc

app = Flask(__name__)

@app.route('/')
def index():
    contents = session.query(Memo).order_by(desc(Memo.created_at)).all()
    session.close()
    return render_template('index.html', contents=contents)

if __name__ == '__main__':
    app.run(debug=True, port=5050)
```

- サーバを起動
```shell
$ python app.py
```

#### メモ新規作成ページの作成
- `app.py`に追記
```python
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    if request.method == 'POST':
        title = request.form['title'] # POSTメソッドでのアクセスの場合にFormからtitleを取得
        content = request.form['content']# POSTメソッドでのアクセスの場合にFormからcontentを取得
        
        memo = Memo() # インスタンス化
        memo.title = title # memoテーブルのtitleカラムに挿入するデータの指定
        memo.detail = content # memoテーブルのdetailカラムに挿入するデータの指定
        memo.created_at = datetime.now() # memoテーブルのcreated_atカラムに挿入するデータの指定・現在時刻を挿入
        session.add(memo) # セッションに追加
        session.commit() # セッションのコミット
        session.close() # セッションの終了
        return redirect(url_for('create')) # create()関数にリダイレクトさせる
```
- `create.html`に記入
```html
<!doctype html>
<html lang="ja">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <title>はじめてのWebアプリ</title>
  </head>
  <body>
    <div class="container">
        <div class="row">
            <div class="col-12">
                <h1 class="text-info">すごいアプリケーション</h1>
                <h3>新規メモ</h3>
                <form method="post">
                    <div class="mb-3">
                        <label for="title" class="form-label">タイトル</label>
                        <input type="text" class="form-control" id="title" name="title" maxlength="30" required>
                    </div>
                    <div class="mb-3">
                        <label for="content" class="form-label">内容</label>
                        <textarea class="form-control" id="content" name="content" rows="3" maxlength="140" required></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary">登録</button>
                    <a href="[あなうめ]" class="btn btn-info" role="button">メモを見る</a>
                </form>
            </div>
        </div>
    </div>
    <!-- Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
  </body>
</html>
```

#### メモ内容を表示するページの作成
- あるURLにアクセスされた際に実行される関数に引数を渡す方法
    - URLパスのうち、変化する部分に**データ型**と**変数名**を記述
    - 例)`/test/<int:id>`・`/test/<string:name>`
```python
@app.route('/test/<int:id>')
def detail(id):
    taget_id = id
    return target_id
```

- メモの詳細を個別に表示
    - memoテーブルのidカラムに格納されているidを活用する
    - idを指定することで、指定したメモの詳細のみをデータベースから取得する
- `app.py`
```python
@app.route('/detail/<int:id>')
def detail(id):
    content = session.query(Memo).filter(Memo.id == id).one() # 指定したidのデータのみをデータベースから取得
    return render_template('detail.html', content=content)
```

- `detail.html`
     - `aタグ`の`href属性`に`url_for('関数名')`を指定することで、クリック時に指定の関数を実行
```html
<!doctype html>
<html lang="ja">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <title>はじめてのWebアプリ</title>
  </head>
  <body>
    <div class="container">
        <div class="row">
            <div class="col-12">
                <h1 class="text-info">すごいアプリケーション</h1>
                <a href="{{ url_for('create') }}" class="btn btn-info">メモを追加</a><br>
                <h3>メモ詳細</h3>
                <h5>メモID: [あなうめ]</h5>
                <h5>タイトル: [あなうめ]</h5>
                <p>詳細：[あなうめ]</p>
                <p>作成日時: [あなうめ]</p>
            </div>
        </div>
    </div>
    <!-- Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
  </body>
</html>
```

- トップページに詳細・削除・編集のボタンを配置
    - 実行したい関数に引数を渡すにはaタグのhref属性に下のように記述する
    - `{{ url_for('実行する関数名', 引数 = 関数に渡す変数) }}`
- `index.html`(追記箇所を抜粋)
```html
{% for content in contents %}
<h4>{{ content.id }}: {{ content.title }}</h4>
<p>作成日時: {{ content.created_at }}</p>
<a href=[あなうめ] class="btn btn-primary" role="button">メモ詳細</a>
<a href=[あなうめ] class="btn btn-danger" role="button" id="delete-btn">削除</a>
<a href=[あなうめ] class="btn btn-info" role="button">編集</a>
<hr>
{% endfor %}
```

#### メモを削除する処理の実装
- メモを削除 = データベースから該当するデータを削除
- 指定されたメモのみを削除するために、idを利用して処理を分ける
- `app.py`
```python
@app.route('/delete/<int:id>')
def delete(id):
    content = session.query(Memo).filter(Memo.id == id).one() # データベースから指定されたidのデータを1つだけ(idはユニークな値なので)取得
    session.delete(content) # データベースから取得したデータを削除
    session.commit() # セッションのコミット
    session.close() # セッションの終了
    return redirect(url_for('index')) # index関数にリダイレクト
```

- 表示する必要がないためHTMLファイルの編集はなし

#### メモを編集する処理の実装
- メモを編集 = データベースのデータ更新
- 指定されたメモを編集するために、編集前の内容をデータベースから取得してフォームから取得した内容にデータベースを更新
- `app.py`
```python
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    # GETメソッドでアクセスされた場合
    if request.method == 'GET':
        content = session.query(Memo).filter(Memo.id == id).one() # 変更対象のデータをデータベースから取得
        return render_template('edit.html', content = content) # 編集ページを表示

    # POSTメソッドでアクセスされた場合
    else:
        content = session.query(Memo).filter(Memo.id == id).one() # 変更対象のデータをデータベースから取得
        content.title = request.form['title'] # Formから変更後のタイトルを取得
        content.detail = request.form['content'] # Formから変更後のメモ内容を取得
        session.commit() # セッションのコミット(変更内容の反映)
        session.close()
        return redirect(url_for('index'))
```

- `edit.html`
```html
<!doctype html>
<html lang="ja">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <title>はじめてのWebアプリ</title>
  </head>
  <body>
    <div class="container">
        <div class="row">
            <div class="col-12">
                <h1 class="text-info">すごいアプリケーション</h1>
                <h3>編集</h3>
                <form method="post">
                    <div class="mb-3">
                        <label for="title" class="form-label">タイトル</label>
                        <input type="text" class="form-control" id="title" name="title" maxlength="30" value="{{ content.title }}" required>
                    </div>
                    <div class="mb-3">
                        <label for="content" class="form-label">内容</label>
                        <textarea class="form-control" id="content" name="content" rows="3" maxlength="140" required>{{ content.detail }}</textarea>
                    </div>
                    <button type="submit" class="btn btn-primary">登録</button>
                    <a href="{{ url_for('index') }}" class="btn btn-info" role="button">メモを見る</a>
                </form>
            </div>
        </div>
    </div>
    <!-- Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
  </body>
</html>
```

### `app.py`の全体
```python
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from initdb import Memo
from dbsetting import session, Engine
from sqlalchemy import desc

app = Flask(__name__)

@app.route('/')
def index():
    contents = session.query(Memo).order_by(desc(Memo.created_at)).all()
    session.close()
    return render_template('index.html', contents=contents)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        memo = Memo()
        memo.title = title
        memo.detail = content
        memo.created_at = datetime.now()
        session.add(memo)
        session.commit()
        session.close()
        return redirect(url_for('create'))
    
@app.route('/detail/<int:id>')
def detail(id):
    content = session.query(Memo).filter(Memo.id == id).one()
    return render_template('detail.html', content=content)

@app.route('/delete/<int:id>')
def delete(id):
    content = session.query(Memo).filter(Memo.id == id).one()
    session.delete(content)
    session.commit()
    session.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'GET':
        content = session.query(Memo).filter(Memo.id == id).one()
        return render_template('edit.html', content = content) 
    else:
        content = session.query(Memo).filter(Memo.id == id).one()
        content.title = request.form['title']
        content.detail = request.form['content']
        session.commit()
        session.close()
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5050)
```

- サーバの起動
```shell
$ python app.py
```
- ブラウザから`http://127.0.0.1:5050` or `http://localhost:5050`にアクセス
- 正常に動作するとこうなる
    - 赤文字でWARNINGがでるがまずは焦らずに読んでみよう
    - 「これは開発用のサーバだから本番環境では使わないでね。本番環境にはかわりにWSGIサーバを使ってね。」と書いてあるだけ
```shell
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5050
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: ***-***-***
```

### 完成
- メモの新規作成・削除・変更が正しくできることを確認しよう