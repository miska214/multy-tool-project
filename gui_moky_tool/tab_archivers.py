import customtkinter as ctk
import threading
from auto_install_WinRAR_and_ZIP.auto_WinRAR import winrar_install
from auto_install_WinRAR_and_ZIP.auto_zip import zip_install

class ArchiversFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=0, fg_color="transparent", **kwargs)
        
        lbl = ctk.CTkLabel(self, text="Установка WinRAR и 7-Zip", font=ctk.CTkFont(size=16, weight="bold"))
        lbl.pack(padx=20, pady=20)
        
        self.arch_status_label = ctk.CTkLabel(self, text="Статус: Ожидание выбора", font=ctk.CTkFont(size=12))
        self.arch_status_label.pack(pady=5)

        self.btn_winrar = ctk.CTkButton(self, text="Скачать WinRAR", command=lambda: self.run_task(winrar_install, "WinRAR"))
        self.btn_winrar.pack(pady=10)

        self.btn_7zip = ctk.CTkButton(self, text="Скачать 7-Zip", command=lambda: self.run_task(zip_install, "7-Zip"))
        self.btn_7zip.pack(pady=10)

    def run_task(self, target_func, arch_name):
        self.toggle_buttons("disabled")
        self.arch_status_label.configure(text=f"Статус: Установка {arch_name}...")
        
        def run():
            try:
                target_func()
                self.arch_status_label.configure(text=f"Статус: {arch_name} успешно установлен!")
            except Exception:
                self.arch_status_label.configure(text=f"Статус: Ошибка установки {arch_name}")
            finally:
                self.toggle_buttons("normal")

        threading.Thread(target=run, daemon=True).start()

    def toggle_buttons(self, state):
        self.btn_winrar.configure(state=state)
        self.btn_7zip.configure(state=state)
