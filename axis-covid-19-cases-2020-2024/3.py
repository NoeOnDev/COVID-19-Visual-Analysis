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

data = pd.read_csv('all-global-countrys.csv')

countries = ['Argentina', 'Brazil', 'Canada', 'El Salvador', 'Ecuador', 'Mexico', 'Venezuela', 'Peru', 'Russian Federation', 'Zimbabwe']

total_infections = []
total_deaths = []

for country in countries:
    country_data = data[data['Country'] == country]
    infections = country_data['New_cases'].sum()
    deaths = country_data['New_deaths'].sum()
    total_infections.append(infections)
    total_deaths.append(deaths)

# Vertical graph
x = range(len(countries))

plt.figure(figsize=(12, 6))

plt.bar(x, total_infections, width=0.4, label='Infecciones', color='b', align='center')
plt.bar(x, total_deaths, width=0.4, label='Muertes', color='r', align='edge')

plt.xlabel('País')
plt.ylabel('Total')
plt.title('Total de infecciones y muertes por COVID por país (Vertical)')
plt.xticks(x, countries, rotation=90)
plt.legend()
plt.tight_layout()
plt.show()

# Horizontal graph
y = range(len(countries))

plt.figure(figsize=(12, 6))

plt.barh(y, total_infections, height=0.4, label='Infecciones', color='b', align='edge')
plt.barh(y, total_deaths, height=0.4, label='Muertes', color='r', align='center')

plt.ylabel('País')
plt.xlabel('Total')
plt.title('Total de infecciones y muertes por COVID por país (Horizontal)')
plt.yticks(y, countries)
plt.legend()
plt.tight_layout()
plt.show()