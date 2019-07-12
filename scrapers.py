import requests

from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.de/Sony-Systemkamera-Megapixel-LCD-Display-SEL-P1650/dp/B00IE9XHE0/ref=sr_1_fkmr0_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=sony+alpha+ilce-7MS&qid=1562952054&s=gateway&sr=8-1-fkmr0'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
def check_price():
    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()

    price = soup.find( id = "priceblock_ourprice").get_text()
    converted_price = int(price[0:3])

    if(converted_price < 530):
        send_mail()

    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 530)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('lopeselio@gmail.com', gfiakovningrvsop)
    subject = 'Hey! The price fell down'
    body = 'Check the amazon link https://www.amazon.de/Sony-Systemkamera-Megapixel-LCD-Display-SEL-P1650/dp/B00IE9XHE0/ref=sr_1_fkmr0_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=sony+alpha+ilce-7MS&qid=1562952054&s=gateway&sr=8-1-fkmr0'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'lopeselio@gmail.com',
        'eliojordan.lopes2018@vitstudent.ac.in',
        msg
    )

    print('Hey an Email Has been sent!')

    server.quit()

while(True)
    check_price()
    time.sleep(60 * 60) 






