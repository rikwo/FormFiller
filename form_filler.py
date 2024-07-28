from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = "C:\Users\Ricky\Desktop\chromedriver-win64\chromedriver"
service = Service(executable_path=path)
website = ''

driver = webdriver.Chrome(service=service)
driver.get(website)

fields = ['Name', 'Email', 'Address', 'Phone number', 'Province']
data = ['Wai Kiu Ricky Kwong', '1005-13696 100 Avenue','wkk4@sfu.ca', '778-898-3013', 'BC']

my_form = dict(zip(fields, data))

def fill_text_field(element, value):
    element.clear()
    element.send_keys(value)

def fill_dropdown(element, value):
    from selenium.webdriver.support.ui import Select
    select = Select(element)
    select.select_by_visible_text(value)

def fill_form_field(field, value):
    try:
        text_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//input[@name="{field}"] | //input[@id="{field}"] | //textarea[@name="{field}"] | //textarea[@id="{field}"]')))
        fill_text_field(text_input, value)
    except:
        pass

    try:
        dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//select[@name="{field}" or @id="{field}"]')))
        fill_dropdown(dropdown, value)
    except:
        pass


for field, data in my_form.items():
    fill_form_field(field, data)

driver.quit()
