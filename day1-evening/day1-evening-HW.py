fs = open("/Users/cmdb/qbb2021-answers/day1-evening/SRR072893.sam")
sam = []
num_alignments = 0
num_perfect_alignments = 0
sum_mapq = 0
num_2L = 0
for line in fs:
    if line[0] == "@": #exclude the header lines, which start with @
        continue
    stripped_line = line.strip() #strip spaces /n from lines
    fields = stripped_line.split("\t") #
    sam.append(fields)
    num_alignments += 1 #number of non-perfect alignments
    if '40M' in fields[5]:
        num_perfect_alignments += 1 #number of perfect alignments
    #print(fields[5])
    fields[4] = int(fields[4])
    fields [3] = int(fields[3])
    sum_mapq += fields[4]
    if fields[2] == '2L' and fields[3] >= 10000 and fields[3] <= 20000:
        num_2L += 1

fs.close
print(num_alignments)
print(num_perfect_alignments)
print(sum_mapq / num_alignments)
print(num_2L)
