import customtkinter as ctk
import threading
from mas_activate.power import start_mas_activation

class ActivationFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=0, fg_color="transparent", **kwargs)
        
        lbl = ctk.CTkLabel(self, text="Активация Windows и Office via MAS", font=ctk.CTkFont(size=16, weight="bold"))
        lbl.pack(padx=20, pady=20)
        
        self.mas_status_label = ctk.CTkLabel(self, text="Статус: Ожидание запуска", font=ctk.CTkFont(size=12))
        self.mas_status_label.pack(pady=5)

        self.btn_mas_start = ctk.CTkButton(self, text="Запустить Microsoft Activation Scripts", command=self.run_mas)
        self.btn_mas_start.pack(pady=10)

    def run_mas(self):
        self.btn_mas_start.configure(state="disabled")
        self.mas_status_label.configure(text="Статус: Запуск MAS в скрытом режиме...")
        
        def run():
            try:
                start_mas_activation()
                self.mas_status_label.configure(text="Статус: Команда активации успешно отправлена.")
            except Exception:
                self.mas_status_label.configure(text="Статус: Ошибка фоновой активации.")
            finally:
                self.btn_mas_start.configure(state="normal")

        threading.Thread(target=run, daemon=True).start()
