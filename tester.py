from bs4 import BeautifulSoup
import requests
import csv
import datetime


def read_csv():
    with open('sources.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        print(csv_reader)

    while True:
        to_read = input("""What do you want me to read for you?
        A) All links
        B) The latest link
        C) Titles only\n>""").lower()
        
        if to_read == "a":
            print("do this")
            break
        elif to_read == "b":
            print("do this")
            break
        elif to_read == "c":
            print("do this")
            break
        else:
            print("Sorry, I don\'t understand what \'{}\' means, please try again\n".format(to_read))
        

    # with open('sources.csv', 'w') as csv_write:
    #     csv_writer = csv_writer(csv_write)

read_csv()
