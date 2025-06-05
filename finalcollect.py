from bs4 import BeautifulSoup
import os
import json

products = []

for file in os.listdir("data"):
    try:
        with open(f"data/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, "html.parser")
    
        t = soup.find("h2")
        title = t.get_text().strip().replace('\n', ' ').replace('  ', ' ')
    
        link = "https://amazon.in/" + (t.find_parent("a")['href'])
    
        price = soup.find("span", class_="a-price-whole").get_text().strip()
    
        product = {
            'title': title,
            'price': f"₹{price}",
            'link': link,
            'file_source': file
        }
        
        products.append(product)
        print(f"Title: {title[:50]}...")
        print(f"Price: ₹{price}")
        print(f"Link: {link[:80]}...")
        print("-" * 80)
        
    except Exception as e:
        print(f"Error processing {file}: {e}")

# Save to JSON file
with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

print(f"\nTotal products scraped: {len(products)}")
print("Data saved to products.json")