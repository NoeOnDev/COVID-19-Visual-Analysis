# 2. Elabora una gráfica de líneas que muestre  en crecimiento acumulativo 
# de infecciones y muertes de covid incluyendo los 10 países.

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

data = pd.read_csv('all-global-countrys.csv', parse_dates=['Date_reported'], index_col='Date_reported')

countries = ['Argentina', 'Brazil', 'Canada', 'El Salvador', 'Ecuador', 'Mexico', 'Venezuela (Bolivarian Republic of)', 'Peru', 'Russian Federation', 'Zimbabwe']

plt.figure(figsize=(12, 6))

for country in countries:
    country_data = data[data['Country'] == country]
    accumulated_cases = country_data['New_cases'].cumsum()
    accumulated_deaths = country_data['New_deaths'].cumsum()
    plt.plot(accumulated_cases.index, accumulated_cases, label=f'Casos acumulados en {country}')
    plt.plot(accumulated_deaths.index, accumulated_deaths, label=f'Muertes acumuladas en {country}')

# plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(800000))

plt.xlabel('Fecha')
plt.ylabel('Número acumulado de casos/muertes')
plt.title('Crecimiento acumulativo de casos y muertes de COVID en varios países')
plt.legend()
plt.show()