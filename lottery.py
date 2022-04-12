import pyautogui
import time

if __name__ == "__main__":
    print('Please go to the correct window...')

    while True:
        x, y = pyautogui.position()

        if x <= 100 and y <= 100:
            print("Program Started...")
            time.sleep(1)
            break

    while True:

        pyautogui.click(x=650, y=670)  # Roll lottery

        while True:
            temp = pyautogui.locateOnScreen('change_pool.png', confidence=0.90)
            if temp == None:
                break
            else:
                time.sleep(2)
                pyautogui.click(x=1697, y=367)  # Change pool
                time.sleep(2)
                pyautogui.click(x=1265, y=851)  # Confirm
                time.sleep(2)
                pyautogui.click(x=956, y=849)  # Confirm
                break

        while True:
            temp = pyautogui.locateOnScreen('retry.png', confidence=0.90)
            if temp == None:
                break
            else:
                time.sleep(2)
                pyautogui.click(x=1697, y=367)  # Change pool
                break


        time.sleep(0.1)

        # while True:
        #     temp = pyautogui.locateOnScreen('dialogue.png', confidence=0.90)
        #     if temp == None:
        #         time.sleep(1)
        #     else:
        #         time.sleep(0.5)
        #         break
        #
        # pyautogui.click(x=650, y=670)  # Skip dialogue
        #
        # while True:
        #     temp = pyautogui.locateOnScreen('roll.png', confidence=0.90)
        #     if temp == None:
        #         time.sleep(1)
        #     else:
        #         time.sleep(0.5)
        #         break
        #
        # pyautogui.click(x=650, y=670)  # Skip dialogue
