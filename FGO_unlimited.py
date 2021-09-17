import pyautogui
import time
import sys
from PIL import Image
import numpy


#pyautogui.FAILSAFE = False
pyautogui.PAUSE = 1

#while(1):
#    time.sleep(3)
#    if(pyautogui.position()==(0,899)):
#        break

print('Please go to the correct window')

def prep():
    pyautogui.FAILSAFE = False
    while(1):
        if(pyautogui.position()==(0,0)):
            print("Program Start")
            time.sleep(1)
            pyautogui.moveTo(x=78,y=693)
            pyautogui.FAILSAFE = True
            return
        time.sleep(5)

def reco():
    return(pyautogui.locateOnScreen('Liang.png',confidence=0.98))

def drag():
    pyautogui.moveTo(x=1393, y=390)
    time.sleep(1)
    pyautogui.dragTo(x=1395, y=674, duration=2,button='left')

def refresh():
    pyautogui.click(x=956, y=189)
    time.sleep(2)
    pyautogui.click(x=947, y=675)

    #state=pyautogui.confirm('Are you in the correct window?')
    #if state=='OK':
    #    break
    #else:
    #    time.sleep(5)
def supportselect():
    while(1):
        temp=reco()
        if temp!=None:
            #print(temp)
            time.sleep(1)
            pyautogui.click(x=temp[0]/2,y=temp[1]/2)
            break
        else:
            drag()
            time.sleep(1)
            temp=reco()
            if temp!=None:
                #print(temp)
                time.sleep(1)
                pyautogui.click(x=temp[0]/2,y=temp[1]/2)
                break
            else:
                refresh()
                time.sleep(10)

def unlimitedpool():
    pyautogui.FAILSAFE = True
    #Phase 1
    pyautogui.click(x=78,y=693)#Rin attack up
    time.sleep(3)
    pyautogui.click(x=1008,y=693)#Liang attack up
    time.sleep(3)
    pyautogui.click(x=899,y=693)#Liang defense up
    time.sleep(3)
    pyautogui.click(x=288,y=693)#Rin 50 NP
    time.sleep(3)
    pyautogui.click(x=1266,y=721)#Attack
    time.sleep(1)
    pyautogui.click(x=462,y=275)#Rin N.P.
    pyautogui.click(x=135,y=628)#command card 1
    pyautogui.click(x=432,y=616)#command card 2
    time.sleep(45)#Rin N.P annimation

    #Phase 2
    pyautogui.click(x=815,y=700)#Liang skill 1
    pyautogui.click(x=369,y=541)#Select Rin
    time.sleep(3)
    pyautogui.click(x=185,y=694)#Rin skill 2
    pyautogui.click(x=369,y=541)#Select green card
    time.sleep(3)
    pyautogui.click(x=1344,y=402)#Master skill
    pyautogui.click(x=1230,y=385)#Order change
    pyautogui.click(x=602,y=430)#Liang 1
    pyautogui.click(x=833,y=430)#Liang 2
    pyautogui.click(x=728,y=748)#Order change confirm
    time.sleep(3)
    pyautogui.click(x=1008,y=693)#Liang attack up
    time.sleep(3)
    pyautogui.click(x=899,y=693)#Liang defense up
    time.sleep(3)
    pyautogui.click(x=815,y=700)#Liang skill 1
    pyautogui.click(x=369,y=541)#Select Rin
    time.sleep(3)
    pyautogui.click(x=1266,y=721)#Attack
    time.sleep(1)
    pyautogui.click(x=462,y=275)#Rin N.P.
    pyautogui.click(x=135,y=628)#command card 1
    pyautogui.click(x=432,y=616)#command card 2
    time.sleep(45)#Rin N.P annimation

    #Phase 3
    pyautogui.click(x=325,y=98)#Select enemy target
    pyautogui.click(x=1344,y=402)#Master skill
    pyautogui.click(x=1019,y=397)#Master skill 1
    time.sleep(3)
    pyautogui.click(x=1344,y=402)#Master skill
    pyautogui.click(x=1120,y=397)#Master skill 2
    time.sleep(3)
    pyautogui.click(x=434,y=697)#Arjuna attack up
    time.sleep(3)
    pyautogui.click(x=538,y=697)#Arjuna 30 NP
    time.sleep(3)
    pyautogui.click(x=1266,y=721)#Attack
    time.sleep(1)
    pyautogui.click(x=722,y=266)#Arjuna N.P
    pyautogui.click(x=135,y=628)#command card 1
    pyautogui.click(x=432,y=616)#command card 2
    time.sleep(35)#Rin N.P annimation
    pyautogui.moveTo(x=438, y=751)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.click(x=1252, y=815)
    time.sleep(3)
    pyautogui.click(x=945, y=685)
    return

def aprefill():
    temp=None
    temp=pyautogui.locateOnScreen('AP_Refill.png',confidence=0.98)
    if temp==None:
        return
    temp=pyautogui.locateOnScreen('GoldenApple.png',confidence=0.98)
    if temp==None:
        raise ValueError("Not enough golden apple")
    pyautogui.click(x=temp[0]/2,y=temp[1]/2)
    time.sleep(2)
    pyautogui.click(x=940, y=677)


prep()
i=0
while(1):
    #prep()
    supportselect()
    time.sleep(20)
    unlimitedpool()
    time.sleep(5)
    aprefill()
    time.sleep(20)
    i+=1
    print("Round {} finish".format(i))
    #sys.stdout.write('\a\a\a')
    #sys.stdout.flush()
#pyautogui.alert('Done')
#sys.stdout.write('\a\a\a')
#sys.stdout.flush()
