# -*- coding: utf-8 -*-
from pyvirtualdisplay import Display
from selenium import webdriver
import time 

output = open('top_twitch_sully_7dollowup.tsv', 'w+')


#textResults = []
with Display():
    driver = webdriver.Firefox()
    driver.get('https://sullygnome.com/channels/watched')
    time.sleep(15)
    for i in range(10):
        results = driver.find_elements_by_xpath('//*[@id="tblControl"]/tbody/tr')
        for result in results:
            #textResults.append([cell.text for cell in result.find_elements_by_tag_name('td')])
            try:
                #output.write('\t'.join([cell.text for cell in result.find_elements_by_tag_name('td')]) + '\n')
                print('\t'.join([cell.text.encode('utf-8') for cell in result.find_elements_by_tag_name('td')]) + '\n')
            except Exception as e:
                print(e)
        button = driver.find_elements_by_xpath('//*[@id="tblControl_next"]')[0]
        button.click() # go to next page
        time.sleep(5)
        print("On Page " + str(i))

    driver.quit()