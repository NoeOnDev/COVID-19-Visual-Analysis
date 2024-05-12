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

# 4. Elabora un gráfico apilado que muestre  el acumulado de infectados 
# por año del total de infectados, incluyendo los 10 países.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('all-global-countrys.csv')

countries = ['Argentina', 'Brazil', 'Canada', 'El Salvador', 'Ecuador', 'Mexico', 'Venezuela (Bolivarian Republic of)', 'Peru', 'Russian Federation', 'Zimbabwe']

data['Date_reported'] = pd.to_datetime(data['Date_reported'])

data['Year'] = data['Date_reported'].dt.year

totals_by_year = pd.DataFrame()

for country in countries:
    country_data = data[data['Country'] == country]
    country_totals = country_data.groupby('Year')['New_cases'].sum()
    totals_by_year[country] = country_totals

totals_by_year = totals_by_year.T

# Vertical graph
totals_by_year.plot(kind='bar', stacked=True, figsize=(12, 6))

plt.xlabel('País')
plt.ylabel('Total de infecciones')
plt.title('Total acumulado de infecciones por COVID por año y país (Vertical)')
plt.xticks(rotation=90)
plt.legend(title='Año')
plt.tight_layout()
plt.show()

# Horizontal graph
totals_by_year.plot(kind='barh', stacked=True, figsize=(12, 6))

plt.ylabel('País')
plt.xlabel('Total de infecciones')
plt.title('Total acumulado de infecciones por COVID por año y país (Horizontal)')
plt.legend(title='Año')
plt.tight_layout()
plt.show()