import tkinter as tk #Mengimport modul tkinter 
from tkinter import ttk #import ttk() widget
from tkinter.messagebox import showinfo

#init
window = tk.Tk()
window.configure(bg="White")
window.geometry("300x200")
window.resizable(False,False)
window.title("Sapa")

#Variabel 
Nama_Depan = tk.StringVar()
Nama_Belakang = tk.StringVar()

#Fungsi 
def tombol_click():
    pesan=f"Hello{Nama_Depan.get()} {Nama_Belakang.get()}, Have a nice day"
    showinfo(title="Hi",message=pesan)
    
#Frame Input 
input_frame = ttk.Frame(window)
input_frame.pack(padx=10, fill="x", expand=True)


nama_depan_label = ttk.Label(input_frame, text="Nama depan:")
nama_depan_label.pack(padx=10, fill="x", expand=True)

nama_depan_entry = ttk.Entry(input_frame,textvariable =Nama_Depan)
nama_depan_entry.pack(padx=10, fill="x", expand=True)

nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang:")
nama_belakang_label.pack(padx=10, fill="x", expand=True)

nama_belakang_entry = ttk.Entry(input_frame,textvariable =Nama_Belakang)
nama_belakang_entry.pack(padx=10, fill="x", expand=True)

tombol = ttk.Button(input_frame, text="Sapa!", command=tombol_click )
tombol.pack(fill="x", expand=True, padx=10 ,pady=10)

window.mainloop()