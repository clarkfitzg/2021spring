# spring2021

SEE IRA research project

Ideas involving code analysis:


## Data table program transformations

One idea is to focus exclusively on scripts for data processing, using packages like `DataTables`.

1. Can we estimate the amount of memory needed for a script as a function of data size?
    How deterministic is this?
    Can we put an upper bound on the memory used by a script?
    This would help us to know which EC2 instance to use to process a given data set, for example.
2. Can we estimate the benefit or speedup that would come from first reorganizing the data into a different format?
1. Can we transform a script that doesn't stream the data into one that does?
    That is, can we programmatically change the script so that it iterates over the rows in a data frame rather than first reading the whole data set?
2. Can we take a script that works on a single input file, and turn it into a script that works on distributed data?


## Code querying

Software that determines what features of the language are used in a certain program.
For example, questions we may be able to ask:

1. How many comprehensions are used?
2. Which anti patterns are used, for example, gratuitous use of global variables.
3. Are people adding type annotations unnecessarily?

More ambitiously, we could see __who__ writes certain kinds of code by combining code analysis with analysis of the version control history.
What is different about how experts write code, versus novices?

