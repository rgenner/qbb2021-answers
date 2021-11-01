A few things: 
- Because the allele frequencies are such a continuous value, 10 bins is not sufficient; this chart could be more informative if you add more bins. Can you try that on your allele frequency spectrum?
- For the Manhattan plot, you correctly labeled the most significant snps (e.g., rs934755). However, we also want you to plot only those significant SNPs in a different color. On both your Manhattans, I see random dots at the bottom of the chromosomes (e.g., chr 2, 4).
I think this is an artifact of the qmplot manhattanplot package and while it’s great to use packages when appropriate, the packages you use need to generate figures that meet the specifications of exactly what you want. Unless you can figure out how to color only those significant SNPs using this package, you shouldn’t use it. 
In general, plotting a manhattan by hand is a generalizable skill for you - so it would be a worthwhile exercise to try to learn it here.
- Your qqplot doesn't look right. It might help to look up qqplots and get a general idea of how the points should interact with your x=y line. 
This might be an artifact of the `qqplot` function you use. Can you try plotting it with just the scatter function (e.g., ax.scatter) from python? 
There are examples for plotting on the course website. 
- Can you label your plots a little more clearly? especially the boxplot... I'm wondering which SNP and dataset we're looking at

6.25/7
