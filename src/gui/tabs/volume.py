from gui.tabs.tab import XTab
import tkinter
from gui import colors

class XVolumeTab(XTab):
    def GetButtonTitle(self) -> str: return "Volume"

    def Enable(self) -> None:
        self.ContentFrame = tkinter.Frame(self.Frame, bg = colors.KBackground)
        self.ContentFrame.rowconfigure(0, weight = 1)
        self.ContentFrame.columnconfigure(0, weight = 1)
        self.ContentFrame.columnconfigure(1, weight = 1)
        self.ContentFrame.columnconfigure(2, weight = 1)
        self.ContentFrame.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True)

        self.Sliders = [
            XSlider(self.ContentFrame, "Master", 0),
            XSlider(self.ContentFrame, "Default", 1),
            XSlider(self.ContentFrame, "Media", 2)
        ]

        return

    def Disable(self) -> None:
        for slider in self.Sliders:
            slider.Destroy()
        return

    def Refresh(self) -> None:
        return

class XSlider:
    def __init__(self, contentFrame, text:str, column:int):
        self.SliderFrame = tkinter.Frame(contentFrame, background = colors.KBackground)
        self.SliderFrame.rowconfigure(0, weight = 10)
        self.SliderFrame.rowconfigure(1, weight = 1)
        self.SliderFrame.rowconfigure(2, weight = 50)
        self.SliderFrame.columnconfigure(0, weight = 1)
        self.SliderFrame.grid(row = 0, column = column, sticky = "nsew", padx = 20)

        self.Value = tkinter.IntVar(value = 50)

        self.Text = tkinter.Label(self.SliderFrame, text = text, bg = colors.KBackground, fg = colors.KAccent, font = ("Helvetica", 30, "bold"))
        self.Text.grid(row = 0, column = 0, sticky = "ns")

        self.VisualValue = tkinter.Label(self.SliderFrame, text = self.Value.get(), bg = colors.KBackground, fg = colors.KAccent, font = ("Helvetica", 20, "bold"))
        self.VisualValue.grid(row = 1, column = 0, sticky = "ns")

        self.Scale = tkinter.Scale (
            self.SliderFrame,
            variable = self.Value,
            showvalue = False,
            command = self.Command,
            from_ = 100,
            to = 0,

            width = 100,
            sliderlength = 100,
            sliderrelief = "flat",
            background = colors.KAccent,
            troughcolor = colors.KBackground
        )
        self.Scale.grid(row = 2, column = 0, sticky = "ns")
        return

    def GetValue(self) -> int:
        return self.Value.get()

    def Command(self, value) -> None:
        self.VisualValue.configure(text = self.GetValue())
        return

    def Destroy(self):
        self.Scale.destroy()
        return