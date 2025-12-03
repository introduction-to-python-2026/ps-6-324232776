def create_codon_dict(file_p ath):

codon_dict = {} with open(file_path, 'r') as

for line in file:

file:

codon, amino_acid, single_letter, full_name = line.split()

codon_dict[codon] =

single_letter

return codon_dict
