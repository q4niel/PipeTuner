from gui.tabs.tab import Tab
import tkinter
from gui.colors import Colors

class VolumeTab(Tab):
    def getButtonTitle(self) -> str: return "Volume"

    def enable(self) -> None:
        self.contentFrame = tkinter.Frame(self.frame, bg = Colors.background())
        self.contentFrame.rowconfigure(0, weight = 1)
        self.contentFrame.columnconfigure(0, weight = 1)
        self.contentFrame.columnconfigure(1, weight = 1)
        self.contentFrame.columnconfigure(2, weight = 1)
        self.contentFrame.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True)

        self.sliders = [
            Slider(self.contentFrame, "Master", 0),
            Slider(self.contentFrame, "Default", 1),
            Slider(self.contentFrame, "Media", 2)
        ]

        return

    def disable(self) -> None:
        for slider in self.sliders:
            slider.destroy()
        return

class Slider:
    def __init__(self, contentFrame, text:str, column:int):
        self.sliderFrame = tkinter.Frame(contentFrame, background = Colors.background())
        self.sliderFrame.rowconfigure(0, weight = 10)
        self.sliderFrame.rowconfigure(1, weight = 1)
        self.sliderFrame.rowconfigure(2, weight = 50)
        self.sliderFrame.columnconfigure(0, weight = 1)
        self.sliderFrame.grid(row = 0, column = column, sticky = "nsew", padx = 20)

        self.value = tkinter.IntVar(value = 50)

        self.text = tkinter.Label(self.sliderFrame, text = text, bg = Colors.background(), fg = Colors.accent(), font = ("Helvetica", 30, "bold"))
        self.text.grid(row = 0, column = 0, sticky = "ns")

        self.visualValue = tkinter.Label(self.sliderFrame, text = self.value.get(), bg = Colors.background(), fg = Colors.accent(), font = ("Helvetica", 20, "bold"))
        self.visualValue.grid(row = 1, column = 0, sticky = "ns")

        self.scale = tkinter.Scale (
            self.sliderFrame,
            variable = self.value,
            showvalue = False,
            command = self.cmd,
            from_ = 100,
            to = 0,

            width = 100,
            sliderlength = 100,
            sliderrelief = "flat",
            background = Colors.accent(),
            troughcolor = Colors.background()
        )
        self.scale.grid(row = 2, column = 0, sticky = "ns")
        return

    def getValue(self) -> int:
        return self.value.get()

    def cmd(self, value) -> None:
        self.visualValue.configure(text = self.getValue())
        return

    def destroy(self):
        self.scale.destroy()
        return