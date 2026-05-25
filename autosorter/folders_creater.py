import winreg
from pathlib import Path


def ger_real_desktop_path():
    adress_reestr = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
    )
    
    nude_path, data_type =  winreg.QueryValueEx(adress_reestr, "Desktop")
    clean_path = winreg.ExpandEnvironmentStrings(nude_path)
    winreg.CloseKey(adress_reestr)
    return Path(clean_path)
    
print(ger_real_desktop_path())

file_rules = {
    ".txt": "office файлы",
    ".doc": "office файлы",
    ".docx": "office файлы",
    ".pdf": "office файлы",
    ".odt": "office файлы",
    ".xls": "office файлы",
    ".xlsx": "office файлы",
    ".csv": "office файлы",
    ".ppt": "office файлы",
    ".pptx": "office файлы",
    ".jpg": "изображения",
    ".png": "изображения",
    ".jpeg": "изображения",
    ".gif": "изображения",
    ".bmp": "изображения",
    ".webp": "изображения",
    ".mp4": "видео",
    ".avi": "видео",
    ".mkv": "видео",
    ".zip": "архивы",
    ".rar": "архивы",
    ".7z": "архивы",
}