import discord
from discord.ext import commands
from time import sleep
import os
import random
from random import randint, choice, choices
import asyncio

client = commands.Bot( command_prefix = '*')

word = {}

word_width = 24
word_height = 8



@client.event
async def on_redy():
    print( 'Bot connected')

  

    
    
token= os.environ.get('BOT_TOKEN')
client.run( token )
