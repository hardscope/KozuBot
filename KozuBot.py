import discord
import os
#from botToken import token
from discord.ext import commands

bot = commands.Bot(command_prefix='<')



@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def fuckshibi(ctx):
    await ctx.send("<:FuckShibi:632362814656479272>")

@bot.event
async def on_message(message):

    #uwu
    if 'uwu' in message.content.casefold() and not message.author.bot:
        await message.channel.send("NO UWU ON MY SERVER")
        
    if '0w0' in message.content.casefold() and not message.author.bot:
        await message.channel.send("NO 0W0 ON MY SERVER")
        
    if 'owo' in message.content.casefold() and not message.author.bot:
        await message.channel.send("NO OWO ON MY SERVER")
        
bot.run(os.environ.get("TOKEN"))