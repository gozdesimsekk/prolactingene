
import sys
sys.path.append("/Users/gozde/Desktop/prolactingene")
from transposevcff import transpose_vcf
from merge import merge_genotypes

vcf_file = '2023-05-18-19-06-51_sheep_chr11_impute.vcf'
output_file = 'transpose_sheep.xlsx'

transpose_vcf(vcf_file, output_file)

transposed_vcf_file = 'transpose_sheep.xlsx'
dataframe_file = 'df_breed_sheep_cleaned.xlsx'
output_file = 'alldata_sheep.xlsx'
output_file1 = 'alldata_sheep.tsv'
merge_genotypes(dataframe_file, transposed_vcf_file, output_file,output_file1)