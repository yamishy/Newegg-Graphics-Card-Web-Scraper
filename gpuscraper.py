import csv #import csv to write to csv file
from bs4 import BeautifulSoup #import beautiful soup to parse html
from urllib.request import urlopen as request #import request to open url
import regex #import regex to search for specific text
import re 


#website url of the page were scraping // GeForce RTX 40 Series
url = "https://www.newegg.com/p/pl?N=100007709%20601408872"

#open connection, grab the page
client = request(url)

#parse the html
page_html = client.read()

#close the connection
client.close()

#html parsing
doc = BeautifulSoup(page_html, "html.parser")

#grabs each product
lists = doc.find_all("div", {"class":"item-container"})

#open csv file to write to
filename = "gpu.csv"

#write to csv file
f = open(filename, "w", newline="")
writer = csv.writer(f) 
writer.writerow(["Brand", "Name", "Price"]) 



#loop through each item
for list in lists:
    #get brand name of item
    item_brand = list.find("img", {"src": regex.compile(r"//c1.neweggimages.com/Brandimage_70x28")}).get("title") 

    #get item name
    title_list = list.findAll("a", {"class":"item-title"})
    item_name = title_list[0].text

    #get price: find > get text > clean up
    price_list = list.findAll("li", {"class":"price-current"})
    item_price = price_list[0].parent #returns price 
    item_price = "$" + item_price.find("strong").string + item_price.find("sup").string #returns price

    #print to console to display data
    print("Brand: " + item_brand)
    print("Name: " + item_name)
    print("Price: " + item_price)

    #write to csv file  
    writer.writerow([item_brand, item_name, item_price])

#close csv file
f.close()

