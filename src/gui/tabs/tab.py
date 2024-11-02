from abc import ABC, abstractmethod
import tkinter
from gui.colors import Colors

class Tab(ABC):
    def __init__(self, menu):
        self.menu = menu
        self.frame = menu.tabFrame
        button = tkinter.Button (
            menu.sidebarFrame,
            text = self.getButtonTitle(),
            command = self.command,
            font = ("Helvetica", 20, "bold"),
            background = Colors.background(),
            activebackground = Colors.background(),
            foreground = Colors.accent(),
            activeforeground = Colors.accent()
        )
        button.pack(fill=tkinter.X)
        return

    @abstractmethod
    def getButtonTitle(self) -> str: return ""

    @abstractmethod
    def enable(self) -> None: pass

    @abstractmethod
    def disable(self) -> None: pass

    def command(self) -> None:
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.menu.openTab.disable()

        self.menu.openTab = self
        self.menu.openTab.enable()
        return