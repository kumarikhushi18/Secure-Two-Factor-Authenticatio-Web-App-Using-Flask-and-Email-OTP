# 🔐 Secure Web Login with Two-Factor Authentication (2FA)

A simple yet secure web application that demonstrates *Two-Factor Authentication* using *Flask* and *OTP (One-Time Password)* sent via email. Users must register and then login using a password followed by a one-time code sent to their registered email.

---

## 📌 Features

- User registration with email and password
- Secure login with password
- OTP generation and email verification (2FA)
- User data stored in a JSON file (for demo purposes)
- Stylish and responsive frontend with modern CSS

---

## 🚀 Tech Stack

- Backend: Python, Flask
- Frontend: HTML5, CSS3
- Email: Python smtplib for OTP delivery
- Data Storage: JSON file

---

## 🛠 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/2fa-flask-demo.git
cd 2fa-flask-demo
2. Create a virtual environment and activate it
bash
Copy
Edit
python -m venv env
# On Windows
env\Scripts\activate
# On Mac/Linux
source env/bin/activate
3. Install dependencies
bash
Copy
Edit
pip install flask
4. Configure your email credentials
Edit the following variables inside app.py:

python
Copy
Edit
from_email = "your-email@gmail.com"
from_password = "your-app-password"  # Use 16-digit App Password from Google
⚠ Note: To use Gmail, enable 2-Step Verification and generate an App Password from your Google Account.

5. Run the application
bash
Copy
Edit
python app.py
Then go to http://localhost:5000 in your browser.

🧪 Project Structure
php
Copy
Edit
2fa-flask-demo/
│
├── static/
│   └── style.css          # Stylish frontend CSS
│
├── templates/
│   ├── login.html         # Login page
│   ├── register.html      # Registration page
│   ├── verify.html        # OTP input page
│   └── success.html       # Success message after login
│
├── users.json             # Stores registered users
├── app.py                 # Main Flask backend
└── README.md              # Project documentation
🔐 How It Works
Register with your email and password.

Login using your credentials.

A 6-digit OTP is generated and sent to your email.

Enter the OTP to verify and complete login.

You’re securely authenticated!

📈 Future Enhancements
SMS-based OTP using Twilio

Google Authenticator (TOTP) support

Database (SQLite/PostgreSQL) instead of JSON

End-to-end encryption for OTPs

CAPTCHA and rate-limiting for brute-force prevention

👩‍💻 Author
Kumari Khushi
Submission for GUVI (HCL) Project Challenge
