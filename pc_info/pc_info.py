import wmi

def get_pc_info():
    computer = wmi.WMI()
    
    result_cpu = ""
    result_gpu = ""
    result_memory = 0.0
    total_disk_size = 0
    result_board = ""

    for cpu in computer.Win32_Processor():
        result_cpu = cpu.Name.strip()

    for gpu in computer.Win32_VideoController():
        result_gpu = gpu.Name

    for memory in computer.Win32_ComputerSystem():
        result_memory = int(memory.TotalPhysicalMemory) / (1024 ** 3)

    for disk in computer.Win32_DiskDrive():
        total_disk_size += int(disk.Size) / (1024 ** 3)

    for board in computer.Win32_BaseBoard():
        result_board = f"{board.Manufacturer} {board.Product}"
        
    full_result = {
        'cpu': result_cpu,
        'gpu': result_gpu,
        'memory': f"{result_memory:.2f} GB", # Сразу округлим для красоты
        'disk': f"{total_disk_size:.0f} GB",
        'board': result_board,
    }
    
    return full_result

info = get_pc_info()
print(info)