import tkinter as tk
from tkinter import messagebox, scrolledtext
from cipher import encrypt_vigenere, decrypt_vigenere
from db import save_message, get_all_messages, init_db  # if renamed from db.py

# Initialize SQLite DB
init_db()

# Functions
def encrypt_and_save():
    text = input_text.get("1.0", tk.END).strip()
    key = input_key.get().strip()

    if not text or not key:
        messagebox.showwarning("Missing input", "Please enter both a message and a key.")
        return
    if not key.isalpha():
        messagebox.showerror("Invalid Key", "Key must contain only letters (A–Z).")
        return

    encrypted = encrypt_vigenere(text, key)
    save_message(encrypted, key)

    output_box.config(state=tk.NORMAL)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, f"✅ Encrypted & Saved:\n{encrypted}")
    output_box.config(state=tk.DISABLED)

def manual_decrypt():
    cipher_text = input_text.get("1.0", tk.END).strip()
    key = input_key.get().strip()

    if not cipher_text or not key:
        messagebox.showwarning("Missing input", "Please enter both the encrypted text and the key.")
        return
    if not key.isalpha():
        messagebox.showerror("Invalid Key", "Key must contain only letters (A–Z).")
        return

    decrypted = decrypt_vigenere(cipher_text, key)
    output_box.config(state=tk.NORMAL)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, f"🔓 Decrypted Message:\n{decrypted}")
    output_box.config(state=tk.DISABLED)

def load_and_decrypt_all():
    output_box.config(state=tk.NORMAL)
    output_box.delete("1.0", tk.END)
    rows = get_all_messages()
    if not rows:
        output_box.insert(tk.END, "No saved messages found.")
    else:
        for row in rows:
            decrypted = decrypt_vigenere(row[1], row[2])
            output_box.insert(tk.END, f"ID: {row[0]}\n🔒 {row[1]}\n🔑 {row[2]}\n📝 {decrypted}\n\n")
    output_box.config(state=tk.DISABLED)

def show_info():
    messagebox.showinfo("About Vigenère Cipher",
        "🔐 The Vigenère cipher encrypts alphabetic text using a key.\n\n"
        "Each letter in the message is shifted by the letter in the key.\n"
        "Only letters are encrypted. Numbers & punctuation remain unchanged.\n\n"
        "Example:\nKey: LEMON\nMessage: ATTACK\nEncrypted: LXFOPV")

# GUI Setup
root = tk.Tk()
root.title("🔐 Vigenère Cipher GUI")
root.geometry("620x600")
root.configure(bg="#f1f3f6")

FONT = ("Segoe UI", 11)

# Frame layout for clean alignment
frame = tk.Frame(root, bg="#f1f3f6")
frame.pack(pady=20)

# Key field
tk.Label(frame, text="Encryption Key:", bg="#f1f3f6", font=FONT).grid(row=0, column=0, sticky="w")
input_key = tk.Entry(frame, width=50, font=FONT)
input_key.grid(row=1, column=0, columnspan=2, pady=(0, 10))

# Text field (for both encrypt/decrypt)
tk.Label(frame, text="Message or Encrypted Text:", bg="#f1f3f6", font=FONT).grid(row=2, column=0, sticky="w")
input_text = scrolledtext.ScrolledText(frame, height=5, width=70, font=("Consolas", 10))
input_text.grid(row=3, column=0, columnspan=2, pady=(0, 15))

# Buttons
btn_frame = tk.Frame(frame, bg="#f1f3f6")
btn_frame.grid(row=4, column=0, columnspan=2, pady=(0, 10))

tk.Button(btn_frame, text="Encrypt & Save", command=encrypt_and_save, bg="#007BFF", fg="white", font=FONT, width=18).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="🔓 Decrypt Text", command=manual_decrypt, bg="#FFC107", fg="black", font=FONT, width=18).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="📥 Load All Messages", command=load_and_decrypt_all, bg="#28A745", fg="white", font=FONT, width=18).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="ℹ️ About Vigenère", command=show_info, bg="#6c757d", fg="white", font=FONT, width=18).grid(row=1, column=1, padx=5, pady=5)

# Output Box
output_box = scrolledtext.ScrolledText(frame, height=12, width=70, font=("Consolas", 10), state=tk.DISABLED, bg="#ffffff")
output_box.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
