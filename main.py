import time
import mail
import scraper

in_stock = mail.product + " in stock, notifying you now.\nHave a nice day."
out_stock = mail.product + " out of stock, trying again in:"

request_rate = 10

while True:
    if not scraper.check_stock():
        print(in_stock)
        mail.notify()
        break
    else:
        print(out_stock)

        for x in range(request_rate):
            print(request_rate-x)
            time.sleep(1)

        print("")
