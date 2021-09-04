from fasta_reader import FASTAReader
import sys

target, query = sys.argv[1], sys.argv[2]
#example input: python3 kmer_matcher.py target.fa query.fa k
#input: python3 kmer_matcher.py subset.fa droYak_seq.fa 11

# Load sequences
target_seqs = FASTAReader(open(target)) #format = list: [('STRNG.1.2'), 'ACTG..'), (STRING.1.3), 'GTCG..')] length = 105 entries
query_seqs = FASTAReader(open(query)) #format = list: [("droyak info", 'GCTA..')], length = 1 entry
# We only need the second part of query (the sequence)
query_seq = query_seqs[0][1] #format = GCTA.. , length = 1000000

kmers = {} #make empty dictionary to put kmers in
k = int(sys.argv[3]) #kmer is 11 bases long

for seq_id, sequence in target_seqs: #seq_id = first thing (STRNG.1.2), sequence = 2nd thing (ACTG..)
    sequence = sequence.upper() #convert to uppercase
    for kmerpos in range(0, len(sequence) - k + 1): #loop through sequence string starting at index[0] ([A]CTGCGTAC..)
    # and ending at len(sequence) - 11 (k) b/c want to end 11 before the end and not get truncated kmers
    # + 1 b/c len() is exclusive (starts at 1) and index[] is inclusive (starts at 0)
        kmer = sequence[kmerpos:kmerpos + k] #truncating sequence into kmers 11 bases long: (0-11), (1-12) (2-13) = [ACTGCGATGTC]GT. A[CTGCGATGTCG]T, AC[TGCGATGTCGT]
        kmers.setdefault(kmer, []) #set default to add new kmer to dict kmers{} if it's not already in kmer
        #another way:
        #kmers[kmer] = []
        #if kmer not in kmers: #if kmer seq (ex.ACTGACCTGATG) is not in kmers{} dict:
          #kmers[kmer] = [(seq_id,kmerpos)] #kmers{} dict key(ACTGACCTGATG) = [(seq_id(STRNG.1.2), kmerpos [2-13])]
          #ex. dict kmers[ACTGACCTGATG] = [(STRNG.1.2, [2-13])]
          #make a new key (sequence) and value (seq_id, kmer position) in kmers{}
      #else: #if kmer seq IS in kmers{} dict
      #for ex. the sequence ACTGACCTGATG is in kmers{} and this is an additional position where the sequence is in the target seq:
        kmers[kmer].append((seq_id,kmerpos)) #add the sequence id (STRNG.1.2) and the target kmer position ([2-13])

tracker = 0 #start tracker to count to 1000
done = False #sets up condition
for seq_id, sequence in query_seqs: #iterate through query seq
    if done == True: #stop when tracker gets to 1000 matches
        break
    sequence = sequence.upper() #convert to uppercase
    for kmerpos in range(0, len(sequence) - k + 1): #kmer position
        kmer = sequence[kmerpos:kmerpos + k]
        if kmer in kmers: #for each kmer that is also in kmers (target seq dict):
            tracker += 1 #add count to tracker (want 1000)
            print(kmer, kmerpos, kmers[kmer]) #print kmer sequence, kmer position (in query seq), and kmers[kmer] which is the target seq ID and position(s)
            if tracker == 1000: #if tracker reaches 1000 matches, meaning 1000 query:target sequences have been matched
                done = True #condition = true
                break #break this loop
