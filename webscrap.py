
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup


my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"

uclient = ureq(my_url)
page_html = uclient.read()
uclient.close

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"item-container"})

filename = "GraphicsProducts.csv"
f = open(filename,"w")

headers = "Product name, Shipping cost\n"
f.write(headers)

for container in containers:
    product = container.a.img["title"]

    shipping_container = container.findAll("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print("Product name: " + product)
    print("Shipping cost: " + shipping)
    print("\n")

    f.write(product.replace(",","|") + "," + shipping + "\n")

f.close()
