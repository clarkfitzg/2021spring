Title: Column Oriented Plain Text

> Attach a 1-2 page Project Justification showing your commitment to the project, how this student project contributes to your own research goals and direction and what outcomes you expect to accomplish with this project including the potential for future research, external presentation with student, grant application and/or publication. 

## Research Goals

Broad:

- Develop new computational approaches to processing large data sets
- Democratize big data by making the technology more accessible to a broader user base, including those with limited funds for computing
- Create high quality software implementations of our ideas

Focused:

- Improve efficiency and speed by storing plain text data in a columnar format
- Increase reliability and reduce ambiguity in data storage formats by adapting an existing metadata standard designed for web browsers, and use it for data analysis
- Scale existing tools to larger data sets by partitioning data into chunks suitable for parallel and distributed processing

It's going to take a dedicated effort for several years if this idea is really going to take off and make a difference.

Entry points for students:

- develop software
- write documentation
- test cases
- write case studies- good for students interested in applied statistics

Our goals in this project are to combine the computational efficiency of column stores with the interoperability and ease of understanding of plain text.
This summer we plan to write software in at least two of the three popular languages used in data science: R, Python, and Julia.



## Outputs

- Blog posts
- Software
- conference presentation?
- article in JSS?

## Outline

### your commitment to the project

- I plan to spend at least one month this summer focused primarily on this project
- one month summer salary from startup
- not teaching summer school
- funds to experiment with large data sets in Amazon Web Service AWS, and to make it publicly available

### how this student project contributes to your own research goals and direction 

### Outcomes

- release high quality software implementation of CTF, most likely PyPI
- paper describing the purpose of this new data format


## Background

Data sets larger than a computer's main memory are challenging to work with, because they often require completely different computational techniques compared to smaller data sets that do fit in memory.
One solution to this problem is to store the data in a high performance binary format, such as [HDF5](https://www.hdfgroup.org/solutions/hdf5/).
Another solution is to combine data storage with a compute cluster, as in [Apache Hadoop](https://hadoop.apache.org/) and [Spark](https://spark.apache.org/).
The issue with both of these technically complex solutions is that they are not as accessible to data scientists without a background in software engineering.

The CSV (Comma Separated Values) data format is probably the most accessible data format, because it can be accessed with spreadsheet applications, standard command line tools, and programming languages used for data science like R and Python.
CSV has two main shortcomings when analyzing large data sets.
First, accessing individual columns requires processing the entire data set, which is inefficient and slow.
Second, column types are ambiguous (is it a string or an integer?), which contributes to errors.
The World Wide Web Consortium, W3C, has solved this column ambiguity problem by providing [clear specifications for tabular metadata](https://www.w3.org/TR/tabular-data-primer/).
The problem is that the W3C standard was written for web sites, and the data science community has not applied these standards.


## Proposal

We propose to develop a new data format that combines the accessiblity and simplicity of CSV with the high performance of a dedicated solution for large data sets.
Our main idea is to store the columns as individual text files, which will address the inefficiency of accessing individual columns.
Secondly, we will supplement these text files with a metadata file adapted to data science use cases from the [W3C specification](https://www.w3.org/TR/tabular-data-model/) to solve the column type ambiguity problem. 


## Project
