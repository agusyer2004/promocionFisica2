import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import tkinter as tk
from tkinter import messagebox

def generar_onda_sinusoidal(tiempo, amplitud, frecuencia, fase):
    """
    Genera una onda sinusoidal.

    :param tiempo: Arreglo de tiempo (en segundos).
    :param amplitud: Amplitud de la onda.
    :param frecuencia: Frecuencia de la onda (en Hz).
    :param fase: Fase de la onda (en radianes).
    :return: Valores de la onda sinusoidal.
    """
    return amplitud * np.sin(2 * np.pi * frecuencia * tiempo + fase)

def graficar_onda_interactiva(amplitud_inicial, frecuencia_inicial, fase_inicial):
    """
    Crea una gráfica interactiva de una onda sinusoidal donde los parámetros
    amplitud, frecuencia y fase se pueden ajustar mediante sliders.

    :param amplitud_inicial: Valor inicial de la amplitud.
    :param frecuencia_inicial: Valor inicial de la frecuencia (en Hz).
    :param fase_inicial: Valor inicial de la fase (en radianes).
    """
    tiempo = np.linspace(0, 2, 1000)

    fig, ax = plt.subplots(figsize=(10, 6))
    plt.subplots_adjust(left=0.1, bottom=0.35)
    ax.set_title("Onda Sinusoidal Interactiva", fontsize=16)
    ax.set_xlabel("Tiempo (s)", fontsize=14)
    ax.set_ylabel("Amplitud", fontsize=14)
    ax.grid(True)

    onda, = ax.plot(tiempo, generar_onda_sinusoidal(tiempo, amplitud_inicial, frecuencia_inicial, fase_inicial),
                    label=f"A={amplitud_inicial}, f={frecuencia_inicial} Hz, ϕ={fase_inicial} rad", color="blue")
    ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
    ax.legend()

    ax_amplitud = plt.axes([0.1, 0.25, 0.8, 0.03])
    slider_amplitud = Slider(ax_amplitud, "Amplitud", 0.1, max(10 * amplitud_inicial, 100.0), valinit=amplitud_inicial)

    ax_frecuencia = plt.axes([0.1, 0.2, 0.8, 0.03])
    slider_frecuencia = Slider(ax_frecuencia, "Frecuencia (Hz)", 0.1, max(10 * frecuencia_inicial, 100.0), valinit=frecuencia_inicial)

    ax_fase = plt.axes([0.1, 0.15, 0.8, 0.03])
    slider_fase = Slider(ax_fase, "Fase (rad)", 0.0, 2 * np.pi, valinit=fase_inicial)

    def actualizar(val):
        amplitud = slider_amplitud.val
        frecuencia = slider_frecuencia.val
        fase = slider_fase.val
        onda.set_ydata(generar_onda_sinusoidal(tiempo, amplitud, frecuencia, fase))
        ax.legend([f"A={amplitud:.2f}, f={frecuencia:.2f} Hz, ϕ={fase:.2f} rad"], loc="upper right")
        fig.canvas.draw_idle()

    slider_amplitud.on_changed(actualizar)
    slider_frecuencia.on_changed(actualizar)
    slider_fase.on_changed(actualizar)

    plt.show()

def validar_entrada(amplitud, frecuencia, fase):
    try:
        amplitud = float(amplitud)
        frecuencia = float(frecuencia)
        fase = float(fase)

        if amplitud <= 0:
            raise ValueError("La amplitud debe ser mayor a 0.")
        if frecuencia <= 0:
            raise ValueError("La frecuencia debe ser mayor a 0.")

        return amplitud, frecuencia, fase
    except ValueError as e:
        messagebox.showerror("Error", f"Entrada no válida: {e}")
        return None

def iniciar_grafica():
    amplitud = entrada_amplitud.get()
    frecuencia = entrada_frecuencia.get()
    fase = entrada_fase.get()

    valores = validar_entrada(amplitud, frecuencia, fase)
    if valores:
        amplitud, frecuencia, fase = valores
        graficar_onda_interactiva(amplitud, frecuencia, fase)

# Crear la ventana principal de la GUI
ventana = tk.Tk()
ventana.title("Simulador de Ondas Sinusoidales")

# Etiquetas y campos de entrada
tk.Label(ventana, text="Amplitud Inicial:").grid(row=0, column=0, padx=10, pady=10)
entrada_amplitud = tk.Entry(ventana)
entrada_amplitud.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Frecuencia Inicial (Hz):").grid(row=1, column=0, padx=10, pady=10)
entrada_frecuencia = tk.Entry(ventana)
entrada_frecuencia.grid(row=1, column=1, padx=10, pady=10)

tk.Label(ventana, text="Fase Inicial (rad):").grid(row=2, column=0, padx=10, pady=10)
entrada_fase = tk.Entry(ventana)
entrada_fase.grid(row=2, column=1, padx=10, pady=10)

# Botón para iniciar la gráfica
boton_graficar = tk.Button(ventana, text="Graficar Onda", command=iniciar_grafica)
boton_graficar.grid(row=3, column=0, columnspan=2, pady=20)

# Sugerencias de conjuntos de prueba
sugerencias_label = tk.Label(ventana, text="Sugerencias de Conjuntos de Prueba:")
sugerencias_label.grid(row=4, column=0, columnspan=2, pady=10)

sugerencia_1 = tk.Label(ventana, text="1. Amplitud = 1, Frecuencia = 1 Hz, Fase = 0  → Onda sinusoidal básica, con frecuencia de 1 Hz.")
sugerencia_1.grid(row=5, column=0, columnspan=2, pady=5)

sugerencia_2 = tk.Label(ventana, text="2. Amplitud = 5, Frecuencia = 2 Hz, Fase = π/2 → Onda con mayor amplitud y desplazada en fase.")
sugerencia_2.grid(row=6, column=0, columnspan=2, pady=5)

sugerencia_3 = tk.Label(ventana, text="3. Amplitud = 10, Frecuencia = 0.5 Hz, Fase = π → Onda más amplia y de menor frecuencia.")
sugerencia_3.grid(row=7, column=0, columnspan=2, pady=5)

ventana.mainloop()
