import subprocess

def start_mas_activation():
    command = 'start powershell.exe -NoExit -ExecutionPolicy Bypass -Command "irm https://get.activated.win | iex"'
    
    try: 
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Ошибка выполнения:", e)
