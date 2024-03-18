---
title: "Definitely Not Photoshop"
author: Jed Rembold & Fred Agbo
date: April 1, 2024
slideNumber: true
theme: "python_monokai"
highlightjs-theme: monokai
width: 1920
height: 1200
transition: slide
hash: true
history: false

---

# Announcements


- PS 5 feedback not ready yet. Apologies!
- Exam 2 on Friday! 
    - Learning Objectives posted
    - Practice Exam 1 &amp; 2 posted with their solutions
- We will post the Enigma project by Friday 
    - Not due until Nov 21

## Maps and Dictionaries

- A common form of information associates pairs of data values 
    - Commonly called a *map* in computer science
    - Python calls such a structure a *dictionary*
- A dictionary associates two different values: 
    - A simple value called the *key*, which is often a string but doesn’t need to be
    - A larger and more complex object called the *value*
- This idea of associating pairs of values is exhibited all over in the real world 
    - Actual dictionaries! The words are the keys, the definitions the values.
    - Web addresses! Keys are the urls, the values are the webpage contents.

## Creating Dictionaries

- Python dictionaries use squiggly brackets `{}` to enclose their contents
- Can create an empty dictionary by providing no key-value pairs:
    
    ```
    empty_dict = {}
    ```
- If creating a dictionary with key-value pairs
    
    
    - Keys are separated from values with a colon `:`
    - Pairs are separated by a comma `,`
    
    ```
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

```
A = {True: 'Seth', False: 'Jesse'}
B = {'Jill': 13, 'Jack': 12}
C = {(1,2): {'x': 1}}
```

```
#X = {{'x': 1, 'y': 2}: 'Shark'}
Y = {[1,3,5]: 'Odd'}
Z = {'A': 13, 'B': 24, 'A': 15}
```

## Selection


- The fundamental operation on dictionaries is selection, which is still indicated with square brackets: `[]`
- Dictionaries though are **unordered**, so it is not a numeric index that goes inside the `[ ]`
- You instead use the key directly to select corresponding values:
    
    ```
    >>> A = {'Jack': 12, 'Jill': 13}['Jack']
    >>> print(A)
    13
    >>> B = {True: 13, 0: 'Why?'}[0]
    >>> print(B)
    Why?
    ```

## Losing your keys

- If you attempt to index out a key that doesn’t exist:
    
    ```
    A = {'Jack': 12, 'Jill': 13}
    print(A['Jil'])
    ```
    
    you will get an error!
- If in doubt, check for the presence of a key with the `in` operator:
    
    ```
    if 'Jil' in A:
        print(A['Jil'])
    ```

## Rewriting the Dictionary

- Dictionaries are *mutable*! 
    - We can add new key-value pairs
    - We can change the value of corresponding keys
    
    ```
    >>> d = {}
    >>> d['A'] = 10
    >>> d['B'] = 12
    >>> print(d)
    {'A':10, 'B':12}
    >>> d['A'] = d['B']
    >>> print(d)
    {'A':12, 'B':12}
    ```

## Grade Sheet Example

- Suppose we had a file of student ids and accompanying scores that we wanted to read into a dictionary and then access.
    
    ```
    def read_to_dict(filename):
        dictionary = {}
        with open(filename) as f:
            for line in f:
                ID, score = line.strip().split(',')
                dictionary[ID] = score
        return dictionary
    
    def get_student_score():
        scores = read_to_dict('SampleGrades.txt')
        done = False
        while not done:
            student_id = input('Enter a student id number: ')
            if student_id == "":
                done = True
            else:
                if student_id in scores:
                    print(f"Student got a {scores[student_id]}.")
                else:
                    print(f"Student id {student_id} was not found in classlist")
    ```

## Understanding Check

What is the printed value of the below code?

```
A = [
    {'name': 'Jill',  'weight':125, 'height':62},
    {'name': 'Sam',   'height':68},
    {'name': 'Bobby', 'height':72},
]
A.append({'weight':204, 'height':70, 'name':'Jim'})
B= A[1]
B['weight'] = 167
print([d['weight'] for d in A if 'weight' in d])
```

1. `[100,204]`
2. `[156,173,204]`

1. `[100,167,173,204]`
2. `[125,167,204]`

## Iterating through a Dictionary

- Frequently we might want to iterate through a dictionary, checking either its values or its keys
- Python supports iteration with the `for` statement, which has the form of:
    
    ```
    for key in dictionary:
        value = dictionary[key]
        code to work with that key and value
    ```
- You can also use the `.items` method to grab both key and values together:
    
    
    - Returns a tuple with both the key and corresponding pair
    
    ```
    for key, value in dictionary.items():
        code to work with that key and value
    ```

## Finding Students by grade

```
def get_students_with_score():
    scores = read_to_dict('SampleGrades.txt')
    done = False
    while not done:
        des_grade = input('Enter a letter grade: ')
        if des_grade == "":
            done = True
        else:
            for st_id, grade in scores.items():
                if grade == des_grade.strip().upper():
                    print(f"{st_id} got a {grade}")
```
<!--
## Common Dictionary Methods

Method callDescription`len(dict)`Returns the number of key-value pairs in the dictionary`dict.get(key, value)`Returns the value associated with the `key` in the dictionary. If the key is not found, returns the specified value, which is `None` by default`dict.pop(key)`Removes the key-value pair corresponding to `key` and returns the associated value. Will raise an error if the key is not found.`dict.clear()`Removes all key-value pairs from the dictionary, leaving it empty.`dict.items()`Returns an iterable object that cycles through the successive tuples consisting of a key-value pair.

Dictionary Records
------------------

- While most commonly used to indicate mappings, dictionaries have seen increased use of late as structures to store records
- Looks surprisingly close to our original template of:
    
    ```
    boss = {
        'name': 'Scrooge',
        'title': 'founder',
        'salary': 1000
        }
    ```
- Allows easy access of attributes without worrying about ordering
    
    ```
    print(boss['name'])
    ```

    // reveal.js plugins         

      // Full list of configuration options available at:
      // https://revealjs.com/config/
      Reveal.initialize({
		//autoAnimateEasing: 'ease-in',
		//autoAnimateDuration: 1.0,
		//autoAnimateUnmatched: false,
        pdfSeparateFragments: false,
        // Display controls in the bottom right corner
        controls: true,
        // Help the user learn the controls by providing hints, for example by
        // bouncing the down arrow when they first encounter a vertical slide
        controlsTutorial: true,
        // Determines where controls appear, "edges" or "bottom-right"
        controlsLayout: 'bottom-right',
        // Visibility rule for backwards navigation arrows; "faded", "hidden"
        // or "visible"
        controlsBackArrows: 'faded',
        // Display a presentation progress bar
        progress: true,
        // Display the page number of the current slide
        slideNumber: true,
        // Add the current slide number to the URL hash so that reloading the
        // page/copying the URL will return you to the same slide
        hash: true,
        // Push each slide change to the browser history
        history: false,
        // Enable keyboard shortcuts for navigation
        keyboard: true,
        // Enable the slide overview mode
        overview: true,
        // Vertical centering of slides
        center: false,
        // Enables touch navigation on devices with touch input
        touch: true,
        // see https://revealjs.com/vertical-slides/#navigation-mode
        navigationMode: 'default',
        // Turns fragments on and off globally
        fragments: true,
        // Flags whether to include the current fragment in the URL,
        // so that reloading brings you to the same fragment position
        fragmentInURL: true,
        // Flags if we should show a help overlay when the questionmark
        // key is pressed
        help: true,
        // Global override for autoplaying embedded media (video/audio/iframe)
        // - null: Media will only autoplay if data-autoplay is present
        // - true: All media will autoplay, regardless of individual setting
        // - false: No media will autoplay, regardless of individual setting
        autoPlayMedia: null,
        // Global override for preloading lazy-loaded iframes
        // - null: Iframes with data-src AND data-preload will be loaded when within
        //   the viewDistance, iframes with only data-src will be loaded when visible
        // - true: All iframes with data-src will be loaded when within the viewDistance
        // - false: All iframes with data-src will be loaded only when visible
        preloadIframes: null,
        // Number of milliseconds between automatically proceeding to the
        // next slide, disabled when set to 0, this value can be overwritten
        // by using a data-autoslide attribute on your slides
        autoSlide: 0,
        // Stop auto-sliding after user input
        autoSlideStoppable: true,
        // Use this method for navigation when auto-sliding
        autoSlideMethod: null,
        // Specify the average time in seconds that you think you will spend
        // presenting each slide. This is used to show a pacing timer in the
        // speaker view
        defaultTiming: null,
        // Hide cursor if inactive
        hideInactiveCursor: true,
        // Time before the cursor is hidden (in ms)
        hideCursorTime: 5000,
        // Transition style
        transition: 'slide', // none/fade/slide/convex/concave/zoom
        // Transition speed
        transitionSpeed: 'default', // default/fast/slow
        // Transition style for full page slide backgrounds
        backgroundTransition: 'fade', // none/fade/slide/convex/concave/zoom
        // Number of slides away from the current that are visible
        viewDistance: 3,
        // Number of slides away from the current that are visible on mobile
        // devices. It is advisable to set this to a lower number than
        // viewDistance in order to save resources.
        mobileViewDistance: 2,
        // The "normal" size of the presentation, aspect ratio will be preserved
        // when the presentation is scaled to fit different resolutions. Can be
        // specified using percentage units.
        width: 1920,
        height: 1200,
        // The display mode that will be used to show slides
        display: 'block',
		math: {
		  
		  
		  
			
			
			
			
			
			
			
			
			
			
		  
		  CommonHTML: {scale: 80},
		},
	reveald3: {
			runLastState: true, // true/false, default: true
			onSlideChangedDelay: 200,
			mapPath: false, // true / false / "spefific/path/as/string", default: false
			tryFallbackURL: true, // true/false, default false
			disableCheckFile: false, //default false
		 },

        // reveal.js plugins
        plugins: [
		  RevealMath,
          RevealHighlight,
          RevealNotes,
          RevealSearch,
          RevealZoom,
		  RevealChart,
		  RevealChalkboard,
        ],
		chalkboard: {
		boardmarkerWidth: 4,
        chalkWidth: 5,
		boardmarkers : [
                { color: 'rgba(248,248,242,1)', cursor: 'url(' + path + 'img/boardmarker-black.png), auto'},
                { color: 'rgba(102,217,239,1)', cursor: 'url(' + path + 'img/boardmarker-blue.png), auto'},
                { color: 'rgba(249,38,114,1)', cursor: 'url(' + path + 'img/boardmarker-red.png), auto'},
                { color: 'rgba(166,226,46,1)', cursor: 'url(' + path + 'img/boardmarker-green.png), auto'},
                { color: 'rgba(253,151,31,1)', cursor: 'url(' + path + 'img/boardmarker-orange.png), auto'},
                { color: 'rgba(174,129,255,1)', cursor: 'url(' + path + 'img/boardmarker-purple.png), auto'},
                { color: 'rgba(255,231,146,1)', cursor: 'url(' + path + 'img/boardmarker-yellow.png), auto'}
        ],
        chalks: [
                { color: 'rgba(248,248,242,0.5)', cursor: 'url(' + path + 'img/chalk-white.png), auto'},
                { color: 'rgba(102,217,239,0.5)', cursor: 'url(' + path + 'img/chalk-blue.png), auto'},
                { color: 'rgba(249,38,114,0.5)', cursor: 'url(' + path + 'img/chalk-red.png), auto'},
                { color: 'rgba(166,226,46,0.5)', cursor: 'url(' + path + 'img/chalk-green.png), auto'},
                { color: 'rgba(253,151,31,0.5)', cursor: 'url(' + path + 'img/chalk-orange.png), auto'},
                { color: 'rgba(174,129,255,0.5)', cursor: 'url(' + path + 'img/chalk-purple.png), auto'},
                { color: 'rgba(255,231,146,0.5)', cursor: 'url(' + path + 'img/chalk-yellow.png), auto'}
        ]
		},
		dependencies: [
			{ src: "../html_srcs/reveal.js/plugin/title-footer/title-footer.js", async: true, callback: function() { title_footer.initialize({css:"../html_srcs/reveal.js/plugin/title-footer/title-footer.css"}); } },
			{ src: "../html_srcs/reveal.js/plugin/d3/reveald3.js" },
		],
      });
      
     -->