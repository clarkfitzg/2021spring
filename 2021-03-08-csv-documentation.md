Mon Mar  8 15:12:13 PST 2021

Which examples can we hope to duplicate with CTF?


Starts with `eggs.csv` a file.

```python
>>> import csv
>>> with open('eggs.csv', newline='') as csvfile:
...     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
...     for row in spamreader:
...         print(', '.join(row))
Spam, Spam, Spam, Spam, Spam, Baked Beans
Spam, Lovely Spam, Wonderful Spam
```

`row` is a list of strings for each column.

Becomes:

Starting with a directory called `eggs`.


```python
>>> import ctf
>>> spamreader = ctf.reader("eggs", quotechar='|')
... for row in spamreader:
...     print(', '.join(row))
Spam, Spam, Spam, Spam, Spam, Baked Beans
Spam, Lovely Spam, Wonderful Spam
```

`quotechar` can be specified in the metadata (preferred), or it can be passed in directly.

Compatibility feature: `row` is the same kind of list of strings like `csv.reader` produces.

------------------------------------------------------------

Going beyond:

One column:

```python
>>> first_column = ctf.Ctf("eggs")["c1"]
... for v in first_column:
...     print(v)
Spam
Spam
```

------------------------------------------------------------

Original:

```python
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
```

Becomes:

Error when we try to write rows with different lengths.

If we specify what's missing it can work:

```python
with ctf.Ctf('eggs', quotechar='|', quoting=csv.QUOTE_MINIMAL) as spamwriter:
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', NULL, 'Wonderful Spam', NULL, NULL])

# alternatively:

spamwriter = ctf.Ctf('eggs', quotechar='|', quoting=csv.QUOTE_MINIMAL)
with spamwriter:
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', NULL, 'Wonderful Spam', NULL, NULL])
```

Both of these guarantee that data is written after the `with` block exits.

------------------------------------------------------------

Conversion:

Maybe, not so sure how this should work.

```python
ctf.convert('eggs.csv')
```

------------------------------------------------------------


```python
>>> import csv
>>> with open('names.csv', newline='') as csvfile:
...     reader = csv.DictReader(csvfile)
...     for row in reader:
...         print(row['first_name'], row['last_name'])
...
Eric Idle
John Cleese

>>> print(row)
{'first_name': 'John', 'last_name': 'Cleese'}
```

Becomes:


```python
>>> with Ctf.DictReader('names') as reader:
...     for row in reader:
...         print(row['first_name'], row['last_name'])
...
Eric Idle
John Cleese

>>> print(row)
{'first_name': 'John', 'last_name': 'Cleese'}
```

First principles: Code should be as readable as it can be.
Dictionaries use the column names, while lists use integer indexes.
`x["last_name"]` is much better than `x[1]`.


------------------------------------------------------------

```python
import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
```

------------------------------------------------------------

```python
import csv

with open('names.csv', 'w', newline='') as csvfile:
    has_header = csv.Sniffer().has_header(csvfile.read(1024))
```

Becomes:

```python
has_header = ctf.Sniffer().has_header('names.csv')
has_header = ctf.Sniffer().has_header('names')
if(has_header):
    print(ctf_file['first_name'])
else:
    print(ctf_file[1])
```

------------------------------------------------------------

Multiple column selection
```python
columns = [ctf_file['column1'], ctf_file['column2']]
for row in columns
    print(row)
> ['data1', 'data in column2']
```

```python
columns = ctf_file.columns('column1', 'column2')
for row in columns
    print(row['column1'])
> 'data1'
```

How pandas does this
```python
columns = ctf_file[['column1', 'column2']]
# columns will be a CTF object with only these two columns
# OR
# columns will be the same CTF object with an internal variable set for these columns
for row in columns
    print(row['column1'])
> 'data1'
```

```python
ctf_file = ctf.Ctf('country_codes', columns=['column1', 'column1'])
for row in ctf_file
    print(row['column1'] + row['column2'])
> 'data1data in column2'
```

# Make ctf[] return a ctf object always rather than a column object

Questions:
- Writing to ctf, if we are writing 30 rows to 10 different columns, should we write 10 lines into each file 30 times or write 1 value to each 30 times, then repeat 10 times. How do we handle crashes?
