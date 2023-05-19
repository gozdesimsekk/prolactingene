
# **Genotype-Phenotype relationship model in the light of lactation milk productivity data of prolactin gene region in cattle, goat and sheep animals.**

## **1.	Data Preperation**

###** 1.1.	Downloading Data**

Animal-SNPAtlas database was used to download data sets containing prolactin gene regions of goat, sheep and cattle animals.

Animal-SNPAtlas is a tool that allows users to search the functional annotation of SNPs, perform online genotype imputation, explore and visualize LD information, browse variant information using the genome browser and download SNP datasets for each species [1] [2] (http://gong_lab.hzau.edu.cn/Animal_SNPAtlas/#!/ )

> Cattle prolactin gene: chr19:48118059-48119771

> Goat prolactin gene: chr19:47730146-47736972

> Sheep prolacting gene: chr11:47843868-47850686

The necessary chromosomal region was entered into the "Reference Panel" and "Sample Information" inputs in Animal-SNPAtlas and the download operations were performed.

Breed-lactation milk productivity (kg) table created using the literature was used.


### 1.2.	Organizing Data

The dataframe was created by selecting the "Sample" and "Breed" columns in the txt file containing the sample information. In the Breed-LSV(kg) dataset, unnecessary columns were cleared and column names were indexed as “Sample” and “LSV (kg)”. The rows without LSV data are cleared.
The data were combined with the matching "Samples" in the two data sets. The name of the animal is processed in the last column.

Then, the homozygous and heterozygous genotype frequencies of the genotypes in the vcf file were analyzed. Visualized as a stacked bar graph.

The vcf file was transposed and transformed with the genomic location genotypes in the "Sample" columns in the rows.

Then, the genotypes found in the vcf file were added to the cleaned and prepared Sample-Breed-LSV-Animal file. Metadata stored in “all_data.tsv” file.

 















References

1 Gao, Y., Jiang, G., Yang, W., Jin, W., Gong, J., Xu, X., & Niu, X. (2023). Animal-SNPAtlas: a comprehensive SNP database for multiple animals. Nucleic acids research, 51(D1), D816–D826. https://doi.org/10.1093/nar/gkac954
2 Gao, Y., Jiang, G., Yang, W., Jin, W., Gong, J., Xu, X., & Niu, X. (2023). Animal-SNPAtlas: a comprehensive SNP database for multiple animals. Nucleic Acids Research, 51(D1), D816-D826.
![image](https://github.com/gozdesimsekk/prolactingene/assets/97754714/7f3c4e9c-774b-43c7-ab5c-aba241810456)
