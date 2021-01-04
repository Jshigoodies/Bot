from discord.ext import commands

token = ""  # for application TestLearn's token

bot = commands.Bot(command_prefix='$')

@bot.command(name="NotTest")
async def test(ctx, arg):
    await ctx.send(arg)


bot.run(token)