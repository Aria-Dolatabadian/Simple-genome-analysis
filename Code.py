import matplotlib.pyplot as plt
from Bio import SeqIO
def analyze_sequence(sequence):
    # Count the number of bases and compute sequence length
    sequence_length = len(sequence)
    # Check for sequence composition and GC content
    gc_count = sequence.count('G') + sequence.count('C')
    gc_content = (gc_count / sequence_length) * 100
    # Display information
    print(f"Sequence Length: {sequence_length} bases")
    print(f"GC Content: {gc_content:.2f}%")
    # Plot the sequence composition as a bar chart with base numbers
    bases = ['A', 'C', 'G', 'T']
    counts = [sequence.count(base) for base in bases]
    plt.bar(bases, counts, color=['green', 'blue', 'orange', 'red'])
    plt.xlabel('Bases')
    plt.ylabel('Count')
    plt.title('Sequence Composition')
    # Add base numbers on top of each bar
    for i, count in enumerate(counts):
        plt.text(i, count + 0.1, str(count), ha='center', va='bottom')
    plt.show()
# Read sequence from a FASTA file
fasta_file_path = "Aspergillus_sequence.fasta"
sequence_record = SeqIO.read(fasta_file_path, "fasta")
sequence_from_file = str(sequence_record.seq)
# Analyze the sequence
analyze_sequence(sequence_from_file)



