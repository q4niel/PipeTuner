import shell

#TODO: pactl device: TempDevice, shouldn't work -> index("TempD")
def index(name:str) -> int:
    name = name[::-1]
    modules:str = shell.cmd("pactl list modules")[::-1]
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

def mk(name:str) -> None:
    if index(name) == -1:
        shell.cmd(f"pactl load-module module-null-sink sink_name=\"{name}\"")
    return

def rm(name:str) -> None:
    i:int = index(name)
    if i != -1:
        shell.cmd(f"pactl unload-module {i}")
    return