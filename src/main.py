import tkinter
from registry import XRegistry
from gui.tab_menu import XTabMenu

def main() -> None:
    root = tkinter.Tk()
    root.title("PipeTuner")
    root.rowconfigure(0, weight = 1)
    root.columnconfigure(0, weight = 1)
    root.columnconfigure(1, weight = 50)

    XRegistry.ZInit("config.json")
    menu = XTabMenu(root)

    root.mainloop()
    return

if __name__ == '__main__': main()