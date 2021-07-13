"""
Automatically moves the Rythm bot message from an incorrect text channel to the correct one.
"""

# bot.py
import os

import discord
from discord.ext.commands import bot
from dotenv import load_dotenv


class MusicMoverBot(discord.Client):

    def __init__(self, guild, rythm_commands, rythm_channel_id, delete_user_msg=False):
        """Initialises bot parameters and rythm commands to intercept (if applicable)."""
        self.guild = guild
        self.rythm_commands = rythm_commands
        self.rythm_channel_id = int(rythm_channel_id)
        self.delete_user_msg = delete_user_msg

        super(MusicMoverBot, self).__init__()

    async def on_ready(self):
        """Confirms bot successfully connected to target guild."""
        for guild in self.guilds:
            if guild.name == self.guild:
                break
        print(
            f'{self.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

        rythm_channel = self.get_channel(self.rythm_channel_id)
        await rythm_channel.send(f"{self.user} joined to clean this discord.")

    async def on_message(self, msg):
        """Intercepts Rythm bot (and optionally Rythm bot commands from users)
        related messages."""
        content = msg.content
        channel = msg.channel

        # Delete original Rhytm bot message and re-send in dedicated channel
        if msg.author.bot and msg.author.name == "Rythm" and msg.channel.name != "rythm":
            embed = msg.embeds[0] if msg.embeds else None
            print(f"Deleting message from Rythm Bot: {content} {embed} {channel}")

            # Send message to correct channel and delete message in wrong channel
            rythm_channel = self.get_channel(self.rythm_channel_id)
            if embed:
                await rythm_channel.send(content, embed=embed)
            else:
                await rythm_channel.send(content, embed=embed)
            await msg.delete()

        # Delete the users message which issued the command
        elif msg.content and self.delete_user_msg and msg.channel.name != "rythm":
            if any(cmd in msg.content for cmd in self.rythm_commands):
                print(f"Deleting message from User: {content} {channel}")
                await msg.delete()


if __name__ == "__main__":
    # Retrieve discord bot token and target guild
    load_dotenv()
    TOKEN      = os.getenv('DISCORD_TOKEN')
    GUILD      = os.getenv('DISCORD_GUILD')
    CHANNEL_ID = os.getenv('DISCORD_RYTHM_CHANNEL_ID')

    with open("./music_bot_commands.txt") as f:
        commands = f.read().split("\n")

    bot = MusicMoverBot(GUILD, commands, CHANNEL_ID, delete_user_msg=True)
    bot.run(TOKEN)