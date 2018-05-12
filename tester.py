from bs4 import BeautifulSoup
import requests
import csv
import datetime


def get_action():
    global action
    while True:
        action = input("""What do you want me to read for you?
        A) All links
        B) The latest link
        C) Titles only\n>""").lower()

        if action == "a":
            print("do this")
            break
        elif action == "b":
            print("do this")
            break
        elif action == "c":
            print("do this")
            break
        else:
            print("Sorry, I don\'t understand what \'{}\' means, please try again\n".format(
                action))


action = "a"
n = 2


def read_csv():
    with open('sources.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        if n == 1:
            for line in csv_reader:
                print(line)
        if action == "a":
            for line in csv_reader:
                print(line[2])
        elif action == "b":
            for line in csv_reader:
                print(row[2]line[2])

        else:
            print("wtf")
    # with open('sources.csv', 'w') as csv_write:
    #     csv_writer = csv_writer(csv_write)


read_csv()
