import time
import numpy as np
import win32gui, win32ui, win32con, win32api

# returns target window size
def window_pos(target):
    toplist, winlist = [], []
    def enum_cb(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
    win32gui.EnumWindows(enum_cb, toplist)

    window = [(hwnd, title) for hwnd, title in winlist if target in title.lower()]

    # print(window)

    for elem in window:
        wndsize = list(win32gui.GetWindowRect(elem[0]))
        xsize = wndsize[2] - wndsize[0]
        ysize = wndsize[3] - wndsize[1]
        #print((xsize,ysize))
        #if (xsize > 400) and (xsize < 600):
    # for elem in winlist:
        hwnd = elem[0]
        bbox = list(win32gui.GetWindowRect(hwnd))
            # if (bbox[2] - bbox[0] == xsize) and bbox[1] != 0:
                # win32gui.SetForegroundWindow(hwnd)
                # print(elem, bbox)
        return hwnd
