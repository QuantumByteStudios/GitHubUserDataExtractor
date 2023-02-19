import subprocess
import platform


def clear():
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)  # nosec B602, B607
    else:
        subprocess.run("clear", shell=True)  # nosec B602, B607


def openResult():
    if platform.system() == "Windows":
        subprocess.run('start Data/ReceivedEvents/boot.html',
                       shell=True)  # nosec B602, B607
    else:
        subprocess.run(
            'open Data/ReceivedEvents/boot.html 2>/dev/null', shell=True)  # nosec B602, B607
