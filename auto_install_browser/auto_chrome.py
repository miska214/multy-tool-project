import subprocess

def install_chrome():
    command = "winget install Google.Chrome"
    print("начинаю устанавливать Chrome!")
    try:
        subprocess.run(["cmd.exe", "/c", command], check=True)
        print("Chrome установлен!")
    except subprocess.CalledProcessError:
        print("Произошла ошибка при установке Chrome.")

if __name__ == "__main__":
    install_chrome()
