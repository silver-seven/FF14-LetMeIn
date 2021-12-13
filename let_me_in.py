import time
import pyautogui
import getpass
import subprocess

class KeyPos:
    #1440p
    launcher_pos = (1580, 386)
    pass_pos = (1530, 695)
    login_pos = (1530, 830)
    play_pos = (1530, 830)
    start_pos = (1275, 1085)
    char_pos = (1940, 220)
    char_login_pos = (1131,743)

def checkScreenSize(positions):
    if pyautogui.size() == (2560, 1440):
        print("1440p")
    else:
        print("default 1080p")

def startLauncher():
    print("Starting launcher")
    result =  subprocess.run(["F:/Apps/SquareEnix/FINAL FANTASY XIV - A Realm Reborn/boot/ffxivboot.exe"], subprocess.CREATE_BREAKAWAY_FROM_JOB)

def login(pwd, positions):
    print("Entering password")
    time.sleep(15)
    pyautogui.click(positions.launcher_pos) #click launcher
    pyautogui.click(positions.pass_pos) #pass field
    # click_pos = pyautogui.locateOnScreen('images/pwd_box.PNG')
    # pyautogui.click(click_pos.left + 20, click_pos.top + 20)
    pyautogui.write(pwd)
    pyautogui.click(positions.login_pos) #login button
    # click_pos = pyautogui.locateOnScreen('images/login_box.PNG')
    # pyautogui.click(click_pos.left + 20, click_pos.top + 20)
    time.sleep(10)
    pyautogui.click(positions.play_pos) #play button
    # click_pos = pyautogui.locateOnScreen('images/play_box.PNG')
    # pyautogui.click(click_pos.left + 20, click_pos.top + 20)

def startGame(positions):
    print("Starting Game")
    time.sleep(15)
    pyautogui.click(positions.start_pos) #start button
    pyautogui.click(positions.start_pos) #start button
    time.sleep(20)
    pyautogui.click(positions.char_pos) #character button
    pyautogui.click(positions.char_pos) #character button
    time.sleep(1)
    pyautogui.click(positions.char_login_pos) #character button
    pyautogui.click(positions.char_login_pos) #character button

def enterWorld():
    print("")

def checkForError():
    #print("Checking for error")
    isError = False
    click_pos = pyautogui.locateOnScreen('images/OK_partial.png')
    if click_pos != None:
        pyautogui.click(click_pos.left + 10, click_pos.top + 10)
        pyautogui.click(click_pos.left + 10, click_pos.top + 10)
        isError = True
    return isError

def checkForWorldEnter():
    #print("Checking if successfully entered world")
    isSuccessful = False
    click_pos = pyautogui.locateOnScreen('images/msq.png')
    if click_pos != None:
        isSuccessful = True
    return isSuccessful

def restartLogin(pwd, positions):
    print("LET MEEEE IIINNNNN!!!!")
    startLauncher()
    login(pwd, positions)
    startGame(positions)    

def main():
    positions = KeyPos()
    pwd = getpass.getpass('Password: ')
    restartLogin(pwd, positions)

    while checkForWorldEnter() == False:
        time.sleep(5)
        if checkForError():
            time.sleep(10)
            restartLogin(pwd, positions)


if __name__ == '__main__':
    main()