import pandas as pd

def hist(region, region_name ='', bins=0):

# Almacenamos a las variables continuas en la variable numerical_data_1
    numerical_data= ['f0', 'f1', 'f2', 'product']

# Establecemos el número de filas y columnas para nuestros subplots
    a = 2 # número de filas
    b = 2 # número de columnas
    c = 1 # inicialización del conteo de plots

# Establecemos el tamaño de nuestra figura de subplots
    fig = plt.subplots(figsize=(10, 6))

# Construimos un bucle for que iterará por cada columna numérica y devolverá un histograma
    for i in numerical_data:
        plt.subplot(a, b, c)
        plt.title(i)
        region[i].hist(bins=bins, edgecolor = 'black', linewidth = 0.8)
        c = c + 1

    plt.suptitle(region_name)
    plt.tight_layout()
    plt.show()