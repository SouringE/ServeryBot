import discord
from discord.ext import commands
import asyncio
from scraper import *

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=intents)

@bot.event
async def on_ready():
	print(f'Bot {bot.user} is online! Id: {bot.user.id}')

async def main():
	await bot.start('MTE1NDk3MDY1MTUwMTc5MzMxMQ.GTjofL.BYGqgjc3gUGu4k6OHsmlTYX_Ny19GXB4CYGRJQ')

@bot.command()
async def timer(ctx: commands.Context, time: int):
	await asyncio.sleep(time)
	await ctx.send("your time is up!")
	await ctx.send("you're dead now")

@bot.command()	
async def menu(ctx: commands.Context, servery: str):
	#using imported function to get menu
	serv_dict = get_menu()
	str_output = ""
	servery = str(servery.capitalize())
	#await ctx.send(servery)

	#adding case for all serveries
	if servery == "All":
		str_output = ""
		for key in serv_dict.keys():
			str_output += " \n"
			str_output += "***" + str(key) + "***" + " \n"
			if len(serv_dict[key]) == 0:
				str_output += " is closed! \n"
				# str_output += "***" + str(key) + "***" + " is closed! \n"
				continue
			for item in serv_dict[key]:
				item = item.replace("amp;","")
				str_output += "- " + item + "\n"

	#case for Baker
	elif servery.__eq__("Baker"):
		str_key = "Baker College Kitchen"
		str_output += "***" + str_key + "*** \n"
		if len(serv_dict[str_key]) == 0:
			str_output = "***" + str_key + " is closed!***"
		else:
			for item in serv_dict[str_key]:
				item = item.replace("amp;","")
				str_output += "- " + item + "\n"
	
	#all other cases
	else:
		str_key = servery + " Servery"
		str_output += "***" + str_key + "*** \n"
		if len(serv_dict[str_key]) == 0:
			str_output = "***" + str_key + "***" + " is closed! \n"
		else:
			for item in serv_dict[str_key]:
				item = item.replace("amp;","")
				str_output += "- " + item + "\n"

	#sending the message
	#await ctx.send(servery + " is having the following for " + meal_name)
	await ctx.send(str_output)

asyncio.run(main())