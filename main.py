import os
client.run(os.getenv('MTU1OTY4NTMzMDMzOTM2NDk2Ng.GBex6L.jFppEk7NG_EkSQCuiDL-DU-AyYeNEjyXBiYrGc')
import discord
from datetime import datetime, timezone

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

INACTIVE_HOURS = 6
last_seen = {}

@client.event
async def on_ready():
    print(f'Logged in successfully as {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    is_admin_or_mod = (
        message.author.guild_permissions.administrator or 
        message.author.guild_permissions.manage_messages
    )

    if is_admin_or_mod:
        now = datetime.now(timezone.utc)
        user_id = message.author.id

        if user_id in last_seen:
            previous_time = last_seen[user_id]
            time_diff = (now - previous_time).total_seconds() / 3600

            if time_diff >= INACTIVE_HOURS:
                await message.channel.send(f"Eternal welcomes Higher Being {message.author.mention}")
        else:
            await message.channel.send(f"Eternal welcomes Higher Being {message.author.mention}")

        last_seen[user_id] = now

client.run('MTU1OTY4NTMzMDMzOTM2NDk2Ng.GBex6L.jFppEk7NG_EkSQCuiDL-DU-AyYeNEjyXBiYrGc')

