from gui.tabs.tab import Tab
import tkinter

class Tab2(Tab):
    def getButtonTitle(self) -> str: return "Tab 2"

    def enable(self) -> None:
        label = tkinter.Label(self.frame, text="Content for Tab 2")
        label.pack(padx=10, pady=10)
        return