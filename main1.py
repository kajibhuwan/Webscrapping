import requests
from bs4 import BeautifulSoup

url= input("enter your website url")
response= requests.get(url)

filename="temp.html"
bs= BeautifulSoup(response.text, "html.parser")

format_text=bs.prettify()
#print(format_text)

with open(filename, "w+") as f:
    f.write(format_text)



list_imgs= bs.find_all('img')
#print(list_imgs)
no_of_img= len(list_imgs)

list_anchor= bs.find_all('a')
no_of_anchor= len(list_anchor)

print("number of img tags", no_of_img)
print("number of anchor tage", no_of_anchor)
