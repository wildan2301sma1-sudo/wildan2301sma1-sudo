import tkinter as tk
from tkinter import messagebox

# =========================
# FUNGSI
# =========================
total_bayar = 0

def tambah_item():
    global total_bayar

    nama = entry_nama.get()
    harga = entry_harga.get()
    jumlah = entry_jumlah.get()

    if nama == "" or harga == "" or jumlah == "":
        messagebox.showwarning("Peringatan", "Semua data harus diisi!")
        return

    harga = int(harga)
    jumlah = int(jumlah)

    subtotal = harga * jumlah
    total_bayar += subtotal

    text_area.insert(tk.END, f"{nama}  x{jumlah}  = Rp{subtotal}\n")
    label_total.config(text=f"Total : Rp{total_bayar}")

    entry_nama.delete(0, tk.END)
    entry_harga.delete(0, tk.END)
    entry_jumlah.delete(0, tk.END)


def reset():
    global total_bayar
    total_bayar = 0
    text_area.delete("1.0", tk.END)
    label_total.config(text="Total : Rp0")


def cetak_struk():
    messagebox.showinfo("Struk", f"Total pembayaran = Rp{total_bayar}\nTerima kasih sudah belanja!")


# =========================
# GUI
# =========================
root = tk.Tk()
root.title("Program Kasir Sederhana")
root.geometry("500x500")

judul = tk.Label(root, text="KASIR TOKO", font=("Arial", 16, "bold"))
judul.pack(pady=10)

frame_input = tk.Frame(root)
frame_input.pack()

tk.Label(frame_input, text="Nama Barang").grid(row=0, column=0)
tk.Label(frame_input, text="Harga").grid(row=1, column=0)
tk.Label(frame_input, text="Jumlah").grid(row=2, column=0)

entry_nama = tk.Entry(frame_input)
entry_harga = tk.Entry(frame_input)
entry_jumlah = tk.Entry(frame_input)

entry_nama.grid(row=0, column=1)
entry_harga.grid(row=1, column=1)
entry_jumlah.grid(row=2, column=1)

btn_tambah = tk.Button(root, text="Tambah Item", command=tambah_item, width=20)
btn_tambah.pack(pady=5)

text_area = tk.Text(root, height=12, width=45)
text_area.pack(pady=10)

label_total = tk.Label(root, text="Total : Rp0", font=("Arial", 14, "bold"))
label_total.pack()

frame_btn = tk.Frame(root)
frame_btn.pack(pady=10)

tk.Button(frame_btn, text="Reset", command=reset, width=10).grid(row=0, column=0, padx=5)
tk.Button(frame_btn, text="Cetak Struk", command=cetak_struk, width=10).grid(row=0, column=1, padx=5)

root.mainloop()
