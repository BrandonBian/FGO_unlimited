import pyautogui
import time
import sys
from PIL import Image
import numpy
import os

# pyautogui.FAILSAFE = False
pyautogui.PAUSE = 1

# while(1):
#    time.sleep(3)
#    if(pyautogui.position()==(0,899)):
#        break

SKIP_SUPPORT = False

print('Please go to the correct window...')


def prep():
    pyautogui.FAILSAFE = False
    while True:
        x, y = pyautogui.position()

        if x <= 100 and y <= 100:
            print("Program Started...")
            time.sleep(2)
            pyautogui.moveTo(x=78, y=693)
            pyautogui.FAILSAFE = True
            return


def reco():
    return pyautogui.locateOnScreen('castoria_support.png', confidence=0.90)


def drag():
    pyautogui.moveTo(x=1880, y=330)  # Select drag bar
    time.sleep(2)
    pyautogui.dragTo(x=1880, y=600, duration=4, button='left')


def refresh():
    pyautogui.click(x=1276, y=189)  # Select refresh
    time.sleep(2)
    pyautogui.click(x=1256, y=844)  # Select confirm


def supportselect():
    if not SKIP_SUPPORT:
        while (1):
            pyautogui.click(x=649, y=188)  # Caster
            temp = reco()
            if temp != None:  # Found support
                time.sleep(2)
                pyautogui.click(x=temp[0] - 100, y=temp[1])  # Select that support
                break
            else:
                drag()
                time.sleep(2)
                temp = reco()
                if temp != None:
                    # print(temp)
                    time.sleep(2)
                    pyautogui.click(x=temp[0] - 100, y=temp[1] - 100)
                    break
                else:
                    refresh()
                    time.sleep(5)
    time.sleep(3)
    pyautogui.click(1741, 994)  # Start mission


def unlimitedpool():
    pyautogui.FAILSAFE = True

    while True:
        temp = pyautogui.locateOnScreen('load_finished.png', confidence=0.90)
        if temp == None:
            time.sleep(1)
        else:
            time.sleep(1)
            break


    # Phase 1
    pyautogui.click(x=112, y=869)  # Support skill 1

    while True:
        temp = pyautogui.locateOnScreen('load_finished.png', confidence=0.90)
        if temp == None:
            time.sleep(1)
        else:
            time.sleep(1)
            break

    pyautogui.click(x=247, y=869)  # Support skill 2

    while True:
        temp = pyautogui.locateOnScreen('musashi_present.png', confidence=0.90)
        if temp == None:
            time.sleep(1)
        else:
            time.sleep(1)
            break

    pyautogui.click(x=957, y=660)  # Give Musashi

    while True:
        temp = pyautogui.locateOnScreen('load_finished.png', confidence=0.90)
        if temp == None:
            time.sleep(1)
        else:
            time.sleep(1)
            break

    pyautogui.click(x=374, y=869)  # Support skill 3

    while True:
        temp = pyautogui.locateOnScreen('musashi_present.png', confidence=0.90)
        if temp == None:
            time.sleep(1)
        else:
            time.sleep(1)
            break

    pyautogui.click(x=957, y=660)  # Give Musashi

    while True:
        temp = pyautogui.locateOnScreen('load_finished.png', confidence=0.90)
        if temp == None:
            time.sleep(1)
        else:
            time.sleep(1)
            break

    pyautogui.click(x=719, y=869)  # Musashi skill 2

    while True:
        temp = pyautogui.locateOnScreen('load_finished.png', confidence=0.90)
        if temp == None:
            time.sleep(1)
        else:
            time.sleep(1)
            break

    pyautogui.click(x=848, y=869)  # Musashi skill 3

    while True:
        temp = pyautogui.locateOnScreen('load_finished.png', confidence=0.90)
        if temp == None:
            time.sleep(1)
        else:
            time.sleep(1)
            break

    pyautogui.click(x=1067, y=869)  # Own Castoria skill 1

    while True:
        temp = pyautogui.locateOnScreen('load_finished.png', confidence=0.90)
        if temp == None:
            time.sleep(1)
        else:
            time.sleep(1)
            break

    pyautogui.click(x=1189, y=869)  # Own Castoria skill 2

    while True:
        temp = pyautogui.locateOnScreen('musashi_present.png', confidence=0.90)
        if temp == None:
            time.sleep(1)
        else:
            time.sleep(1)
            break

    pyautogui.click(x=957, y=660)  # Give Musashi

    while True:
        temp = pyautogui.locateOnScreen('load_finished.png', confidence=0.90)
        if temp == None:
            time.sleep(1)
        else:
            time.sleep(1)
            break

    pyautogui.click(x=1321, y=869)  # Own Castoria skill 3

    while True:
        temp = pyautogui.locateOnScreen('musashi_present.png', confidence=0.90)
        if temp == None:
            time.sleep(1)
        else:
            time.sleep(1)
            break

    pyautogui.click(x=957, y=660)  # Give Musashi

    while True:
        temp = pyautogui.locateOnScreen('load_finished.png', confidence=0.90)
        if temp == None:
            time.sleep(1)
        else:
            time.sleep(1)
            break

    pyautogui.click(x=1706, y=907)  # Select command cards

    while True:
        temp = pyautogui.locateOnScreen('select_command.png', confidence=0.90)
        if temp == None:
            time.sleep(1)
        else:
            time.sleep(2)
            break

    pyautogui.click(x=960, y=327)  # Musashi Noble Phantasm
    time.sleep(1)
    pyautogui.click(x=197, y=748)  # Command card 2
    time.sleep(1)
    pyautogui.click(x=574, y=758)  # Command card 3


    while True:
        temp = pyautogui.locateOnScreen('load_finished.png', confidence=0.90)
        if temp == None:
            time.sleep(1)
        else:
            time.sleep(1)
            break


    # Phase 2
    pyautogui.click(x=1706, y=907)  # Select command cards

    while True:
        temp = pyautogui.locateOnScreen('select_command.png', confidence=0.90)
        if temp == None:
            time.sleep(1)
        else:
            time.sleep(2)
            break

    pyautogui.click(x=960, y=327)  # Musashi Noble Phantasm
    time.sleep(1)
    pyautogui.click(x=197, y=748)  # Command card 2
    time.sleep(1)
    pyautogui.click(x=574, y=758)  # Command card 3

    while True:
        temp = pyautogui.locateOnScreen('load_finished.png', confidence=0.90)
        if temp == None:
            time.sleep(1)
        else:
            time.sleep(1)
            break

    # Phase 3
    pyautogui.click(x=1706, y=907)  # Select command cards

    while True:
        temp = pyautogui.locateOnScreen('select_command.png', confidence=0.90)
        if temp == None:
            time.sleep(1)
        else:
            time.sleep(2)
            break

    pyautogui.click(x=960, y=327)  # Musashi Noble Phantasm
    time.sleep(1)
    pyautogui.click(x=197, y=748)  # Command card 2
    time.sleep(1)
    pyautogui.click(x=574, y=758)  # Command card 3

    while True:
        temp = pyautogui.locateOnScreen('battle_finished.png', confidence=0.90)
        if temp == None:
            time.sleep(1)
        else:
            time.sleep(2)
            break

    pyautogui.click(x=940, y=562)  # Bond statistics
    time.sleep(1)
    pyautogui.click(x=940, y=562)  # Master level
    time.sleep(1)
    pyautogui.click(x=1661, y=949)  # Spoils
    time.sleep(1)

    temp = pyautogui.locateOnScreen('friend_request.png', confidence=0.90)

    if temp != None:  # If ask whether to add friend
        pyautogui.click(x=505, y=919)  # Cancel

    time.sleep(1)
    pyautogui.click(x=1268, y=852)  # Successive battle


    return


def aprefill():
    temp = pyautogui.locateOnScreen('AP_Refill.png', confidence=0.90)

    if temp == None:  # Don't need refill
        return

    temp = pyautogui.locateOnScreen('GoldenApple.png', confidence=0.90)

    if temp == None:
        raise ValueError("Not enough golden apples")

    pyautogui.click(x=temp[0] + 20 , y=temp[1] + 20)
    time.sleep(2)
    pyautogui.click(x=1239, y=841)


prep()
i = 0
first_past = False

while (1):
    
    temp = pyautogui.locateOnScreen('load_finished.png', confidence=0.90)
    if temp == None:
        supportselect()  # Select Support

    unlimitedpool()  # Start unlimited pool
    time.sleep(5)
    aprefill()  # Refill apple
    time.sleep(5)
    i += 1
    print("Round {} finish".format(i))

