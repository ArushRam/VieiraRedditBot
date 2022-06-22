A Reddit bot correcting incorrect spellings of Vieira on /r/Gunners, and replying with a chant based on which Vieira is being referred to!

Inspired by Manik Narang's Arsene Wenger bot (https://github.com/maniknarang/arsenal-reddit-bot).
## RUNNING SCRIPT

Build an `.env` file as follows:

```env
CLIENT_ID="your client id"
CLIENT_SECRET="your client secret"
REDDIT_USERNAME="your bot's reddit username"
REDDIT_PASSWORD="your bot's reddit password"
```

Set these `environment variables` as:

```bash
set -a
source <filename>.env
set +a
```

Run script as `python3 bot.py` or `python bot.py`
