
import sys
sys.path.append("/Users/gozde/Desktop/prolactingene")
from transposevcff import transpose_vcf
from merge import merge_genotypes

vcf_file = '2023-05-18-18-49-36_cattle_chr19_impute.vcf'
output_file = 'transpose_cattle.xlsx'

transpose_vcf(vcf_file, output_file)


# Kullanım örneği
transposed_vcf_file = 'transpose_cattle.xlsx'
dataframe_file = 'df_breed_cattle_cleaned.xlsx'
output_file = 'alldata_cattle.xlsx'
output_file1 = 'alldata_cattle.tsv'
merge_genotypes(dataframe_file, transposed_vcf_file, output_file,output_file1)