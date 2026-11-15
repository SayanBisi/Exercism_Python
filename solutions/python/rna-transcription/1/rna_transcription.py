def to_rna(dna_strand):
    dna_strand_copy = dna_strand
    rna_strand = ""
    for ch in dna_strand_copy:
        if ch == 'C':
            rna_strand += 'G'
        elif ch == 'G':
            rna_strand += 'C'
        elif ch == 'T':
            rna_strand += 'A'
        elif ch == 'A':
            rna_strand += 'U'
        else:
            raise ValueError('Invalid input.')

    return rna_strand