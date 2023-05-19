import pandas as pd

def merge_genotypes(df_breef_goat_file, ornek_file, output_file,output_file1):
    # DataFrame'leri oku
    df_breef_goat = pd.read_excel(df_breef_goat_file)
    ornek = pd.read_excel(ornek_file)

    # Sample isimlerini eşleştirerek genotipleri birleştir
    merged_df = pd.merge(df_breef_goat, ornek, on="Sample", how="inner")

    # Yeni dosyayı kaydet
    merged_df.to_excel(output_file, index=False)
    merged_df.to_csv(output_file1, sep="\t", index=False)