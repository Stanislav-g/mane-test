import discord
from discord.ext import commands
from time import sleep
import os
import random
from random import randint, choice, choices
import asyncio

client = commands.Bot( command_prefix = '*', self_bot = True)

@client.event
async def on_redy():
    print( 'Bot connected')

  
@client.command()
async def start( ctx ):
    while True:
        await ctx.send(f"!d bump")
        await asyncio.sleep(7200)
        await ctx.send(f"!d bump")
        await asyncio.sleep(7200)
        await ctx.send(f"!d bump")
        await asyncio.sleep(7200)
        await ctx.send(f"!d bump")
        await asyncio.sleep(7200)
        await ctx.send(f"!d bump")
        await asyncio.sleep(7200)
        await ctx.send(f"!d bump")
        await asyncio.sleep(7200)
        await ctx.send(f"!d bump")
        await asyncio.sleep(7200)
        await ctx.send(f"!d bump")
        await asyncio.sleep(7200)
        await ctx.send(f"!d bump")
        await asyncio.sleep(7200)
    

@client.command( pass_context = True )
async def spam( ctx, member: discord.Member):
    while True:
        await ctx.send('hi : {}'.format( member.mention ) )
        await asyncio.sleep(1)
        await ctx.send('hi : {}'.format( member.mention ) )
        await asyncio.sleep(1)
        await ctx.send('hi : {}'.format( member.mention ) )
        await asyncio.sleep(1)
        await ctx.send('hi : {}'.format( member.mention ) )
        await asyncio.sleep(1)
        await ctx.send('hi : {}'.format( member.mention ) )
        await asyncio.sleep(1)
        await ctx.send('hi : {}'.format( member.mention ) )
        await asyncio.sleep(1)
        await ctx.send('hi : {}'.format( member.mention ) )
        await asyncio.sleep(1)
        await ctx.send('hi : {}'.format( member.mention ) )
        await asyncio.sleep(1)
        
  
    
@client.command()
async def priv( ctx ):
    while True:
        a = random.choice(['эй','привет','алло','девять чи десять?','ку','аваава','как дела?','упс','ДЕВЯТЬ???','ало','алооо','здарова'])
        await ctx.send(a)
        await asyncio.sleep(20)
@client.command()
async def status( ctx ):
    await ctx.channel.purge( limit = 1 )
    while True:
        await client.change_presence(activity=discord.Game(name='LEGO'))   # играет в 'ваш текст '      
        
#send_a
@client.command()
@commands.has_permissions(administrator = True)
async def send_a(ctx, member: discord.Member, *, arg):
    await ctx.channel.purge(limit = 1)
    await member.send('```' + arg + '```')

    
token= os.environ.get('BOT_TOKEN')
client.run( token, bot = False )
