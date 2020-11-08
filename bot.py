import discord
import asyncio
import time
from discord.ext import commands
token = ""

ID = 692572871322632222
messaged = joined = 0

#____________________________________________________________
client = discord.Client()

async def update_stats():
    await client.wait_until_ready() #method for class client
    global messaged, joined #global, so it can be acessed everywhere

    while not client.is_closed(): #while client is 'not' stopped (stopped as in i don't press the red button)
        try:
            with open("stat.txt", "a") as f: #open stats.txt and stats.txt == 'f'
                f.write(f"Time: {int(time.time())}, Messages: {messaged}, Members Joined: {joined}\n")

            messaged = 0 #reset variables
            joined = 0

            await asyncio.sleep(600)

        except Exception as e:
            print(e)
            await asyncio.sleep(600) #10 minutes

@client.event
async def on_member_join(member):
    global joined
    joined = joined + 1
    for channel in member.guild.channels: #for whatever channel joined
        if(str(channel) == "general"): #if it's general
            await channel.send_message(f"""Welcome {member.mention}""") #welcome them


@client.event
async def on_message(message):
    global messaged
    messaged = messaged + 1
    id = client.get_guild(ID)
    channels = ["commands", "#nguyenthm-commands", "#nguyeneral"]
    valid_users = ["jshi#9154"]
    #if str(message.channel) in channels and str(message.author) in valid_users: #if the message is in the commands channel and in the command channel, the messanger/author is one of the valid users, then it's true
    if message.content.find("!hello") != -1: #finds it
        await message.channel.send("Hi") #sends it
    elif message.content == "!users": #sees if the message is the same
        await message.channel.send(f"""# of Members: {id.member_count}""")


    ##############################
    elif message.content == "!Die":
        await message.channel.send("Plz wait")
        await asyncio.sleep(6) #waits for 10 seconds
        await message.channel.send("xD")
    elif message.content == "indeed":
        await message.channel.send("INDEEEEED")
    elif message.content == "!Image":
        await message.channel.send(file=discord.File('Nightcore.png'))
    ###############################



client.loop.create_task(update_stats()) #pretty sure this is a while loop for the client to run over and over again without stopping for the method update_stats()
client.run(token)
