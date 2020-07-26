import bs4
import requests

def get_price(product_url):
    res = requests.get(product_url)
    res.raise_for_status()


    soup = bs4.BeautifulSoup(res.text, "html.parser")
    elems = soup.select("#main-content > div.grid-section-xs--gap-4.grid-section-m--gap-5 > div > div.grid-unit-xs--col-12.grid-unit-m--col-6.grid-unit-xl--col-5.js-sticky-bar-trigger > div > div.grid-section-xs--gap-4.grid-section-m--gap-5.js-order-block > div.is-hidden-until-size-m > div.js-desktop-order-block > div > div:nth-child(1) > div > div.flex-unit.space--right-2 > span > strong")

    return elems[0].text.strip()



price = get_price("https://www.coolblue.nl/product/805073/haier-hw80-b14636.html")
print("The price is " + price)