# The bot that kills Barons for a moderate fee

## Setup

1. Create a virtual environment: `python3 -m venv ./env`
2. Activate it: `source ./env/bin/activate`
3. Install deps: `pip install -r requirements.txt`
4. Copy env variables template to `.env` and set it up with the values inside
5. Execute `run.sh`

### Bot permissions

On creation, enable the "Server Members Intent". Afterwards, generate the invite URL on OAuth2 --> URL Generator
Click "Bot" on scopes, and then "Manage Roles" on the thingy that pops up below

You can open the generated URL to get the bot into the server