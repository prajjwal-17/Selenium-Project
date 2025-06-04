from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query= "laptop"
for i in range(1,20):
    driver.get(f"https://www.amazon.in/s?k=laptop&page={i}&crid=217F29KATSHVE&qid=1749051180&sprefix=laptop+u%2Caps%2C284&xpid=uZcVnQ4jbLd9Y&ref=sr_pg_2")


    elems=driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"{len(elems)} items found")
    for elem in elems:
        print(elem.text)

# print(elem.text)

    time.sleep(4)
    driver.close()
    

