import tkinter as tk
from tkinter import messagebox

def simpan_data():
    data = f"""
Nama Lengkap : {entry_nama.get()}
Tanggal Lahir : {entry_tgl.get()}
Asal Sekolah : {entry_sekolah.get()}
NISN : {entry_nisn.get()}
Nama Ayah : {entry_ayah.get()}
Nama Ibu : {entry_ibu.get()}
No Telp : {entry_telp.get()}
Alamat : {text_alamat.get("1.0", tk.END)}
"""
    messagebox.showinfo("Data Disimpan", data)

def hapus_data():
    entry_nama.delete(0, tk.END)
    entry_tgl.delete(0, tk.END)
    entry_sekolah.delete(0, tk.END)
    entry_nisn.delete(0, tk.END)
    entry_ayah.delete(0, tk.END)
    entry_ibu.delete(0, tk.END)
    entry_telp.delete(0, tk.END)
    text_alamat.delete("1.0", tk.END)

# ===== Window =====
root = tk.Tk()
root.title("Data Siswa Baru")
root.geometry("600x550")

# ===== Header =====
header = tk.Label(
    root,
    text="DATA SISWA BARU",
    bg="#AEEEEE",
    font=("Arial", 18, "bold"),
    pady=10
)
header.pack(fill="x")

frame = tk.Frame(root, padx=20, pady=10)
frame.pack(fill="both", expand=True)

def buat_label_entry(text, row):
    tk.Label(frame, text=text).grid(row=row, column=0, sticky="w", pady=5)
    entry = tk.Entry(frame, width=50)
    entry.grid(row=row, column=1, pady=5)
    return entry

# ===== Form =====
entry_nama = buat_label_entry("Nama Lengkap", 0)
entry_tgl = buat_label_entry("Tanggal Lahir", 1)
entry_sekolah = buat_label_entry("Asal Sekolah", 2)
entry_nisn = buat_label_entry("NISN", 3)
entry_ayah = buat_label_entry("Nama Ayah", 4)
entry_ibu = buat_label_entry("Nama Ibu", 5)
entry_telp = buat_label_entry("Nomor Telepon / HP", 6)

tk.Label(frame, text="Alamat").grid(row=7, column=0, sticky="nw", pady=5)
text_alamat = tk.Text(frame, width=38, height=5)
text_alamat.grid(row=7, column=1, pady=5)

# ===== Tombol =====
frame_btn = tk.Frame(root, pady=10)
frame_btn.pack()

tk.Button(
    frame_btn,
    text="Hapus",
    bg="#D2691E",
    fg="white",
    width=12,
    command=hapus_data
).pack(side="left", padx=10)

tk.Button(
    frame_btn,
    text="Simpan",
    bg="#D2691E",
    fg="white",
    width=12,
    command=simpan_data
).pack(side="left", padx=10)

root.mainloop()
