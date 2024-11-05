from typing import List
from gui.tabs.tab import XTab
from gui import colors
import tkinter
import pw
from registry import XRegistry, XSink
import copy

class XDeviceTab(XTab):
    def GetButtonTitle(self) -> str: return "Device"

    def Enable(self) -> None:
        self.ContentFrame = tkinter.Frame(self.Frame, bg = colors.KBackground)
        self.ContentFrame.rowconfigure(0, weight = 1)
        self.ContentFrame.columnconfigure(0, weight = 1)
        self.ContentFrame.columnconfigure(1, weight = 4)
        self.ContentFrame.pack(side = tkinter.BOTTOM, fill=tkinter.BOTH, expand = True)

        self.DevicesFrame = tkinter.Frame(self.ContentFrame, bg = colors.KInnerSidebar)
        self.DevicesFrame.rowconfigure(0, weight = 1)
        self.DevicesFrame.columnconfigure(0, weight = 1)
        self.DevicesFrame.grid(row = 0, column = 0, sticky = "nsew")

        self.DeviceFrame = tkinter.Frame(self.ContentFrame, bg = colors.KBackground)
        self.DeviceFrame.grid(row = 0, column = 1, sticky = "nsew")

        self.Refresh()
        return

    def Disable(self) -> None:
        return

    def Refresh(self) -> None:
        for widget in self.DevicesFrame.winfo_children():
            widget.destroy()
        for widget in self.DeviceFrame.winfo_children():
            widget.destroy()

        createDeviceButton = tkinter.Button (
            self.DevicesFrame,
            text = "Create Device",
            command = self.CreateDevice,
            font = ("Helvetica", 20, "bold"),
            background = colors.KBackground,
            activebackground = colors.KBackground,
            foreground = colors.KAccent,
            activeforeground = colors.KAccent
        )
        createDeviceButton.pack(side = tkinter.BOTTOM, fill = tkinter.X)

        for sink in XRegistry.ZSinks:
            tkinter.Button (
                self.DevicesFrame,
                text = sink.name,
                command = lambda n=sink.name: self.DeviceInfo(n),
                font = ("Helvetica", 20, "bold"),
                background = colors.KBackground,
                activebackground = colors.KBackground,
                foreground = colors.KAccent,
                activeforeground = colors.KAccent
            ).pack(side = tkinter.TOP, fill = tkinter.X)
        return

    def CreateDevice(self) -> None:
        frame = tkinter.Frame(self.ContentFrame, bg = colors.KBackground)
        frame.rowconfigure(0, weight = 2)
        frame.rowconfigure(1, weight = 1)
        frame.rowconfigure(2, weight = 2)
        frame.columnconfigure(0, weight = 1)
        frame.columnconfigure(1, weight = 2)
        frame.columnconfigure(2, weight = 1)
        frame.grid(row = 0, column = 1, sticky = "nsew")

        interestFrame = tkinter.Frame(frame, bg = colors.KInnerSidebar)
        interestFrame.rowconfigure(0, weight = 1)
        interestFrame.columnconfigure(0, weight = 1)
        interestFrame.grid(row = 1, column = 1, sticky = "nsew")

        entry = tkinter.Entry(interestFrame)
        entry.config (
            font = ("Helvetica", 20, "bold"),
            background = colors.KBackground,
            foreground = colors.KAccent
        )
        entry.grid(row = 0, column = 0, sticky = "ew")

        addBtn = tkinter.Button (
            interestFrame,
            text = "Add",
            command = lambda: self.TryAddDevice(frame, entry.get()),
            font = ("Helvetica", 20, "bold"),
            background = colors.KBackground,
            activebackground = colors.KBackground,
            foreground = colors.KAccent,
            activeforeground = colors.KAccent
        )
        addBtn.grid(row = 0, column = 0, sticky = "se")

        cancelBtn = tkinter.Button (
            interestFrame,
            text = "Cancel",
            command = lambda: self.CancelCreateDevice(frame),
            font = ("Helvetica", 20, "bold"),
            background = colors.KBackground,
            activebackground = colors.KBackground,
            foreground = colors.KAccent,
            activeforeground = colors.KAccent
        )
        cancelBtn.grid(row = 0, column = 0, sticky = "sw")
        return

    def CancelCreateDevice(self, frame) -> None:
        for widget in frame.winfo_children():
            widget.destroy()
        return

    def TryAddDevice(self, frame, name) -> None:
        if name == "": return
        if not XRegistry.ZAdd(name): return
        self.CancelCreateDevice(frame)
        self.Refresh()
        return

    def DeviceInfo(self, name:str) -> None:
        for widget in self.DeviceFrame.winfo_children():
            widget.destroy()

        label = tkinter.Label (
            self.DeviceFrame,
            text = name,
            bg = colors.KBackground,
            fg = colors.KAccent,
            font = ("Helvetica", 30, "bold")
        )
        label.pack(side = tkinter.TOP)

        btn = tkinter.Button (
            self.DeviceFrame,
            text = "Remove Device",
            command = lambda n=name: self.RemoveDevice(n),
            font = ("Helvetica", 20, "bold"),
            background = colors.KBackground,
            activebackground = colors.KBackground,
            foreground = colors.KAccent,
            activeforeground = colors.KAccent
        )
        btn.pack(side = tkinter.BOTTOM)
        return

    def RemoveDevice(self, name:str) -> None:
        XRegistry.ZRemove(name)
        self.Refresh()
        return