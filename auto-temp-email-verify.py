import time 
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from html.parser import HTMLParser


driver = webdriver.Chrome("./chromedriver")
driver.get("https://console.mail7.io/admin/inbox/inbox?username=anh-giang")

# Wait until email loaded
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#depublicemailinbox > li")))
print("root wait 1")
# Wait 2 more seconds to make sure it fully loaded
time.sleep(2)
print("root wait 2")
email_group = driver.find_element(By.ID, "depublicemailinbox")
email_list = email_group.find_elements(By.TAG_NAME, "li")
print("email len", len(email_list))
print("email:")
for email in email_list:
    title = email.find_element(By.TAG_NAME, "p")
    content = email.find_element(By.CLASS_NAME, "subject")
    print(title.text)
    print(content.text)
    print()

    if ("airtable" in title.text.lower() and "Please confirm your email" in content.text):
        print("I fucking found it")
        print("Here is the link")
        print(re.search("(?P<url>https?://[^\s]+)", content.text).group("url"))
        # Note to self: for some reason, the verification email content has hyperlink display as plain text inside it. Other email
        # don't, instead just appear as the hyperlink name ("Click here" or "Check this guideb  ")
        break

driver.close()