import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from pytube import YouTube

# Función para actualizar la barra de progreso
def update_progress(stream, chunk, remaining):
    file_size = stream.filesize
    bytes_downloaded = file_size - remaining
    percent = (bytes_downloaded / file_size) * 100
    progress_bar["value"] = percent
    root.update_idletasks()


# Función para descargar el video de YouTube
def download_video():
    link = link_entry.get()  # Obtener el enlace del campo de entrada
    try:
        yt = YouTube(link, on_progress_callback=update_progress)
        title = yt.title
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        stream.download()
        messagebox.showinfo("Descarga completada", f"El video '{title}' se ha descargado correctamente.")
        link_entry.delete(0, tk.END)  # Limpiar el campo de entrada
    except Exception as e:
        messagebox.showerror("Error de descarga", f"Ocurrió un error durante la descarga: {str(e)}")


# Crear la ventana principal
root = tk.Tk()
root.title("Descargador de videos de YouTube")

# Cambiar el icono de la ventana
icon_path = os.path.join(os.path.dirname(__file__), 'icon.icns')
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)

# Crear y posicionar los elementos de la interfaz de usuario
label = tk.Label(root, text="Ingresa el enlace de YouTube del video que deseas descargar:")
label.pack(pady=10)

link_entry = tk.Entry(root, width=50)
link_entry.pack(pady=5)

download_button = tk.Button(root, text="Descargar", command=download_video)
download_button.pack(pady=5)

# Ejecutar la interfaz de usuario
root.mainloop()
