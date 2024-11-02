from gui.tabs.tab import Tab
import tkinter

class Tab3(Tab):
    def getButtonTitle(self) -> str: return "Tab 3"

    def enable(self) -> None:
        label = tkinter.Label(self.frame, text="Content for Tab 3")
        label.pack(padx=10, pady=10)
        return