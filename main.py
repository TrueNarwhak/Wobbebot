 ################
# CONTRIBUTORS #
##############

# True Narwhak#7055

import discord
from discord.ext import commands

client = discord.Client()

prefix = "!" # what you use to issue a command


# commands; what makes the bot do shit

@client.event #(Start Up)
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.find("!hello") != -1: # simple hello command, just for helping
        await message.channel.send(":wave:")
    elif message.content.startswith("!info"):
        embedVar = discord.Embed(title="Hello!", description="I'm Wobbebot", color=0x00ff00)
        embedVar.add_field(name="What do I do?", value="I am a bot for a discord server based of the Doc Assets extention (which you can get here: https://chrome.google.com/webstore/detail/doctorpus-assets/cmlbeiacmcbdiepcenjmhmkclmffbgbd?hl=en)", inline=False)
        embedVar.add_field(name="What fucntions do I serve?", value="I serve many functions, but my primary ones are to:/nEasily acsess any png of an animal (under construction)/And provide automatic update alerts", inline=False) # definatley rework this
        embedVar.add_field(name="hello", value="hi3", inline=False)
        await message.channel.send(embed=embedVar)


# reading the token, and runing the bot with it
# try to hack the bot, now ;)

readTokenFile = open("token.txt", "r")
tokenFileList = readTokenFile.read()

client.run(tokenFileList)
