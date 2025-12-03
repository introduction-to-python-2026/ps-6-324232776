def create_codon_dict(file_path):
    codon_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Remove leading/trailing whitespace and split by tab
            parts = line.strip().split('\t')
            # Extract codon (first part) and single-letter amino acid (third part)
            codon = parts[0]
            single_letter = parts[2]
            codon_dict[codon] = single_letter
    return codon_dict
