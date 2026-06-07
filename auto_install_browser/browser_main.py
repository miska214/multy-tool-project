while True:
    print("1. Скачать Chrome \n2. скачать FireFox \n3. скачать Yandex \n0. выход")
    try:
        choice = input("Выберите действие: ").strip()
        if choice == "1":
            print("Идет установка Chrome...")
        elif choice == "2":
            print("Идет установка FireFox...")
        elif choice == "3":
            print("Идет установка Yandex...")
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод, попробуйте еще раз")
    except ValueError:
        print("Произошла ошибка ввода, попробуйте еще раз")
        
        