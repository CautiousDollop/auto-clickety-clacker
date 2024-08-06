import tkinter as tk
from tkinter import ttk
from tkinter import font

def setup_gui(root, start_command, pause_command, stop_command, reset_command):
    root.title("Simple Auto Clicker")
    root.configure(background='#2C2F33')  # Dark background color

    # Define the font to use with a fallback
    font_choice = ('Roboto', 12) if 'Roboto' in font.families() else ('Helvetica', 12)

    style = ttk.Style(root)
    style.theme_use('clam')

    # Configure the primary style elements
    style.configure('TButton', font=font_choice, padding=6, background='#7289DA', foreground='#FFFFFF', borderwidth=0)
    style.map('TButton', background=[('active', '#5A6FB0')])

    style.configure('TLabel', font=font_choice, padding=6, background='#2C2F33', foreground='#FFFFFF')

    style.configure('TEntry', font=font_choice, padding=6, fieldbackground='#99AAB5', foreground='#000000')

    style.configure('TCheckbutton', font=font_choice, background='#2C2F33', foreground='#FFFFFF')
    style.map('TCheckbutton', background=[('active', '#99AAB5')])

    style.configure('TRadiobutton', font=font_choice, background='#2C2F33', foreground='#FFFFFF')
    style.map('TRadiobutton', background=[('active', '#99AAB5')])

    # Interval label and entry
    interval_label = ttk.Label(root, text="Click Interval (seconds):", style='TLabel')
    interval_label.pack(pady=5)
    interval_entry = ttk.Entry(root, style='TEntry')
    interval_entry.pack(pady=5)

    # Time limit label and entry
    time_limit_label = ttk.Label(root, text="Time Limit (seconds):", style='TLabel')
    time_limit_label.pack(pady=5)
    time_limit_entry = ttk.Entry(root, style='TEntry')
    time_limit_entry.pack(pady=5)

    # Use time limit checkbox
    use_time_limit_var = tk.IntVar()
    use_time_limit_checkbox = ttk.Checkbutton(root, text="Use Time Limit", variable=use_time_limit_var, style='TCheckbutton')
    use_time_limit_checkbox.pack(pady=5)

    # Click button selection
    click_button_label = ttk.Label(root, text="Click Button:", style='TLabel')
    click_button_label.pack(pady=5)
    click_button_var = tk.StringVar(value="left")
    click_button_left = ttk.Radiobutton(root, text="Left", variable=click_button_var, value="left", style='TRadiobutton')
    click_button_left.pack(pady=5)
    click_button_right = ttk.Radiobutton(root, text="Right", variable=click_button_var, value="right", style='TRadiobutton')
    click_button_right.pack(pady=5)

    # Click type selection
    click_type_label = ttk.Label(root, text="Click Type:", style='TLabel')
    click_type_label.pack(pady=5)
    click_type_var = tk.StringVar(value="single")
    click_type_single = ttk.Radiobutton(root, text="Single", variable=click_type_var, value="single", style='TRadiobutton')
    click_type_single.pack(pady=5)
    click_type_double = ttk.Radiobutton(root, text="Double", variable=click_type_var, value="double", style='TRadiobutton')
    click_type_double.pack(pady=5)

    # Fixed position selection
    fixed_position_var = tk.IntVar()
    fixed_position_checkbox = ttk.Checkbutton(root, text="Fixed Position", variable=fixed_position_var, style='TCheckbutton')
    fixed_position_checkbox.pack(pady=5)

    # Fixed position coordinates
    fixed_x_label = ttk.Label(root, text="Fixed X:", style='TLabel')
    fixed_x_label.pack(pady=5)
    fixed_x_entry = ttk.Entry(root, style='TEntry')
    fixed_x_entry.pack(pady=5)

    fixed_y_label = ttk.Label(root, text="Fixed Y:", style='TLabel')
    fixed_y_label.pack(pady=5)
    fixed_y_entry = ttk.Entry(root, style='TEntry')
    fixed_y_entry.pack(pady=5)

    # Start button
    start_button = ttk.Button(root, text="Start", command=start_command, style='TButton')
    start_button.pack(pady=10)

    # Pause button
    pause_button = ttk.Button(root, text="Pause/Resume", command=pause_command, style='TButton')
    pause_button.pack(pady=10)

    # Stop button
    stop_button = ttk.Button(root, text="Stop", command=stop_command, style='TButton')
    stop_button.pack(pady=10)

    # Reset button
    reset_button = ttk.Button(root, text="Reset", command=reset_command, style='TButton')
    reset_button.pack(pady=10)

    # Status label
    status_label = ttk.Label(root, text="Status: Stopped", style='TLabel')
    status_label.pack(pady=10)

    return (interval_entry, time_limit_entry, use_time_limit_var, click_button_var, click_type_var,
            fixed_position_var, fixed_x_entry, fixed_y_entry, start_button, pause_button, stop_button,
            reset_button, status_label)
