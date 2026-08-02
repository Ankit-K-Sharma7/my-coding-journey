def to_rna(dna_strand):
    transcription_map = {"G" : "C" , "C" : "G" , "T" : "A" , "A" : "U"}
    return "".join(transcription_map[strand] for strand in dna_strand)