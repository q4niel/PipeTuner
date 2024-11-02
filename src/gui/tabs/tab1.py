from gui.tabs.tab import Tab
import tkinter

class Tab1(Tab):
    def getButtonTitle(self) -> str: return "Tab 1"

    def enable(self) -> None:
        label = tkinter.Label(self.frame, text="Content for Tab 1")
        label.pack(padx=10, pady=10)
        return