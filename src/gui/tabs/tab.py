from abc import ABC, abstractmethod
import tkinter
from gui import colors

class XTab(ABC):
    def __init__(self, menu):
        self.Menu = menu
        self.Frame = menu.TabFrame
        button = tkinter.Button (
            menu.SidebarFrame,
            text = self.GetButtonTitle(),
            command = self.Command,
            font = ("Helvetica", 20, "bold"),
            background = colors.KBackground,
            activebackground = colors.KBackground,
            foreground = colors.KAccent,
            activeforeground = colors.KAccent
        )
        button.pack(fill=tkinter.X)
        return

    @abstractmethod
    def GetButtonTitle(self) -> str: return ""

    @abstractmethod
    def Enable(self) -> None: pass

    @abstractmethod
    def Disable(self) -> None: pass

    @abstractmethod
    def Refresh(self) -> None: pass

    def Command(self) -> None:
        for widget in self.Frame.winfo_children():
            widget.destroy()
        self.Menu.OpenTab.Disable()

        self.Menu.OpenTab = self
        self.Menu.OpenTab.Enable()
        return