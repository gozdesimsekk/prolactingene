import pandas as pd
import vcf
from openpyxl import Workbook
import sys
sys.path.append("/Users/gozde/Desktop/prolactingene")

from transposevcff import transpose_vcf
from merge import merge_genotypes

vcf_file = '2023-05-18-19-04-42_goat_chr19_impute.vcf'
output_file = 'transpose_goat.xlsx'

transpose_vcf(vcf_file, output_file)

# Kullanım örneği
transposed_vcf_file = 'transpose_goat.xlsx'
dataframe_file = 'df_breed_goat_cleaned.xlsx'
output_file = 'alldata_goat.xlsx'
output_file1 = 'alldata_goat.tsv'

merge_genotypes(dataframe_file, transposed_vcf_file, output_file,output_file1)



