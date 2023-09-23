import discord
import requests
import datetime
from bs4 import BeautifulSoup
from discord.ext import commands
import asyncio

today = datetime.date.today()
weekday = today.weekday()
week_number = weekday + 1
print(week_number)

day_id = "block-views-block-day-menu-block-" + str(week_number)

menu = requests.get('https://dining.rice.edu/')
soup = BeautifulSoup(menu.text, 'html.parser')

today_menu = soup.find(id=day_id)
print(today_menu)
#print(soup.get_text())
#print(today_menu.find_all("div",{"class" : "mitem"}))
#print(soup.prettify())
menu_items = today_menu.find_all("div", class_="mname")
for item in menu_items:
    print(item.text)
servery = today_menu.find(string="Seibel Servery")
print(servery)