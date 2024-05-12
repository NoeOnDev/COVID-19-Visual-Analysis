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

# 2. Elabora una gráfica de líneas que muestre  en crecimiento acumulativo 
# de infecciones y muertes de covid incluyendo los 10 países.

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

datos = pd.read_csv('all-global-countrys.csv', parse_dates=['Date_reported'], index_col='Date_reported')

paises = ['Argentina', 'Brazil', 'Canada', 'El Salvador', 'Ecuador', 'Mexico', 'Venezuela', 'Peru', 'Russian Federation', 'Zimbabwe']

plt.figure(figsize=(12, 6))

for pais in paises:
    datos_pais = datos[datos['Country'] == pais]
    casos_acumulados = datos_pais['New_cases'].cumsum()
    muertes_acumuladas = datos_pais['New_deaths'].cumsum()
    plt.plot(casos_acumulados.index, casos_acumulados, label=f'Casos acumulados en {pais}')
    plt.plot(muertes_acumuladas.index, muertes_acumuladas, label=f'Muertes acumuladas en {pais}')

# plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(800000))

plt.xlabel('Fecha')
plt.ylabel('Número acumulado de casos/muertes')
plt.title('Crecimiento acumulativo de casos y muertes de COVID en varios países')
plt.legend()
plt.show()