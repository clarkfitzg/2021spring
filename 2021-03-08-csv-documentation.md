Mon Mar  8 15:12:13 PST 2021

Which examples can we hope to duplicate with CTF?


Starts with `eggs.csv` a file.

```
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


```
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

```
>>> first_column = ctf.Ctf("eggs")["c1"]
... for v in first_column:
...     print(v)
Spam
Spam
```

------------------------------------------------------------

Original:

```
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
```

Becomes:

Error when we try to write rows with different lengths.

If we specify what's missing it can work:

```
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

```
ctf.convert('eggs.csv')
```

------------------------------------------------------------


```
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


```
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

```
import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
```
