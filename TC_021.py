import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def wait (seconds):
    time.sleep(seconds)

print('TC_021')

driver = webdriver.Chrome()
driver.get('https://demo.betgames.tv')

# maximize the browser
driver.maximize_window()

# change the display
driver.switch_to.frame(driver.find_element(By.ID, "betgames_iframe"))
wait(5)

# select a game Lucky 7
lucky_7_path = "//button[@data-qa='button-game-menu-1']"
driver.find_element(By.XPATH, lucky_7_path).click()
print("The content of the Lucky 7 game is opened.")
wait(5)

# select a tab 'Numbers'
tab_path = "//button[@data-qa='button-odds-tab-15']"
driver.find_element(By.XPATH, tab_path).click()
print("The tab 'Numbers' is selected.")

# select a bet area 'Selected ball will be dropped with No. 1,...,42'
driver.find_element(By.XPATH, "//div[@data-qa='area-odd-item-1']").click()
print("The bet area is selected.")

# select a number 14 
driver.find_element(By.XPATH, "//span[@data-qa='area-selectable-item-14']").click()
print("The number 14 is selected.")

# confirm a number 14
driver.find_element(By.XPATH, "//button[@data-qa='button-odd-item-dropdown-confirm']").click()
print("The button 'Confirm' is pressed.")

# check if an input exists and enter a bet amount
try:
    bet_amount = driver.find_element(By.XPATH, "//input[@data-qa='input-bet-slip-amount']")
    print("Input text field exists.")
    bet_amount.clear()
    wait(3)
    
    print("Iteration numbers: ")
    for i in range (3):     #set the cursor to the 3rd place of the input
        bet_amount.send_keys(Keys.LEFT)
        print(i)
    
    wait(5)
    value = "1.33" 
    value_characters = [*value]

    # enter a bet amount
    print("Value characters: ")
    for i in range(len(value_characters)):
        bet_amount.send_keys(value_characters[i])  # enter i character to imput
        print(value_characters[i])
        wait(0.5)
        
    entered_value = bet_amount.get_attribute('value')

    print("The bet amount " + entered_value + " is entered.") 
    assert value == entered_value, "The amount is entered incorrectly."
    wait(3)
except NoSuchElementException:
    print("Input text field does not exist.")

# place a bet
driver.find_element(By.XPATH, "//button[@data-qa='button-place-bet']" ).click()
print("The bet is placed.")

wait(2)

# check if bet is successful;
# check if bet appears at the bet history 
assert driver.find_element(By.XPATH, "//span[@data-qa='text-bet-slip-notification']").get_attribute('innerText') == "Bet accepted.","Bet notification does not appear."
assert driver.find_element(By.XPATH, "//span[@data-qa='text-odd-title']").get_attribute('innerText') == "Selected ball will be dropped with No. 1,...,42", "The bet does not appear in the bet history."

print("The bet is placed successfully")
print("The TC_021 is passed.")


