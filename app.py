import os
from flask import Flask, request, render_template, redirect, url_for
from dotenv import load_dotenv
from messageSender import MessageSender


app = Flask(__name__)

load_dotenv()

@app.route('/')
def home():
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    messageSender = MessageSender(email, password)
    stu_count = messageSender.getCount()
    message = messageSender.getMessage()
    return render_template('index.html', stu_count=stu_count, message=message)

@app.route('/get_notification', methods = ['POST'])
def get_notification():
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    messageSender = MessageSender(email, password)
    messageSender.notfClick()
    
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

 