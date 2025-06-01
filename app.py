import customtkinter as ctk
from tkinter import messagebox
from cipher import encrypt_vigenere, decrypt_vigenere
from db import save_message, get_all_messages, init_db

# Initialize DB
init_db()

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Colors
BG_GRADIENT = "#e0c3fc"  # pastel purple
CARD_BG = "#f8fafc"      # card background
BTN_PURPLE = "#a259f7"
BTN_RED = "#ff6b6b"
BTN_GREEN = "#43e97b"
BTN_BLUE = "#38b6ff"
BTN_GRAY = "#6c757d"

FONT_TITLE = ("Segoe UI", 24, "bold")
FONT_SUBTITLE = ("Segoe UI", 12, "italic")
FONT_LABEL = ("Segoe UI", 13, "bold")
FONT = ("Segoe UI", 11)

# Main window
root = ctk.CTk()
root.title("🔐 Vigenère Cipher GUI")
root.geometry("900x700")
root.configure(bg=BG_GRADIENT)

# Title & subtitle
title = ctk.CTkLabel(root, text="Vigenère Cipher", font=FONT_TITLE, text_color="#a259f7", bg_color=BG_GRADIENT)
title.pack(pady=(20, 0))
subtitle = ctk.CTkLabel(root, text="🔒 Secure text encryption and decryption tool ✨", font=FONT_SUBTITLE, text_color="#888", bg_color=BG_GRADIENT)
subtitle.pack(pady=(0, 20))

# --- Card 1: Input ---
card1 = ctk.CTkFrame(root, fg_color=CARD_BG, corner_radius=18)
card1.pack(pady=10, padx=20, fill="x", ipadx=10, ipady=10)

# Encryption Key
key_label = ctk.CTkLabel(card1, text="\U0001F511 Encryption Key", font=FONT_LABEL, text_color="#a259f7", anchor="w")
key_label.pack(anchor="w", pady=(10, 0), padx=20)
input_key = ctk.CTkEntry(card1, width=400, font=FONT, placeholder_text="Enter your secret key... \U0001F511")
input_key.pack(pady=(0, 10), padx=20, anchor="w")

# Message/Encrypted Text
msg_label = ctk.CTkLabel(card1, text="\U0001F4DD Message or Encrypted Text", font=FONT_LABEL, text_color="#38b6ff", anchor="w")
msg_label.pack(anchor="w", pady=(5, 0), padx=20)
input_text = ctk.CTkTextbox(card1, height=80, width=600, font=("Consolas", 11))
input_text.pack(pady=(0, 15), padx=20, anchor="w")
placeholder = "Enter your message here... \U0001F4DD"
input_text.insert("1.0", placeholder)

def on_focus_in(event):
    if input_text.get("1.0", "end").strip() == placeholder:
        input_text.delete("1.0", "end")

def on_focus_out(event):
    if input_text.get("1.0", "end").strip() == "":
        input_text.insert("1.0", placeholder)

input_text.bind("<FocusIn>", on_focus_in)
input_text.bind("<FocusOut>", on_focus_out)

# Button Row
btn_row = ctk.CTkFrame(card1, fg_color="transparent")
btn_row.pack(pady=(0, 10), padx=20, fill="x")

def encrypt_and_save():
    text = input_text.get("1.0", "end").strip()
    key = input_key.get().strip()
    if not text or not key:
        messagebox.showwarning("Missing input", "Please enter both a message and a key.")
        return
    if not key.isalpha():
        messagebox.showerror("Invalid Key", "Key must contain only letters (A–Z).")
        return
    encrypted = encrypt_vigenere(text, key)
    save_message(encrypted, key)
    output_box.configure(state="normal")
    output_box.delete("1.0", "end")
    output_box.insert("end", f"✅ Encrypted & Saved:\n{encrypted}")
    output_box.configure(state="disabled")

def manual_decrypt():
    cipher_text = input_text.get("1.0", "end").strip()
    key = input_key.get().strip()
    if not cipher_text or not key:
        messagebox.showwarning("Missing input", "Please enter both the encrypted text and the key.")
        return
    if not key.isalpha():
        messagebox.showerror("Invalid Key", "Key must contain only letters (A–Z).")
        return
    decrypted = decrypt_vigenere(cipher_text, key)
    output_box.configure(state="normal")
    output_box.delete("1.0", "end")
    output_box.insert("end", f"🔓 Decrypted Message:\n{decrypted}")
    output_box.configure(state="disabled")

def load_and_decrypt_all():
    output_box.configure(state="normal")
    output_box.delete("1.0", "end")
    rows = get_all_messages()
    if not rows:
        output_box.insert("end", "No saved messages found.")
    else:
        for row in rows:
            decrypted = decrypt_vigenere(row[1], row[2])
            output_box.insert("end", f"ID: {row[0]}\n🔒 {row[1]}\n🔑 {row[2]}\n📝 {decrypted}\n\n")
    output_box.configure(state="disabled")

def show_info():
    messagebox.showinfo("About Vigenère Cipher",
        "🔐 The Vigenère cipher encrypts alphabetic text using a key.\n\n"
        "Each letter in the message is shifted by the letter in the key.\n"
        "Only letters are encrypted. Numbers & punctuation remain unchanged.\n\n"
        "Example:\nKey: LEMON\nMessage: ATTACK\nEncrypted: LXFOPV")

# Buttons
btn_encrypt = ctk.CTkButton(btn_row, text="Encrypt & Save", command=encrypt_and_save, fg_color=BTN_PURPLE, hover_color="#7c3aed", text_color="white", font=FONT, width=150)
btn_encrypt.grid(row=0, column=0, padx=8, pady=5)
btn_decrypt = ctk.CTkButton(btn_row, text="Decrypt Text", command=manual_decrypt, fg_color=BTN_RED, hover_color="#c0392b", text_color="white", font=FONT, width=150)
btn_decrypt.grid(row=0, column=1, padx=8, pady=5)
btn_load = ctk.CTkButton(btn_row, text="Load Messages", command=load_and_decrypt_all, fg_color=BTN_GREEN, hover_color="#27ae60", text_color="white", font=FONT, width=150)
btn_load.grid(row=0, column=2, padx=8, pady=5)
btn_info = ctk.CTkButton(btn_row, text="About Vigenère", command=show_info, fg_color=BTN_GRAY, hover_color="#495057", text_color="white", font=FONT, width=150)
btn_info.grid(row=0, column=3, padx=8, pady=5)

# --- Card 2: Output ---
card2 = ctk.CTkFrame(root, fg_color=CARD_BG, corner_radius=18)
card2.pack(pady=10, padx=20, fill="x", ipadx=10, ipady=10)

output_label = ctk.CTkLabel(card2, text="\u2728 Output", font=FONT_LABEL, text_color="#38b6ff", anchor="w")
output_label.pack(anchor="w", pady=(10, 0), padx=20)
output_box = ctk.CTkTextbox(card2, height=180, width=600, font=("Consolas", 11), state="disabled")
output_box.pack(pady=(0, 15), padx=20, anchor="w")
output_box.configure(state="normal")
output_box.insert("1.0", "Your encrypted or decrypted text will appear here... \U0001F31F")
output_box.configure(state="disabled")

root.mainloop()
