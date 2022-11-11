import requests
from settings import MAILGUN_URL, MAILGUN_API_KEY, EMAIL_RECEIVER


def send_email(text: str,
               sender_name: str,
               sender_email: str):
    r = requests.post(MAILGUN_URL,
                      auth=("api", MAILGUN_API_KEY),
                      data={"from": f'{sender_name} <{sender_email}>',
                            "to": [EMAIL_RECEIVER],
                            "subject": "New Contact Entry for WeiWeiGFU",
                            "text": text}
                      )
    return r
