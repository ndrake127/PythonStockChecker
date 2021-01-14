import scraper
import smtplib
import ssl

port = 465

# Setting up email contents #

sender = input("Sender: ")
receiver = input("Recipient: ")

URL = input("Product URL: ")
product = scraper.get_product_name(URL)

subject = "Subject: Urgent\n"

message = product + " is now in stock at Best Buy\n"

password = input("Password: ")
print("")

#############################

context = ssl.create_default_context()


def notify():
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, subject + message + URL)