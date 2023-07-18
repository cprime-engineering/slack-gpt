import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


# Set Slack API credentials
SLACK_BOT_TOKEN = os.environ["SEBASTIAN_SLACK_BOT_TOKEN"]
SLACK_APP_TOKEN = os.environ["SEBASTIAN_SLACK_APP_TOKEN"]

# Initializes app with your bot token
app = App(token=SLACK_BOT_TOKEN)


# Message handler for Slack
@app.message(".*")
def message_handler(message, say, logger):
    print(message)
    say("Hello from Sebastian!")


# Start app
if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
