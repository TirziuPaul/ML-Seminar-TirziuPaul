# Cerinta 1
def calculeaza_nota_finala(t1, t2, proiect):
    media = t1 * 0.30 + t2 * 0.30 + proiect * 0.40
    return round(media, 2)

# Testare funcție
print(calculeaza_nota_finala(8.5, 7.0, 9.5))



# Cerinta 2
import numpy as np
ore_studiu = np.array([12, 5, 18, 8, 15, 3, 22, 10])

# 1. Statistici
print("Media:", np.mean(ore_studiu))
print("Deviația standard:", np.std(ore_studiu))
print("Minim:", np.min(ore_studiu))
print("Maxim:", np.max(ore_studiu))

# 2. Filtru boolean
filtru = ore_studiu > 10
print("Filtru:", filtru)
print("Ore > 10:", ore_studiu[filtru])



# Cerinta 3
import pandas as pd

def calculeaza_nota_finala(t1, t2, proiect):
    media = t1 * 0.30 + t2 * 0.30 + proiect * 0.40
    return round(media, 2)

date_studenti = {
    'Nume': ['Ana', 'Bogdan', 'Cristian', 'Elena', 'Florin', 'Gabriela', 'Horia', 'Ioana'],
    'Test_1': [8.5, 5.0, 9.0, 6.5, 4.0, 9.5, 7.0, 8.0],
    'Test_2': [7.0, 6.0, 8.5, 5.5, 4.5, 10.0, 6.5, 8.5],
    'Proiect': [9.5, 7.0, 9.5, 8.0, 5.0, 9.5, 7.5, 9.0],
    'Ore_Studiu': [12, 5, 18, 8, 15, 3, 22, 10]
}

df_studenti = pd.DataFrame(date_studenti)

# 1. Calcul Nota_Finala
df_studenti['Nota_Finala'] = df_studenti.apply(
    lambda rand: calculeaza_nota_finala(rand['Test_1'], rand['Test_2'], rand['Proiect']),
    axis=1
)

# 2. Adăugare coloană Admis
df_studenti['Admis'] = df_studenti['Nota_Finala'] >= 6.0

# 3. Filtrare
print(df_studenti[(df_studenti['Admis']) & (df_studenti['Ore_Studiu'] > 10)])



#Cerinta 4
# Da, Gabriela are nota finala 9.65 si a invatat doar 3 ore pe saptamana.
# In realitate, poate stia deja materia sau invata foarte repede dar poate fi si o greseala in date.
# Pentru un model de Machine Learning este o valoare ciudata (outlier), care il poate incurca si ii poate scadea acuratetea, mai ales cand sunt putine date.
