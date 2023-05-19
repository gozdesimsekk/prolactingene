import pandas as pd
import sys
sys.path.append("/Users/gozde/Desktop/prolactingene")
from freq import calculate_genotype_frequencies
import numpy as np
import matplotlib.pyplot  as plt

df = pd.read_csv("cattle_sample_information.txt", delimiter="\t")

# Sadece "Sample" ve "Breed" sütunlarının seçilmesi
df_breed = df[["Sample", "Breed"]]
# Frekans dosyasının dataframe haline getirilmesi
df_freq = pd.read_excel("cattle_sample_information_breedFrequencies.xlsx")
df_freq = df_freq.rename(columns={"Unnamed: 2": "Breed"})

#filtreleme NaN değerlerini çıkartma
df_freq = df_freq[["Breed","LSV (kg)", ]].dropna()

# Yeni sütunu eklemek için df_breed DataFrame'ine "Eşleşen LSV" adında bir sütun ekle
df_breed["LSV (kg)"] = ""

# df_breed DataFrame'indeki her bir Breed değeri için döngü
for index, row in df_breed.iterrows():
    breed_value = row["Breed"]

    # df_freq DataFrame'inde Breed değerine göre filtrele
    filtered_df = df_freq[df_freq["Breed"] == breed_value]

    # Eşleşen LSV değerini al
    if not filtered_df.empty:
        lsv_value = filtered_df.iloc[0]["LSV (kg)"]
    else:
        lsv_value = ""

    # df_breed DataFrame'inde ilgili satıra Eşleşen LSV değerini yaz
    df_breed.loc[index, "LSV (kg)"] = lsv_value


#animal sütunu ekle
df_breed['Animal'] = 'cattle'
# "LSV (kg)" sütununu sayısal olarak tanımla
df_breed['LSV (kg)'] = pd.to_numeric(df_breed['LSV (kg)'], errors='coerce')

# Boş olan "LSV (kg)" değerine sahip satırları sil
df_cleaned = df_breed.dropna(subset=['LSV (kg)'])

"bu kısımda dosya kaydetme işlemi yapılmaktadır gerekli görüldüğünde comment satırını silebilirsiniz"

#df_breed.to_excel('df_breed_cattle.xlsx', index=False)
#df_cleaned.to_excel('df_breed_cattle_cleaned.xlsx', index=False)
#df_cleaned.to_csv('breed_cattle_cleaned.txt', sep='\t', index=False)

"frekansların bulunması ve txt dosyasına yazdırılması"

vcf_file = "2023-05-18-18-49-36_cattle_chr19_impute.vcf"
heterozygous_frequencies, homozygous_frequencies = calculate_genotype_frequencies(vcf_file)

for pos, heterozygous_freq in heterozygous_frequencies.items():
    homozygous_freq = homozygous_frequencies[pos]
    print("Genomik Lokasyon:", pos)
    print("Heterozigot Frekansı:", heterozygous_freq)
    print("Homozigot Frekansı:", homozygous_freq)
    print()

"txt olarak kaydetme"
"""output_file = "cattle_genotip_frekanslari.txt"

with open(output_file, 'w') as file:
    # Sütun başlıkları
    file.write("Genomik Lokasyon\tHeterozigot Frekansı\tHomozigot Frekansı\n")

    # Her bir genomik lokasyon için frekanslar
    for pos, heterozygous_freq in heterozygous_frequencies.items():
        homozygous_freq = homozygous_frequencies[pos]
        file.write(str(pos) + "\t" + str(heterozygous_freq) + "\t" + str(homozygous_freq) + "\n")
        """

# Verileri ve genomik lokasyon adlarını listelere ayırdık
positions = list(heterozygous_frequencies.keys())
heterozygous_freqs = list(heterozygous_frequencies.values())
homozygous_freqs = list(homozygous_frequencies.values())

# stacked bar
ind = np.arange(len(positions))
width = 0.35
height = 0.20
fig, ax = plt.subplots()
hetero_bars = ax.bar(ind, heterozygous_freqs, width, label='Heterozygous Frequency')
homo_bars = ax.bar(ind, homozygous_freqs, width, bottom=heterozygous_freqs, label='Homozygous Frequency')

# grafik ayarları
ax.set_xlabel('Genomic Location')
ax.set_ylabel('Frequency')
ax.set_title('Cattle Genotype Frequencies by Genomic Locations')
ax.tick_params(axis='x', labelsize=6)
ax.set_xticks(ind)
ax.set_xticklabels(positions, rotation=90)
ax.legend()
plt.subplots_adjust(top=0.85, bottom=0.2)

# Grafik gösterme veya kaydetme tercihe göre

#plt.show()
#plt.savefig('cattle_genotype_freq.png', dpi=300)