Hi Rylee, 

- For the left side of the panel, your values for ER4 are right, but the values for G1E look off. You could review your commands because it looks like you 
used `bedtools windows` instead of `bedtools subtract` for that command. (-1) 
- Your motif doesn't look quite right. You could look over your process in which you extract the sequences (the command for `tomtom` looks okay; you might review 
your command for `meme-chip`) (-0.5) 

4.5/6

Revisions: 
•	Reran command with bedtools subtract (CTCFlost.bed now has 32 lines)
•	Updated part1terminalcommands.txt to reflect that
•	Updated jupyter notebook to reflect the new output

