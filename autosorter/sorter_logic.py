from pathlib import Path
import shutil

def execute_sorting(clean_path,rules_dict, mode):
    black_list = {"Windows", "Program Files", "Program Files (x86)", "$Recycle.Bin", "AppData"}
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for letter in letters:
        pc_disk = Path(f"{letter}:/")
        if pc_disk.exists():
            try:
                    for root_folder in pc_disk.iterdir():
                        for file in root_folder.rglob("*"):
                    
                            if set(file.parts).intersection(black_list):
                                continue
                    
                            if file.is_file():
                                extension = file.suffix.lower()
                                
                                if extension in rules_dict:
                                    print(f"файл {file.name}, поедет в папку {rules_dict[extension]}")
                                    
                                    folder_name = rules_dict[extension]
                                    target_folder = clean_path/folder_name
                                    target_folder.mkdir(exist_ok=True)
                                    final_file_path = target_folder/file.name
                                    
                                    if mode == "1":
                                        file.rename(final_file_path)
                                    elif mode == "2":
                                        shutil.copy2(file, final_file_path)
            except PermissionError:
                continue