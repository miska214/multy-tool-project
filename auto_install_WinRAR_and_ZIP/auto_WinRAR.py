import subprocess

def winrar_install():
    command = "winget install RARLab.WinRAR"
    print("начинаю устанавливать WinRAR!")
    try:
        subprocess.run(["cmd.exe", "/c", command], check=True)
        print("WinRAR установлен!")
    except subprocess.CalledProcessError:
        print("Произошла ошибка при установке WinRAR.")

if __name__ == "__main__":
    winrar_install()