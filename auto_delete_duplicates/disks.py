from pathlib import Path


def get_system_disks():
    black_list = {
        "Windows",
        "Program Files",
        "Program Files (x86)",
        "$Recycle.Bin",
        "AppData",
        "System Volume Information",
        "ProgramData",
        "$WinREAgent",
        "Boot",
        "EFI",
        "node_modules",
        ".git",
        ".venv",
        "venv",
        "Config.Msi",
        "Recovery",
        "MSOCache",
        "OneDrive",
        "YandexDisk",
        "Google Drive",
        "iCloudDrive",
        "Dropbox",
    }
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    found_disks = []

    for letter in letters:
        pc_disk = Path(f"{letter}:/")
        if pc_disk.exists():
            found_disks.append(pc_disk)

    return found_disks, black_list