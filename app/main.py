import sqlalchemy
from flask import render_template
from app import app
from os import getenv


DB = getenv('DB')

@app.route('/')
def index():
  books = [
    {
    'title':'はらぺこあおむし',
    'price':'12',
    'arrival_day': '5-20-2023', 
    },
    {
    'title':'ぐりとぐら',
    'price':'9',
    'arrival_day': '5-27-2023', 
    },
  ]
  return render_template(
    'index.html',
    books=books
  )

@app.route('/form')
def form():
  return render_template(
    'form.html'
  )