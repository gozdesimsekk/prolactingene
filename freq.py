
def calculate_genotype_frequencies(vcf_file):
    with open(vcf_file, 'r') as file:
        heterozygous_frequencies = {}
        homozygous_frequencies = {}
        total_genotypes = 0

        for line in file:
            if not line.startswith('#'):  # Başlık satırını atladık
                fields = line.strip().split('\t')
                pos = fields[1]  # Genomik lokasyon adını aldık
                genotypes = fields[9:]  # Genotipleri aldık

                heterozygous_count = 0
                homozygous_count = 0

                for genotype in genotypes:
                    alleles = genotype.split('|')  # Genotipleri alllellere ayırdık

                    if len(alleles) == 2:
                        if alleles[0] != alleles[1]:
                            heterozygous_count += 1
                        else:
                            homozygous_count += 1

                    total_genotypes += 1

                heterozygous_freq = heterozygous_count / len(genotypes)
                homozygous_freq = homozygous_count / len(genotypes)

                heterozygous_frequencies[pos] = heterozygous_freq
                homozygous_frequencies[pos] = homozygous_freq

    return heterozygous_frequencies, homozygous_frequencies