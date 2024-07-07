import tkinter as tk
import customtkinter as ctk
from clicker_mechanics.clicker import ClickerMechanics
from Shop.shop import ShopWindow
import pickle
import os

class ClickerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Super Duper Sus Clicker - beta-test")
        self.geometry("400x300")
        
        self.clicker = ClickerMechanics()
        self.load_progress()
        
        self.label = ctk.CTkLabel(self, text=f"Clicks: {self.clicker.count}", font=("Helvetica", 24))
        self.label.pack(pady=20)

        self.click_button = ctk.CTkButton(self, text="Click me!", command=self.increase_count)
        self.click_button.pack(pady=20)
        
        self.shop_button = ctk.CTkButton(self, text="Shop", command=self.open_shop)
        self.shop_button.pack(pady=20)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.auto_farm()

    def increase_count(self):
        self.clicker.increase_count()
        self.update_label()

    def update_label(self):
        self.label.configure(text=f"Clicks: {self.clicker.count}")

    def open_shop(self):
        ShopWindow(self, self.clicker, self.update_label)

    def auto_farm(self):
        self.clicker.auto_farm_update()
        self.update_label()
        self.after(1000, self.auto_farm)

    def on_closing(self):
        self.save_progress()
        self.destroy()

    def save_progress(self):
        with open("progress.pkl", "wb") as f:
            pickle.dump(self.clicker.get_state(), f)

    def load_progress(self):
        if os.path.exists("progress.pkl"):
            with open("progress.pkl", "rb") as f:
                state = pickle.load(f)
                self.clicker.set_state(state)

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # "light" for light mode
    ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"
    
    app = ClickerApp()
    app.mainloop()
