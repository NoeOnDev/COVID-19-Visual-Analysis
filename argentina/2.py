import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv('./csv/argentina.csv', parse_dates=['Date_reported'], index_col='Date_reported')

plt.figure(figsize=(12, 6))
plt.bar(datos.index, datos['Cumulative_cases'], label='Casos acumulados', color='blue', alpha=0.5)
plt.bar(datos.index, datos['Cumulative_deaths'], label='Defunciones acumuladas', color='red', alpha=0.5)

plt.yticks(range(0, max(datos['Cumulative_cases']), 100000))
plt.xlabel('Fecha')
plt.ylabel('Número acumulado de casos/defunciones')
plt.title('Crecimiento acumulativo de infecciones y muertes de COVID en Argentina')
plt.legend()
plt.show()