from abc import ABC, abstractmethod
import tkinter

class Tab(ABC):
    def __init__(self, menu):
        self.menu = menu
        self.frame = menu.tabFrame
        button = tkinter.Button(menu.sidebarFrame, text=self.getButtonTitle(), command=self.command)
        button.pack(fill=tkinter.X)
        return

    @abstractmethod
    def getButtonTitle(self) -> str: return ""

    @abstractmethod
    def enable(self) -> None: pass

    def disable(self) -> None:
        for widget in self.frame.winfo_children():
            widget.destroy()
        return

    def command(self) -> None:
        self.menu.openTab.disable()
        self.menu.openTab = self
        self.menu.openTab.enable()
        return