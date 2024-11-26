import tkinter as tk
from tkinter import ttk

def calcular():
    operacion = operacion_seleccionada.get()
    presion = get_float(entry1)
    volumen = get_float(entry2)
    moles = get_float(entry3)
    temperatura = get_float(entry4)
    cte = 0.082
    if(unidad_temperatura_seleccionada.get() == "Celsius"):
        temperatura = pasajeTemp(temperatura)
    if(unidad_presion_seleccionada.get() == "mm Hg"):
        presion = pasajePresion(presion)
    if(unidad_volumen_seleccionada.get() != "Litros"):
        volumen = pasajeVolumen(volumen)


    if(operacion == "Calcular Presion"):
        resultado = calcularPresion(volumen,moles,temperatura,cte)
    if(operacion == "Calcular Volumen"):
        resultado = calcularVolumen(presion,temperatura,moles,cte)
    if(operacion == "Calcular numero de moles"):
        resultado = calcularNroMoles(presion,temperatura,volumen,cte)
    if(operacion == "Calcular Temperatura"):
        resultado = calcularTemp(presion,volumen,moles,cte)
    label_resultado.config(text=f"Resultado: {resultado:.2f}")


def get_float(entry):
    # este metodo sirve para que si dejamos un textfield en blanco no explote el programa(el que dejamos en blanco es el que queremos calcular)
    value = entry.get()
    return float(value) if value else None
    

def pasajeTemp(temp):
    return temp+273

def pasajePresion(presion):
    return presion/760

def pasajeVolumen(volumen):
    unidad = unidad_volumen_seleccionada.get()
    if unidad == "mililitro":
        return volumen * 0.001
    if unidad == "centimetro cubico":
        return volumen * 0.001
    if unidad == "decimetro cubico":
        return volumen
    if unidad == "metro cubico":
        return volumen * 1000
    if unidad == "galon estadounidense":
        return volumen * 3.785

    return volumen



def calcularPresion(volumen,moles,temperatura,cte):
    resultado = ((moles * cte * temperatura)/volumen)
    return resultado

def calcularVolumen(presion,temperatura,moles,cte):
    resultado = ((moles * cte * temperatura)/presion)
    return resultado

def calcularNroMoles(presion,temperatura,volumen,cte):
    resultado = ((presion * volumen)/(cte * temperatura))
    return resultado

def calcularTemp(presion,volumen,moles,cte):
    resultado = ((presion * volumen)/(cte * moles))
    return resultado

    


root = tk.Tk()
root.title("Calculadora de propiedades termodinamicas basicas")

label1 = tk.Label(root, text="Presión")
label1.grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

unidad_presion_seleccionada = tk.StringVar()
menu_operacionespresion = ttk.Combobox(root, textvariable=unidad_presion_seleccionada)
menu_operacionespresion['values'] = ["atm", "mm Hg"]
menu_operacionespresion.grid(row=0, column=2, padx=10, pady=10)
menu_operacionespresion.current(0)

label2 = tk.Label(root, text="Volumen")
label2.grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

unidad_volumen_seleccionada = tk.StringVar()
menu_operacionesvolumen = ttk.Combobox(root, textvariable=unidad_volumen_seleccionada)
menu_operacionesvolumen['values'] = ["litro", "mililitro", "decimetro cubico", "centimetro cubico", "metro cubico", "galon estadounidense"]
menu_operacionesvolumen.grid(row=1, column=2, padx=10, pady=10)
menu_operacionesvolumen.current(0)

label3 = tk.Label(root, text="Número de moles")
label3.grid(row=2, column=0, padx=10, pady=10)
entry3 = tk.Entry(root)
entry3.grid(row=2, column=1, padx=10, pady=10)

label4 = tk.Label(root, text="Temperatura")
label4.grid(row=3, column=0, padx=10, pady=10)
entry4 = tk.Entry(root)
entry4.grid(row=3, column=1, padx=10, pady=10)

unidad_temperatura_seleccionada = tk.StringVar()
menu_operacionestemp = ttk.Combobox(root, textvariable=unidad_temperatura_seleccionada)
menu_operacionestemp['values'] = ["Celsius", "Kelvin"]
menu_operacionestemp.grid(row=3, column=2, padx=10, pady=10)
menu_operacionestemp.current(0)

label_operacion = tk.Label(root, text="Operación:")
label_operacion.grid(row=4, column=0, padx=10, pady=10)

operacion_seleccionada = tk.StringVar()
menu_operaciones = ttk.Combobox(root, textvariable=operacion_seleccionada)
menu_operaciones['values'] = ["Calcular Presion", "Calcular Volumen", "Calcular Temperatura", "Calcular numero de moles"]
menu_operaciones.grid(row=4, column=1, padx=10, pady=10)
menu_operaciones.current(0)

boton_calcular = tk.Button(root, text="Calcular", command=calcular)
boton_calcular.grid(row=6, column=0, columnspan=2, pady=20)

label_resultado = tk.Label(root, text="Resultado: ")
label_resultado.grid(row=8, column=0, columnspan=2, pady=10)

root.mainloop()