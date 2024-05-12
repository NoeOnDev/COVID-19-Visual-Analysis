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

# 4. Elabora un grafico apilado que muestre  el acumulado de infectados 
# por año del total de infectados, incluyendo los 10 países.

import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv('all-global-countrys.csv')

paises = ['Argentina', 'Brazil', 'Canada', 'El Salvador', 'Ecuador', 'Mexico', 'Venezuela', 'Peru', 'Russian Federation', 'Zimbabwe']

datos['Date_reported'] = pd.to_datetime(datos['Date_reported'])

datos['Year'] = datos['Date_reported'].dt.year

totales_por_año = pd.DataFrame()

for pais in paises:
    datos_pais = datos[datos['Country'] == pais]
    totales_pais = datos_pais.groupby('Year')['New_cases'].sum()
    totales_por_año[pais] = totales_pais

totales_por_año = totales_por_año.T

# Gráfico vertical
totales_por_año.plot(kind='bar', stacked=True, figsize=(12, 6))

plt.xlabel('País')
plt.ylabel('Total de infecciones')
plt.title('Total acumulado de infecciones por COVID por año y país (Vertical)')
plt.xticks(rotation=90)
plt.legend(title='Año')
plt.tight_layout()
plt.show()

# Gráfico horizontal
totales_por_año.plot(kind='barh', stacked=True, figsize=(12, 6))

plt.ylabel('País')
plt.xlabel('Total de infecciones')
plt.title('Total acumulado de infecciones por COVID por año y país (Horizontal)')
plt.legend(title='Año')
plt.tight_layout()
plt.show()