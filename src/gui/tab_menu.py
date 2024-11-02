import tkinter
from gui.colors import Colors
from gui.tabs.tab import Tab
from gui.tabs.volume import VolumeTab
from gui.tabs.devices import DevicesTab

class TabMenu():
    def __init__(self, root:tkinter.Tk):
        self.sidebarFrame = tkinter.Frame(root, bg = Colors.sidebar())
        self.sidebarFrame.grid(row = 0, column = 0, sticky = "nsew")

        self.tabFrame = tkinter.Frame(root, bg = Colors.background())
        self.tabFrame.grid(row = 0, column = 1, sticky = "nsew")

        self.openTab = VolumeTab(self)
        self.openTab.enable()
        DevicesTab(self)
        return