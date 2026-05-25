def scan_disks(found_disks, black_list):
    black_list_lower = {folder.lower() for folder in black_list}
    files_size = {}
    file_count = 0

    for disk in found_disks:
        print(f"Сканирование диска {disk}...")
        folders_to_scan = [disk]

        while folders_to_scan:
            current_folder = folders_to_scan.pop(0)

            try:
                for file in current_folder.iterdir():
                    if file.is_dir():
                        if file.name.lower() not in black_list_lower:
                            folders_to_scan.append(file)
                    elif file.is_file():
                        try:
                            size = file.stat().st_size
                            if size > 0:
                                if size not in files_size:
                                    files_size[size] = []
                                files_size[size].append(file)
                                
                                file_count += 1
                                if file_count % 5000 == 0:
                                    print(f"Найдено файлов для анализа: {file_count}")
                                    
                        except (PermissionError, FileNotFoundError):
                            continue
            except (PermissionError, FileNotFoundError):
                continue

    print(f"Этап сканирования завершен. Всего найдено файлов: {file_count}")
    return files_size
