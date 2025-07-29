from flask import Flask, render_template, request, redirect, session, url_for
import json
import random
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'your-secret-key'

USER_FILE = 'users.json'
OTP_LENGTH = 6

# Load users
def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, 'r') as file:
        return json.load(file)

# Save users
def save_users(users):
    with open(USER_FILE, 'w') as file:
        json.dump(users, file, indent=4)

# Send OTP
def send_otp(email, otp):
    from_email = "sameernabeen@gmail.com"
    from_password = "ykdm yjlp vduf llos"

    msg = MIMEMultipart("alternative")
    msg['Subject'] = "Your OTP Code"
    msg['From'] = from_email
    msg['To'] = email
    html = f"<html><body><h2>Your OTP is: <b>{otp}</b></h2></body></html>"

    msg.attach(MIMEText(html, 'html'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(from_email, from_password)
            server.sendmail(from_email, email, msg.as_string())
    except Exception as e:
        print("Failed to send OTP:", e)

@app.route('/')
def home():
    return redirect('/register')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        users = load_users()
        if username in users:
            return "User already exists!"
        users[username] = {'password': password, 'email': email}
        save_users(users)
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = load_users()
        if username in users and users[username]['password'] == password:
            session['username'] = username
            otp = ''.join([str(random.randint(0, 9)) for _ in range(OTP_LENGTH)])
            session['otp'] = otp
            send_otp(users[username]['email'], otp)
            return redirect('/verify')
        return "Invalid credentials"
    return render_template('login.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if 'username' not in session:
        return redirect('/login')
    if request.method == 'POST':
        entered_otp = request.form['otp']
        if entered_otp == session.get('otp'):
            return redirect('/success')
        return "Invalid OTP!"
    return render_template('verify.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
