from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url) 