import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv('./csv/argentina.csv', parse_dates=['Date_reported'], index_col='Date_reported')

plt.figure(figsize=(12, 6))
plt.bar(datos.index, datos['New_cases'], label='Nuevos casos', color='blue', alpha=0.5)
plt.bar(datos.index, datos['New_deaths'], label='Nuevas defunciones', color='red', alpha=0.5)

plt.xlabel('Fecha')
plt.ylabel('Número de casos/defunciones')
plt.title('Comportamiento de nuevos casos y defunciones en Argentina')
plt.legend()
plt.show()