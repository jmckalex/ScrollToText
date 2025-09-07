# ScrollToText — a Sublime Text plugin

This is a simple Python program that provides forward-search capability between
Sublime Text and Google Chrome.  When editing a markdown file in Sublime Text,
selecting "Scroll to Text in Browser" will tell Chrome to search for the text
on the current line in Sublime Text and, if found, scroll it into view.
A short animation will also be invoked on the element, making it clear which
one it is.

Here’s a demonstration:



https://github.com/user-attachments/assets/d4d9e6c9-4e12-497b-b997-2c5beccd2fdc




This only works on a Mac, because it uses AppleScript to communicate between
Sublime Text and the browser.  There are probably ways to do this on a Windows
machine, but I don’t have one.

# Installation

1. Create a folder named `ScrollToText` inside 
   `~/Library/Application Support/Sublime Text/Packages/` and copy all of
   these files into there. 

2. Restart Sublime Text.
