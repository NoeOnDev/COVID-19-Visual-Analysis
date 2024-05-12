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

# 3. Elabora un grafico de barras que muestre el total de
# infecciones y muertes por países, incluyendo los 10 países.

import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv('all-global-countrys.csv')

paises = ['Argentina', 'Brazil', 'Canada', 'El Salvador', 'Ecuador', 'Mexico', 'Venezuela', 'Peru', 'Russian Federation', 'Zimbabwe']

totales_infecciones = []
totales_muertes = []

for pais in paises:
    datos_pais = datos[datos['Country'] == pais]
    total_infecciones = datos_pais['New_cases'].sum()
    total_muertes = datos_pais['New_deaths'].sum()
    totales_infecciones.append(total_infecciones)
    totales_muertes.append(total_muertes)

# Gráfico vertical
x = range(len(paises))

plt.figure(figsize=(12, 6))

plt.bar(x, totales_infecciones, width=0.4, label='Infecciones', color='b', align='center')
plt.bar(x, totales_muertes, width=0.4, label='Muertes', color='r', align='edge')

plt.xlabel('País')
plt.ylabel('Total')
plt.title('Total de infecciones y muertes por COVID por país (Vertical)')
plt.xticks(x, paises, rotation=90)
plt.legend()
plt.tight_layout()
plt.show()

# Gráfico horizontal
y = range(len(paises))

plt.figure(figsize=(12, 6))

plt.barh(y, totales_infecciones, height=0.4, label='Infecciones', color='b', align='edge')
plt.barh(y, totales_muertes, height=0.4, label='Muertes', color='r', align='center')

plt.ylabel('País')
plt.xlabel('Total')
plt.title('Total de infecciones y muertes por COVID por país (Horizontal)')
plt.yticks(y, paises)
plt.legend()
plt.tight_layout()
plt.show()