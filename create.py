import sys
import os
from selenium import webdriver

path = "/C/pyProject"
webbrowser = webdriver.Chrome()
webbrowser.get('http://github.com/login')

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + folderName)
    python_button =webbrowser.find_element_by_xpath("//input[@name='login']")[0]
    python_button.click()

create()

