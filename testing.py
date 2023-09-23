
import discord
from discord.ext import commands
import asyncio

intents = commands.Intents.all()
bot = commands.Bot(command_prefix= commands.when_mentioned_or("!"))

@bot.event
async def on_ready():
    print(f"Bot [bot.user] is online")

async def main():
    bot.start("insert token")

@bot.command()
async def timer(ctx: commands.Context, time: int):
    await asyncio.sleep(time)
    await ctx.send("Your time is up!")

asyncio.run(main())
#hhahaha