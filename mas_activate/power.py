import subprocess

command = "irm https://get.activated.win | iex"

try: 
     subprocess.run(["powershell.exe","-command", command], check=True)
except subprocess.CalledProcessError as e:
    print("Ошибка выполнения:", e.stderr)
