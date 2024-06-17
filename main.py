##################### Hard Starting Project ######################
import random
# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import smtplib
import datetime as dt
import pandas

MY_EMAIL = "someone@gmail.com"
MY_PASSWORD = "################"
TO_ADDRESS = "somebody@somewhere.com"

letters =["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
now = dt.datetime.now()

try:
    data = pandas.read_csv("birthdays.csv")
except FileNotFoundError:
    print("Error: no birthdays list found")
    exit()

contacts = data.values.tolist()
for row in contacts:
    if row[3] == now.month and row[4] == now.day:
        birthday_contact = row


if birthday_contact:
    letter = random.choice(letters)
    with open(letter,"r") as file:
        temp_message = file.read()

    birthday_message = temp_message.replace("[NAME]", birthday_contact[0])
    TO_ADDRESS = birthday_contact[1]

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_ADDRESS,
                            msg=f"Subject: Happy Birthday\n\n{birthday_message}")



