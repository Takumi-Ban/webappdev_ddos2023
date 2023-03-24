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