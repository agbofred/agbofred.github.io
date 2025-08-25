Define a recursive function `removeAll` that expects an item and a Lisp-like list as arguments. This function returns a Lisp-like list with all of the instances of the item removed. (Hint: Keep on removing the item if it equals the list’s first item.)

Here is an example of its use: 

```
>>> from lisplist import *
>>> lyst = cons(2, cons(2, (cons 3, THE_EMPTY_LIST)))
>>> lyst
(2 2 3)
>>> removeAll(2, lyst)
(3)
>>> removeAll(3, lyst)
(2 2)
```
