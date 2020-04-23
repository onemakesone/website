from flask import Flask, render_template,jsonify,request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

## URL 별로 함수명이 같거나,
## route('/') 등의 주소가 같으면 안됩니다.

@app.route('/')
def home():
   return render_template('main.html')



@app.route('/animal',methods=['GET'])
def lis

if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=False)