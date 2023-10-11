# Importing required libraries

# pip install selenium

from selenium import webdriver
import selenium.webdriver.common.keys
import time

# Setting up the webdriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Navigating to the Star Alliance homepage
driver.get("https://www.staralliance.com/en/home")
time.sleep(10)

# Clicking to accept cookie
cookie_button = driver.find_element("xpath","/html/body/div[11]/div/div/div[3]/div/div/p[3]")
cookie_button.click()
time.sleep(5)

# Clicking for flight search
flight_search_button = driver.find_element("id","fSearchContainer")
flight_search_button.click()
time.sleep(5)

# Selecting roundtrip flight
#round_trip_button = driver.find_element("xpath","/html/body/div[3]/div[3]/div[1]/div/div/div/div/div[3]/section/div/div[2]/div/div/div/div/div/div/ul/li[1]/div/section/div/div[2]/div/div/div/div/div[1]/a[1]")
#round_trip_button.click()

# Finding the Origin "From" bar and entering text
origin_bar = driver.find_element("id","airportFrom")
origin_bar.send_keys("Toronto-Lester B. Pearson [YYZ], Canada")
#origin_bar.click()
time.sleep(5)

# Finding the Destination "To" bar and entering text
destination_bar = driver.find_element("id","airportTo")
destination_bar.send_keys("Los Angeles International [LAX], United States")
time.sleep(5)


# Finding the Departure date bar and entering text
departure_date_bar = driver.find_element("id","datepickerDepart")
#departure_date_bar.send_keys("17/02/2024")
departure_date_bar.click()
time.sleep(5)
click_next = driver.find_element("xpath", "/html/body/div[3]/div[3]/div[1]/div/div/div/div/div[3]/section/div/div[2]/div/div/div/div/div/div/ul/li[1]/div/section/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/p[1]/div/div/a/span")
click_next.click()
time.sleep(5)
click_date_from = driver.find_element("xpath", "/html/body/div[3]/div[3]/div[1]/div/div/div/div/div[3]/section/div/div[2]/div/div/div/div/div/div/ul/li[1]/div/section/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/p[1]/div/table/tbody/tr[3]/td[7]/a")
click_date_from.click()
time.sleep(5)

# Finding the Return date bar and entering text
return_date_bar = driver.find_element("id","datepickerArrive")
#return_date_bar.send_keys("24/02/2024")
return_date_bar.click()
#click_next2 = driver.find_element("xpath", "/html/body/div[3]/div[3]/div[1]/div/div/div/div/div[3]/section/div/div[2]/div/div/div/div/div/div/ul/li[1]/div/section/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/p[1]/div/div/a/span")
#click_next2.click()
time.sleep(5)
click_date_to = driver.find_element("xpath", "/html/body/div[3]/div[3]/div[1]/div/div/div/div/div[3]/section/div/div[2]/div/div/div/div/div/div/ul/li[1]/div/section/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/p[2]/div/table/tbody/tr[4]/td[7]/a")
click_date_to.click()
time.sleep(5)


# Selecting Search flights button
search_flight_button = driver.find_element("xpath","/html/body/div[3]/div[3]/div[1]/div/div/div/div/div[3]/section/div/div[2]/div/div/div/div/div/div/ul/li[1]/div/section/div/div[2]/div/div/div/div/div[1]/form/div/div[2]/div/button")
#search_flight_button = driver.find_element("id", "bkmgFlights_findButton")
search_flight_button.click()

# Waiting for the search results page to load
time.sleep(5)

# Selecting flight and book via airline
book_via_airline_button = driver.find_element("xpath","/html/body/div[3]/div[3]/div[1]/div/div/div/div/div/section/div/div[2]/div/div[3]/div[1]/div/div[6]/div[1]/div[2]/div[2]/a")
book_via_airline_button.click()

# Waiting for the search results page to load
time.sleep(40)


# Verifying that the laptop has been added to the cart
# cart_count = driver.find_element("id","nav-cart-count")
# assert cart_count.text == "1"
# cart_count.click()

# Closing the webdriver
driver.close()

