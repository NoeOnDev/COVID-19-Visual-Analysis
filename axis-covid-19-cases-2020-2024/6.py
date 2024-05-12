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

# Elabora los siguientes gráficos en su formato vertical y horizontal

# 4. Elabora un gráfico de barras adyacentes que muestre por cada país
# las muertes indicando el total de cada año., incluyendo los 10 países.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

datos = pd.read_csv('all-global-countrys.csv')

paises = ['Argentina', 'Brazil', 'Canada', 'El Salvador', 'Ecuador', 'Mexico', 'Venezuela', 'Peru', 'Russian Federation', 'Zimbabwe']

datos['Date_reported'] = pd.to_datetime(datos['Date_reported'])

datos['Year'] = datos['Date_reported'].dt.year

totales_por_año = pd.DataFrame()

for pais in paises:
    datos_pais = datos[datos['Country'] == pais]
    totales_pais = datos_pais.groupby('Year')['New_deaths'].sum()
    totales_por_año[pais] = totales_pais

totales_por_año = totales_por_año.T

# Gráfico vertical
totales_por_año.plot(kind='bar', figsize=(12, 6))

plt.xlabel('País')
plt.ylabel('Total de muertes')
plt.title('Comparativo por año de las muertes de los países (Vertical)')
plt.xticks(rotation=90)
plt.legend(title='Año')
plt.tight_layout()
plt.show()

# Gráfico horizontal
totales_por_año.plot(kind='barh', figsize=(12, 6))

plt.ylabel('País')
plt.xlabel('Total de muertes')
plt.title('Comparativo por año de las muertes de los países (Horizontal)')
plt.legend(title='Año')
plt.tight_layout()
plt.show()