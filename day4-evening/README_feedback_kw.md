## Day 4 Homework feedback from Kate Weaver

* Fantastic work with this assignment! Overall, your plots and observations rock!
* A legend could be helpful for the merged histogram, but no need for you to go back through to add it
* Alternatively, and I would in fact suggest, you should try a ttest for testing whether maternal and paternal differ from each other
* The third part of question 10, where you're redoing the t-test is a little tricky. You're on the right track, but you'll want to use a data frame like the following:
  * you want to use a t-test, but keeping in mind the poisson model, you want to make a new data frame that has twice the number of rows where for each proband there are two lines with one column saying the number of DNMs (originating from a parent) and a new column that says which parent those de novo mutations originate from. So something like the below. Then you use those two columns in the ttest.

```
Proband_id 	num_dnm 	parent_cat
0 	91410 	111 	pat
1 	114094 	98 	pat
2 	111288 	93 	pat
3 	8147 	78 	pat
4 	88246 	87 	pat
... 	... 	... 	...
391 	121087 	1 	mat
392 	62630 	5 	mat
393 	76504 	5 	mat
394 	37789 	3 	mat
395 	13990 	7 	mat
```
* Great work on the prediction problem! I really appreciate all of your bolded conclusions throughout the notebook
