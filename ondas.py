import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

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
    # Tiempo de la onda (2 segundos con alta resolución)
    tiempo = np.linspace(0, 2, 1000)

    # Crear la figura y el eje
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.subplots_adjust(left=0.1, bottom=0.3)  # Espacio para los sliders
    ax.set_title("Onda Sinusoidal Interactiva")
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Amplitud")
    ax.grid()

    # Onda inicial
    onda, = ax.plot(tiempo, generar_onda_sinusoidal(tiempo, amplitud_inicial, frecuencia_inicial, fase_inicial),
                    label=f"A={amplitud_inicial}, f={frecuencia_inicial} Hz, ϕ={fase_inicial} rad")
    ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
    ax.legend()

    # Crear sliders para amplitud, frecuencia y fase
    ax_amplitud = plt.axes([0.1, 0.2, 0.8, 0.03])  # Posición del slider de amplitud
    slider_amplitud = Slider(ax_amplitud, "Amplitud", 0.1, 100.0, valinit=amplitud_inicial)

    ax_frecuencia = plt.axes([0.1, 0.15, 0.8, 0.03])  # Posición del slider de frecuencia
    slider_frecuencia = Slider(ax_frecuencia, "Frecuencia (Hz)", 0.1, 100.0, valinit=frecuencia_inicial)

    ax_fase = plt.axes([0.1, 0.1, 0.8, 0.03])  # Posición del slider de fase
    slider_fase = Slider(ax_fase, "Fase (rad)", 0.0, 2 * np.pi, valinit=fase_inicial)

    # Función que actualiza la gráfica cuando se cambian los valores de los sliders
    def actualizar(val):
        amplitud = slider_amplitud.val
        frecuencia = slider_frecuencia.val
        fase = slider_fase.val
        onda.set_ydata(generar_onda_sinusoidal(tiempo, amplitud, frecuencia, fase))
        ax.legend([f"A={amplitud:.2f}, f={frecuencia:.2f} Hz, ϕ={fase:.2f} rad"])
        fig.canvas.draw_idle()

    # Conectar los sliders con la función de actualización
    slider_amplitud.on_changed(actualizar)
    slider_frecuencia.on_changed(actualizar)
    slider_fase.on_changed(actualizar)

    plt.show()

def main():
    print("Simulador de Ondas Sinusoidales")
    print("Primero ingresa los parámetros iniciales de la onda:")
    try:
        amplitud_inicial = float(input("Amplitud inicial: "))
        frecuencia_inicial = float(input("Frecuencia inicial (en Hz): "))
        fase_inicial = float(input("Fase inicial (en radianes): "))

        # Inicia la gráfica interactiva con los valores ingresados
        graficar_onda_interactiva(amplitud_inicial, frecuencia_inicial, fase_inicial)

    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")

if __name__ == "__main__":
    main()