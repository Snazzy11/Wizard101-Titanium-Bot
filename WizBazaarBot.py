import pyautogui
pyautogui.FAILSAFE = True

from time import sleep

import os

# HERE IS THE LOCATION YOU NEED TO CHANGE AS SPECIFIED IN 'README'; PUT IN THE DIRECTORY THAT THESE FILES ARE LOCATED
# THE EXECUTEABLE AND THE IMAGE TO LOOK FOR SHOULD BOTH BE IN THE FOLDER THIS POINTS TO
os.chdir(r'FILL IN HERE')


pyautogui.size()
(1920, 1080)

pyautogui.useImageNotFoundException()

def main():
    input('Press enter to start, then it will start in 6 seconds')
    for i in range(6, 0, -1):
            print(f"Countdown: {i}")
            sleep(1)
            i += 1

    while True:

        # drag to reagent button
        pyautogui.moveTo(515, 275)
        pyautogui.click()
        sleep(1.05)

        # drag to name button
        pyautogui.moveTo(950, 345)
        pyautogui.click()
        sleep(0.05)

        # look for titanium
        try:
            # If the titanium is showing on-screen but the bot is not clicking on it, you may have to adjust this 'confidence' value
            titanium_location = pyautogui.locateOnScreen('titanium.png', confidence=0.7)
            # drag to titanium
            pyautogui.moveTo(titanium_location)
            pyautogui.click()
            sleep(0.05)
        
            # drag to buy button
            pyautogui.moveTo(620, 815)
            pyautogui.click()
            sleep(0.05)
        
            # drag to max buy slider
            pyautogui.moveTo(1108, 617)
            pyautogui.click()
            sleep(0.05)
        
            # drag to 2nd buy button
            pyautogui.moveTo(820, 800)
            pyautogui.click()
            sleep(0.5)
        
            # drag to ok button
            pyautogui.moveTo(1135, 620)
            pyautogui.click()    #x: 515 y:275

            sleep(0.05) 
            continue
        except:
            continue
        
       




main()

# pixel locations
# reagent button 
# name button
    #x: 950 y: 345
# buy button   
    #x: 620 y: 815
# max buy slider
    #x: 1117 y: 614
# 2nd buy button
    #x: 820 y: 800
# ok button
    #x: 1135 y: 620
