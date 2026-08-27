def proteins(strand):
    amino_acids = []
    strand_map = {"AUG" : "Methionine" , "UUU" : "Phenylalanine", "UUC" : "Phenylalanine",
"UUA" : "Leucine", "UUG" : "Leucine",
"UCU" : "Serine", "UCC" : "Serine", "UCA" : "Serine", "UCG" : "Serine",
"UAU" : "Tyrosine", "UAC" : "Tyrosine",
"UGU" : "Cysteine", "UGC" : "Cysteine",
"UGG" : "Tryptophan",
"UAA" : "STOP", "UAG" : "STOP", "UGA" : "STOP"}
    strand_list = [strand[codon : codon + 3] for codon in range(0 , len(strand) , 3)]
    for codon in strand_list:
        if strand_map[codon] == "STOP":
            return amino_acids
        else:
            amino_acids.append(strand_map[codon])
    return amino_acids