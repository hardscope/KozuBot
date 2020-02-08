import discord
from botToken import token
from discord.ext import commands

bot = commands.Bot(command_prefix='<')



@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def fuckshibi(ctx):
    await ctx.send("<:FuckShibi:632362814656479272>")

bot.run(token)