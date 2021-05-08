import pywinauto
import time
from inv_and_stats import *
from directkeys import PressKey, ReleaseKey, MoveCursor, LeftClick
from directkeys import Q, W, E, R, T, Y, U, I, O, P, A, S, D, F, G, H, J, K, L, Z, X, C, V, B, N, M, DIK_DIVIDE, ENTER, SPACE, SHIFT, NUM_7, DIK_DICT

# // IDENTIFYING WINDOW TO USE //
# 1. pid brings process id from executable's path.
pid = pywinauto.application.process_from_module('C:\\Games\\Tierras del Sur 2\\Tierras del Sur.exe')

# 2. Connecting to target program.
prog=pywinauto.application.Application()
prog.connect(process=pid)

# 3. Retrieving target handles (hwnd) based on class_name
# Console which contains text we're aiming for.
console_hwnd = [w.handle for w in prog.windows(top_level_only=False, visible_only=False, enabled_only=False, class_name="RichTextWndClass")]
if console_hwnd:
    console_hwnd = console_hwnd[0]
else:
    print("Consola no encontrada, por favor abrir la ventana emergente.")
    quit()
print(f"Ventana de consola encontrada! Process: {pid}, Handle:{console_hwnd}")
# Main window handle.
main_hwnd = [w.handle for w in prog.windows(class_name="ThunderRT6Main")]
main_hwnd = main_hwnd[0]
print(f"Ventana principal encontrada! Process: {pid}, Handle:{main_hwnd}")

# Connecting to both windows.
console_window = prog.window(handle=console_hwnd)
main_window = prog.window(handle=main_hwnd)

print("Arrancando. Presionar CTRL + C para interrumpir.\nIMPORTANTE: TENER COMIDA EN SLOT 1 Y BEBIDA EN SLOT 2 DEL INVENTARIO!!")
main_window.set_focus()
# // START READING WINDOW TEXT (CTRL+C TO INTERRUPT) //
try:
    while True:
        #Read console text.
        all_texts = []
        all_texts.extend(console_window.texts())
        #Save only last line of text for printing.
        last_line = all_texts[-1].splitlines()[-1]
        check_sed(main_window)
        check_hambre(main_window)
        print(last_line)
        time.sleep(2)
        # Target string has this pattern: "Debes tipear el comando /CENTINELA xxxx." xxxx is the code we want to identify.
        if "CENTINELA" in last_line:
            main_window.set_focus()
            last_5_chars = last_line[-5:]
            code = last_5_chars[:-1] # remove last stop from last 5 characters.
            # type "/centinela code"
            time.sleep(1)
            PressKey(ENTER)
            ReleaseKey(ENTER)
            time.sleep(0.2)
            PressKey(SHIFT)
            PressKey(NUM_7)
            ReleaseKey(NUM_7)
            ReleaseKey(SHIFT)
            for c in [C,E,N,T,I,N,E,L,A]:
                time.sleep(0.2)
                PressKey(c)
                ReleaseKey(c)
            time.sleep(0.2)
            PressKey(SPACE)
            ReleaseKey(SPACE)
            for char in code.upper():
                time.sleep(0.2)
                PressKey(DIK_DICT[char])
                ReleaseKey(DIK_DICT[char])
            time.sleep(0.2)
            PressKey(ENTER)
            ReleaseKey(ENTER)
            time.sleep(4)


except KeyboardInterrupt:
    pass

#
# extra code
# print(pywinauto.findwindows.find_window(title="Juego Tierras del Sur"))
# prog.start(r'C:\\Games\\Tierras del Sur 2\\Tierras del Sur.exe')
# w_handle = pywinauto.findwindows.find_windows(title=u'Fight plan setting dialog', class_name='#32770')[0]

# for i in win.children():
# print(i.friendly_class_name(), i.client_rects(), i.rectangle())
# print(win., win.children())
