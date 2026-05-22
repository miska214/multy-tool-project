from pathlib import Path
import shutil

for file in Path("C:/").glob("**/*"):
    if file.is_file():
        if file.name ==  "comfy":
            file.rename(file.with_name("comfy2"))
            new_file = file.shutil.copy("comfy2")
            new_file.rename(file.with_name("comfy3"))
            new_file.rename(Path(r"C:\Users\zarda\OneDrive\Рабочий стол"))
