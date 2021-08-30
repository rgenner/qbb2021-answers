$cp qbb2021/data/*.bed  qbb2021-answers/day1-lunch
$cp qbb2021/data/*.sizes  qbb2021-answers/day1-lunch

~/qbb2021-answers/day1-lunch/$ls -s > directory.txt

~/qbb2021-answers/day1-lunch/$wc -l *.bed > feature_count.txt
#2C observations: fbgenes.bed is the largest file with 30718 features. There are 68767 total features in all files. 

3B)
~/qbb2021-answers/day1-lunch/$cut -f 1 fbgenes.bed | sort | uniq -c > fbgenes.info
# observations: chrM has the least features (13)
# chr3R has the most features (7246)

4B)
~/qbb2021-answers/day1-lunch/$bedtools intersect -wb -a k9me3.bed -b *.bed | cut -f 1 | uniq -c > chr-with-fbgenes-k9.txt  
#observations: chromosome X has the most overlap (6387) 
#chromosome Y has the least overlap (36)
