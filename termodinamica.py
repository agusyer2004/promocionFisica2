import tkinter as tk
from tkinter import ttk

def validar_campos(presion, volumen, moles, temperatura):
    campos = [presion, volumen, moles, temperatura]
    if campos.count(None) != 1:
        label_resultado.config(text="Debe dejar solo un campo vacío para calcular.")
        return False
    return True

def get_float(entry):
    """Convierte el valor ingresado en el campo a float, si está vacío retorna None."""
    value = entry.get()
    return float(value) if value else None

def calcular():
    operacion = operacion_seleccionada.get()
    presion = get_float(entry1)
    volumen = get_float(entry2)
    moles = get_float(entry3)
    temperatura = get_float(entry4)
    cte = 0.082  # R en L·atm/(mol·K)

    # Validar que solo un campo esté vacío
    if not validar_campos(presion, volumen, moles, temperatura):
        return

    # Convertir las unidades
    if unidad_temperatura_seleccionada.get() == "Celsius" and temperatura is not None:
        temperatura = pasajeTemp(temperatura)
    if unidad_presion_seleccionada.get() == "mm Hg" and presion is not None:
        presion = pasajePresion(presion)
    if unidad_volumen_seleccionada.get() != "litro" and volumen is not None:
        volumen = pasajeVolumen(volumen)

    # Calcular propiedad faltante
    if operacion == "Calcular Presión" and presion is None:
        resultado = calcularPresion(volumen, moles, temperatura, cte)
        label_resultado.config(text=f"Resultado: {resultado:.2f} atm")
    elif operacion == "Calcular Volumen" and volumen is None:
        resultado = calcularVolumen(presion, temperatura, moles, cte)
        label_resultado.config(text=f"Resultado: {resultado:.2f} L")
    elif operacion == "Calcular Número de Moles" and moles is None:
        resultado = calcularNroMoles(presion, temperatura, volumen, cte)
        label_resultado.config(text=f"Resultado: {resultado:.2f} moles")
    elif operacion == "Calcular Temperatura" and temperatura is None:
        resultado = calcularTemp(presion, volumen, moles, cte)
        label_resultado.config(text=f"Resultado: {resultado:.2f} K")
    else:
        label_resultado.config(text="Error: Verifique la operación y campos ingresados.")

def pasajeTemp(temp):
    return temp + 273

def pasajePresion(presion):
    return presion / 760

def pasajeVolumen(volumen):
    unidad = unidad_volumen_seleccionada.get()
    if unidad == "mililitro" or unidad == "centímetro cúbico":
        return volumen * 0.001
    elif unidad == "metro cúbico":
        return volumen * 1000
    elif unidad == "galón estadounidense":
        return volumen * 3.785
    return volumen

def calcularPresion(volumen, moles, temperatura, cte):
    return (moles * cte * temperatura) / volumen

def calcularVolumen(presion, temperatura, moles, cte):
    return (moles * cte * temperatura) / presion

def calcularNroMoles(presion, temperatura, volumen, cte):
    return (presion * volumen) / (cte * temperatura)

def calcularTemp(presion, volumen, moles, cte):
    return (presion * volumen) / (cte * moles)

def actualizar_campos(*args):
    """ Actualiza los campos a habilitar o deshabilitar según la operación seleccionada """
    operacion = operacion_seleccionada.get()
    campos = {'Calcular Presión': entry1, 
              'Calcular Volumen': entry2, 
              'Calcular Número de Moles': entry3, 
              'Calcular Temperatura': entry4}
    for campo, entry in campos.items():
        if campo == operacion:
            entry.config(state='disabled')
            entry.delete(0, tk.END)
        else:
            entry.config(state='normal')

def validar_entrada(valor):
    """ Valida que solo se puedan ingresar números en los campos de entrada """
    if valor == "" or valor.replace('.', '', 1).isdigit():
        return True
    return False

root = tk.Tk()
root.title("Calculadora de propiedades termodinámicas básicas")

vcmd = (root.register(validar_entrada), '%P')

label1 = tk.Label(root, text="Presión")
label1.grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root, validate="key", validatecommand=vcmd)
entry1.grid(row=0, column=1, padx=10, pady=10)
unidad_presion_seleccionada = tk.StringVar()
menu_operacionespresion = ttk.Combobox(root, textvariable=unidad_presion_seleccionada)
menu_operacionespresion['values'] = ["atm", "mm Hg"]
menu_operacionespresion.grid(row=0, column=2, padx=10, pady=10)
menu_operacionespresion.current(0)

label2 = tk.Label(root, text="Volumen")
label2.grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root, validate="key", validatecommand=vcmd)
entry2.grid(row=1, column=1, padx=10, pady=10)
unidad_volumen_seleccionada = tk.StringVar()
menu_operacionesvolumen = ttk.Combobox(root, textvariable=unidad_volumen_seleccionada)
menu_operacionesvolumen['values'] = ["litro", "mililitro", "centímetro cúbico", "metro cúbico", "galón estadounidense"]
menu_operacionesvolumen.grid(row=1, column=2, padx=10, pady=10)
menu_operacionesvolumen.current(0)

label3 = tk.Label(root, text="Número de Moles")
label3.grid(row=2, column=0, padx=10, pady=10)
entry3 = tk.Entry(root, validate="key", validatecommand=vcmd)
entry3.grid(row=2, column=1, padx=10, pady=10)

label4 = tk.Label(root, text="Temperatura")
label4.grid(row=3, column=0, padx=10, pady=10)
entry4 = tk.Entry(root, validate="key", validatecommand=vcmd)
entry4.grid(row=3, column=1, padx=10, pady=10)
unidad_temperatura_seleccionada = tk.StringVar()
menu_operacionestemp = ttk.Combobox(root, textvariable=unidad_temperatura_seleccionada)
menu_operacionestemp['values'] = ["Celsius", "Kelvin"]
menu_operacionestemp.grid(row=3, column=2, padx=10, pady=10)
menu_operacionestemp.current(0)

label_operacion = tk.Label(root, text="Operación:")
label_operacion.grid(row=4, column=0, padx=10, pady=10)
operacion_seleccionada = tk.StringVar()
operacion_seleccionada.trace('w', actualizar_campos)
menu_operaciones = ttk.Combobox(root, textvariable=operacion_seleccionada)
menu_operaciones['values'] = ["Calcular Presión", "Calcular Volumen", "Calcular Número de Moles", "Calcular Temperatura"]
menu_operaciones.grid(row=4, column=1, padx=10, pady=10)
menu_operaciones.current(0)

boton_calcular = tk.Button(root, text="Calcular", command=calcular)
boton_calcular.grid(row=6, column=0, columnspan=2, pady=20)
label_resultado = tk.Label(root, text="Resultado: ")
label_resultado.grid(row=8, column=0, columnspan=2, pady=10)

root.mainloop()
