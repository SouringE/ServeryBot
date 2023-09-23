import discord
import requests
import re
import datetime
from bs4 import BeautifulSoup
from discord.ext import commands
import asyncio

def item_text(item):
    start = re.escape(">")
    end   = re.escape("<")
    return re.search('%s(.*)%s' % (start, end), item).group(1)

today = datetime.date.today()
weekday = today.weekday()
week_number = weekday + 1
print(week_number)

day_id = "block-views-block-day-menu-block-" + str(week_number)

menu = requests.get('https://dining.rice.edu/')
soup = BeautifulSoup(menu.text, 'html.parser')

today_menu = soup.find(id=day_id)
#print(today_menu)
#print(soup.get_text())
#print(today_menu.find_all("div",{"class" : "mitem"}))
#print(soup.prettify())
#menu_items = today_menu.find_all("div", class_="mname")

str_menu = str(today_menu)
current_serv = ""
serv_dict = {"Seibel Servery" : [], "South Servery" : [], "West Servery" : [], "North Servery" : [], "Baker Kitchen" : []}


for item in str(today_menu).splitlines():
    if "Servery" in item:
       item_name = item_text(item)
       # print(item_name)
       current_serv = item_name
    if "mname" in item:
        item_name = item_text(item)
        serv_dict[current_serv].append(item_name)
       
       
    #if "Servery" in str(item):
    #    print(item)
    #menu_items = item.find_all("div", class_="mname")

#for item in menu_items:
    #rint(item.text)
print(serv_dict)
print()
# servery = today_menu.find(string="Seibel Servery")
# print(servery)

print("Seibel:")
for item in serv_dict["Seibel Servery"]:
    print("- " + item)
print()

print("North:")
for item in serv_dict["North Servery"]:
    print("- " + item)
