import customtkinter as ctk
import threading
from auto_delete_duplicates.disks import get_system_disks
from auto_delete_duplicates.hash import find_duplicates, remove_duplicates
from auto_delete_duplicates.scanner import scan_disks

class DuplicatesFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=0, fg_color="transparent", **kwargs)
        
        lbl = ctk.CTkLabel(self, text="Поиск и удаление дубликатов файлов", font=ctk.CTkFont(size=16, weight="bold"))
        lbl.pack(padx=20, pady=20)
        
        self.start_btn = ctk.CTkButton(self, text="Запустить поиск дубликатов", command=self.start_search)
        self.start_btn.pack(pady=10)

        self.status_label = ctk.CTkLabel(self, text="Статус: Ожидание запуска", font=ctk.CTkFont(size=12))
        self.status_label.pack(pady=10)

    def start_search(self):
        self.status_label.configure(text="Статус: Поиск запущен... Окно не зависнет!")
        self.start_btn.configure(state="disabled")
        
        def run():
            disks, b_list = get_system_disks()
            size_dict = scan_disks(disks, b_list)
            dup_dict = find_duplicates(size_dict)
            remove_duplicates(dup_dict)
            self.status_label.configure(text="Статус: Работа программы завершена.")
            self.start_btn.configure(state="normal")

        threading.Thread(target=run, daemon=True).start()
