import random, pyautogui as pyauto

#WARNING, THIS IS A SIMPLE VIRUS THAT OPENS AND MINIMIZES WINDOWS WHILE MOVING MOUSE AROUND.
#TO STOP THIS SCRIPT, PRESS CTRL+ALT+DELETE TO OPEN TASK
while True:
    h = random.randint(0, 1000)
    w = random.randint(0, 1920)
    pyauto.click(h, w,)
    pyauto.hotkey('winleft', 'm')
    pyauto.hotkey("winleft")


#Source: https://youtu.be/qZikSq-4_so?si=WKX92KhoI5usFJhn