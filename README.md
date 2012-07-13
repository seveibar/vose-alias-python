This python library implements Vose's Alias Method as described here http://www.keithschwarz.com/darts-dice-coins/ . This algorithm can be used to efficiently find weighted random data ex. rolling a weighted die.

### Usage

```python
import vose

plist = [
    ("A",25),
    ("B",65),
    ("C",10)
]

vose_object = vose.Vose(plist)

print vose_object.get()
```

or a more obvious example...

```python

import vose

v = vose.Vose([('a',25),('b',65),('c',10)])

accuracy = 10000 #increase for better results
d = {'a':0,'b':0,'c':0}
for i in range(accuracy):
    d[v.get()] += 1./accuracy
print "\n".join([v + " : " + str(round(k*1000)/1000.) for v,k in d.items()])

```

It should print out values close to your entered ones
