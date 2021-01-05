from discord.ext import commands

token = ""  # for application TestLearn's token

bot = commands.Bot(command_prefix='$')


@bot.command(name="NotTest")
async def test1(ctx, arg):
    await ctx.send(arg)


@bot.command()
async def test2(ctx, arg1, arg2):
    await ctx.send('You passed {} and {}'.format(arg1, arg2))


@bot.command()
async def test3(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))  # .joins the args list by ','


@bot.command()
async def test4(ctx, *, arg):  # * = as many parameters as you want to be equal to one thing. You can only have one
    # keyword-only argument due to parsing ambiguities.
    await ctx.send(arg)

#___________ctx - means Context______________________

# Context.guild to fetch the Guild of the command, if any.
#
# Context.message to fetch the Message of the command.
#
# Context.author to fetch the Member or User that called the command.
#
# Context.send() to send a message to the channel the command was used in.


bot.run(token)
