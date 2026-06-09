import subprocess

def install_firefox():
    command = "winget install Mozilla.Firefox"
    print("начинаю скачивать firefox!")
    try:
        subprocess.run(["cmd.exe", "/c", command], check=True)
        print("Успешно!")
    except subprocess.CalledProcessError:
        print("ошибка!")

if __name__ == "__main__":
    install_firefox()
