import pyautogui
import time
import sys
from PIL import Image
import numpy

# pyautogui.FAILSAFE = False
pyautogui.PAUSE = 1

# while(1):
#    time.sleep(3)
#    if(pyautogui.position()==(0,899)):
#        break

print('Please go to the correct window...')


def prep():
    pyautogui.FAILSAFE = False
    while True:
        x, y = pyautogui.position()

        if x <= 100 and y <= 100:
            print("Program Started...")
            time.sleep(1)
            pyautogui.moveTo(x=78, y=693)
            pyautogui.FAILSAFE = True
            return


def reco():
    return pyautogui.locateOnScreen('castoria_support.png', confidence=0.90)


def drag():
    pyautogui.moveTo(x=1880, y=330)  # Select drag bar
    time.sleep(1)
    pyautogui.dragTo(x=1880, y=600, duration=4, button='left')


def refresh():
    pyautogui.click(x=1276, y=189)  # Select refresh
    time.sleep(2)
    pyautogui.click(x=1256, y=844)  # Select confirm


def supportselect():

    while (1):
        pyautogui.click(x=649, y=188) # Caster
        temp = reco()
        if temp != None:  # Found support
            time.sleep(1)
            pyautogui.click(x=temp[0] - 100, y=temp[1] - 100)  # Select that support
            break
        else:
            drag()
            time.sleep(1)
            temp = reco()
            if temp != None:
                # print(temp)
                time.sleep(1)
                pyautogui.click(x=temp[0] - 100, y=temp[1] - 100)
                break
            else:
                refresh()
                time.sleep(10)
    time.sleep(3)
    pyautogui.click(1741, 994)  # Start mission


def unlimitedpool():
    pyautogui.FAILSAFE = True

    # Phase 1
    pyautogui.click(x=112, y=869)  # Support skill 1
    time.sleep(3)

    pyautogui.click(x=247, y=869)  # Support skill 2
    time.sleep(3)
    pyautogui.click(x=957, y=660)  # Give Musashi
    time.sleep(3)

    pyautogui.click(x=374, y=869)  # Support skill 3
    time.sleep(3)
    pyautogui.click(x=957, y=660)  # Give Musashi
    time.sleep(3)

    pyautogui.click(x=719, y=869)  # Musashi skill 2
    time.sleep(3)
    pyautogui.click(x=848, y=869)  # Musashi skill 3
    time.sleep(3)

    pyautogui.click(x=1067, y=869)  # Own Castoria skill 1
    time.sleep(3)

    pyautogui.click(x=1189, y=869)  # Own Castoria skill 2
    time.sleep(3)
    pyautogui.click(x=957, y=660)  # Give Musashi
    time.sleep(3)

    pyautogui.click(x=1321, y=869)  # Own Castoria skill 3
    time.sleep(3)
    pyautogui.click(x=957, y=660)  # Give Musashi
    time.sleep(3)

    pyautogui.click(x=1706, y=907) # Select command cards
    time.sleep(3)
    pyautogui.click(x=960, y=327)  # Musashi Noble Phantasm
    time.sleep(2)
    pyautogui.click(x=197, y=748)  # Command card 2
    time.sleep(2)
    pyautogui.click(x=574, y=758)  # Command card 3

    time.sleep(40)  # Wait for change of phase

    # Phase 2
    pyautogui.click(x=1706, y=907) # Select command cards
    time.sleep(3)
    pyautogui.click(x=960, y=327)  # Musashi Noble Phantasm
    time.sleep(2)
    pyautogui.click(x=197, y=748)  # Command card 2
    time.sleep(2)
    pyautogui.click(x=574, y=758)  # Command card 3

    time.sleep(40)  # Wait for change of phase

    # Phase 3
    pyautogui.click(x=1706, y=907) # Select command cards
    time.sleep(3)
    pyautogui.click(x=960, y=327)  # Musashi Noble Phantasm
    time.sleep(2)
    pyautogui.click(x=197, y=748)  # Command card 2
    time.sleep(2)
    pyautogui.click(x=574, y=758)  # Command card 3

    time.sleep(45)  # Wait for finishing

    pyautogui.click(x=940, y=562)  # Bond statistics
    time.sleep(3)
    pyautogui.click(x=940, y=562)  # Master level
    time.sleep(3)
    pyautogui.click(x=1661, y=949)  # Spoils

    pyautogui.click(x=1268, y=852)  # Successive battle

    return


def aprefill():
    temp = pyautogui.locateOnScreen('AP_Refill.png', confidence=0.90)

    if temp == None:  # Don't need refill
        return

    temp = pyautogui.locateOnScreen('SilverApple.png', confidence=0.90)

    if temp == None:
        raise ValueError("Not enough golden apples")

    pyautogui.click(x=temp[0], y=temp[1])
    time.sleep(2)
    pyautogui.click(x=1239, y=841)


prep()
i = 0
while (1):
    # prep()
    supportselect()  # Select Support
    time.sleep(10)
    unlimitedpool()  # Start unlimited pool
    time.sleep(5)
    aprefill()  # Refill apple
    time.sleep(10)
    i += 1
    print("Round {} finish".format(i))
    # sys.stdout.write('\a\a\a')
    # sys.stdout.flush()
# pyautogui.alert('Done')
# sys.stdout.write('\a\a\a')
# sys.stdout.flush()
