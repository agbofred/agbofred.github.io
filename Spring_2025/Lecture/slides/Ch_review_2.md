---
title: "Chapters 5,6,8-11 Review "
author: Fred Agbo
date: April 28, 2025
slideNumber: true
theme: "python_monokai"
highlightjs-theme: monokai
width: 1920
height: 1200
transition: slide
hash: true
history: false

---

## Announcements
- Project 5 is due today ***at 10:59pm***. 
- Schedules for __finals__:
	- 10:20 – 11:20 M/W/F -> ***Friday 2nd May (8:00am – 11am)***
	- 12:00 – 1:00 M/W/F -> ***Wednesday 7th May (2:00pm - 5pm)***
    	- Venue is this same hall
		- More about the final on Monday next week
   	- For those concerned, arrange with testing center ASAP & cc me
    - If possible, arrange to take the exam within that same week
- Polling [here](https://www.polleverywhere.com/agbofred203)

## Final Exam Arrengement
- Final exam last for 2 hours 
    - Will be partially open exam. Same rules as midterm 1 exams
    - Basically covers 
        - functions (program reading/tracing)
        - expressions and data representations
        - data structures: strings, lists, dictionary, tuple, reading and writing files
		- Asymptotic time complexity of algorithms
        - simple functions for interactive graphics. 
    - Go over the PS and Class Notes, Practice questions
	- Practice questions will be posted today on Canvas week 16 (did not cover all the topics!)
	- strongly recommend that you attend the session this week and ask questions where you're confused 
	- Do well to carefully ***read and follow all instruction***. 


<!--
## Announcements
- Project 5 is due on ***Wednesday 6th December***. 
- **Game Contest**, is due on __Friday 15th December__. ***NO EXTENSION***
- Final exam is **Next week Mondays 11th December** ***at 7:00 pm - 10 pm***
    - Venue is ***Ford Hall 102***, our usual lecture hall!
    - Last for 2 hours 
    - Will be open exam. Same rules as midterm exams applies
    - Will cover everyhting. Go over the PS and Class Notes
    - Practice questions will be posted before Wednesday (May not cover all)
    - For those concerned, arrange with testing center ASAP & cc me
    - Arrange to take the exam within that same week of Dec 11
- __Course Evaluation__: email from Kelley Strawn is sent to everyone
    - 15 minutes is reserved to fill out the form after exams
-->

## Understanding Check
::::cols
:::col
```python
def f(x,y):
	return x**2 + y

def g(z,n):
	x = 2
	for i in range(n):
		x += z(i,n)
	return x

print(g(f,2))
```
:::
:::col
What value will be printed to the screen when the code to the left is run?

:::::{.poll}
#. 2
#. 4
#. 7
#. This will give an error
:::::

:::
::::


## Ch-5: Summary of a Function Call & Scoping

:::{.incremental style='font-size:.8em'}
#. Evaluate the arguments in the context of the caller
#. Reserve space for the function in a new stack frame
#. Copy each positional argument to the corresponding parameter variable
#. Copy each keyword argument to the parameter with that name
#. For parameters with default values, if not already assigned, assign those values
#. Evaluate statements in the function body, using current stack frame to look up values of local variables
#. On encountering a `return`, compute the return value and substitute that value in place of the function call
#. Remove the stack frame
#. Return to the caller, continuing from just after the function call
:::


## Name Resolution and Scope
- When Python encounters a variable name in a program, it looks for where the variable was defined in an expanding search:
	1. **Local** - The local context is all the variables defined within the current function. This includes variables appearing as a parameter!
	2. **Enclosing** - The enclosing context consists of the names defined in a function enclosing the current one.
	3. **Global** - The global context consists of names defined outside of any function or imported into the current module.
	4. **Built-in** - The last place Python looks is in the names of any built-in functions, like `abs`, `str`, `print`, etc.
- The part of a program in which a name is defined in called its _scope_

## First Class Functions
- Functions in Python are treated as data values just like anything else!
	- We will need to take advantage of this to write listener functions.
- You can assign a function to a variable, pass it as a parameter, return it as a result, etc
- Functions treated like any other data value are called _first-class functions_
- To work with a function itself, you leave off the `()`. Including the parentheses is how you _call_ the function!

## CH-6:Interactive Example
:::{style='font-size:.9em'}
- Consider the simple program below, where we've imported the basics and some of our helper functions
  ```python
  def draw_dots():
      def click_action(event):
          c = create_filled_rect(
              event.get_x(), event.get_y(), 
              10,10, random_color())
          gw.add(c)
  
      gw = GWindow(500, 500)
      gw.add_event_listener("click", click_action)
  ```
- The `click_action` function specifies what to do when the mouse is clicked
	- Note that it has access to the `gw` variable since it is in the enclosing function and thus in the closure.
:::

## Registering a Listener
- The last line of our example function:

	```python
	gw.add_event_listener("click", click_action)
	```
	tells the graphics window (`gw`) to call the `click_action` function whenever a mouse "click" occurs within the window.
- When the user clicks the mouse, the graphics window, in essense, calls the client back to let them know that a click has occured. Thus, functions such as `click_action` are known as _callback functions_.
- The parameter `event` given to the callback function is a special data structure called a _mouse event_, which contains details about the specifics of the event that triggered the action.


## Types of Events

| Name | Description
---:|:-----
`"click"` | The user clicks the mouse in the window
`"dblclk"` | The user double-clicks the mouse in the window
`"mousedown"` | The user presses the mouse button down
`"mouseup"` | The user releases the mouse button
`"mousemove"` | The user moves the mouse
`"drag"` | The user moves the mouse with the button down


## More Graphics Object: Fillable Arcs
- The `GArc` class is a `GFillableObject`, and so you can call `.set_filled()` on a `GArc` object
- Filled like a pie-shaped wedge formed between the center of the bounding box and the starting and end points of the arc

::::::cols
::::col
```python
def filled_arc():
    gw = GWindow(400, 400)
    arc = GArc(50, 50, 
			   350, 350, 
			   90, 135)
    arc.set_color("orange")
    arc.set_filled(True)
    gw.add(arc)
```
::::

::::col
![](../images/FilledArc.png){width=50%}
::::
::::::

## The `GPolygon` class
- Used to represent graphical objects bounded by line segments
	- Polygons consist of several _vertices_ bounded by _edges_

![\ ](../images/GPolygons.svg)

- Location not fixed in upper left, but at some convenient reference point
- Often a convenient reference point is near the center of the object, but it doesn't need to be
- `GPolygon`s are `GFillableObject`s, so they can be filled


## Polygonal Construction
- The `GPolygon` function creates an **empty** polygon, to which you then can add vertexes
- Can create a vertex by calling `.add_vertex(x,y)` on the `GPolygon` object
	- `x` and `y` measured **relative to the reference point**
- Vertexes past the first can be defined in a few ways:
	- `.add_vertex(x,y)` adds another new vertex relative to the reference point
	- `.add_edge(dx,dy)` adds a new vertex relative to the preceding vertex
	- `.add_polar_edge(r, theta)` adds a new vertex relative to the previous using polar coordinates

## Ch-8: Arrays and Lists
- From the earliest days, programming languages have supported the idea of an _array_, or an ordered sequence of values.
- Individual values in an array are called _elements_, and the number of elements is the _length_ of the array.
- Each element's position in the array is given by its _index_, with index numbers starting at 0 and extending up to 1 less than the length of the array
- Python implements the array concept in a bit more general form called a _list_.

## Mutants
- The most important difference between strings and lists is one of _mutability_
	- Strings we have already identified as being _immutable_: you can not change the individual elements
	- Lists, in contrast, are _mutable_, which means that we **can** change or assign new values to the elements of a list
- Immutable objects have many advantages in programming:
	- You don't have to worry about if the values will change
	- Immutable values can be more easily shared
	- Immutable objects are easier to use with concurrent programs
- In some situations though, mutable objects are the perfect tool for the job

## For Reference
- When working with mutable objects, it is better to think of the variable as holding a _reference_ to the object, rather than the actual contents of the object
- I find it useful to think of a reference as the "address" in memory where that object's contents can be found
- This undeniably complicates things, as referencing a mutable object lets you change it, which will immediately be reflected in anything _else_ that referenced that object
- Mutable objects can be terrific to work with, as their mutability makes them very flexible, but be wary of unexpected behavior


## Lists as Arguments
- When you pass a list as an argument to a function or return a list as a result, only the **reference** to the list is actually passed back and forth
- This means that the elements of the list are effectively shared between the function and the caller
	- Changes that the function makes to the elements **will** persist after the function returns
- Example of reversing a list in PythonTutor: [here](http://www.pythontutor.com/visualize.html#code=def%20reverse_in_place%28array%29%3A%0A%20%20%20%20for%20lh%20in%20range%28len%28array%29//2%29%3A%0A%20%20%20%20%20%20%20%20rh%20%3D%20len%28array%29%20-%20lh%20-%201%0A%20%20%20%20%20%20%20%20array%5Blh%5D,%20array%5Brh%5D%20%3D%20array%5Brh%5D,%20array%5Blh%5D%0A%0Aarray%20%3D%20%5B0,%201,%202,%203,%204,%205,%206,%207,%208,%209%5D%0Aprint%28f%22Forward%3A%20%7Barray%7D%22%29%0Areverse_in_place%28array%29%0Aprint%28f%22Reverse%3A%20%7Barray%7D%22%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

## Cloning
- What can we do in these sorts of instances to not let mutability trip us up?
- _Clone_ the list instead of just assigning a reference
	- Creates a **new** object in memory
- Several ways you can make a shallow clone (in code)
	- Using the `.copy()` list method
	- Any slice always returns a new object
	- Using the `list()` function will return a new object

## Common Useful List Methods

Method | Description
---- | ------
`list.copy()` | Returns a new list whose elements are the same as the original
`list.append(value)` | Adds `value` to the end of the list
`list.insert(idx, val)` | Inserts `val` before the specified `idx`
`list.remove(value)` | Removes the first instance of `value` from the list, or errors
`list.reverse()` | Reverses the order of the elements in the list
`list.sort()` | Sorts the elements of the list. Can take an optional argument `key` to specify how to sort

##  Lists Comprehension
- The simplest list comprehension syntax is:
	
	```python
	[ expression iterator ]
	```
	where `expression` is any Python expression and `iterator` is a `for` loop header
- The iterator component can be followed by any number of additional modifiers
	- More `for` loop headers for nested loops
	- or `if` statements to select specific values
- Example: all even numbers to 20 not also visible by 3

	```python
	[i for i in range(0,20,2) if i % 3 != 0]
	```

## Multidimensional Arrays
- We know that elements of a list can be lists in and of themselves. If the lengths of all the lists making up the elements of a list remain fixed, then the list of lists is called a _multidimensional array_
- In Python, we can create multidimensional arrays just by creating lists of constant length as the elements to another list
  ```python
  magic = [ [2, 9, 4], [7, 5, 3], [6, 1, 8] ]
  ```
- We can always get the individual element of one of the inner lists by using **2** indices.
	- `magic[1][1] = 5`
	- `magic[-1][0] = 6`


## Picturing Multidimensional Arrays
- Multidimensional arrays are commonly pictured as each inner list being stacked beneath the previous
- In such a representation, the outermost/first elements/indices represent the row, and the inner/second elements/indices represent the column

`[ [2, 9, 4], [7, 5, 3], [6, 1, 8] ]`{style="display: block; margin: auto; text-align: center;"}

<br>

\begin{tikzpicture}%%width=80%
[
block/.style = {draw, MGreen, outer sep=0pt, font=\Large, minimum size=1cm},
]
\node[block](00) at (0,0) {2};
\node[block,below=0 of 00](10) {7};
\node[block,below=0 of 10](20) {6};

\node[block,right=0 of 00](01) {9};
\node[block,right=0 of 10](11) {5};
\node[block,right=0 of 20](21) {1};

\node[block,right=0 of 01](02) {4};
\node[block,right=0 of 11](12) {3};
\node[block,right=0 of 21](22) {8};


\node[block,color=MBlue,font=\tt,](00) at (5,0) {magic[0][0]};
\node[block,color=MBlue,font=\tt,below=0 of 00](10) {magic[1][0]};
\node[block,color=MBlue,font=\tt,below=0 of 10](20) {magic[2][0]};

\node[block,color=MBlue,font=\tt,right=0 of 00](01) {magic[0][1]};
\node[block,color=MBlue,font=\tt,right=0 of 10](11) {magic[1][1]};
\node[block,color=MBlue,font=\tt,right=0 of 20](21) {magic[2][1]};

\node[block,color=MBlue,font=\tt,right=0 of 01](02) {magic[0][2]};
\node[block,color=MBlue,font=\tt,right=0 of 11](12) {magic[1][2]};
\node[block,color=MBlue,font=\tt,right=0 of 21](22) {magic[2][2]};
\end{tikzpicture} 

## Reading
- Programs often need to work with collections of data that are too large to reasonably exist typed all out in the code
	- Easier to read in the values of a list from some external data file
- A _file_ is the generic name for any named collection of data maintained on some permanent storage media attached to a computer
- Files can contain information encoded in many different ways
	- Most common is the _text file_
	- Contains character data like you'd find in a string


## Strings vs Text Files
- While strings and text files both store characters, there are some important differences:
	- **The longevity of the data stored**
		- The value of a string variable lasts only as long as the string exists, is not overridden, or is not thrown out when a function completes
		- Information in a text file exists until the file is deleted
	- **How data is read in**
		- You have access to all the characters in a string variable pretty much immediately
		- Data from text files is generally read in sequentially, starting from the beginning and proceeding until the end of the file is reached

## Reading Text Files
- The general approach for reading a text file is to first _open_ the file and associate that file with a variable, commonly called its _file handle_
- We will also use the _with_ keyword to ensure that Python cleans up after itself (closes the file) when we are done with it (Many of us could use a `with` irl)
  ```python
  with open(filename) as file_handle:
  	# Code to read the file using the file_handle
  ```
- Python gives you several ways to actually read in the data
	- `read` reads the entire file in as a string
	- `readline` or `readlines` reads a single line or lines from the file
	- `read` alongside `splitlines` gets you a list of line strings
	- Can use the file handle as an iterator to loop over

## Entire file ⟶ String
- The `read` method reads the entire file into a string, with includes newline characters (`\n`) to mark the end of lines
- Simple, but can be cumbersome to work with the newline characters, and, for large files, it can take a large amount of memory

- As an example, the file:<br><br>

  :::{.block name="Seuss.txt" style='width:40%; margin-left: auto; margin-right: auto;'}
	One fish<br>
	two fish<br>
	red fish<br>
	blue fish
  :::

  would get read as

`"One fish\ntwo fish\nred fish\nblue fish"`{style="display: block; margin: auto; text-align: center;"}

## Line by Line
- Of the ways to read the file in a string at a time, using the file handler as an iterator and looping is probably best and certainly most flexible
- Leads to code that looks like:
  ```python
  with open(filename) as f:
	  for line in f:
		  # Do something with the line
  ```
- Note that **most** strategies preserve the newline character, which you very likely do not want, so be ready to strip them out before doing more processing


## Powers Combined
- So long as your files are not gigantic, using `read` and then the `splitlines` method can be a good option
- This **does** remove the newline characters, since it splits the string at them
  ```python
  with open(filename) as f:
	  lines = f.read().splitlines()
  # Then you can do whatever you want with the list of lines
  ```

<!-- This section below is chapter 10-12 which was copied from the Review #3 slides in the previous year -->


## CH-10: Tuple
- In Python, the simplest strategy for representing a record uses the built-in type _tuple_
	- Comes from terms like _quintuple_ or _sextuple_, that denote fixed-size collections
- An ordered, **immutable** sequence of values
- Feel similar to lists, except immutable, and thus used very differently
	- Think of tuples as records 
- Created by enclosing a collection of elements in parentheses
`employee = ("Bob Cratchit", "clerk", 15)`{.inlinecode}
- Stored internally similarly to a list, so each element has a corresponding index

## Tuple Usage
- Can largely envision tuples as sitting between strings and lists
	- Immutable, like strings
	- Elements can be _anything_, like lists
- Common operations mimic that of strings
	- Can concatenate with addition
	- Can duplicate by multiplying by an integer
	- Can index and slice them
	- Can loop over them directly or via index
- A tuple of a single value **needs** a comma at the end in order to be a tuple
- Be sure you are concatenating objects of the same type (Tuble `+` Tuble)


## Tuple Selection
- You can select or slice elements from a tuple just like you can with lists
	- Unfortunately, records are not usually ordered in a particular way. Rather, it is the field name that is usually important
- If using tuples, you can make programs more readable by using a _destructuring assignment_, which breaks a tuple into named components:

  ```python
  employee = ("Bob Cratchit", "clerk", 15)
  name, title, salary = employee
  ```


## Pointy Tuples!
::::::{.cols style='align-items:center'}
::::col
- One of the most simple examples of tuple usage would be storing location information in 2d space
- By storing both $x$ and $y$ coordinates in a tuple, it makes that information easier to store and pass around your program
- When you need to use the points, best to destructure:
  ```python
  x,y = pt
  ```
::::

::::col

\begin{tikzpicture}%%width=80%
\draw[very thick, MGreen] (0,0) rectangle + (5,5);
\node[circle, fill=MRed, label={[MRed]below right: ($x_1$,$y_1$)}, minimum size=5pt, inner sep=0pt] at (3,4) {};
\node[circle, fill=MBlue, label={[MBlue]below right: ($x_2$,$y_2$)}, minimum size=5pt, inner sep=0pt] at (2,1) {};
\end{tikzpicture}

::::
::::::

## Returning Tuples
- Tuples give us a convenient way to return multiple objects from a function
  - `return x, y` is the same as `return (x,y)`
- Several Python built-in functions return tuples, of which a few are particularly useful
	- `enumerate`
	- `zip`

## Enumerating
- We have multiple ways to iterate through a string or list:
	- By element:
	
	  ```python
	  for ch in string:
		  # body of loop using ch
	  ```

	- By index:
	
	  ```python
	  for i in range(len(string)):
		  # body of loop using i
	  ```
- Using `enumerate` lets us get both!
  ```python
  for i, ch in enumerate(string):
      # body of loop using both ch and i
  ```

## Zipping
- Sometimes you have multiple lists that you want to loop over in a "synced" fashion
- The `zip` function iterates through tuples of pairs of elements
- For example
  ```python
  zip([1,2,3], ["one", "two", "three"])
  ```
  would yield `(1, "one")`, then `(2, "two")`, and then `(3, "three")`
- Can unpack or destructure as part of a `for` loop:
  ```python
  for x,y in zip([1,2,3],[4,5,6]):
	  # body of loop using paired x and y
  ```


## Classes vs Objects
- When we introduced PGL early in the semester, we stressed the difference between types/classes and objects
	- A _class_ is the pattern or template that defines the structure and behavior of values with that particular type (the species of ant)
	- An _object_ is an individual value that belongs to a class (an individual ant)
		- A single class can be used to create any number of objects, each of which is said to be an _instance_ of that class
- PGL defines the `GRect` class.
	- In Breakout, you used that class to create **many** different rectangles, each of which was an instance of the `GRect` class


## Thinking about Objects
![\ ](../images/Interface2.svg)

## An Object's Purpose
- Python uses the concepts of objects and classes to achieve at least three different goals:
	- __Aggregation__. Objects make it possible to represent collections of independent data as a single unit. Such collections are traditionally called _records_.
	- __Encapsulation__. Classes make it possible to store data together with the operations that manipulate that data.
		- In Python the data values are called _attributes_ and the operations are called _methods_
	- __Inheritance__. Class hierarchies make it possible for a class that shares some attributes and methods with a previously defined class to _inherit_ those definitions without rewriting them all
- We'll introduce many of these concepts in this course, but for more exposure and practice you'll want to take CS 152 (Data Structures)

## Classes as Templates
- Since they share the same attributes, it is natural to regard the two employees at Scrooge and Marley as two instances of the same class
- Could view the class as a template or empty form:
\begin{tikzpicture}%%width=40%
[record/.style={draw, minimum width=4cm, font=\tt},
lab/.style={font=\tt\small, anchor=south west},
]
\node[record, MBlue](n) at (0,0) {};
\node[lab, MBlue](nl) at (n.north west) {name};
\node[record, MBlue, below=.75cm of n](t){};
\node[lab, MBlue] at (t.north west) {title};
\node[record, MBlue, below=.75cm of t](s) {};
\node[lab, MBlue] at (s.north west) {salary};
\node[fit=(nl)(s), draw, very thick, MBlue] {};
\end{tikzpicture}

- Can help initially to just start with an empty template and then fill in the necessary fields

## Starting Empty
- Class definitions in Python start with a header line consisting of the keyword `class` and then the class name
- The body of the class will later contain definitions, but initially can just leave blank
	- Almost. Python does not allow an empty body, so need to include a docstring or use the `pass` keyword
  ```python
  class Employee:
  	"""This class is currently empty!"""
  ```
- Once the class is defined, you can create an object of this class type by calling the class as if it were a function:
  ```python
  clerk = Employee()
  ```

## More References
- Instances of custom Python classes are mutable
- Thus custom class instances are stored as _references_ to that information in memory
- Any code with access to this reference can manipulate the object
	- Can get or set the contents of any attributes or create new ones
<br><br>

![Objects are references!](../images/ObjectRepresentations.png)


## Selecting Object Attributes
- You can select an attribute from an object by writing out the object name, followed by a dot and then the attribute name.
	- As an example

		```python
		clerk.name
		```
		would select the `name` attribute for the `clerk` object
- Attributes are assignable, so

	```python
	clerk.salary *= 2
	```
	would double the clerk's current salary

- You can create a new attribute in Python by simply assigning a name and a value, just like you'd define a new variable


## Constructors
- While the previous method works, it is not ideal
	- Forces the client to tinker with the internal workings of the Employee
	- Details of the data structure are the property of the implementation, not the client
- Better to add a method to the `Employee` class called a _constructor_, which is responsible for initializing attributes to a newly created object
	- In Python, a constructor is created by defining a special function named `__init__`
	- The constructor function is called automatically whenever a new object of that type is created


## Know Thy `self`
:::incremental
- Moving the function into the Employee class has a problem:
	- When we set attributes, they are specific to a given object
	- The class itself though is just a template, and not linked to a specific object
- We need a general way within the class to refer to whatever object is being created
	- The overwhelming convention in Python is to call this variable `self`
	- Whenever a new object is created, you could imagine that, for that object, Python replaces all of the `self`s in the class with that object's name
		- This isn't quite the order of what is happening, but it can help envision what `self` is doing
- `self` is always the first parameter to the `__init__` constructor
	- Any other arguments provided are passed in as additional parameters afterwards
:::

## An Employee Constructor
```python
class Employee:
	def __init__(self, name, title, salary):
		self.name = name
		self.title = title
		self.salary = salary


clerk = Employee('Bob Cratchit', 'clerk', 15)
```
- Note that you do not need to provide an argument for `self` when creating the object, Python supplies this reference automatically
- Viewing in PythonTutor can be helpful, as is shown [here](https://pythontutor.com/render.html#code=class%20Employee%3A%0A%20%20%20%20def%20__init__%28self,%20name,%20title,%20salary%29%3A%0A%20%20%20%20%20%20%20%20self.name%20%3D%20name%0A%20%20%20%20%20%20%20%20self.title%20%3D%20title%0A%20%20%20%20%20%20%20%20self.salary%20%3D%20salary%0A%0A%0Aclerk%20%3D%20Employee%28'Bob%20Cratchit',%20'clerk',%2015%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


## Methods
- Most classes define additional functions called methods to allow clients to read or update attributes or manipulate the object
- Methods look like a normal function definition but will **always** declare the parameter `self` at the beginning of the parameter list
	- This is true even if the method has no other parameters
- Methods are defined in the body of the class and would thus look something like:
  ```python
  def method_name (self, other_parameters):
  	...body of the method...
  ```
- For example
  ```python
  def give_raise(self, amount):
  	self.salary += amount
  ```

## Accessing and Using Methods
- After definition, there are two mains ways you can access and use the method:
	- **Dot Notation (Conventional)**
		- Python sets `self` to be a reference to the _receiver_, which is the object to which the method is applied

		  ```python
		  clerk = Employee('Bob', 'clerk', 15)
		  clerk.give_raise(15)
		  ```

	- **Function Notation**
		- You retrieve the method from the class itself, and then provide self manually

		  ```python
		  clerk = Employee('Bob', 'clerk', 15)
		  Employee.give_raise(clerk, 15)
		  ```

## Getters and Setters
- In the object-oriented model, the client is not supposed to muck-about with the object internals
- The implementation should therefore provide methods to retrieve desired attributes (called _getters_) or to make changes to desired attributes (called _setters_)
- Setting up getters and setters for the attribute `salary` might look like:
  ```python
  def get_salary(self):
  	return self.salary
  
  def set_salary(self, new_salary):
  	self.salary = new_salary
  ```
- Getters are far more common than setters, as you don't always want the client to have the freedom to change attributes on a whim


## Maps and Dictionaries
- A common form of information associates pairs of data values
	- Commonly called a _map_ in computer science
	- Python calls such a structure a _dictionary_
- A dictionary associates two different values:
	- A simple value called the _key_, which is often a string but doesn't need to be
	- A larger and more complex object called the _value_
- This idea of associating pairs of values is exhibited all over in the real world
	- Actual dictionaries! The words are the keys, the definitions the values.
	- Web addresses! Keys are the urls, the values are the webpage contents.

## Creating Dictionaries
- Python dictionaries use squiggly brackets `{}` to enclose their contents
- Can create an empty dictionary by providing no key-value pairs:
  ```python
  empty_dict = {}
  ```
- If creating a dictionary with key-value pairs
	- Keys are separated from values with a colon `:`
	- Pairs are separated by a comma `,`
  ```python
  generic_dict = {'Bob': 21, 0: False, 13: 'Thirteen'}
  ```

## Keys and Values
- The value of a key-value pair can be **any** Python object, mutable or immutable
	- This include other dictionaries!
- The key is more restricted:
	- Must be immutable
		- So dictionaries or lists can **not** work as a key
		- Tuples can though!
	- Must be unique per dictionary



## Selection
- The fundamental operation on dictionaries is selection, which is still indicated with square brackets: `[]`
- Dictionaries though are **unordered**, so it is not a numeric index that goes inside the `[ ]`
- You instead use the key directly to select corresponding values:
  ```python-repl
  >>> A = {'Jack': 12, 'Jill': 17}['Jack']
  >>> print(A)
  12
  >>> B = {True: 13, 0: 'Why?'}[0]
  >>> print(B)
  Why?
  ```

## Losing your keys
- If you attempt to index out a key that doesn't exist:
  ```{.python .badcode}
  A = {'Jack': 12, 'Jill': 13}
  print(A['Jil'])
  ```
  you will get an error!
- If in doubt, check for the presence of a key with the `in` operator:
  ```python
  if 'Jil' in A:
	  print(A['Jil'])
  ```

## Rewriting the Dictionary
- Dictionaries are _mutable_!
	- We can add new key-value pairs
	- We can change the value of corresponding keys
```python-repl
>>> d = {}
>>> d['A'] = 10
>>> d['B'] = 12
>>> print(d)
{'A':10, 'B':12}
>>> d['A'] = d['B']
>>> print(d)
{'A':12, 'B':12}
```


## Iterating through a Dictionary
- Frequently we might want to iterate through a dictionary, checking either its values or its keys
- Python supports iteration with the `for` statement, which has the form of:
  ```python
  for key in dictionary:
  	  value = dictionary[key]
  	  code to work with that key and value
  ```
- You can also use the `.items` method to grab both key and values together:
	- Returns a tuple with both the key and corresponding pair
  ```python
  for key, value in dictionary.items():
  	  code to work with that key and value
  ```

## Common Dictionary Methods

Method call | Description
---|-----
`len(dict)`{.python} | Returns the number of key-value pairs in the dictionary
`dict.get(key, value)`{.python} | Returns the value associated with the `key` in the dictionary. If the key is not found, returns the specified value, which is `None` by default
`dict.pop(key)`{.python} | Removes the key-value pair corresponding to `key` and returns the associated value. Will raise an error if the key is not found.
`dict.clear()`{.python} | Removes all key-value pairs from the dictionary, leaving it empty.
`dict.items()`{.python} | Returns an iterable object that cycles through the successive tuples consisting of a key-value pair.


## Dictionary Records
- While most commonly used to indicate mappings, dictionaries have seen increased use of late as structures to store records
- Looks surprisingly close to our original template of:
  ```python
  boss = {
	  'name': 'Scrooge',
	  'title': 'founder',
	  'salary': 1000
	  }
  ```
- Allows easy access of attributes without worrying about ordering
  ```python
  print(boss['name'])
  ```

## Compound Structure Storage
- Structures representing complicated data can often be large enough that you don't want to store them within your program itself
- We can put them in their own file, but reading them in with our current tools would be complicated
	- Current methods read in text, so we would need to _parse_ the text to identify what data structures we needed to create and what elements we needed to add
	- This is certainly possible, but potentially more overhead than what we would like for some structures
- Useful then to store the data structure in file in such a format that it can be easily read into Python

## File I/O
- A variety of ways this can be done
	- XML, YAML, JSON
- JSON is particularly interesting to us, because its syntax almost exactly matches Python's (even though it was made for Javascript)
- Python has a built-in library to read and write JSON files, just called `json`
	- `json.load(file_handle)`
		- Loads the JSON data structure from the specified file into its Python equivalent
	- `json.dump(data_object, file_handle)`
		- Writes a JSON text representation of the data object to the given file
	- Both methods are used inside our normal `with open() as fhandle:` syntax

## Using JSON
- To read a JSON file into a variable `data`:
  ```python
  import json
  with open('file.json') as fh:
	  data = json.load(fh)
  ```
- To write a variable with complex structure out to a JSON file:
  ```python
  import json
  with open('file.json', 'w') as fh:
  	  json.dump(data, fh)
  ```

