import sys
import argparse
import win32gui
import win32api

def get_window_handle(window_title):
    hwnd = win32gui.FindWindow(None, window_title)
    return hwnd

def center_mouse_in_window(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    center_x = (rect[0] + rect[2]) // 2
    center_y = (rect[1] + rect[3]) // 2
    win32api.SetCursorPos((center_x, center_y))

def list_window_titles():
    def enum_window_titles(hwnd, titles):
        if win32gui.IsWindowVisible(hwnd):
            titles.append(win32gui.GetWindowText(hwnd))

    titles = []
    win32gui.EnumWindows(enum_window_titles, titles)
    return titles

def main():
    parser = argparse.ArgumentParser(description="Center the mouse cursor in a specified window.")
    parser.add_argument("window_title", nargs="?", help="Title of the window to center the mouse cursor in (i.e. \"Digital Combat Simulator\")")
    parser.add_argument("-l", "--list", action="store_true", help="List titles of all active windows")
    args = parser.parse_args()

    if args.list:
        print("Active window titles:")
        for title in list_window_titles():
            print(title)
        sys.exit()

    if args.window_title:
        hwnd = get_window_handle(args.window_title)
        if hwnd:
            center_mouse_in_window(hwnd)
            print("Mouse centered in the window:", args.window_title)
        else:
            print("Window not found:", args.window_title)
    else:
        print("Window title is required. Use --help for usage instructions.")

if __name__ == "__main__":
    main()
