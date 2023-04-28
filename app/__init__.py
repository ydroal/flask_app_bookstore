from flask import Flask
from app import db

# 先にappインスタンスを作成
app = Flask(__name__)

# Flaskアプリの初期化が完了するまで待ってからインポート
from app import main







