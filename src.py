#Import all the necessary libraries
from __future__ import print_function
import base64
import os.path
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
#SCOPE for read and write access
SCOPES = ['https://mail.google.com/']

creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())


service = build('gmail', 'v1', credentials=creds)

#function to create message
def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

#function to send message
def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                   .execute())
        print('Message Id: %s' % message['id'])
        return message
    except Exception as error:
        print(error)

message = create_message('me','sirishajp.testing@gmail.com', 'Launch: Recommendation Service - Test Email', ''' Dear Customer,

I hope this email finds you well. I am writing to let you know that we have recently launched a recommendation service that we believe would be of interest to you.

As one of our valued customers, we would like to offer you the opportunity to test this service before it is released to the public. This will give you the chance to provide feedback and suggestions that will help us improve it further.

If you are interested in participating in the testing program, please reply to this email with your confirmation. We will then provide you with the necessary information to access the service and instructions on how to use it.

Thank you for your continued support, and we look forward to hearing from you soon.

Best regards,

Sirisha Jotheeswaran Padmasekhar
Company xyz ''')
                         
print(send_message(service=service, user_id='me', message=message))
#function to search emails using keyword
def search_email(service, query):
    try:
        result = service.users().messages().list(q=query, userId='me').execute()
        messages = result.get('messages', [])
        if not messages:
            print('No messages found.')
        else:
            print(f"Found {len(messages)} messages with query '{query}'\n")
            for message in messages:
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                payload = msg['payload']
                headers = payload['headers']
                subject = ''
                sender = ''
                for header in headers:
                    if header['name'] == 'Subject':
                        subject = header['value']
                    elif header['name'] == 'From':
                        sender = header['value']
                print(f'Subject: {subject}\nFrom: {sender}\n')
    except Exception as error:
        print(f'An error occurred: {error}')

search_email(service=service, query='recommendation service')
