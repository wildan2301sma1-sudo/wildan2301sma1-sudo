import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

TARIF_PER_JAM = 2000

def hitung_biaya():
    try:
        plat = entry_plat.get()
        waktu_masuk = datetime.strptime(entry_masuk.get(), "%H:%M")
        waktu_keluar = datetime.strptime(entry_keluar.get(), "%H:%M")

        durasi = (waktu_keluar - waktu_masuk).seconds / 3600
        durasi = int(durasi) if durasi.is_integer() else int(durasi) + 1

        biaya = durasi * TARIF_PER_JAM
        label_biaya.config(text=f"Rp {biaya:,}")

        tabel.insert("", "end", values=(
            plat,
            entry_masuk.get(),
            entry_keluar.get(),
            f"Rp {biaya:,}"
        ))

    except ValueError:
        messagebox.showerror(
            "Error",
            "Format waktu salah!\nGunakan format HH:MM"
        )

# Window utama
root = tk.Tk()
root.title("Aplikasi Parkir")
root.geometry("700x450")

# ===== INPUT =====
frame_input = tk.LabelFrame(root, text="Data Parkir")
frame_input.pack(fill="x", padx=10, pady=10)

tk.Label(frame_input, text="No Plat Polisi").grid(row=0, column=0, padx=5, pady=5)
entry_plat = tk.Entry(frame_input)
entry_plat.grid(row=0, column=1)

tk.Label(frame_input, text="Waktu Masuk (HH:MM)").grid(row=1, column=0, padx=5, pady=5)
entry_masuk = tk.Entry(frame_input)
entry_masuk.grid(row=1, column=1)

tk.Label(frame_input, text="Waktu Keluar (HH:MM)").grid(row=2, column=0, padx=5, pady=5)
entry_keluar = tk.Entry(frame_input)
entry_keluar.grid(row=2, column=1)

tk.Button(frame_input, text="Hitung Biaya", command=hitung_biaya)\
    .grid(row=3, column=1, pady=10)

# ===== BIAYA =====
frame_biaya = tk.Frame(root)
frame_biaya.pack()

tk.Label(
    frame_biaya,
    text="Biaya Per Jam\nRp 2.000",
    fg="red",
    font=("Arial", 16, "bold")
).pack()

label_biaya = tk.Label(root, text="Rp 0", font=("Arial", 14))
label_biaya.pack(pady=5)

# ===== TABEL =====
frame_tabel = tk.Frame(root)
frame_tabel.pack(fill="both", expand=True, padx=10, pady=10)

tabel = ttk.Treeview(
    frame_tabel,
    columns=("plat", "masuk", "keluar", "biaya"),
    show="headings"
)

tabel.heading("plat", text="No Plat")
tabel.heading("masuk", text="Masuk")
tabel.heading("keluar", text="Keluar")
tabel.heading("biaya", text="Biaya")

tabel.pack(fill="both", expand=True)

root.mainloop()
