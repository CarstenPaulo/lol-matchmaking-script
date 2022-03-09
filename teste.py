import win32gui, win32ui, win32con,win32api
from time import sleep



def main():
    VK_KEY_W = 0x57
    window_name = "Realera 8.0 - Hobo Cop"
    hwnd = win32gui.FindWindow(None,window_name)
    #give that
    win32gui.SetForegroundWindow(hwnd)
    sleep(1.0)
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 'f1', 0)
    sleep(0.5)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 'f1', 0)


def list_window_names():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')
    win32gui.EnumWindows(winEnumHandler, None)


def get_inner_windows(whndl):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            hwnds[win32gui.GetClassName(hwnd)] = hwnd
        return True
    hwnds = {}
    win32gui.EnumChildWindows(whndl, callback, hwnds)
    return hwnds

main()
