from flask import Flask, request, redirect, url_for, session, render_template
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import base64
import json
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
#logging imports: 
import logging
from logging.handlers import RotatingFileHandler

#-----------------------------------------
# LOGGING
#-----------------------------------------
log_dir = '/home2/rftboymy/public_html/website_1194c547/logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
file_handler = RotatingFileHandler(os.path.join(log_dir, 'flask_app.log'), maxBytes=10240, backupCount=10)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
file_handler.setFormatter(formatter)
app.logger.addHandler(file_handler)

app.logger.setLevel(logging.INFO)
app.logger.info('Flask app started')
#-----------------------------------------
# SERVER.
#-----------------------------------------
app = Flask(__name__)

# Load the client secret from the JSON file
with open('/home2/rftboymy/public_html/website_1194c547/credentials.json', 'r') as f:
    client_info = json.load(f)
    app.secret_key = client_info['web']['client_secret']

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

@app.route('/')
def index():
    return render_template('contact_form.html')

@app.route('/send-email', methods=['GET','POST'])
def send_email():
    app.logger.info("Received reqauest to send an email")
    return "Send Emial Route Working!!"
    # if 'credentials' not in session:
    #     return redirect(url_for('authorize'))

    # credentials = Credentials(**session['credentials'])
    # service = build('gmail', 'v1', credentials=credentials)

    # name = request.form['name']
    # email = request.form['email']
    # phone = request.form['phone']
    # message = request.form['message']

    # email_message = MIMEText(f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}")
    # email_message['to'] = 'your_email@gmail.com'
    # email_message['from'] = 'sethmglover@gmail.com'
    # email_message['subject'] = 'New Contact Form Submission'
    # raw_message = base64.urlsafe_b64encode(email_message.as_bytes()).decode()

    # try:
    #     service.users().messages().send(userId='me', body={'raw': raw_message}).execute()
    #     return "Email sent successfully! Thank you for contacting us."
    # except HttpError as error:
    #     return f"An error occurred: {error}"

@app.route('/authorize')
def authorize():
    flow = InstalledAppFlow.from_client_secrets_file(
        '/home2/rftboymy/public_html/website_1194c547/credentials.json', SCOPES)
    flow.redirect_uri = url_for('oauth2callback', _external=True)
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true')

    session['state'] = state
    return redirect(authorization_url)

@app.route('/oauth2callback')
def oauth2callback():
    state = session.get('state')
    if not state:
        return redirect(url_for('authorize'))

    flow = InstalledAppFlow.from_client_secrets_file(
        '/home2/rftboymy/public_html/website_1194c547/credentials.json', SCOPES, state=state)
    flow.redirect_uri = 'http://sethgdesigns.com/oauth2callback'

    authorization_response = request.url
    flow.fetch_token(authorization_response=authorization_response)

    credentials = flow.credentials
    session['credentials'] = credentials_to_dict(credentials)

    return redirect(url_for('send_email'))

def credentials_to_dict(credentials):
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }

if __name__ == '__main__':
    app.run(debug=True)
