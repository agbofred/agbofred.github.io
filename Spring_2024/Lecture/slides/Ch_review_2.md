---
title: "Chapters 4-6,8 Review "
author: Fred Agbo
date: December 4, 2023
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


## CH-4: The Portable Graphics Library
- Built atop Tkinter
- The library (`pgl.py`) is available on the Canvas website [here](https://willamette.instructure.com/courses/3703/modules/items/160252)
	- Put it in the same folder as your code, and then you can import it
- Operates on the idea of a collage or cork-board

![Test](../images/CorkBoard.svg)

- Note that newer objects can obscure older objects. This layering arrangement is called the _stacking order_.
- The window (or felt-board/cork-board)
	- Created with the `GWindow` function
	- Takes two arguments: a width and a height in pixels

## Other Simple Objects
Functions to create simple geometric objects:
<br>

- Rectangles!
	- `GRect( x, y, width, height )`
	- Creates a rectangle whose upper left corner is at (x,y) of the specified size
- Circles/Ovals!
	- `GOval( x, y, width, height )`
	- Creates an oval that fits inside the rectangle with the same dimensions
	- Placement based on the upper left corner of that enclosing rectangle
- Lines!
	- `GLine( x1, y1, x2, y2 )`
	- Creates a line extending from (x1, y1) to (x2, y2)

## The `GObject` Hierarchy
- The types of graphical objects form a hierarchy:

![](../images/GObject_Hierarchy.svg)

- The `GObject` class represents the collection of all graphical objects
- The `GFillableObject` class represents those that have a fillable interior

## Interacting with the `GWindow`
- We've already shown creation:

```python
gw = GWindow(width, height)
```
- You have several more operations that you can apply to the `GWindow` object:

-------------------------------------- -------------------------------------
       `gw.add(object)`{.no-highlight} Adds an object to the window
 `gw.add(object, x, y)`{.no-highlight} Adds an object to the window after moving it to (x,y)
    `gw.remove(object)`{.no-highlight} Removes an object from the window
       `gw.get_width()`{.no-highlight} Returns the width of the graphics window in pixels
      `gw.get_height()`{.no-highlight} Returns the height of the graphics window in pixels
-------------------------------------- -------------------------------------


## Interacting with `GObject`s
- The following operations apply to all GObjects,  where `object`{.no-highlight} is the name of any specific instance.

---------------------------------------- ----------------------------
         `object.get_x()`{.no-highlight} Returns the x coordinate of this object
         `object.get_y()`{.no-highlight} Returns the y coordinate of this object
     `object.get_width()`{.no-highlight} Returns the width of this object
    `object.get_height()`{.no-highlight} Returns the height of this object
`object.set_color(color)`{.no-highlight} Sets the color of the object to the specified color
---------------------------------------- ----------------------------

- All coordinates and distances are measured in pixels


## Interacting with `GFillableObject`s
- Fillable GObjects have a smaller subset of commands that also apply to them.
- Initially the only fillable objects available to you are rectangles and ovals

--------------------------------------------- ----------------------------
     `object.set_filled(bool)`{.no-highlight} Sets the fill state of the object
`object.set_fill_color(color)`{.no-highlight} Sets the color to be used to fill the interior, otherwise same as the outer line
     `object.get_fill_color()`{.no-highlight} Gets the current color used to display the object interior
          `object.is_filled()`{.no-highlight} Returns True or False depending on whether the object is currently filled
--------------------------------------------- ----------------------------

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

## Midterm 1 review
