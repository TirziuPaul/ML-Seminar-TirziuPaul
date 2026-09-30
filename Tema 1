# Rezolvare Cerința 1
def calculeaza_nota_finala(t1, t2, proiect):
    media = 0.30 * t1 + 0.30 * t2 + 0.40 * proiect
    return round(media, 2)

# Testare funcție
print(calculeaza_nota_finala(8.5, 7.0, 9.5))




# Rezolvare Cerința 2
import numpy as np

ore_studiu = np.array([12, 5, 18, 8, 15, 3, 22, 10])

# 1. Statistici descriptive
print("Media:", np.mean(ore_studiu))
print("Deviația standard:", np.std(ore_studiu))
print("Minim:", np.min(ore_studiu))
print("Maxim:", np.max(ore_studiu))

# 2 & 3. Filtrare booleană
filtru = ore_studiu > 10
print("Filtru boolean:", filtru)
print("Ore de studiu > 10:", ore_studiu[filtru])




# Rezolvare Cerința 3
import pandas as pd

date_studenti = {
    'Nume': ['Ana', 'Bogdan', 'Cristian', 'Elena', 'Florin', 'Gabriela', 'Horia', 'Ioana'],
    'Test_1': [8.5, 5.0, 9.0, 6.5, 4.0, 9.5, 7.0, 8.0],
    'Test_2': [7.0, 6.0, 8.5, 5.5, 4.5, 10.0, 6.5, 8.5],
    'Proiect': [9.5, 7.0, 9.5, 8.0, 5.0, 9.5, 7.5, 9.0],
    'Ore_Studiu': [12, 5, 18, 8, 15, 3, 22, 10]
}

df_studenti = pd.DataFrame(date_studenti)

# 1. Calcul Nota_Finala
note = []
for i in range(len(df_studenti)):
    nota = calculeaza_nota_finala(df_studenti['Test_1'][i],
                                  df_studenti['Test_2'][i],
                                  df_studenti['Proiect'][i])
    note.append(nota)

df_studenti['Nota_Finala'] = note

# 2. Adăugare coloană Admis
df_studenti['Admis'] = df_studenti['Nota_Finala'] >= 6.0

print(df_studenti)

# 3. Filtrare
admisi = df_studenti[df_studenti['Admis'] == True]
rezultat = admisi[admisi['Ore_Studiu'] > 10]
print(rezultat)




# Răspuns Cerința 4

# 1. Există un astfel de student?
#    Da, Gabriela: nota finală 9.65, dar doar 3 ore de studiu pe săptămână.

# 2. Explicație în lumea reală:
#    - știa deja materia
#    - orele au fost notate greșit
#    - există factori care nu apar în tabel (talent, studiu în grup)

# 3. Impact asupra unui model de Machine Learning:
#    - este un outlier care nu respectă regula "mai multe ore = notă mai mare"
#    - într-un set mic de date poate încurca modelul și duce la predicții mai slabe
