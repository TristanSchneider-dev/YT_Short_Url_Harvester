import time
import keyboard
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_url():
    print("Press Ctrl + C to exit...")
    url = "https://www.youtube.com/shorts"

    # Specify the path to the GeckoDriver
    gecko_driver_path = '\geckodriver_firefox_win_x64.exe'

    # Create and initialize the Service object
    service = Service(gecko_driver_path)
    driver = webdriver.Firefox(service=service)

    driver.get(url)  # Open the webpage

    # Accept cookies (YouTube banner)
    button = driver.find_element(By.CSS_SELECTOR, "button[data-idom-class='nCP5yc AjY5Oe DuMIQc LQeN7 IIdkle']")
    button.click()

    first_iteration = True
    previous_url = None

    while True:
        if keyboard.is_pressed('ctrl+c'):
            break

        # Scroll the webpage
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.PAGE_DOWN)

        # Save the URL of the scrolled page
        current_url = driver.current_url

        if first_iteration:
            first_iteration = False
        else:
            if current_url == previous_url:
                continue  # Skip this iteration
            else:
                save_url_to_file(current_url)   # Save the URL to a text file

        print(current_url)
        previous_url = current_url
        time.sleep(1.2)

    driver.quit()
    print("Scraper has been terminated.")


def save_url_to_file(url):
    with open("yt_short_urls.txt", "a") as file:
        file.write(url + "\n")


if __name__ == '__main__':
    get_url()
