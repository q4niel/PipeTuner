from typing import List
import sys
import json
import pw

class XSink():
    def __init__(self, name:str, index:str):
        self.name = name
        self.index = index
        return

class XRegistry():
    ZPath:str
    ZRaw = {}
    ZSinks:List[XSink] = []

    @staticmethod
    def ZInit(path:str):
        XRegistry.ZPath = path
        if not XRegistry.ZLoad(): sys.exit(1)

        for device in XRegistry.ZRaw["devices"]:
            XRegistry.ZSinks.append(XSink(device["name"], device["index"]))
        return

    @staticmethod
    def ZWrite() -> None:
        with open(XRegistry.ZPath, 'w') as file:
            json.dump(XRegistry.ZRaw, file, indent = 4)
        file.close()
        return

    @staticmethod
    def ZLoad() -> bool:
        try:
            with open(XRegistry.ZPath, 'r') as file:
                XRegistry.ZRaw = json.load(file)
            file.close()
            return True
        except FileNotFoundError:
            return False

    @staticmethod
    def ZAdd(name:str) -> bool:
        index:str = pw.Make(name)
        if index == "None": return False

        XRegistry.ZRaw["devices"].append({
            "name": f"{name}",
            "index": f"{index}"
        })
        XRegistry.ZSinks.append(XSink(name, index))

        XRegistry.ZWrite()
        return True

    @staticmethod
    def ZRemove(name:str) -> None:
        popper = lambda: None
        for iter, device in enumerate(XRegistry.ZRaw["devices"]):
            if device["name"] == name:
                popper = lambda i=iter: XRegistry.ZRaw["devices"].pop(i)
        popper()

        popper = lambda: None
        for iter, sink in enumerate(XRegistry.ZSinks):
            if sink.name == name:
                popper = lambda i=iter: XRegistry.ZSinks.pop(i)
        popper()

        pw.Remove(name)
        XRegistry.ZWrite()
        return