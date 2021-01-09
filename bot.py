# bot.py
import os
import discord
import random

from dotenv import load_dotenv
from random import choice

# 1
# importing commands from discord.ext
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents(messages=True, members=True, guilds=True)
bot = commands.Bot(command_prefix="bp ", case_insensitive=True, intents=intents)


# Bekpes command targetted at random users
@bot.command(name="Bekpes")
async def bekpes(ctx, user: discord.Member = None):
    bekpes_quotes = [
        "is my BEKPES",
        "kenak ku BEKPES",
        "BEKPES AH",
        "imagine getting bekpes",
        "DOWN LA BODO",
        "hate em",
        "xtnYk",
        "SORRY LORRR UUUUEEEEEE",
        "cornelius.",
        "FUCKINGG SMACKKK",
        "can't be arsed",
        "HAA?",
        "BEKPES CAKK BISSS",
        "is gay",
        "kenak PAMPES",
        "FAK LOR"
    ]

    response = random.choice(bekpes_quotes)
    if user!=None:
        await ctx.send(f"{user.mention } " + response)
    else:
        user = choice(ctx.message.channel.guild.members)
        await ctx.send(f"{user.mention} " + response)

# Poke command which selects a random user to poke
@bot.command(name="Poke")
async def poke(ctx):
    user = choice(ctx.message.channel.guild.members)
    await ctx.send(f"{ctx.message.author.mention} poked {user.mention}")
    
bot.run(TOKEN)
