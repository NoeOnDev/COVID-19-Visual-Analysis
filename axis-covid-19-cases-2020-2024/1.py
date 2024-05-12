# 1. Elabora una gráfica de líneas que muestre el comportamiento del crecimiento
# de nuevos casos con respecto al numero de defunciones a lo largo de tiempo incluyendo los 10 países.

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

data = pd.read_csv('all-global-countrys.csv', parse_dates=['Date_reported'], index_col='Date_reported')

countries = ['Argentina', 'Brazil', 'Canada', 'El Salvador', 'Ecuador', 'Mexico', 'Venezuela (Bolivarian Republic of)', 'Peru', 'Russian Federation', 'Zimbabwe']

plt.figure(figsize=(12, 6))

for country in countries:
    country_data = data[data['Country'] == country]
    plt.plot(country_data.index, country_data['New_cases'], label=f'Nuevos casos en {country}')
    plt.plot(country_data.index, country_data['New_deaths'], label=f'Nuevas muertes en {country}')

plt.gca().get_yaxis().get_major_formatter().set_scientific(False)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(50000))

plt.xlabel('Fecha')
plt.ylabel('Número de casos/muertes')
plt.title('Crecimiento de nuevos casos y muertes de COVID en varios países')
plt.legend()
plt.show()
