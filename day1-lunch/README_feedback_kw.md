## Day 1 lunch feedback from Kate Weaver

* I see everything filewise I was looking for!
* Nice biological observations overall! However, I'm not fully convinced by your observations for 4d. This is because I think you want to revisit the command you used in 4a. The idea is that you want to `Look for chromosomes enriched in genes that overlap K9me3 histone modifications`. Using your command `bedtools intersect -wb -a K9me3.bed -b *.bed`, bedtools will report whatever the feature is in every bed file in the directory, rather than just genes. So we're asking for a count of the genes on each chromosome that overlap these histone modifications.
  * The best way to alleviate this issue would be to switch which files you give to the `-b` flags to report the genes directly. This should be just one gene. But then, you also want to make sure you only report each gene a single time. Because what if a single gene overlaps multiple K9me3 histone marks? It'll get reported more than once. The following flag will help to report just unique genes
  ```
  -u	Write the original A entry _once_ if _any_ overlaps found in B.
      - In other words, just report the fact >=1 hit was found.
      - Overlaps restricted by -f and -r.
  ```

* Estimated reasonable completion: 100%.
  * All 4 questions are reasonably complete, because you clearly put effort into the 4th question. If you have time to revisit question 4, I would recommend it. Please let me know if you have any questions.
