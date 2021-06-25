import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/dp/B07CJ7NJHG/ref=redir_mobile_desktop?_encoding=UTF8&aaxitk=144591a2fb2e7473fb9b908941a73db4&hsa_cr_id=3765222870802&pd_rd_plhdr=t&pd_rd_r=c8f6df54-b8bc-466e-93c7-ecb7a81251b5&pd_rd_w=2W5H5&pd_rd_wg=m7bSy&ref_=sbx_be_s_sparkle_mcd_asin_0_img'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify)

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    
    current_price  =price.replace(',','')


    converted_price = float(current_price[1:10])

    if (converted_price > 14000):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('saju.sajjan@gmail.com', 'cptjylyjkqkesufd')
    subject = 'Price fell down!'
    body = 'check the amazon link https://www.amazon.in/dp/B07CJ7NJHG/ref=redir_mobile_desktop?_encoding=UTF8&aaxitk=144591a2fb2e7473fb9b908941a73db4&hsa_cr_id=3765222870802&pd_rd_plhdr=t&pd_rd_r=c8f6df54-b8bc-466e-93c7-ecb7a81251b5&pd_rd_w=2W5H5&pd_rd_wg=m7bSy&ref_=sbx_be_s_sparkle_mcd_asin_0_img'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'saju.sajjan@gmail.com',
        'saju.sajjan@gmail.com',
        msg
        )
    print('HEY EMAIL HAS BEEN SENT!')

# print(converted_price)
# print(title.strip())

check_price()
