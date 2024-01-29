import pygame
from tkinter import Tk, filedialog, Button, Label, StringVar
import os

class ReproductorMusica:
    def __init__(self, master):
        self.master = master
        self.master.title("Reproductor de Música")
        self.master.geometry("400x200")

        # Configuración del reproductor
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.5)  # Volumen inicial
        self.volumen = pygame.mixer.music.get_volume()

        self.music_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "musica")

        self.playlist = [os.path.join(self.music_directory, archivo) for archivo in os.listdir(self.music_directory)
                         if archivo.endswith((".mp3", ".wav"))]

        self.current_song = StringVar()
        self.current_song.set("Ninguna canción seleccionada")

        # Etiqueta para mostrar la canción actual
        self.label_cancion = Label(master, textvariable=self.current_song, font=("Helvetica", 12))
        self.label_cancion.grid(row=0, column=0, columnspan=2, pady=10)

        # Botones de control
        self.boton_play = Button(master, text="▶ Play", command=self.play, font=("Helvetica", 12), padx=10)
        self.boton_play.grid(row=1, column=0, pady=5)

        self.boton_pause = Button(master, text="❚❚ Pause", command=self.pause, font=("Helvetica", 12), padx=10)
        self.boton_pause.grid(row=2, column=0, pady=5)

        self.boton_stop = Button(master, text="■ Stop", command=self.stop, font=("Helvetica", 12), padx=10)
        self.boton_stop.grid(row=3, column=0, pady=5)

        self.boton_elegir = Button(master, text="Elegir Canción", command=self.elegir_cancion, font=("Helvetica", 12))
        self.boton_elegir.grid(row=4, column=0, pady=5)

        # Botones de volumen
        self.boton_subir_volumen = Button(master, text="Subir Volumen", command=self.subir_volumen, font=("Helvetica", 12), padx=10)
        self.boton_subir_volumen.grid(row=5, column=0, pady=5)

        self.boton_bajar_volumen = Button(master, text="Bajar Volumen", command=self.bajar_volumen, font=("Helvetica", 12), padx=10)
        self.boton_bajar_volumen.grid(row=6, column=0, pady=10)

    def play(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[0])
            pygame.mixer.music.play()
            self.current_song.set(os.path.basename(self.playlist[0]))

    def pause(self):
        pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()
        self.current_song.set("Ninguna canción seleccionada")

    def elegir_cancion(self):
        Tk().withdraw()  # No mostrar la ventana principal de Tkinter
        ruta_personalizada = filedialog.askopenfilename(title="Selecciona tu archivo de música", filetypes=[("Archivos de música", "*.mp3;*.wav")])

        if ruta_personalizada:
            self.playlist.insert(0, ruta_personalizada)
            self.current_song.set(os.path.basename(ruta_personalizada))

    def subir_volumen(self):
        if self.volumen < 1.0:
            self.volumen += 0.1
            pygame.mixer.music.set_volume(self.volumen)

    def bajar_volumen(self):
        if self.volumen > 0.0:
            self.volumen -= 0.1
            pygame.mixer.music.set_volume(self.volumen)

if __name__ == "__main__":
    root = Tk()
    reproductor = ReproductorMusica(root)
    root.mainloop()
