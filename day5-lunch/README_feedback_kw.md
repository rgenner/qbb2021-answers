## Day 5 lunch feedback from Kate Weaver

* I really really like your way of getting `SNP_data_nums_only`. It's so cool and efficient. Alternatively, you could try something like `SNP_data.iloc[:,4:]` or `SNP_data.loc[:,"HG00096":]`, but your way is fantastic too!
* Good work on finding the allele frequency spectrum and plotting it. Great labels on the plot. Only advice I have here (and this is really nitpicky -- which just shows how great your work is -- the title could specifically reference which data you're working with)
*  Great work finding common variation!
* Running/plotting PCA! was almost perfect! But you'll notice that your output was length 986 rather than 2548. This is because the `Tranpose this data frame (swap x and y axes)` cell was never run. Therefore, the PCA was done by treating the samples as features and the SNPs as samples. Re-running the analysis with this cell should fix it, running the PCA such that the SNPs are features and the samples are samples.
