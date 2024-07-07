import tkinter as tk
import customtkinter as ctk

class ShopWindow(ctk.CTkToplevel):
    def __init__(self, parent, clicker, update_callback):
        super().__init__(parent)
        self.clicker = clicker
        self.update_callback = update_callback

        self.title("Shop")
        self.geometry("300x300")

        self.label = ctk.CTkLabel(self, text="Shop", font=("Helvetica", 18))
        self.label.pack(pady=10)

        self.item1_button = ctk.CTkButton(self, text="Клик I - 49 очков", command=self.buy_click1)
        self.item1_button.pack(pady=10)

        self.item2_button = ctk.CTkButton(self, text="Клик II - 99 очков", command=self.buy_click2)
        self.item2_button.pack(pady=10)

        self.item3_button = ctk.CTkButton(self, text="Клик III - 149 очков", command=self.buy_click3)
        self.item3_button.pack(pady=10)

        self.item4_button = ctk.CTkButton(self, text="Клик IV - 199 очков", command=self.buy_click4)
        self.item4_button.pack(pady=10)

        self.auto_farm_button = ctk.CTkButton(self, text="Авто-ферма I уровень - 199 очков", command=self.buy_auto_farm)
        self.auto_farm_button.pack(pady=10)

        self.error_label = ctk.CTkLabel(self, text="", font=("Helvetica", 14), text_color="red")
        self.error_label.pack(pady=10)

    def buy_click1(self):
        if self.clicker.buy_upgrade(49, 1):
            self.update_buttons()
            self.update_callback()
            self.error_label.configure(text="")
        else:
            self.error_label.configure(text="Недостаточно очков для покупки!")

    def buy_click2(self):
        if self.clicker.buy_upgrade(99, 2):
            self.update_buttons()
            self.update_callback()
            self.error_label.configure(text="")
        else:
            self.error_label.configure(text="Недостаточно очков для покупки!")

    def buy_click3(self):
        if self.clicker.buy_upgrade(149, 3):
            self.update_buttons()
            self.update_callback()
            self.error_label.configure(text="")
        else:
            self.error_label.configure(text="Недостаточно очков для покупки!")

    def buy_click4(self):
        if self.clicker.buy_upgrade(199, 4):
            self.update_buttons()
            self.update_callback()
            self.error_label.configure(text="")
        else:
            self.error_label.configure(text="Недостаточно очков для покупки!")

    def buy_auto_farm(self):
        if self.clicker.buy_auto_farm(199):
            self.update_buttons()
            self.update_callback()
            self.error_label.configure(text="")
        else:
            self.error_label.configure(text="Недостаточно очков для покупки!")

    def update_buttons(self):
        self.item1_button.configure(text=f"Клик I - 49 очков")
        self.item2_button.configure(text=f"Клик II - 99 очков")
        self.item3_button.configure(text=f"Клик III - 149 очков")
        self.item4_button.configure(text=f"Клик IV - 199 очков")
        self.auto_farm_button.configure(text=f"Авто-ферма I уровень - 199 очков")
