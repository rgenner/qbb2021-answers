Overall, the code looks very good. You clearly feel comfortable enough with the use of the for loop, dictionaries, and reading in files.

It would be helpful for both you (if you come back to your code) and anyone else (me) who looks at your code to have comments explaning what each part of the code is doing, and why. It doesn't need to be every line, but each block of test clearly has a specific purpose that would be made easier to understand with a couple of comments.

Your conditional statement for the length of sys.argv is effective in accomplishing the goal of the assignment. But it does mean that you have to rewrite a lot of the same code. You could put the if statement inside your for loop as part of the if statement you already have, perhaps as an `elif len(sys.argv) == 4`.

In your line reading in the file names, you could simplify the right-hand side to sys.argv[1:3]

% completion: 100%

keep up the good work