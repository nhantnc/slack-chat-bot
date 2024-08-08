from dotenv import load_dotenv
import os
from slack_sdk import WebClient
from datetime import datetime
from pytz import timezone


load_dotenv()
DEFAULT_TIMEZONE = 'Asia/Ho_Chi_Minh'
# Set up a WebClient with the Slack OAuth token
client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
group = os.environ["SLACK_GROUP_ID"]

def send_message(message):
    # Send a message
    client.chat_postMessage(
        channel=os.environ["SLACK_CHANNEL_ID"], 
        text=message, 
        mrkdwn=True,
        username="R&D Bot"
    )

def send_syncing_message():
    today = datetime.now(timezone(DEFAULT_TIMEZONE)).strftime('%Y-%m-%d')
    send_message(f"""
    :spiral_calendar_pad: `{today}` [Daily-Report]\n>Hi <!subteam^{group}>, please report in this thread :man-tipping-hand::skin-tone-2:
    """)