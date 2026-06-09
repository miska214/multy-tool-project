import customtkinter as ctk
import threading
from autosorter.folders_creater import ger_real_desktop_path, file_rules
from autosorter.sorter_logic import execute_sorting

class SorterFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=0, fg_color="transparent", **kwargs)
        
        lbl = ctk.CTkLabel(self, text="Автоматический сортировщик файлов", font=ctk.CTkFont(size=16, weight="bold"))
        lbl.pack(padx=20, pady=20)
        
        self.sort_status_label = ctk.CTkLabel(self, text="Статус: Ожидание запуска", font=ctk.CTkFont(size=12))
        self.sort_status_label.pack(pady=5)

        self.sort_mode_switch = ctk.CTkSegmentedButton(self, values=["Переместить файлы", "Скопировать файлы"])
        self.sort_mode_switch.set("Переместить файлы")
        self.sort_mode_switch.pack(pady=15)

        self.btn_sort_start = ctk.CTkButton(self, text="Начать сортировку всех дисков", command=self.start_sorting)
        self.btn_sort_start.pack(pady=10)

    def start_sorting(self):
        self.btn_sort_start.configure(state="disabled")
        self.sort_status_label.configure(text="Статус: Сортировка запущена... Сканируем диски!")
        selected_mode = "1" if self.sort_mode_switch.get() == "Переместить файлы" else "2"

        def run():
            try:
                desktop_path = ger_real_desktop_path()
                execute_sorting(desktop_path, file_rules, selected_mode)
                self.sort_status_label.configure(text="Статус: Сортировка успешно завершена!")
            except Exception:
                self.sort_status_label.configure(text="Статус: Произошла ошибка при сортировке")
            finally:
                self.btn_sort_start.configure(state="normal")

        threading.Thread(target=run, daemon=True).start()
