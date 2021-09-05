1A. 
~/qbb2021-answers/$mkdir day1-lunch

1B.
~/qbb2021-answers/$cd day1-lunch
~/qbb2021-answers/day1-lunch/$nano README.md

1C.
$cp qbb2021/data/*.bed  qbb2021-answers/day1-lunch
$cp qbb2021/data/*.sizes  qbb2021-answers/day1-lunch
~/qbb2021-answers/day1-lunch/$ls -s  #to check file sizes

1E. 
~/qbb2021-answers/day1-lunch/$ls -s > directory.txt 

1F.
~/qbb2021-answers/day1-lunch/$ git add directory.txt README.md
~/qbb2021-answers/day1-lunch/$ git commit -m "upload directory.txt and README.md files"
~/qbb2021-answers/day1-lunch/$ git push

2A.
~/qbb2021-answers/day1-lunch/$wc -l *.bed > feature_count.txt. 

2C observations: 
fbgenes.bed is the largest file with 30718 features
There are 68768 total features in all files

3A.
~/qbb2021-answers/day1-lunch/$cut -f 1 fbgenes.bed | sort | uniq -c > fbgenes.info

3C observations:
chrM has the least features (13) 
chr3R has the most features (7246)

4A.
~/qbb2021-answers/day1-lunch/$bedtools intersect -wb -a k9me3.bed -b *.bed | cut -f 1 | uniq -c > chr-with-fbgenes-k9.txt

4D observations:  
Chromosome X has the most overlap (6387) 
Chromosome Y has the least overlap (36) 
