# Music Bot Mover

Discord.py based discord bot which automatically re-directs Rythm bot messages (and optionally the user command message) from other text channels into a specified channel.

## Usage

Create a `.env` file in the same directory as `main.py` with the following format:

```config
DISCORD_TOKEN=discord_bot_token
DISCORD_GUILD=name_of_discord_server
DISCORD_RYTHM_CHANNEL_ID=id_of_channel_to_redirect_rythm_bot_messages_to
```
