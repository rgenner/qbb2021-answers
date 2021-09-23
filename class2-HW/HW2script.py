import matplotlib.pyplot as plt
import numpy

AF = []
DP = []
QA = []
ANN = []
muts=''
muts_total= {}

INFO = open('INFO.vcf')
for line in INFO:
    splitINFO = line.split(';')
    for line in splitINFO:
        try:
            AFnums = (float(splitINFO[3][3:]))
        except ValueError:
            pass
    AF.append(AFnums)
    for line in splitINFO:
        try:
            DPnums = (int(splitINFO[7][3:]))
        except ValueError:
            pass
    DP.append(DPnums)
    for line in splitINFO:
        try:
            QAnums = (int(splitINFO[26][3:]))
        except ValueError:
            pass
    QA.append(QAnums)
    for line in splitINFO:
        if 'ANN' in line:
            muts = line[4:].split('|')[1]
        elif muts == '':
            continue
        else:
            muts_total.setdefault(muts, 0)
            muts_total[muts] += 1


#print(DP)
AFmax = max(AF) #1
#print(AFmax)
#DPmax = max(DP) #250?
#print(DPmax)
#QAmax = max(QA) #3000?

fig, axis = plt.subplots(2,2, figsize = (14,10))
axis[0,0].hist(AF, range=(0,AFmax), bins=5)
axis[0,0].title.set_text('Allele Frequency Spectrum of Identified Variants')
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
axis[1,1].tick_params(axis = "x", which = "both", bottom = False, top = False)
plt.xticks(rotation = 90)

plt.show()
plt.savefig('HW2plots.png')
