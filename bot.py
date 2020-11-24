import discord
import asyncio
import time
import random
from discord import VoiceClient
from discord.ext.commands import bot  # vc

import youtube_dl

from discord.ext import commands

token = "NzcyMTYwMTg2ODQ4MjQ3ODQ4.X52oNg.dLPJI7cI6njIPLT_i0j9SGDL9mo"

ID = 692572871322632222
messaged = joined = 0

# ____________________________________________________________
client = discord.Client()


async def update_stats():
    await client.wait_until_ready()  # method for class client
    global messaged, joined  # global, so it can be acessed everywhere

    while not client.is_closed():  # while client is 'not' stopped (stopped as in i don't press the red button)
        try:
            with open("stat.txt", "a") as f:  # open stats.txt and stats.txt == 'f'
                f.write(f"Time: {int(time.time())}, Messages: {messaged}, Members Joined: {joined}\n")

            messaged = 0  # reset variables
            joined = 0

            await asyncio.sleep(600)

        except Exception as e:
            print(e)
            await asyncio.sleep(600)  # 10 minutes


# member joins
@client.event
async def on_member_join(member):
    global joined
    joined = joined + 1
    for channel in member.guild.channels:  # for whatever channel joined
        if (str(channel) == "general"):  # if it's general
            await channel.send_message(f"""Welcome {member.mention}""")  # welcome them


# read messages
@client.event
async def on_message(message):
    global messaged
    messaged = messaged + 1
    id = client.get_guild(ID)
    channels = ["commands", "#nguyenthm-commands", "#nguyeneral"]
    valid_users = ["jshi#9154"]

    bad_words = ["fuck", "hate", "die"]

    for word in bad_words:
        if message.content.count(word) > 0:
            print("A bad word was said")
            await message.channel.purge(limit=1)

    # if str(message.channel) in channels and str(message.author) in valid_users: #if the message is in the commands channel and in the command channel, the messanger/author is one of the valid users, then it's true
    if message.content.find("!hello") != -1:  # finds it
        await message.channel.send("Hi")  # sends it
    elif message.content == "!users":  # sees if the message is the same
        await message.channel.send(f"""# of Members: {id.member_count}""")

    ##############################
    elif message.content == "!Die":
        await message.channel.send("Plz wait")
        await asyncio.sleep(6)  # waits for 6 seconds
        await message.channel.send("xD")
    elif message.content == "indeed":
        await message.channel.send("INDEEEEED")
    elif message.content == "!Image":
        await message.channel.send(file=discord.File('meme.png'))
    elif message.content == "!Leave":
        toleave = client.get_server("363541040013115392")
        await client.leave_server(toleave)
    ###############################


@client.event
async def on_member_update(before, after):
    n = after.nick
    if n:  # Check if they updated their username
        if n.lower().count("guy") > 0:  # If username contains guy
            last = before.nick
            if last:  # If they had a usernae before change it back to that
                await after.edit(nick=last)
            else:  # Otherwise set it to "NO STOP THAT"
                await after.edit(nick="NO STOP THAT")


####################################################### the stuff above does not work because I'm doing another way to command a bot below (i think)
client = commands.Bot(command_prefix='.')
#most of the stuff down here is pretty self explanatory

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def clear(ctx, amount = 2):
    await ctx.channel.purge(limit=amount)

@client.command(aliases=["h"])
async def _help(ctx):
    await ctx.send("h (help), ping, 8ball, join <- joins vc, leave <- leaves vc, clear (deletes the message above it)")


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


@client.command(aliases=["8ball", "eightball"])
async def _8ball(ctx, *, question):
    responses = ["no", "yes", "maybe"]
    await ctx.send(f"Question: {question}\nAnswser: {random.choice(responses)}")


@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


##########################################################

client.loop.create_task(
    update_stats())  # pretty sure this is a while loop for the client to run over and over again without stopping for the method update_stats()
client.run(token)
