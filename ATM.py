import tkinter as tk
from tkinter import messagebox

bakiye = 1000

def bakiye_goster():
    messagebox.showinfo("Bakiyeniz", f"Bakiyeniz: {bakiye} TL")

def para_cek():
    global bakiye
    try:
        miktar = int(entry_miktar.get())
        if miktar > bakiye:
            messagebox.showwarning("Yetersiz Bakiye", "Maalesef bakiyenizde yeterli miktar yok.")
        else:
            bakiye -= miktar
            messagebox.showinfo("Başarılı", "Para çekme işlemi başarıyla gerçekleşti.")
            label_bakiye.config(text=f"Bakiyeniz: {bakiye} TL")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir miktar girin.")

def para_yatir():
    global bakiye
    try:
        miktar = int(entry_miktar.get())
        if miktar < 0:
            messagebox.showerror("Hata", "Lütfen pozitif bir miktar girin.")
            return
        bakiye += miktar
        messagebox.showinfo("Başarılı", "Para yatırma işlemi başarıyla gerçekleşti.")
        label_bakiye.config(text=f"Bakiyeniz: {bakiye} TL")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir miktar girin.")

def cikis():
    root.destroy()

root = tk.Tk()
root.title("Draxera'nın ATM Sistemi")
root.geometry("400x400")
root.configure(bg="#f0f0f0")  # Arka plan rengi

# Başlık etiketi
label_welcome = tk.Label(root, text="Draxera'nın ATM Sistemine Hoşgeldiniz", font=("Arial", 16), bg="#f0f0f0")
label_welcome.pack(pady=10)

# Bakiye etiketi
label_bakiye = tk.Label(root, text=f"Bakiyeniz: {bakiye} TL", font=("Arial", 14), bg="#f0f0f0")
label_bakiye.pack(pady=10)

# Butonlar ve etiketler
button_bakiye = tk.Button(root, text="Bakiyeyi Göster", command=bakiye_goster, font=("Arial", 12), bg="#4CAF50", fg="white")
button_bakiye.pack(pady=5, padx=20, fill=tk.X)

label_miktar = tk.Label(root, text="Miktar: ", font=("Arial", 12), bg="#f0f0f0")
label_miktar.pack(pady=5)

entry_miktar = tk.Entry(root, font=("Arial", 12), justify='center')
entry_miktar.pack(pady=5)

button_cek = tk.Button(root, text="Para Çek", command=para_cek, font=("Arial", 12), bg="#FF5733", fg="white")
button_cek.pack(pady=5, padx=20, fill=tk.X)

button_yatir = tk.Button(root, text="Para Yatır", command=para_yatir, font=("Arial", 12), bg="#008CBA", fg="white")
button_yatir.pack(pady=5, padx=20, fill=tk.X)

button_cikis = tk.Button(root, text="Çıkış", command=cikis, font=("Arial", 12), bg="#f44336", fg="white")
button_cikis.pack(pady=5, padx=20, fill=tk.X)

root.mainloop()
