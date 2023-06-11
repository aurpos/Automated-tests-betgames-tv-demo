import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
 
def wait (seconds):
    time.sleep(seconds)

print('TC_001')

driver = webdriver.Chrome()
driver.get('https://demo.betgames.tv')
driver.maximize_window()

# enter the message 
message_field = driver.find_element(By.ID, "message")
message_field.send_keys("Test message") 
message_value = message_field.get_attribute('value')
value_lenght = len(message_value)
assert value_lenght > 0, "Message field is empty."
print("Message '%s' is entered." % message_value)
print("Message length: ", value_lenght)

# enter the correct email
email_field = driver.find_element(By.ID, "email")
email_field.send_keys("test@mail.com")
email_value = email_field.get_attribute('value')
assert email_value == "test@mail.com", "Email is incorrect."
print("Email '%s' is entered." % email_value)

# click the button 'Send'
button_xpath = "//button[@class='send btn btn-primary pull-left']"
driver.find_element(By.XPATH, button_xpath).click()
print("The button 'SEND' is pressed.")

# check if message 'Your message is sent' appears
wait(3)
text = "Your message is sent."
text_element = driver.find_element(By.ID,"send")
send_text = text_element.get_attribute('innerText')
assert text == send_text, "Text is incorrect after sending."
print("The message is send successfully.")

driver.quit()
print("TC_001 is passed.")