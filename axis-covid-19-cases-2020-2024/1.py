# Argentina
# Brazil
# Canada
# El Salvador
# Ecuador
# Mexico
# Venezuela
# Peru
# Russian Federation
# Zimbabwe

# 1. Elabora una gráfica de líneas que muestre el comportamiento del crecimiento
# de nuevos casos con respecto al numero de defunciones a lo largo de tiempo incluyendo los 10 países.

import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv('all-global-countrys.csv', parse_dates=['Date_reported'], index_col='Date_reported')

paises = ['Argentina', 'Brazil', 'Canada', 'El Salvador', 'Ecuador', 'Mexico', 'Venezuela', 'Peru', 'Russian Federation', 'Zimbabwe']

plt.figure(figsize=(12, 6))

for pais in paises:
    datos_pais = datos[datos['Country'] == pais]
    plt.plot(datos_pais.index, datos_pais['New_cases'], label=f'Nuevos casos en {pais}')
    plt.plot(datos_pais.index, datos_pais['New_deaths'], label=f'Nuevas muertes en {pais}')

plt.xlabel('Fecha')
plt.ylabel('Número de casos/muertes')
plt.title('Crecimiento de nuevos casos y muertes de COVID en varios países')
plt.legend()
plt.show()
