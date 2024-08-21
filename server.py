from flask import Flask, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/send-email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    # Email configuration
    sender_email = "your_email@example.com"
    receiver_email = "your_email@example.com"
    password = "your_email_password"

    # Create the email content
    msg = MIMEText(f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}")
    msg['Subject'] = 'New Contact Form Submission'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send the email
    try:
        server = smtplib.SMTP_SSL('smtp.example.com', 465)  # Use your email provider's SMTP server
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        return redirect(url_for('index'))  # Redirect to a thank-you page or back to the form
    except Exception as e:
        return f"There was an error sending your message: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)
