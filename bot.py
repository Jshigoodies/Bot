import discord
from discord.ext import commands
token = ""

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.find("!hello") != -1:
        await message.channel.send("Hi")


client.run(token)
