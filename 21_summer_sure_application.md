# Faculty Research Justification


March 8, 2021

Project: Column Text Format, Summer Undergraduate Research Experience

Faculty: Clark Fitzgerald, Assistant Professor, Mathematics and Statistics Department


I plan to spend most of this summer working closely with Shawheen on the project described here, and we have all the necessary resources in place to succeed.
Shawheen has proven himself to be a bright, dedicated, and reliable student since joining in [last year's summer study group](https://github.com/clarkfitzg/summer20euler), and I am confident in his ability to succeed in this project.
I am not teaching summer school, so I will have time available.
The College of NSM has provided me with sufficient funds to perform the necessary computational experiments using Amazon Web Services, and that infrastructure is working well.


## Problem Statement

Data sets larger than a computer's main memory are challenging to work with, because they often require completely different computational techniques compared to smaller data sets that do fit in memory.
One solution to this problem is to store the data in a high performance binary format, such as [HDF5](https://www.hdfgroup.org/solutions/hdf5/).
Another solution is to combine data storage with a compute cluster, as in [Apache Hadoop](https://hadoop.apache.org/) and [Spark](https://spark.apache.org/).
The issue with both of these technically complex solutions is that they are not as accessible to data scientists without a background in software engineering.

The CSV (Comma Separated Values) data format is the most accessible data format, because it can be accessed with spreadsheet applications, standard command line tools, and programming languages used for data science like R and Python.
CSV has two main shortcomings when analyzing large data sets.
First, accessing individual columns requires processing the entire data set, which is inefficient and slow.
Second, column types are ambiguous (is it a string or an integer?), which contributes to errors.


## Proposal

We propose to develop a new data format that combines the accessibility and simplicity of CSV with the high performance of a dedicated solution for large data sets.
Our main idea is to store the columns as individual text files, which will address the inefficiency of accessing individual columns.
Secondly, we will supplement these text files with a metadata file adapted to data science use cases from the existing [W3C specification](https://www.w3.org/TR/tabular-data-model/) to apply the best practices and solution to the column ambiguity problem from the web development community to a data science application.

This summer we plan to produce an open source software implementation and a draft of a paper describing this new data format, which we call Column Text Format, or CTF.
We will release the software publicly by publishing it on the [Python Package Index](https://pypi.org/).
Depending on our progress on the paper by the end of the summer, we will consider submitting it to an open access academic journal such as the [Journal of Statistical Software](https://www.jstatsoft.org/index) or the [Journal of Big Data](https://journalofbigdata.springeropen.com/articles).
We also plan seek out opportunities for the students to present our work at conferences and meetups in the fall, for example, the [Bay Area R User Group](https://www.meetup.com/R-Users/) or the local [Sacramento Women in Data](https://www.meetup.com/Sacramento-Women-in-Data/).

When working with Shawheen, I will provide direction, code reviews, and make sure that we're following best practices.
Shawheen and another student, Julian Hernandez, have been working for the past month together with me on this software through support from the SEE/IRA research program, and we've already demonstrated significant speedups using a minimal version of CTF.
Much work still remains, and I expect Shawheen will spend time on the following tasks, which vary in complexity.

1) Write documentation so that users understand how to use the software.
2) Define unit tests to verify the correct behavior of the software.
3) Write case studies demonstrating the use cases for CTF.
4) Benchmark and compare CTF against other data formats.
6) Debug errors and profile code to identify performance issues.
5) Improve the code and add features.

When deep technical problems arise in the above tasks, I will help out, as I don't want Shawheen to spend days in frustration.
Overall, my goal is to keep Shawheen working at a level where he continuously builds confidence and practical competence.
I anticipate no problems in this regard.


## Future

My research interests lie at the intersection of big data, software development, and democracy, and this project aligns perfectly.
Intellectually, I'm fascinated by the technical challenge of developing computational approaches to apply statistics to large, messy, real world data sets.
Practically, software development is necessary to make these ideas come alive, demonstrate their merit, and allow others to apply and build on them so that the idea can have a real impact.
Morally, those without significant resources can better join in the Big Data revolution when the technology is more accessible.

If our project proves itself as a useful new technology, then there will be many future opportunities for Sac State students and for me to continue to develop the idea through software implementations in other programming languages and case studies.
Students with different interests and varying levels of programming experience can join in this project.
For example, beginning programmers often write better introductory narratives than experienced programmers precisely because they are beginners, and they don't take for granted concepts that warrant explanation.
As another example, a student who is more interested in statistical methodology can write a case study demonstrating how to apply a particular methodology to CTF data.
With sufficient adoption over several years, the software could become a member of [Numfocus](https://numfocus.org/), and secure future funding for students through external programs such as [Google Summer of Code](https://summerofcode.withgoogle.com/), which pays college students to work on open source software.
