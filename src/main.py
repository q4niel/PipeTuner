import tkinter
import gui

def main() -> None:
    root = tkinter.Tk()
    root.title("PipeTuner")
    root.config(background="#2C2F33")
    menu = gui.TabMenu(root)
    root.mainloop()
    return

if __name__ == '__main__': main()