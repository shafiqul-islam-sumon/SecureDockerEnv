import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def check_credentials():
    token = os.getenv('SLACK_BOT_TOKEN')
    secret = os.getenv('SLACK_SIGNING_SECRET')
    key = os.getenv('OPENAI_API_KEY')

    print("### SLACK_BOT_TOKEN : ", token)
    print("### SLACK_SIGNING_SECRET : ", secret)
    print("### OPENAI_API_KEY : ", key)


if __name__ == "__main__":
    check_credentials()
