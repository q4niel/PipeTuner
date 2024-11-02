import tkinter
from gui.tabs.tab1 import Tab1
from gui.tabs.tab2 import Tab2
from gui.tabs.tab3 import Tab3

class TabMenu:
    def __init__(self, root:tkinter.Tk):
        self.root = root
        self.sidebarFrame = tkinter.Frame(root, bg="#23272A")
        self.sidebarFrame.pack(side=tkinter.LEFT, fill=tkinter.Y)

        self.tabFrame = tkinter.Frame(self.root, bg="#2C2F33")
        self.tabFrame.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True)

        self.openTab = Tab1(self)
        Tab2(self)
        Tab3(self)

        self.openTab.enable()
        return