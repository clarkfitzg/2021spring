## Background

I felt inspired while reading [The Art of Unix Programming](https://homepage.cs.uri.edu/~thenry/resources/unix_art/ch01s06.html)
It's making me think about better ways to store and process data.
How can we make processing big data more accessible?
By going back to our UNIX roots, and making it simpler.

Further, this book helps me understand why I don't like Hadoop, Spark, and complex binary data formats.
Hadoop isn't so easy to hack.
It's a big, opaque massive monolith to me.
It's predicated on setting everything up in HDFS.

Then there is software like Jupyter notebooks. 
They're great, but it's a glossy veneer hiding a good deal of complexity.

In the future, it seems like more data will live in cloud storage, places like AWS S3.
We need tools that are aware of this, that can process the data there, in place.
Amazon certainly has this with some of their query tools.

But proprietary tools like Amazon offers aren't the answer.
Better to make the data itself hackable as cheaply as possible, with as many different kinds of software as possible.

This means representing the data as text.
The most ubiquitous text data format is CSV, and all it's variations.


## CSV

Advantages:

1. Represents most any kind of table
1. Text based, human readable
2. Any program can read it
3. Widely used

Disadvantages:

1. Ambiguous column types
1. Ambiguous column meanings
2. Performance, particularly:
    1. row oriented structure
    1. not easy to parallelize or distribute
2. Scale- nobody wants to open up a CSV file larger than 2 GB.


## Use case: data science

The data science use case I imagine is offline analytical processing of a bunch of data, the "write once, read many" pattern.
For example, the data lakes that businesses store.
The transactional systems put it all there, and there it sits, ready to be mined, or to do some hypothesis tests, stats, machine learning, whatever.

Databases offer many features that we don't really need for this use case.
For example, we don't usually update rows, so we can forget about that.

When I've written code to process huge CSV files, it usually uses the same pattern over and over.
Why not generate this code?


## Idea

What's the simplest possible way that we can address the disadvantages of a simple text based format like CSV, while preserving the advantages?

Non negotiable:

1. __simple and hackable__
    That is, people should be able to easily understand it and write programs using existing technology without having to install a bunch of external software.
    It's not sufficient for it to work with only one or two languages, like R and Python.
2. __works well locally and in cloud__
    I'm not sure yet what this requirement implies.
    It should work well for small and large data sets, and on underpowered machines.

What we're proposing here will never be the fastest thing; that's not the point.
The point is to be useful, not optimal.
A good binary data storage format will always outperform this format; if it doesn't, then that binary storage format is obsolete.


## Switching to column oriented

Here's the simplest thing I can think of for more efficiently representing this CSV file, call is `ABC.csv`:

```
A,B,C
10,20,hello
11,21,goodbye
```

Create a directory, say `ABC` dedicated to representing everything the data in the file `ABC.csv`.
That is, everything in this directory has a purpose in representing and describing this data, and everything that you need to represent and describe this data is contained in the directory.

The directory will contain three files, `A.txt`, `B.txt`, and `C.txt`, each containing the data for each column, with each row on a newline.
This will address the row oriented performance issue by switching it to columnar.

`A.txt` contains 
```
10
11
```

`B.txt` contains 
```
20
21
```

`C.txt` contains 
```
hello
goodbye
```

With this format, we can process each column as a simple text stream, using any tool that understands text streams.
As another step towards optimization, we could compress the files, or even the whole ABC directory.
It might even compress smaller with this columnar format.


## Ambiguity

Optionally, the folder `ABC` can contain or point to a URL for a file representing the metadata for the table and for each column.
We can borrow from [W3C's existing standard](https://www.w3.org/TR/tabular-data-primer/#documenting-csvs) here.
This will address the ambiguity aspect.
They even offer guidance on where to put the file.

> If processors don't see an appropriate Link header, they will append -metadata.json to the end of the URL of the CSV file to try to find metadata for it. If they can't find a metadata file there, they will look in the directory containing the CSV file for a file called csv-metadata.json and use that file.


## Scale, Distributed and Parallel Computing

The simplest way I can imagine to make this work for distributed and parallel computing is to break it into chunks.
In our example above, we would have a directory structure like the following:

```
- ABC               <- directory
    - metadata.json
    - chunk1        <- directory
        - A.txt
        - B.txt
        - C.txt
    - chunk2        <- directory
        - A.txt
        - B.txt
        - C.txt

    ...

    - chunkN        <- directory
        - A.txt
        - B.txt
        - C.txt
```

### Specialization to grouped computations

For a computation like `median(income) GROUP BY country` where `country` is any column with categorical values, we would want to organize the data chunks so that each chunk contains all the values for that group, `country` here.


## Software

The storage pattern should be relatively painless to implement.
What software is necessary for it to be useful?

1. Read and write this data from the popular data science programming languages.
    When we write the data, we need to translate the types from the language and store them in the data.
    I'd like these packages to be as dependence free as possible.
2. Efficiently convert regular CSV files into this representation.
3. Cloud oriented tools to make it easy to work with these files stored on AWS S3.
    We should be able to piggyback on existing tools.
4. SQL engine.
    Implement a subset of SQL to work on data stored in this format.
4. Tools to generate code to process large data sets given input programs.
    This requires metaprogramming, and I'll draw on my PhD research here.


## Proof of Concept

How will we demonstrate that this storage pattern is useful?


## Conclusion

This UNIX idea of simple text streams is one of the oldest in computer science.
We're simply applying the UNIX ideas to data science / analytical data processing.

What to call this storage pattern?
Some ideas:

- column text
- text columns
- column text chunks
