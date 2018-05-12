from bs4 import BeautifulSoup
import requests
import csv
import datetime

print(requests)








def open_csv():
    with open('sources.csv', "rw") as csv_file:
        pass

def give_link():
    global link
    link = input("please give the link you\'d like to save\n> ")


def open_link(link):
    page = requests.get(link)
    print(page)





running = True
while running: 
    give_link()
    open_link(link)
    running = False


# def save_to_csv:
#     dunno how to do this yet, read docs boi
