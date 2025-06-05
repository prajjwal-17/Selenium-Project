from bs4 import BeautifulSoup
import os

d={'title': [], 'price':[], 'link':[]}

for file in os.listdir("data"):
    try:
        
        with open(f"data/{file}") as f:
            html_doc=f.read()
        soup = BeautifulSoup(html_doc,"html.parser")
    
        t = soup.find("h2")
        title = t.get_text().strip().replace('\n', ' ').replace('  ', ' ')
    
        link = "https://amazon.in/"+(t.find_parent("a")['href'])
    
        price = soup.find("span", class_="a-price-whole").get_text().strip()
    
        d['title'].append(title)
        d['price'].append(price)
        d['link'].append(link)
    
        print(title, price, link)
    except Exception as e:
        print(e)
        