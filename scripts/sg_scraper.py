# -*- coding: utf-8 -*-
# import libraries
# import urllib.request as request
# from bs4 import BeautifulSoup
# import csv
# import requests
from selenium import webdriver
import time
# import time
# import pprint
# import webapp2


# output = open('top_twitch_sully_7dollowup.tsv', 'w+')
# driver = webdriver.Chrome()
# driver.get('https://sullygnome.com/channels/watched')

# #textResults = []
# for i in range(2000):
#     results = driver.find_elements_by_xpath('//*[@id="tblControl"]/tbody/tr')
#     for result in results:
#         #textResults.append([cell.text for cell in result.find_elements_by_tag_name('td')])
#         try:
#             output.write('\t'.join([cell.text for cell in result.find_elements_by_tag_name('td')]) + '\n')
#         except:
#             print("Uhhh error")
#     button = driver.find_elements_by_xpath('//*[@id="tblControl_next"]')[0]
#     button.click() # go to next page
#     time.sleep(5)
#     print("On Page " + str(i))


def scrape(script, time_range, response):
    base_urls = {
        'twitch_follow': 'https://sullygnome.com/channels/{}/mostfollowers',
        'twitch_wt': 'https://sullygnome.com/channels/{}/watched',
        'twitch_languagegames': 'test',
    }

    data_header = 'TODO'

    url = base_urls[script].format(time_range)
    driver = webdriver.Chrome()
    driver.get(url)

    #textResults = []
    for i in range(10):
        results = driver.find_elements_by_xpath('//*[@id="tblControl"]/tbody/tr')
        for result in results:
            #textResults.append([cell.text for cell in result.find_elements_by_tag_name('td')])
            try:
                # output.write('\t'.join([cell.text for cell in result.find_elements_by_tag_name('td')]) + '\n')
                response.write('\t'.join([cell.text for cell in result.find_elements_by_tag_name('td')]) + '\n')
            except:
                response.write("Uhhh error")
        button = driver.find_elements_by_xpath('//*[@id="tblControl_next"]')[0]
        button.click() # go to next page
        time.sleep(5)
        response.write("On Page " + str(i))
    response.write('\n'+url)