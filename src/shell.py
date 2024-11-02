import subprocess

def cmd(cmd:str) -> str:
    try:
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode()

    except subprocess.CalledProcessError as e:
        return e.stderr.decode()