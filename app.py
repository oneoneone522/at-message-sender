import os
from flask import Flask, request, render_template, redirect, url_for
from dotenv import load_dotenv
from messageSender import MessageSender
from save_cookies import Cookies
from load_cookies import CookiesSaved

app = Flask(__name__)

load_dotenv()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method =='POST':
        email = request.form.get('email')
        password = request.form.get('password')
        return redirect('/')
    
    try:
        cookies = Cookies(email, password)
        driver = Cookies.initializeDriver()
        cookies = Cookies(email, password)
        cookies.SaveCookies(driver)
        print("Succeeded")
        return redirect('/')

    except Exception as e:
        print("Logging in failed")                
    return render_template('login.html', Cookies=Cookies)

@app.route('/notification', methods = ['POST','GET'])
def get_notification():
    # email = os.getenv('EMAIL')
    # password = os.getenv('PASSWORD')
    messageSender = MessageSender(Cookies)
    messageSender.notfClick()
    print("notification clicked!!")
    return redirect('/')

@app.route('/tester_check', methods = ['POST','GET'])
def get_tester():
    messageSender = MessageSender(Cookies)
    try:
        messageSender.testerClick()
        print("Tester clicked!!!!!!!!")
        messageSender.tester_message_send()
        print("Message send...TT")
    except Exception as e:
        print("Tester not clicked: ", e)
    return redirect('/')


if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=8000, debug=True)

 