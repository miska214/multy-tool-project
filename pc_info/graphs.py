import customtkinter as ctk
import psutil
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.ticker as ticker

from pc_info.pc_info_parser import get_pc_info

class LiveGraph:
    def __init__(self, parent_frame, title_name, line_color="#1f77b4"):
        self.fig, self.ax = plt.subplots(figsize=(4.5, 1.8))
        
        self.fig.patch.set_facecolor('#1a1a1a')
        self.ax.set_facecolor('#1a1a1a')
        
        self.ax.set_title(title_name, color='white', fontsize=11, pad=10, loc='left')
        self.ax.grid(True, color='#333333', linestyle='--', linewidth=0.5)
        
        self.data_history = [0] * 60
        self.line, = self.ax.plot(self.data_history, color=line_color, linewidth=2)
        
        self.ax.set_ylim(0, 100)
        self.ax.set_xlim(0, 59)
        
        self.ax.xaxis.set_major_locator(ticker.NullLocator())
        self.ax.yaxis.set_major_locator(ticker.MultipleLocator(25))
        self.ax.tick_params(colors='gray', labelsize=9)
        
        self.fig.tight_layout()
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=parent_frame)
        self.canvas_widget = self.canvas.get_tk_widget()

    def pack(self, **kwargs):
        self.canvas_widget.pack(**kwargs)

    def update_value(self, new_value):
        self.data_history.pop(0)
        self.data_history.append(new_value)
        
        self.line.set_ydata(self.data_history)
        self.canvas.draw_idle()


class SystemMonitorFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=0, fg_color="transparent", **kwargs)
        
        hardware = get_pc_info()
        
        self.hardware_frame = ctk.CTkFrame(self, fg_color="#222222", corner_radius=8)
        self.hardware_frame.pack(fill="x", padx=20, pady=(10, 10))
        
        self.lbl_cpu_info = ctk.CTkLabel(self.hardware_frame, text=f"Процессор: {hardware['cpu']}", font=("Arial", 12, "bold"), text_color="#00bcff")
        self.lbl_cpu_info.pack(anchor="w", padx=15, pady=(10, 2))
        
        self.lbl_gpu_info = ctk.CTkLabel(self.hardware_frame, text=f"Видеокарта: {hardware['gpu']}", font=("Arial", 12, "bold"), text_color="#2ecc71")
        self.lbl_gpu_info.pack(anchor="w", padx=15, pady=2)

        self.lbl_board_info = ctk.CTkLabel(self.hardware_frame, text=f"Мат. плата: {hardware['board']}", font=("Arial", 11), text_color="gray")
        self.lbl_board_info.pack(anchor="w", padx=15, pady=2)

        self.lbl_mem_info = ctk.CTkLabel(self.hardware_frame, text=f"Оперативная память: {hardware['memory']}  |  Всего на дисках: {hardware['disk']}", font=("Arial", 11), text_color="gray")
        self.lbl_mem_info.pack(anchor="w", padx=15, pady=(2, 10))
        
        self.graphs_container = ctk.CTkFrame(self, fg_color="transparent")
        self.graphs_container.pack(fill="both", expand=True, padx=20, pady=5)

        self.cpu_graph = LiveGraph(self.graphs_container, title_name="Загрузка ЦП (%)", line_color="#00bcff")
        self.cpu_graph.pack(fill="x", pady=5)
        
        self.ram_graph = LiveGraph(self.graphs_container, title_name="Использование ОЗУ (%)", line_color="#2ecc71")
        self.ram_graph.pack(fill="x", pady=5)
        
        self.animate_graphs()

    def animate_graphs(self):
        cpu_percent = psutil.cpu_percent()
        ram_percent = psutil.virtual_memory().percent
        
        self.cpu_graph.update_value(cpu_percent)
        self.ram_graph.update_value(ram_percent)
        
        self.after(1000, self.animate_graphs)
