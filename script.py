from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

import time

import argparse


def send_text(num, driver, message):
    # divided the url into 2 parts
    url_fhalf = "https://web.whatsapp.com/send/?phone="
    url_shalf = "&text&app_absent=0"
    inp_xpath = (
        "/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]"
    )
    wait = WebDriverWait(driver, 600)

    driver.get(url_fhalf + num + url_shalf)
    input_box = wait.until(presence_of_element_located((By.XPATH, inp_xpath)))
    input_box.send_keys(message + Keys.ENTER)

    print(f"Message sent to {num}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("nums", help="List of numbers", type=list)
    parser.add_argument("message", help="Message text to be sent", type=str)
    parser.add_argument(
        "--chrome",
        action="store_true",
        help="Use chrome as the WebDriver (default is Firefox)",
    )

    args = parser.parse_args()
    numbers = args.nums
    message = args.message
    if args.chrome:
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    for i in numbers:
        send_text(i, driver, message)
        time.sleep(25)
    driver.close()