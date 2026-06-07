import wmi

def get_pc_info():
    computer = wmi.WMI()
    
    result_cpu = ""
    result_gpu = ""
    result_memory = 0.0
    total_disk_size = 0  # Будем складывать объем всех дисков
    result_board = ""
    
    # 1. Процессор
    for cpu in computer.Win32_Processor():
        result_cpu = cpu.Name.strip()
    
    # 2. Видеокарта (убрали скобки () у свойств)
    for gpu in computer.Win32_VideoController():
        result_gpu = gpu.Name
        # Объем видеопамяти нам тут не критичен, если нужно только название
    
    # 3. Оперативная память
    for memory in computer.Win32_ComputerSystem():
        result_memory = int(memory.TotalPhysicalMemory) / (1024 ** 3)
        
    # 4. Накопители (суммируем общий объем всех SSD/HDD)
    for disk in computer.Win32_DiskDrive():
        total_disk_size += int(disk.Size) / (1024 ** 3)
            
    # 5. Материнская плата (добавим, раз переменная создана)
    for board in computer.Win32_BaseBoard():
        result_board = f"{board.Manufacturer} {board.Product}"
        
    full_result = {
        'cpu': result_cpu,
        'gpu': result_gpu,
        'memory': f"{result_memory:.2f} GB", # Сразу округлим для красоты
        'disk': f"{total_disk_size:.0f} GB",
        'board': result_board,
    }
    
    return full_result # ОБЯЗАТЕЛЬНО возвращаем результат из функции

# Проверяем работу функции
info = get_pc_info()
print(info)