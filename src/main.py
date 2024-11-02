import tkinter
from gui.tab_menu import TabMenu

def main() -> None:
    root = tkinter.Tk()
    root.title("PipeTuner")
    root.rowconfigure(0, weight = 1)
    root.columnconfigure(0, weight = 1)
    root.columnconfigure(1, weight = 50)
    menu = TabMenu(root)
    root.mainloop()
    return

if __name__ == '__main__': main()