
#!/usr/bin/env python3

import numpy as np
import pandas as pd
import sys
from fasta_reader import FASTAReader



gap_penalty = float(sys.argv[3]) # Should be negative #-10

fasta = sys.argv[1]

seqs = FASTAReader(open(fasta))
sequence1 = seqs[0][1]
sequence2 = seqs[1][1]

fscore = sys.argv[2]
score = pd.read_csv(fscore, delim_whitespace=True) #delim by space

#print(score)
#print(score.loc["A", "A"])

F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))
max_matrix = np.empty((len(sequence1)+1, len(sequence2)+1), dtype='str')

# Now we need to fill in the values in the first row and
# first column, based on the gap penalty. Let's fill in the
# first column.



for i in range(len(sequence1)+1):
	F_matrix[i,0] = i*gap_penalty

# Now fill in the first row

for j in range(len(sequence2)+1):
	F_matrix[0,j] = j*gap_penalty

for i in range(1, len(sequence1)+1):
    max_matrix[i,0] = "v"

for j in range(1, len(sequence2)+1):
    max_matrix[0,j] = "h"




#=======================#
# Populate the F-matrix #
#=======================#

# Now that we've filled in the first row and column, we need
# to go row-by-row, and within each row go column-by-column,
# calculating the scores for the three possible alignments
# and storing the maximum score


for i in range(1, len(sequence1)+1): # loop through rows
    for j in range(1, len(sequence2)+1): # loop through columns
        d = F_matrix[i-1, j-1] + score.loc[sequence1[i-1], sequence2[j-1]]
        h = F_matrix[i,j-1] + gap_penalty
        v = F_matrix[i-1,j] + gap_penalty

        F_matrix[i,j] = max(d,h,v)
        if d > h and d > v:
            max_matrix[i,j] = "d"
        elif h > d and h > v:
            max_matrix[i,j] = "h"
        else:
            max_matrix[i,j] = "v"

seq1_pos = len(sequence1)
seq2_pos = len(sequence2)

seq1_alignment = ''
seq2_alignment = ''

while seq1_pos !=0 and seq2_pos !=0:
    if max_matrix[seq1_pos, seq2_pos] == "d":
        seq1_pos = seq1_pos-1
        seq1_alignment = sequence1[seq1_pos] + seq1_alignment
        seq2_pos = seq2_pos-1
        seq2_alignment = sequence2[seq2_pos] + seq2_alignment
    elif max_matrix[seq1_pos, seq2_pos] == "h":
        seq1_alignment = "-" + seq1_alignment
        seq2_alignment = sequence2[seq2_pos] + seq2_alignment
        seq2_pos = seq2_pos-1
    else:
        seq1_alignment = sequence1[seq1_pos] + seq1_alignment
        seq1_pos = seq1_pos -1
        seq2_alignment = "-" + seq2_alignment

output = sys.argv[4]

f = open(output, "w")
f.write(seq1_alignment)
f.write("\n")
f.write(seq2_alignment)
f.close()


#last val in F_matrix
#count number of gaps
