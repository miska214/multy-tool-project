import subprocess

def zip_install():
    command = "winget install 7zip.7zip"
    print("начинаю устанавливать 7zip!")
    try:
        subprocess.run(["cmd.exe", "/c", command], check=True)
        print("7zip установлен!")
    except subprocess.CalledProcessError:
        print("Произошла ошибка при установке 7zip.")

if __name__ == "__main__":
   zip_install()