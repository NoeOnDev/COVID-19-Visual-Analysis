# Elabora los siguientes gráficos en su formato vertical y horizontal

# 6. Elabora un gráfico de barras adyacentes que muestre por cada país
# las muertes indicando el total de cada año, incluyendo los 10 países.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('all-global-countrys.csv')

countries = ['Argentina', 'Brazil', 'Canada', 'El Salvador', 'Ecuador', 'Mexico', 'Venezuela (Bolivarian Republic of)', 'Peru', 'Russian Federation', 'Zimbabwe']

data['Date_reported'] = pd.to_datetime(data['Date_reported'])

data['Year'] = data['Date_reported'].dt.year

totals_by_year = pd.DataFrame()

for country in countries:
    country_data = data[data['Country'] == country]
    country_totals = country_data.groupby('Year')['New_deaths'].sum()
    totals_by_year[country] = country_totals

totals_by_year = totals_by_year.T

# Vertical graph
totals_by_year.plot(kind='bar', figsize=(12, 6))

plt.xlabel('País')
plt.ylabel('Total de muertes')
plt.title('Comparativo por año de las muertes de los países (Vertical)')
plt.xticks(rotation=90)
plt.legend(title='Año')
plt.tight_layout()
plt.show()

# Horizontal graph
totals_by_year.plot(kind='barh', figsize=(12, 6))

plt.ylabel('País')
plt.xlabel('Total de muertes')
plt.title('Comparativo por año de las muertes de los países (Horizontal)')
plt.legend(title='Año')
plt.tight_layout()
plt.show()