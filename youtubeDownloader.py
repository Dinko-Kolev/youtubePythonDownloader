import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

# Función para descargar el video de YouTube
def download_video():
    link = link_entry.get()  # Obtener el enlace del campo de entrada
    try:
        yt = YouTube(link)
        title = yt.title
        yt.streams.filter(progressive=True, file_extension='mp4').first().download()
        messagebox.showinfo("Descarga completada", f"El video '{title}' se ha descargado correctamente.")
    except Exception as e:
        messagebox.showerror("Error de descarga", f"Ocurrió un error durante la descarga: {str(e)}")

# Crear la ventana principal
root = tk.Tk()
root.title("Descargador de videos de YouTube")

# Crear y posicionar los elementos de la interfaz de usuario
label = tk.Label(root, text="Ingresa el enlace de YouTube del video que deseas descargar:")
label.pack(pady=10)

link_entry = tk.Entry(root, width=50)
link_entry.pack(pady=5)

download_button = tk.Button(root, text="Descargar", command=download_video)
download_button.pack(pady=5)

# Ejecutar la interfaz de usuario
root.mainloop()
