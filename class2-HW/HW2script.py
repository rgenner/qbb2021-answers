#import modules
import matplotlib.pyplot as plt
import numpy

#create empty lists, string, and directory
AF = []
DP = []
QA = []
ANN = []
muts=''
muts_total= {}

INFO = open('INFO.vcf') #open VCF file
for line in INFO:
    splitINFO = line.split(';') #split lines by ;
    for val in splitINFO:
        try:
            AFnums = (float(splitINFO[3][3:6])) #assign AF# to AF[] (field 3 = AF=##, [3:] deletes 'AF' and gives you just the #)
        except ValueError:
            pass #skip over random (#,#) value
    AF.append(AFnums) #add AF #'s to AF[]
    for val in splitINFO:
        try:
            DPnums = (int(splitINFO[7][3:6])) #assign DP# to DP[] (field 7 = DP=##)
        except ValueError:
            pass
    DP.append(DPnums) #add DP #'s to DP[]
    for val in splitINFO:
        try:
            QAnums = (int(splitINFO[26][3:6])) #assign QA# to QA[] (fiel 26 = QA=##)
        except ValueError:
            pass
    QA.append(QAnums)
    for val in splitINFO:
        if 'ANN' in val: #isolate lines with ANN
            muts = line[4:].split('|')[1] #get rid of ANN= , split by |, grab second item
        elif muts == '': #if empty value, skip
            continue
        else:
            muts_total.setdefault(muts, 0) #set defaults for dictionary, key = muts, value starts at 0
            muts_total[muts] += 1 #add value count to muts_total

#print(DP)
AFmax = max(AF) #1
#print(AFmax)
#DPmax = max(DP) #250?
#print(DPmax)
#QAmax = max(QA) #3000?

fig, axis = plt.subplots(2,2, figsize = (14,10))
axis[0,0].hist(AF, range=(0,AFmax), bins=5) #create AF graph
axis[0,0].title.set_text('Allele Frequency Spectrum of Identified Variants') #assign title
axis[0,0].set_xlabel('Allele Frequency')
axis[0,0].set_ylabel('Variant Count')
axis[0,1].hist(DP, range=(0,150), bins=25)
axis[0,1].title.set_text('Read Depth Distribution of Variant Genotypes')
axis[0,1].set_xlabel('Read Depth Distribution')
axis[0,1].set_ylabel('Variant Count')
axis[1,0].hist(QA, range=(0,3000), bins=25)
axis[1,0].title.set_text('Quality Distribution of Variant Genotypes')
axis[1,0].set_xlabel('Quality Distribution')
axis[1,0].set_ylabel('Variant Count')
axis[1,1].bar(muts_total.keys(), muts_total.values())
axis[1,1].title.set_text('Summary of Predicted Effects of Each Variant')
axis[1,1].set_ylabel('Variant Count')
labels = ("upstream gene", "synonymous", "missense", "stop gained", "splice region & intron", "stop lost & splice region", "frameshift", "frameshift & stop lost & splice region", "disruptive inframe deletion", "downstream gene", "disruptive inframe insertion", "conservative inframe insertion", "splice region & stop regained", "initiator codon", "start lost", "conservative inframe deletion", "frameshift & start lost", "splice donor & intron", "splice region & synonymous", "start lost & conservative inframe insertion", "missense & splice region", "frameshift & stop gained")
axis[1,1].set_xticklabels(labels, fontsize=5)
axis[1,1].tick_params(axis = "x", which = "both", bottom = False, top = False) #delete ticks for last graph
plt.xticks(rotation = 90) #rotate x tick labels

plt.show()
plt.savefig('HW2plots.png') #save to png
