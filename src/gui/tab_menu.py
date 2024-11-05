import tkinter
from gui import colors
from gui.tabs.tab import XTab
from gui.tabs.volume import XVolumeTab
from gui.tabs.device import XDeviceTab

class XTabMenu():
    def __init__(self, root:tkinter.Tk):
        self.SidebarFrame = tkinter.Frame(root, bg = colors.KSidebar)
        self.SidebarFrame.grid(row = 0, column = 0, sticky = "nsew")

        self.TabFrame = tkinter.Frame(root, bg = colors.KBackground)
        self.TabFrame.grid(row = 0, column = 1, sticky = "nsew")

        self.OpenTab = XVolumeTab(self)
        self.OpenTab.Enable()
        XDeviceTab(self)

        refreshButton = tkinter.Button (
            self.SidebarFrame,
            text = "Refresh",
            command = lambda: self.OpenTab.Refresh(),
            font = ("Helvetica", 20, "bold"),
            background = colors.KBackground,
            activebackground = colors.KBackground,
            foreground = colors.KAccent,
            activeforeground = colors.KAccent
        )
        refreshButton.pack(side = tkinter.BOTTOM, fill = tkinter.X)
        return