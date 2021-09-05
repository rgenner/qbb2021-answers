import sys

gtf_file = sys.argv[1]
mut_chrom = sys.argv[2]
mut_pos = int(sys.argv[3]) #21378950
f = open(gtf_file)

#$python3 binary_search.py BDGP6.Ensembl.81.gtf 3R 21378950

genes = [] #create empty list for genes[]
for line in f: #(gtf file)
    if line.startswith("#"): #skip header lines
        continue
    fields = line.strip("\r\n").split("\t") #strip by space & carraige return, split by tab
#print(fields)
# ['211000022279132', 'FlyBase', 'exon', '1', '1005', '.', '+', '.', 'gene_id "FBgn0085825";
# gene_version "1"; transcript_id "FBtr0114283"; transcript_version "1"; exon_number "1";
# gene_name "CR41619"; gene_source "FlyBase"; gene_biotype "rRNA"; transcript_name "CR41619-RA";
# transcript_source "FlyBase"; transcript_biotype "rRNA"; exon_id "FBtr0114283-E1"; exon_version "1";']
    start = int(fields[3])
    end = int(fields[4])
    if (fields[0] == mut_chrom) and (fields[2] == "gene") and ('gene_biotype "protein_coding"' in line):
        subfields = fields[-1].split(';')
        # if list item contains '3R', 'gene', and 'gene_biotype "protein_coding"' :
        # make subfields list, indexing from the end ([-1]) and split by ';'
        # print(subfields)
        # ['3R', 'FlyBase', 'gene', '722370', '722621', '.', '-', '.', 'gene_id "FBgn0085804"; gene_version "1";
        # gene_name "CR41571"; gene_source "FlyBase"; gene_biotype "pseudogene";']
        for field in subfields: #within the subfields
            if "gene_name" in field: #if "gene_name" present, split the line by space (;?) and take the 2nd field, save to variable "gene_name"
                gene_name = field.split()[1]
                #print(gene_name)
                # "CG6690" \n "CG17843" '\n'"Eip93F" \n "CG6332" \n "CG6439" \n "CG6455"
        genes.append((gene_name, start, end)) #add gene_name, start position and end position to genes[] list
#print(genes)
# ('"CG1607"', 31382109, 31391893),
# ('"CG31204"', 31391894, 31393527),
# ('"CG31002"', 31393582, 31395304),

lo = 0 #lower limit = 0
hi = int(len(genes))-1 #upper limit = length of genes -1 (because python starts at 0)
mid = int(lo + hi) // 2 # set midpoint; // = floor division, makes answer integer

condition = True #set condition
tally = 0 #initiate count

# while True: #while the mut_pos (21378950) is not in the range of:
while mut_pos not in range(genes[mid][1],genes[mid][2]):
# midposition of genes (ex. 500,000), 1st field (start position of that gene) - "" (end position of that gene)]
# ex. entry # pos # 500,000 in genes[], range[31382109 - 311391893]
    #print(mid)
    old_mid = mid #set old mid position = new mid position
    tally += 1 # add to count; this was one iteration

    if mut_pos < genes[mid][1]: # 21378950 < start position (ex. 31382109):
        hi = mid -1 #new hi position = mid -1 (inclusive)
        mid = int(lo + hi) // 2 #new mid = middle of lo & new hi, // integer
    elif mut_pos > genes[mid][2]: # otherwise, if 21378950 > end position (ex. 311391893):
        lo = mid + 1 # new lo = mid + 1
        mid = int(lo + hi) // 2 # new mid = middle of new lo * hi, // integer
    if mid == old_mid: # if mid = old mid, you've reached the last 2 genes; stop
        break

print("position of gene closest to mutation:", mid)
print("number of iterations to find gene:", tally)
print("name of gene closest to mutation:", genes[mid][0])
print("starting position of gene closest to mutation:", genes[mid][1])
print("ending position of gene closest to mutation:", genes[mid][2])
