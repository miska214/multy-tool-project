import customtkinter as ctk
import threading
from auto_install_browser.auto_chrome import install_chrome
from auto_install_browser.auto_mazzila import install_firefox
from auto_install_browser.auto_yandex import install_yandex

class BrowsersFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=0, fg_color="transparent", **kwargs)
        
        lbl = ctk.CTkLabel(self, text="Автоматическая установка браузеров", font=ctk.CTkFont(size=16, weight="bold"))
        lbl.pack(padx=20, pady=20)
        
        self.browser_status_label = ctk.CTkLabel(self, text="Статус: Ожидание выбора", font=ctk.CTkFont(size=12))
        self.browser_status_label.pack(pady=5)

        self.btn_chrome = ctk.CTkButton(self, text="Скачать Google Chrome", command=lambda: self.run_task(install_chrome, "Google Chrome"))
        self.btn_chrome.pack(pady=10)

        self.btn_firefox = ctk.CTkButton(self, text="Скачать Mozilla Firefox", command=lambda: self.run_task(install_firefox, "Mozilla Firefox"))
        self.btn_firefox.pack(pady=10)

        self.btn_yandex = ctk.CTkButton(self, text="Скачать Яндекс.Браузер", command=lambda: self.run_task(install_yandex, "Яндекс.Браузер"))
        self.btn_yandex.pack(pady=10)

    def run_task(self, target_func, browser_name):
        self.toggle_buttons("disabled")
        self.browser_status_label.configure(text=f"Статус: Установка {browser_name}...")
        
        def run():
            try:
                target_func()
                self.browser_status_label.configure(text=f"Статус: {browser_name} установлен!")
            except Exception:
                self.browser_status_label.configure(text=f"Статус: Ошибка установки {browser_name}")
            finally:
                self.toggle_buttons("normal")

        threading.Thread(target=run, daemon=True).start()

    def toggle_buttons(self, state):
        self.btn_chrome.configure(state=state)
        self.btn_firefox.configure(state=state)
        self.btn_yandex.configure(state=state)
