from openpyxl import Workbook

def transpose_vcf(vcf_file, output_file):
    data = {}
    samples = []
    positions = []

    with open(vcf_file, 'r') as f:
        for line in f:
            if line.startswith('#CHROM'):  # Başlık satırını bul
                samples = line.strip().split('\t')[9:]  # Sütun adlarını  al
                for sample in samples:
                    data[sample] = []  # Boş genotip listeleri
            elif not line.startswith('#'):
                fields = line.strip().split('\t')
                pos = fields[1]
                positions.append(pos)  # Pozisyonları listeye ekle
                genotypes = fields[9:]  # Genotipleri al
                for i, genotype in enumerate(genotypes):
                    sample = samples[i]
                    data[sample].append(genotype)  # Sample'a genotip ekle

    workbook = Workbook()
    sheet = workbook.active


    header = ['Sample'] + positions
    sheet.append(header)

    for sample in samples:
        row = [sample] + data[sample]
        sheet.append(row)

    workbook.save(output_file)