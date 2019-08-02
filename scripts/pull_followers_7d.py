from pyvirtualdisplay import Display
from selenium import webdriver
import time
from datetime import date

import mysql.connector

ds = date.today()

cnx = mysql.connector.connect(user='csfb', password='beepboop',
                              host='csfb.mysql.pythonanywhere-services.com',
                              database='csfb$scrapes')

cursor = cnx.cursor()

add_row = ("INSERT INTO followers_7d "
               "(channel, watch_time, stream_time, peak_viewers, average_viewers,"
               "followers, followers_gained, partnered, mature, language, ds) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

with Display():
    driver = webdriver.Firefox()
    driver.get('https://sullygnome.com/channels/mostfollowers')
    time.sleep(15)
    print("start")
    for i in range(200):
        results = driver.find_elements_by_xpath('//*[@id="tblControl"]/tbody/tr')
        if len(results) == 0:
            time.sleep(15)
            results = driver.find_elements_by_xpath('//*[@id="tblControl"]/tbody/tr')

        for result in results:
            #textResults.append([cell.text for cell in result.find_elements_by_tag_name('td')])
            try:
                data_raw = [cell.text.encode('utf-8') for cell in 
                    result.find_elements_by_tag_name('td')]

                data_row = (
                    data_raw[2], #channel
                    int(data_raw[3].replace(',','').replace('hour','').replace('s','')), # whours
                    int(data_raw[4].replace(',','').replace('hour','').replace('s','')), # bhours
                    int(data_raw[5].replace(',','')), #peak
                    int(data_raw[6].replace(',','')), #avg
                    int(data_raw[7].replace(',','')), #fol
                    int(data_raw[8].replace(',','')), #new fol
                    data_raw[9], #partner
                    data_raw[10], #mature
                    data_raw[11], #labg 
                    ds
                )

                #print(data_row)

                cursor.execute(add_row, data_row)
                #print('\t'.join([cell.text.encode('utf-8') for cell in result.find_elements_by_tag_name('td')]) + '\n')
            except Exception as e:
                print(e)

        cnx.commit()

        button = driver.find_elements_by_xpath('//*[@id="tblControl_next"]')[0]
        button.click() # go to next page
        time.sleep(5)
        print("On Page " + str(i))

    driver.quit()

cursor.close()
cnx.close()
