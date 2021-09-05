#open and read the .SAM file as a single string
fs = open("/Users/cmdb/qbb2021-answers/day1-evening/SRR072893.sam", "r")

#about .SAM file
#1000+ header lines starting with "@":
#@SQ	SN:2L	LN:23513712
# core data:
# SRR072893.1692271	 0	 2L	   7583	  60   40M	 * 	    0    	AGAGAACCCACGTTTGAACAAGTATCGGCGTGTGGACAAC	<9799:>A>?:?:?>A?>><1;297-00+/C@@C8/>@4AS:i:0	XN:i:0	XM:i:0	XO:i:0	XG:i:0	NM:i:0	MD:Z:40	YT:Z:UU	NH:i:1
#      QNAME       FLAG RNAME   POS  MAPQ  CIGAR RNEXT? PNEXT?  SEQ?                                        QUAL? (ASCII)
sam = [] #create empty list sam[]
num_alignments = 0 #start counter for total number of alignments
num_perfect_alignments = 0 #start counter for number of perfect alignments
sum_mapq = 0
num_2L = 0
for line in fs:
    if line[0] == "@": #exclude the header lines, which start with @
        continue
    stripped_line = line.strip() #strip spaces /n from lines
    # SRR072893.1692271	 0	 2L
    # ATTCGCTGCA
    fields = stripped_line.split("\t") #split string by tabs
    # ['SRR072893.1692271',	'0', '2L', 'ACTGCTGC...'] ['SRR072...']
    sam.append(fields) #add split strings to sam[] list
#print([sam])
# sam[] = ['SRR072893.1692271',	'0', '2L', 'ACTGCTGC...'] ['SRR072...']
    num_alignments += 1 #count number of alignments (each [SRR..] string)
    if '40M' in fields[5]: #cigar string = compressed representation of alignment
    #40M CIGAR = 40 nts of match (M)
        num_perfect_alignments += 1 #add to number of perfect alignments
    #print(fields[5]) #print 40M
    fields[4] = int(fields[4]) #fields[4] = MAPQ value
    #MAPQ = MAPping Quality; 20 = probability of correctly mapping a read [0-30?], 255 = N/A
    fields [3] = int(fields[3]) #fields[3] = POS
    #POS = left-most mapping POSition of first matching base (starts at 1)
    sum_mapq += fields[4] #sum MAPQ values
    if fields[2] == '2L' and fields[3] >= 10000 and fields[3] <= 20000:
        num_2L += 1 # add to num_2L count
    # Count number of reads that start their alignment on chromosome 2L
    # between base 10000 and 20000 (inclusive)

fs.close
print("total number of alignments: ", num_alignments)
print("total number of perfect alignments: ", num_perfect_alignments)
print("average MAPQ scores: ", (sum_mapq / num_alignments))
print("number of reads on chromosome 2L between bases 1000 and 2000: ", num_2L)
