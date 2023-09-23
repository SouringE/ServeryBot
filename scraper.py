import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
import asyncio

menu = requests.get('https://dining.rice.edu/')
ah = BeautifulSoup(menu.text, 'html.parser')

print(ah.get_text())