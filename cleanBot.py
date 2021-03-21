# I want a fresh start with this

import discord
from discord.ext import commands

token = '' # CleanBot

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("CleanBot is ready")


client.run(token)