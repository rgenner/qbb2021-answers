Overall, this code looks good. It's clear that you understand what the purpose of your script is and how to get there. The code runs and makes sense.

It would be a good habit and helpful to anyone looking at the code to put comments in, including yourself. It's something that you will either start doing from the beginning or not start for years.

It's easy to follow the logic with your variable names.

The condition that you are using to end your loop is such a rare case and your code will function without it, you could just create an infinite while loop. Alternatively, you could use the last conditional line as your condition. `while mid != old_mid:`

The conditionals that you have set up to decide whether to move the lower boundary forward or the higher boundary down look like your program assumes that the mut_pos occurs inside a gene. I get that this works with your while condition, but it means that this code can't be used for a generalized binary search. Just food for thought.

On line 44, when you move `lo` up, you are setting it to mid + 1. However, what about the case where the mutation is ad `genes[mid][2] + 1`? It is now outside your new search range. Just something to watch out for.

In addition, once you find a single mid but the mutation isn't in a gene, you actually have to check the flanking genes to see which is truly closest. 

For problems like this, it's helpful to try and make your code work for any case. That means you have to think about edge cases. Meaning, what happens when a rare situation comes up like the mutation is past the last gene or before the first?

All that being said, you did a really good job with this, so pat yourself on the back.

% completion: 95%