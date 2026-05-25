from disks import get_system_disks
from hash import find_duplicates, remove_duplicates
from scanner import scan_disks


def main():
    print("запуск поиска дубликатов ! ")

    disks, b_list = get_system_disks()
    size_dict = scan_disks(disks, b_list)
    dup_dict = find_duplicates(size_dict)
    remove_duplicates(dup_dict)
    print("\nРабота программы завершена.")

if __name__ == "__main__":
    main()
