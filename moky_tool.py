import customtkinter as ctk

from pc_info.graphs import SystemMonitorFrame

from gui_moky_tool.tab_duplicates import DuplicatesFrame
from gui_moky_tool.tab_sorter import SorterFrame
from gui_moky_tool.tab_browsers import BrowsersFrame
from gui_moky_tool.tab_archivers import ArchiversFrame
from gui_moky_tool.tab_activation import ActivationFrame


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("moky tool")
app.geometry("1000x600")
app.resizable(False, False)

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

nav_frame = ctk.CTkFrame(app, corner_radius=0)
nav_frame.grid(row=0, column=0, sticky="nsew")
nav_frame.grid_rowconfigure(7, weight=1)

logo = ctk.CTkLabel(nav_frame, text="moky tool", font=ctk.CTkFont(size=20, weight="bold"))
logo.grid(row=0, column=0, padx=20, pady=20)

frames = {}
buttons = {}

def show_tab(name):
    for f in frames.values():
        f.grid_forget()
    for b in buttons.values():
        b.configure(fg_color="transparent")
    
    frames[name].grid(row=0, column=1, sticky="nsew")
    buttons[name].configure(fg_color=("gray75", "gray25"))

def change_theme(mode):
    ctk.set_appearance_mode(mode)

tabs_classes = {
    "sys": (SystemMonitorFrame, "Система и Нагрузка"),
    "dup": (DuplicatesFrame, "Поиск дубликатов"),
    "sort": (SorterFrame, "Авто-сортировщик"),
    "browser": (BrowsersFrame, "Установка браузеров"),
    "arch": (ArchiversFrame, "Установка архиваторов"),
    "act": (ActivationFrame, "Активация (MAS)")
}

for i, (key, (FrameClass, label)) in enumerate(tabs_classes.items(), start=1):
    frames[key] = FrameClass(app)
    
    btn = ctk.CTkButton(
        nav_frame, corner_radius=0, height=40, border_spacing=10, 
        text=label, fg_color="transparent", text_color=("gray10", "gray90"), 
        hover_color=("gray70", "gray30"), anchor="w",
        command=lambda k=key: show_tab(k)
    )
    btn.grid(row=i, column=0, sticky="ew")
    buttons[key] = btn

theme_menu = ctk.CTkOptionMenu(nav_frame, values=["Dark", "Light", "System"], command=change_theme)
theme_menu.grid(row=8, column=0, padx=20, pady=20, sticky="s")

show_tab("sys")

app.mainloop()
