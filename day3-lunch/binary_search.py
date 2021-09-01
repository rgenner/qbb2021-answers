import sys

gtf_file = sys.argv[1]
mut_chrom = sys.argv[2]
mut_pos = int(sys.argv[3]) #21378950
f = open(gtf_file)

#$python3 binary_search.py BDGP6.Ensembl.81.gtf 3R 21378950

genes = []
for line in f:
    if line.startswith("#"):
        continue
    fields = line.strip("\r\n").split("\t")
    start = int(fields[3])
    end = int(fields[4])
    if (fields[0] == mut_chrom) and (fields[2] == "gene") and ('gene_biotype "protein_coding"' in line):
        subfields = fields[-1].split(';')
        for field in subfields:
            if "gene_name" in field:
                gene_name = field.split()[1]
        genes.append((gene_name, start, end))
#print(genes)

lo = 0
hi = int(len(genes))-1
mid = int(lo + hi) // 2 #makes integer (floor function)

count = 0
condition = True
tally = 0

#while condition == True:
while mut_pos not in range(genes[mid][1],genes[mid][2]):

    print(mid)
    old_mid = mid
    tally += 1

    if mut_pos < genes[mid][1]:
        hi = mid -1
        mid = int(lo + hi) // 2
    elif mut_pos > genes[mid][2]:
        lo = mid + 1
        mid = int(lo + hi) // 2
    if mid == old_mid:
        break

print("position of gene closest to mutation:", mid)
print("number of iterations to find gene:", tally)
print("name of gene closest to mutation:", genes[mid][0])
print("starting position of gene closest to mutation:", genes[mid][1])
print("ending position of gene closest to mutation:", genes[mid][2])































#hi = len(int(genes)-1)
#mid = (lo + hi) // 2
