import json
from easygui import *

from defs import *

inventoryPath = os.path.join('data', 'Menu.json')
koshel = os.path.join('data', 'KoselAll.json')
clientsPath = os.path.join('data', 'clients_baza.json')
Personal = os.path.join('data', 'Personal.json')
with open(inventoryPath, "r", encoding='utf-8') as menu:
    base_menu = json.load(menu)

coffemenu = ('images\\c5d3533af5a86bd4966d9206c4ddaaee.gif', 'images\\da318526245381.563536837107b.gif',
             'images\\b8a2d007e93b475b92aea523f75feb92.gif')
cmakolikmenu = ('images\\1115353179b2a4213ea888579cf50635.gif', 'images\\original.gif', 'images\\croisant.gif')

while True:
    choice = msgbox("Ласкаво просимо в кав'ярню", 'CoffeeShop', 'Перейти до покупок', image='images\\212409.gif')
    with open(inventoryPath, "r", encoding='utf-8') as menu:
        base_menu = json.load(menu)
        while True:
            choice = buttonbox("Що бажаєте купити?: ", "CoffeeShop", ['Кава', "Смаколики", "Відміна"],
                               image='images\\763a73bb9b8e0bdf01e02f523946a313.gif')
            if choice == "Кава":
                but = []
                [but.append(i) for i in base_menu[choice].keys()]
                but.append("Відміна")
                lst = ""
                for txt in base_menu.get(choice):
                    lst += f'{txt} - {base_menu.get(choice).get(txt).get("Ціна")} {base_menu.get(choice).get(txt).get("Валюта")}\n'
                choise = buttonbox(lst, "CoffeeShop", but, coffemenu)
                if choise != "Відміна":
                    Counting(choice)
                else:
                    continue

                Сhoice_of_milk(choice)
                Discount()
                Receipt()
                msgbox("Відскануйте QR код для оплати", image='images\\56.gif')
                # pay = input("Зчитування")
                Payment()

            elif choice == "Смаколики":
                but = []
                [but.append(i) for i in base_menu[choice].keys()]
                but.append("Відміна")
                lst = ""
                for txt in base_menu.get(choice):
                    lst += f'{txt} - {base_menu.get(choice).get(txt).get("Ціна")} {base_menu.get(choice).get(txt).get("Валюта")}\n'
                choise = buttonbox(lst, "CoffeeShop", but, cmakolikmenu)
                if choise != "Відміна":
                    Counting(choice)
                else:
                    continue

                Discount()
                Receipt()
                msgbox("Відскануйте QR код для оплати", image='images\\56.gif')
                # pay = input("Зчитування")
                Payment()

            elif choice == 'Відміна':
                Cleaning_basket()
                break
