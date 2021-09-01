from fasta_reader import FASTAReader
import sys

target, query = sys.argv[1], sys.argv[2]
#input: python3 kmer_matcher.py target.fa query.fa k
#input: python3 kmer_matcher.py subset.fa droYak_seq.fa 11

# Load sequences
target_seqs = FASTAReader(open(target))
query_seqs = FASTAReader(open(query))
# We only need the first query sequence
query_seq = query_seqs[0][1]

kmers = {} #make empty dictionary
k = 11 # kmer is 11 bases long

for seq_id, sequence in target_seqs: #seq_id = first thing, sequence = 2nd thing
    sequence = sequence.upper() #convert to uppercase
    for kmerpos in range(0, len(sequence) - k + 1):
        kmer = sequence[kmerpos:kmerpos + k]
        kmers.setdefault(kmer, []) #set default to add new kmer to dict if it's not already in kmer
        kmers[kmer].append((seq_id, kmerpos)) #make dictionary with seq_id and position for target seq


tracker = 0
for seq_id, sequence in query_seqs: #iterate through query seq
    sequence = sequence.upper() #convert to uppercase
    for kmerpos in range(0, len(sequence) - k + 1):
        kmer = sequence[kmerpos:kmerpos + k]
        if kmer in kmers: #for each kmer that is also in kmers (target seq dict):
            tracker += 1
            print(kmer, kmerpos, kmers[kmer])
            if tracker == 1000:
                break
             #print kmer, position, and seq id
            #print(list(kmer, i, kmers[kmer])[:1000])
