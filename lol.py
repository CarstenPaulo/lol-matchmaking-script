import pyautogui
import time

def press_play():
    play_img = pyautogui.locateOnScreen('img/jogar.png', confidence=0.7)

    if play_img != None:
        pyautogui.moveTo(play_img)
        pyautogui.click()
        pyautogui.click()
        return True
    return False


def choose_ranked():
    rank_img = pyautogui.locateOnScreen('img/ranked.png', confidence=0.7)

    if rank_img != None:
        pyautogui.moveTo(rank_img)
        pyautogui.click()
        return True
    return False


def confirm_match():
    confirm_img = pyautogui.locateOnScreen('img/confirm.png', confidence=0.7)

    if confirm_img != None:
        pyautogui.moveTo(confirm_img)
        pyautogui.click()
        return True
    return False


def choose_role():
    role_img = pyautogui.locateOnScreen('img/choose_role.png', confidence=0.7)

    if role_img != None:
        pyautogui.moveTo(role_img)
        pyautogui.click()
        return True
    return False


def autofill():
    autofill_img = pyautogui.locateOnScreen('img/autofill.png', confidence=0.7)

    if autofill_img != None:
        pyautogui.moveTo(autofill_img)
        pyautogui.click()
        return True
    return False


def findmatch():
    findgame_img = pyautogui.locateOnScreen('img/find-match.png', confidence=0.7)

    if findgame_img != None:
        pyautogui.moveTo(findgame_img)
        pyautogui.click()
        return True
    return False



def accept_match():
    accept_img = pyautogui.locateOnScreen('img/aceitar.png', confidence=0.7)

    if accept_img != None:
        pyautogui.moveTo(accept_img)
        pyautogui.click()
        pyautogui.click()
        return True
    return False


def search_box():
    search_img = pyautogui.locateOnScreen('img/search.png', confidence=0.7)

    if search_img != None:
        pyautogui.moveTo(search_img)
        pyautogui.click()
        pyautogui.click()
        return True
    return False

def evelyn_ban():
    evelyn_img = pyautogui.locateOnScreen('img/evelyn-ban.png', confidence=0.7)

    if evelyn_img != None:
        pyautogui.moveTo(evelyn_img)
        pyautogui.click()
        pyautogui.click()
        return True
    return False




def find_urgot():
    urgot_img = pyautogui.locateOnScreen('img/urgot.png', confidence=0.7)

    if urgot_img != None:
        pyautogui.moveTo(urgot_img)
        pyautogui.click()
        pyautogui.click()
        return True
    return False


def confirmmatch():
    confirmmatch_img = pyautogui.locateOnScreen('img/confirmmatch.png', confidence=0.7)

    if confirmmatch_img != None:
        pyautogui.moveTo(confirmmatch_img)
        pyautogui.click()
        pyautogui.click()
        return True
    return False
    



def main():
    while True:
        if press_play():
            time.sleep(2)
            choose_ranked()
            time.sleep(2)
            confirm_match()
            time.sleep(2)
            choose_role()
            time.sleep(5)
            autofill()
            time.sleep(5)
            findmatch()
            time.sleep(10)
            accept_match()
            accept_match()
            time.sleep(10)
            accept_match()
            time.sleep()
            search_box()
            time.sleep(5)
            pyautogui.write('evelyn')
            time.sleep(5)
            evelyn_ban()
            time.sleep(15)
            search_box()
            time.sleep(5)
            pyautogui.write('urgot')
            time.sleep(5)
            find_urgot()
            time.sleep(5)
            confirmmatch()
            break



main()
