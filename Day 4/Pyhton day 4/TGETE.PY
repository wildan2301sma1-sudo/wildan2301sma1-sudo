import tkinter as tk

# ======================
# BUAT WINDOW
# ======================
root = tk.Tk()
root.title("iqballllll")
root.geometry("400x200")
root.configure(bg="#4facfe")

# ======================
# LABEL NAMA
# ======================
label = tk.Label(
    root,
    text="iqqballlikbalikbalikbalikikbalikbalikbalikbalikbalikbalikbalikbalikbailk",
    font=("Arial", 32, "bold"),
    fg="white",
    bg="#4facfe"
)

label.pack(expand=True)

# ======================
# JALANKAN PROGRAM
# ======================
root.mainloop()
