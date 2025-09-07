Title: ScrollToText - a Sublime Text plugin
Date: 7 September 2025
Author: J. McKenzie Alexander
CSS: jmarkdown.css
Biblify activate: true
Bibliography: bibliography.bib
Bibliography style: harvard1
---

<style>
    @media print {
        a.edit-link {
            display: none;
        }
    }

    a.edit-link {
        position: absolute;
        left: 75px;
        transform: translateY(1pt);
        color: grey;
        font-size: 10pt;
        opacity: 0.5;
    }

    body {
    	position: relative;
    }
</style>

# ScrollToText — a Sublime Text plugin

This is a simple Python program that provides forward-search capability between
Sublime Text and Google Chrome.  When editing a markdown file in Sublime Text,
selecting "Scroll to Text in Browser" will tell Chrome to search for the text
on the current line in Sublime Text and, if found, scroll it into view.
A short animation will also be invoked on the element, making it clear which
one it is.

Here’s a demonstration:

<video width="100%" controls>
  <source src="demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

This only works on a Mac, because it uses AppleScript to communicate between
Sublime Text and the browser.  There are probably ways to do this on a Windows
machine, but I don’t have one.

# Installation

1. Create a folder named `ScrollToText` inside 
   `~/Library/Application Support/Sublime Text/Packages/` and copy all of
   these files into there. 

2. Restart Sublime Text.
