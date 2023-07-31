# Slack Setup

1: Navigate to https://api.slack.com/apps

2: Click 'create new app'.

3: Select 'from scratch'.

4: Enter app name and select workspace.

5: In basic information upload app image and add short description.

6: In oauth and permissions add scopes (chat:write, chat:write:public).

7: In App Home check box 'Allow users to send Slash commands and messages from the messages tab'.

8: In Install App, click 'install into workspace'.

9: In socket Mode, click turn on socket mode.

10: enter tocken name and generate token (copy token to safe location).

11: In Interactivity and shortcuts ensure 'interactivity' is turned on.

12: In event subscriptions, enable events.

13: In event subsctiptions, subscribe to bot events (app_mention, message:im).

14: Save changes and re-install app.

15: Create GitHub code spaces secret 'SLACK_APP_TOKEN' and enter generated 'App-Level-Token' (beginning xapp-)

16: Create GitHub code spaces secret 'SLACK_BOT_TOKEN' and enter 'Bot User OAuth Token' (beginning xoxb-)

Start coding!