import discord
from discord.ext import commands
from time import sleep
import os
import random
from random import randint, choice, choices
import asyncio

client = commands.Bot( command_prefix = '*')

world = {}
world_width = 24
world_height = 8

second_part = [0,1]
third_part = [1,2]

@client.event
async def on_redy():
    print( 'Bot connected')

    
@client.command()
async def generate_world(ctx):
    for x in range(world_height):
        if x <= 2:
            for x in range(world_height):
                await ctx.send(f'0')
            await ctx.send()
        elif x <= 3:
            for x in range(world_width):
                await ctx.send(random.choice(second_part))
            await ctx.send()
        elif x <= 4:
            for x in range(world_width):
                await ctx.send(f'1')
            await ctx.send()
        elif x <= 5:
            for x in range(world_width):
                await ctx.send(random.choice(third_part))
            await ctx.send()
        elif x <= 7:
            for x in range(world_width):
                await ctx.send(f'2', end = '')
            await ctx.send()

generate_world()
 

@client.command()
async def world(ctx): 
    a = random.choice(['0'])
    sec = random.choice(['1','0'])
    th = random.choice(['1'])
    four = random.choice(['1','2'])
    await ctx.send( a, a, a, a, a, a, a, a, a, a, a, a, a )                   
    
                       
                       
                      
token= os.environ.get('BOT_TOKEN')
client.run( token )
