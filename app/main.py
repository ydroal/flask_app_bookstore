from datetime import datetime
from flask import render_template, request, redirect, url_for
from app import app
from app.db import session, Books


@app.route('/', strict_slashes=False)
def index():
  # dbからbooksデータ抽出(list型)
  db_books = session.query(Books).all() 
  
  books = []
  for book in db_books:
    books.append({'title': book.book_id,
                  'title': book.title,
                  'price': book.price,
                  'arrival_day': book.arrival_day.strftime('%Y-%m-%d') # 時刻情報を除いた文字列に変換
                 })
  session.close()  
  return render_template(
    'index.html',
    books=books
  )

@app.route('/form', strict_slashes=False)
def form():
  return render_template(
    'form.html'
  ) 
  
@app.route('/form', methods=['POST'], strict_slashes=False)  
def register():
  title =  request.form['title']
  price =  request.form['price']
  arrival_day =  request.form['arrival_day']
  
  # yyyy-mm-dd形式の日付文字列をdatetimeオブジェクトに変換
  arrival_day_formated = datetime.strptime(arrival_day, "%Y-%m-%d")
  
  new_data = Books(title=title, price=price, arrival_day=arrival_day_formated)
  session.add(new_data)
  session.commit()
    
  return redirect(url_for('index'))