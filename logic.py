import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import time
from pynput import mouse, keyboard
from design import setup_gui
import platform

class AutoClicker:
    def __init__(self, root):
        self.root = root
        self.running = False
        self.paused = False

        self.interval_entry = None
        self.time_limit_entry = None
        self.use_time_limit_var = None
        self.click_button_var = None
        self.click_type_var = None
        self.fixed_position_var = None
        self.fixed_x_entry = None
        self.fixed_y_entry = None
        self.start_button = None
        self.pause_button = None
        self.stop_button = None
        self.reset_button = None
        self.status_label = None

        self.setup_widgets()
        self.setup_killswitch_thread()

        self.mouse = mouse.Controller()

    def setup_widgets(self):
        (self.interval_entry, self.time_limit_entry, self.use_time_limit_var,
         self.click_button_var, self.click_type_var, self.fixed_position_var,
         self.fixed_x_entry, self.fixed_y_entry, self.start_button, 
         self.pause_button, self.stop_button, self.reset_button,
         self.status_label) = setup_gui(self.root, self.start_clicking, self.pause_clicking, self.stop_clicking, self.reset)

    def setup_killswitch_thread(self):
        killswitch_thread = threading.Thread(target=self.setup_killswitch)
        killswitch_thread.daemon = True
        killswitch_thread.start()

    def setup_killswitch(self):
        def on_press(key):
            if key == keyboard.Key.esc:
                print("Kill switch pressed.")
                self.stop_clicking()
            elif key == keyboard.Key.ctrl:
                print("Start switch pressed.")
                self.start_clicking()

        print("Setting up kill switch listener...")
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

    def start_clicking(self):
        if self.paused:
            self.paused = False
            self.update_status("Running")
            return

        try:
            interval = float(self.interval_entry.get())
            if interval <= 0:
                raise ValueError("Interval must be a positive number.")
            if self.use_time_limit_var.get():
                time_limit = float(self.time_limit_entry.get())
                if time_limit <= 0:
                    raise ValueError("Time limit must be a positive number.")
            else:
                time_limit = float('inf')
        except ValueError as e:
            messagebox.showerror("Invalid input", str(e))
            return

        if not self.running:
            self.running = True
            self.root.iconify()  # Minimize the window
            self.update_status("Running")
            self.click_thread = threading.Thread(target=self.click_loop, args=(interval, time_limit))
            self.click_thread.start()
            print("Auto clicker started.")

    def click_loop(self, interval, time_limit):
        start_time = time.time()
        try:
            while self.running and (time.time() - start_time) < time_limit:
                if not self.paused:
                    self.perform_click()
                    time.sleep(interval)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            self.running = False
            self.root.deiconify()  # Restore the window
            self.update_status("Stopped")
            print("Time limit reached or auto clicker stopped.")

    def perform_click(self):
        click_type = self.click_type_var.get()
        click_button = mouse.Button.left if self.click_button_var.get() == "left" else mouse.Button.right
        if self.fixed_position_var.get():
            x = int(self.fixed_x_entry.get())
            y = int(self.fixed_y_entry.get())
            self.mouse.position = (x, y)
        if click_type == "single":
            self.mouse.click(click_button)
        else:
            self.mouse.click(click_button)
            time.sleep(0.05)
            self.mouse.click(click_button)

    def pause_clicking(self):
        if self.running:
            self.paused = not self.paused
            status = "Paused" if self.paused else "Running"
            self.update_status(status)
            print(f"Auto clicker {status.lower()}.")

    def stop_clicking(self):
        if self.running:
            print("Stopping auto clicker...")
            self.running = False
            if hasattr(self, 'click_thread'):
                self.click_thread.join(timeout=1)
            self.update_status("Stopped")
            print("Auto clicker stopped.")

    def reset(self):
        self.stop_clicking()
        self.interval_entry.delete(0, tk.END)
        self.time_limit_entry.delete(0, tk.END)
        self.use_time_limit_var.set(0)
        self.click_button_var.set("left")
        self.click_type_var.set("single")
        self.fixed_position_var.set(0)
        self.fixed_x_entry.delete(0, tk.END)
        self.fixed_y_entry.delete(0, tk.END)
        self.update_status("Stopped")
        print("Settings reset.")

    def update_status(self, status):
        self.status_label.config(text=f"Status: {status}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoClicker(root)
    root.mainloop()
