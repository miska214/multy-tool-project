import hashlib


def get_file_hash(file_path):
    hasher = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(65536):
                hasher.update(chunk)
        return hasher.hexdigest()
    except (PermissionError, FileNotFoundError):
        return None


def find_duplicates(files_size):
    duplicates = {}
    for size, paths in files_size.items():
        if len(paths) < 2:
            continue

        hashes = {}
        for path in paths:
            file_hash = get_file_hash(path)
            if file_hash:
                if file_hash not in hashes:
                    hashes[file_hash] = []
                hashes[file_hash].append(path)

        for file_hash, paths_list in hashes.items():
            if len(paths_list) > 1:
                if file_hash not in duplicates:
                    duplicates[file_hash] = []
                duplicates[file_hash].extend(paths_list)

    return duplicates


def remove_duplicates(duplicates):
    if not duplicates:
        print("Дубликаты не обнаружены.")
        return

    print(f"\nОбнаружено групп дубликатов: {len(duplicates)}")
    total_deleted = 0

    for file_hash, paths in duplicates.items():
        print(f"\nОригинал: {paths}")
        for dup in paths[1:]:
            print(f"  -> Дубликат: {dup}")

    choice = (
        input("\nУдалить все найденные дубликаты? (y/n): ").strip().lower()
    )
    if choice == "y":
        for file_hash, paths in duplicates.items():
            for dup in paths[1:]:
                try:
                    dup.unlink()
                    total_deleted += 1
                except Exception as e:
                    print(f"Ошибка удаления {dup}: {e}")
        print(f"Успешно удалено файлов: {total_deleted}")
    else:
        print("Удаление отменено.")