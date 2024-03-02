from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('https://mail.yahoo.com')

signin_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Sign in')))
signin_button.click()

# You should interact with elements after the page has loaded, so it's better to wait for the element to be present
username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'login-username')))
# Now you can interact with the element
username_field.click()
username_field.clear()
username_field.send_keys("yourUserName")#eg: yohan_saby@yahoo.co.in
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'login-signin'))).click()

# You should interact with elements after the page has loaded, so it's better to wait for the element to be present
passwordField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'login-passwd')))
# Now you can interact with the element
passwordField.click()
passwordField.clear()
passwordField.send_keys("yourPassword")

#Sing In
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'login-signin'))).click()
while(True):
    print ('deleting')
    
    # I had superslow internet and hence i gave implicit wait 30. You can ofcourse reduce it 
    # but it actually won't matter since its implicit wait.
    driver.implicitly_wait(30)
    checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-test-id="checkbox"]')))
    i = 0
    ''' 
    There are arbitarily 10 attempts made to select the checkbox. 
    The reason it is put in while loop is because sometimes for unknown reasons the checkbox is not selected in one go.
    Also, if there are no more mails to be deleted then the loop might go infinte. Hence, I arbitarily chose 10 attempts
    '''
    while i < 10:
        checkbox.click()
        # Introduce a small delay to allow the checkbox to update its state
        time.sleep(1)
        if checkbox.get_attribute("aria-checked") == "true":
            break
        i += 1

    if checkbox.get_attribute("aria-checked") == "true":
        wait = WebDriverWait(driver, 30)#arbitary wait time
        delete_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[data-test-id="toolbar-delete"]')))
        delete_button.click()
        
        time.sleep(3)#sleeping as yahoo mail takes some time if there are lot of messages to be deleted.
        print ('deleted')
    else:
        print ('Looks like there are no more mails to delete')
        break
