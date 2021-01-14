# TestBot by Sidpatchy
# This is apart of my tutorial series: <playlist link>

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio

bot = commands.Bot(command_prefix='!')

# Things to run when the bot connects to Discord
@bot.event
async def on_ready():
    print('Connected!')

# Test command
@bot.command(pass_context=True)
async def test(ctx):
    await ctx.send('Working!')

bot.run('BOT_TOKEN_HERE')