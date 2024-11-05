import shell

def Info() -> str:
    return shell.CMD("pactl list modules")

#TODO: pactl device: TempDevice, shouldn't work -> index("TempD")
def Index(name:str) -> int:
    name = name[::-1]
    modules:str = shell.CMD("pactl list modules")[::-1]
    nameBuffer:str = ""
    moduleBuffer:str = ""
    index:str = ""

    for c in modules:
        if name != nameBuffer:
            if c == name[len(nameBuffer)]:
                nameBuffer += c
            else: nameBuffer = ""
            continue

        if c.isdigit():
            index += c
            continue

        if len(index) == 0: continue
        moduleBuffer += c

        if len(moduleBuffer) == 8:
            if moduleBuffer == "# eludoM":
                break
            moduleBuffer = ""
            index = ""

    return -1 if index == "" else int(index[::-1])

def Make(name:str) -> str:
    if Index(name) != -1: return "None"
    return shell.CMD(f"pactl load-module module-null-sink sink_name=\"{name}\"")

def Remove(name:str) -> None:
    i:int = Index(name)
    if i != -1:
        shell.CMD(f"pactl unload-module {i}")
    return