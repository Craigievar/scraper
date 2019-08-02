# -*- coding: utf-8 -*-

from selenium import webdriver

output = open('top_twitch_sully_7dollowup.tsv', 'w+')
driver = webdriver.Chrome()
driver.get('https://sullygnome.com/channels/watched')

#textResults = []
for i in range(10):
    results = driver.find_elements_by_xpath('//*[@id="tblControl"]/tbody/tr')
    for result in results:
        #textResults.append([cell.text for cell in result.find_elements_by_tag_name('td')])
        try:
            output.write('\t'.join([cell.text for cell in result.find_elements_by_tag_name('td')]) + '\n')
        except:
            print("Uhhh error")
    button = driver.find_elements_by_xpath('//*[@id="tblControl_next"]')[0]
    button.click() # go to next page
    time.sleep(5)
    print("On Page " + str(i))