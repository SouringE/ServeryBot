import requests
import re
import datetime
from bs4 import BeautifulSoup

# Allows me to get only the text (part between <> <>) of an HTML element from a string
def item_text(item):
    start = re.escape(">")
    end   = re.escape("<")
    return re.search('%s(.*)%s' % (start, end), item).group(1)

# Gets the menu data for only today's block in the HTML, since the HTML has menu data
# for all days but only today's is visible
def get_menu():
    today = datetime.date.today()
    weekday = today.weekday()
    week_number = weekday + 1
    #print(week_number)
    day_id = "block-views-block-day-menu-block-" + "2" # str(week_number)

    # Today's Rice dining website
    # url = 'https://dining.rice.edu/'

    # Found this on internet archive for more test cases :D
    url = "https://web.archive.org/web/20230829132709/https://dining.rice.edu/"

    menu = requests.get(url)
    soup = BeautifulSoup(menu.text, 'html.parser')

    # today_menu is only the block containing the menu for today
    today_menu = soup.find(id=day_id)

    # This finds whether it's lunch or dinner. (Have to test whether it works for dinner during dinner lol)
    meal = today_menu.find("h2")
    meal_name = item_text(str(meal))

    # Dictionary mapping servery names to a list of the menu items in that servery
    serv_dict = {"Seibel Servery" : [], "South Servery" : [], "West Servery" : [], "North Servery" : [], "Baker College Kitchen" : []}
    #  Sets which servery the menu items are added to in the dictionary
    current_serv = ""

    # Iterates through every line in the today_menu block of HTML
    for item in str(today_menu).splitlines():
        # Sets the current servery if it finds a line of HTML text that has a servery name
        if "Servery" in item or "Baker" in item:
            item_name = item_text(item)
            # print(item_name)
            current_serv = item_name
        # Finds the menu items and adds them to the list in the dictionary for the current menu item
        if "mname" in item:
            item_name = item_text(item)
            serv_dict[current_serv].append(item_name)
    return serv_dict

# Prints out serv_dict so you can see it when the loop is done
serv_dict = get_menu()
print(serv_dict)
print() 

# This is just example print statements for how you can use the dictionary
#print(meal_name + " menu for today:")
print("-------------------------")

print("Seibel:")
for item in serv_dict["Seibel Servery"]:
    print("- " + item)
print()

print("Baker:")
for item in serv_dict["North Servery"]:
    print("- " + item)