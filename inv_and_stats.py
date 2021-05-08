import win32gui
import pywinauto
import time
from win32api import GetSystemMetrics
from directkeys import PressKey, ReleaseKey, MoveCursor, LeftClick
from directkeys import Q, W, E, R, T, Y, U, I, O, P, A, S, D, F, G, H, J, K, L, Z, X, C, V, B, N, M, DIK_DIVIDE, ENTER, SPACE, SHIFT, NUM_7, DIK_DICT


# Define variables based on screen size (very roughly)
if GetSystemMetrics(0) <= 1920 and GetSystemMetrics(1) <= 1080:
    INVSLOT1= (810, 175)
    INVSLOT2= (840, 175)
    INVSLOT3= (870, 175)
    INVSLOT4= (905, 175)
    INVSLOT5= (935, 175)
    INVSLOT6= (970, 175)
    INVSLOT7= (1000, 175)
    INVSLOT8= (1035, 175)
    INVSLOT9= (810, 210)
    INVSLOT10= (840, 210)
    INVSLOT11= (870, 210)
    INVSLOT12= (905, 210)
    INVSLOT13= (935, 210)
    INVSLOT14= (970, 210)
    INVSLOT15= (1000, 210)
    INVSLOT16= (1035, 210)

    SED = (1005, 545)
    HAMBRE = (1005, 610)
    ENERGIA = (810, 490)
elif GetSystemMetrics(0) == 2560 and GetSystemMetrics(1) == 1440:
    INVSLOT1= (1450, 530)
    INVSLOT2= (1480, 530)
    INVSLOT3= (1510, 530)
    INVSLOT4= (1545, 530)
    INVSLOT5= (1575, 530)
    INVSLOT6= (1610, 530)
    INVSLOT7= (1645, 530)
    INVSLOT8= (1670, 530)
    INVSLOT9= (1450, 565)
    INVSLOT10= (1480, 565)
    INVSLOT11= (1510, 565)
    INVSLOT12= (1545, 565)
    INVSLOT13= (1575, 565)
    INVSLOT14= (1610, 565)
    INVSLOT15= (1645, 565)
    INVSLOT16= (1670, 565)

    SED = (1650, 905)
    HAMBRE = (1650, 970)
    ENERGIA = (1460, 850)

#Define useful functions to get pixel colours and to check specific values.
def get_pixel_color(stat):
    desktop_window_id = win32gui.GetDesktopWindow()
    desktop_window_dc = win32gui.GetWindowDC(desktop_window_id)
    long_color = win32gui.GetPixel(desktop_window_dc, stat[0], stat[1])
    color = int(long_color)
    return (color & 0xff), ((color >> 8) & 0xff), ((color >> 16) & 0xff)

def check_hambre(window):
    if get_pixel_color(HAMBRE) == (0,0,0):
        window.set_focus()
        pywinauto.mouse.click(coords=INVSLOT1)
        time.sleep(0.2)
        pywinauto.mouse.release()
        time.sleep(0.2)
        PressKey(U)
        ReleaseKey(U)
        time.sleep(0.2)
        PressKey(U)
        ReleaseKey(U)
        time.sleep(0.2)
        PressKey(U)
        ReleaseKey(U)

def check_sed(window):
    if get_pixel_color(SED) == (0,0,0):
        window.set_focus()
        pywinauto.mouse.click(coords=INVSLOT2)
        time.sleep(0.2)
        pywinauto.mouse.release()
        time.sleep(0.2)
        PressKey(U)
        ReleaseKey(U)
        time.sleep(0.2)
        PressKey(U)
        ReleaseKey(U)
        time.sleep(0.2)
        PressKey(U)
        ReleaseKey(U)
