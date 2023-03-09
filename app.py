from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from initdb import Memo
from dbsetting import session, Engine

app = Flask(__name__)

@app.route('/')
def index():
    contents = session.query(Memo).all()
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
        memo.content = content
        memo.created_at = datetime.now()
        session.add(memo)
        session.commit()
        session.close()
        return redirect(url_for('create'))

if __name__ == '__main__':
    app.run(debug=True, port=5050)