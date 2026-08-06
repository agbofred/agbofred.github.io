# Default output format
FORMAT ?= html

# Get all markdown files in current directory
MD_FILES := $(wildcard *.md)

# For each md file, produce an output file with the chosen format (e.g., .html for slides)
OUTPUT_FILES := $(MD_FILES:.md=.$(FORMAT))

.PHONY: all
all: $(OUTPUT_FILES)

# Convert .md to .$(FORMAT) (e.g., .html) using pandoc and reveal.js template for slides
%.$(FORMAT): %.md
	pandoc $< -t revealjs -s -o $@ --slide-level=2
test.html: test.md
	pandoc test.md -t revealjs -s -o test.html -V theme=moon --highlight-style=espresso --slide-level=2
