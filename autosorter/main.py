from autosorter.folders_creater import ger_real_desktop_path, file_rules
from autosorter.sorter_logic import execute_sorting

while (True):
    print(" Меню")
    print("1. Сортировка без копирования (перемещение)")
    print("2. Сортировка с копированием")
    print("3. Выход")
    
    choice = input("Выберите действие: ").strip()
    
    if choice == "1":
        desktop = ger_real_desktop_path()
        execute_sorting(desktop, file_rules, choice)
        print("Сортировка с перемещением...")
        
    elif choice == "2":
        desktop = ger_real_desktop_path()
        execute_sorting(desktop, file_rules, choice)
        print("Сортировка без копирования...")
        
    elif choice == "3":
        print("выход...")
        break
    else:
        print("Неверный ввод, попробуйте еще раз")