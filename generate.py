import tkinter as tk
from tkinter import messagebox
import json
import os

# Hàm để tạo file .bat
def create_bat_file(lower_delay, upper_delay):
    bat_content = f"""
@echo off
echo Lower delay: {lower_delay} seconds...
echo Upper delay: {upper_delay} seconds...
:loop
set /a delay=%random% %% {upper_delay - lower_delay + 1} + {lower_delay}

echo Waiting for %delay% seconds...

timeout /t %delay% /nobreak >nul

echo Running node index.js after the delay...
node index.js

goto loop
"""
    with open("run_with_delay.bat", "w") as bat_file:
        bat_file.write(bat_content)

def create_json_file(token, channel, bot_id, command, subcommand):
    info = {
        "token": token,
        "channel": channel,
        "bot_id": bot_id,
        "command": command,
        "subcommand": subcommand
    }
    with open("info.json", "w") as json_file:
        json.dump(info, json_file, indent=4)

def generate_files():
    lower_delay = lower_delay_entry.get()
    upper_delay = upper_delay_entry.get()
    token = token_entry.get()
    channel = channel_entry.get()
    bot_id = bot_id_entry.get()
    command = command_entry.get()
    subcommand = subcommand_entry.get()

    if not lower_delay.isdigit() or not upper_delay.isdigit():
        messagebox.showerror("Input Error", "Delay must be valid numbers.")
        return

    lower_delay = int(lower_delay)
    upper_delay = int(upper_delay)

    if lower_delay >= upper_delay:
        messagebox.showerror("Input Error", "Lower Delay must be less than Upper Delay.")
        return

    create_bat_file(lower_delay, upper_delay)
    create_json_file(token, channel, bot_id, command, subcommand)

    messagebox.showinfo("Success", "Files created successfully!")

root = tk.Tk()
root.title("Create BAT and JSON files")


tk.Label(root, text="Lower Delay (seconds):").grid(row=0, column=0, padx=10, pady=10)
lower_delay_entry = tk.Entry(root)
lower_delay_entry.grid(row=0, column=1, padx=10, pady=10)


tk.Label(root, text="Upper Delay (seconds):").grid(row=1, column=0, padx=10, pady=10)
upper_delay_entry = tk.Entry(root)
upper_delay_entry.grid(row=1, column=1, padx=10, pady=10)


tk.Label(root, text="Token:").grid(row=2, column=0, padx=10, pady=10)
token_entry = tk.Entry(root)
token_entry.grid(row=2, column=1, padx=10, pady=10)


tk.Label(root, text="Channel:").grid(row=3, column=0, padx=10, pady=10)
channel_entry = tk.Entry(root)
channel_entry.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Bot ID:").grid(row=4, column=0, padx=10, pady=10)
bot_id_entry = tk.Entry(root)
bot_id_entry.grid(row=4, column=1, padx=10, pady=10)


tk.Label(root, text="Command:").grid(row=5, column=0, padx=10, pady=10)
command_entry = tk.Entry(root)
command_entry.grid(row=5, column=1, padx=10, pady=10)

tk.Label(root, text="Sub Command:").grid(row=6, column=0, padx=10, pady=10)
subcommand_entry = tk.Entry(root)
subcommand_entry.grid(row=6, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Files", command=generate_files)
generate_button.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()
