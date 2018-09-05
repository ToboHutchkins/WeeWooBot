import discord                      #MAKE SURE YOU DO "py -m pip install discord" IN COMMAND PROMPT!
from discord.ext.commands import bot
from discord.ext import commands
import random
import asyncio
import time
 
##PREFIX##
bot = commands.Bot(command_prefix='!')
 
##BOT IS READY##
@bot.event
async def on_ready():
    print("Bot Is Ready To WeeWoo!")

@bot.event
async def on_message(message):
    channel = message.channel
    if message.content.startswith('!weewoo'):
        await bot.send_message(channel, 'WEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO')
        await bot.send_message(channel, 'WEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO')
        await bot.send_message(channel, 'WEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO')
        await bot.send_message(channel, 'WEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO')
        await bot.send_message(channel, 'WEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO')
        await bot.send_message(channel, 'WEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO')
        await bot.send_message(channel, 'WEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO')
        await bot.send_message(channel, 'WEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO')
        await bot.send_message(channel, 'WEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO\nWEEWOO')

        
             
                       
 ##BOT TOKEN##
bot.run ("NDg2OTAyODgzODA4NDQ0NDI5.DnF3nQ.pYHec-QU7kQjfo-DGespZ3iYbpo")
