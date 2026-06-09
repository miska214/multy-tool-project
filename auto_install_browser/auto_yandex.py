import subprocess

def install_yandex():
    command = "winget install Yandex.Browser --silent --accept-package-agreements --accept-source-agreements"
    print("начинаю установку яндекс")
    try:
        subprocess.run(["cmd.exe", "/c", command], check=True)
        print("Успешно!")
    except subprocess.CalledProcessError:
        print("ошибка")

if __name__ == "__main__":
    install_yandex()
