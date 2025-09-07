import sublime
import sublime_plugin
import re
import json
import subprocess


class ScrollToTextCommand(sublime_plugin.TextCommand):
    """Main command to scroll to text in Chrome"""
    
    def run(self, edit):
        # Get the current line
        current_line = self.view.line(self.view.sel()[0])
        line_text = self.view.substr(current_line).strip()
        
        if not line_text:
            sublime.status_message("No text on current line")
            return
        
        # Clean the text for better matching
        cleaned_text = self.clean_text_for_matching(line_text)
        
        if len(cleaned_text) < 3:
            sublime.status_message("Text too short for reliable matching")
            return
        
        # Search for the text in Chrome
        success = self.scroll_to_text_in_chrome(cleaned_text)
        
        if success:
            sublime.status_message("Searching for: {}".format(cleaned_text))
        else:
            sublime.status_message("Failed to search for: {}".format(cleaned_text))
    
    def clean_text_for_matching(self, text):
        """Clean text to improve matching accuracy"""
        # Remove markdown formatting
        text = re.sub(r'[*_`#\[\]()/]', '', text)
        text = text.strip()
        text = re.sub(r'^>+\s*', '', text)
        text = re.sub(r'^\d+\.\s*', '', text)
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        print("Searching for '" + text + "'")
        # Take a reasonable substring if too long
        if len(text) > 100:
            text = text[:100]
        return text.strip()
    
    def scroll_to_text_in_chrome(self, search_text):
        """Search for text in Chrome and scroll to it"""
        try:
            # Create JavaScript to search for and scroll to text
            js_code = '''
            var searchText = "''' + search_text.replace('"', '\\\\"').replace("'", "\\\\'") + '''";
            var elements = document.querySelectorAll("p, h1, h2, h3, h4, h5, h6, li, div, span");
            var found = false;
            
            for (var i = 0; i < elements.length; i++) {
                var element = elements[i];
                var text = element.textContent || "";
                if (text.toLowerCase().indexOf(searchText.toLowerCase()) !== -1) {
                    element.scrollIntoView({behavior: "smooth", block: "center"});
                    element.style.backgroundColor = "#ffff99";
                    element.style.border = "2px solid #ff6600";
                    setTimeout(function() {
                        element.style.backgroundColor = "";
                        element.style.border = "";
                    }, 3000);
                    found = true;
                    break;
                }
            }
            
            if (!found) {
                alert("No match found for: " + searchText);
            }
            '''
            
            # Create AppleScript to execute the JavaScript
            applescript = 'tell application "Google Chrome" to execute active tab of front window javascript "' + js_code.replace('"', '\\"').replace('\n', ' ') + '"'
            
            # Execute AppleScript
            result = subprocess.call(['osascript', '-e', applescript])
            
            return result == 0
            
        except Exception as e:
            sublime.status_message("Error: {}".format(str(e)))
            return False
    
    def is_enabled(self):
        """Only enable in markdown files"""
        return self.view.match_selector(0, "text.html.markdown")


class ScrollToTextTestCommand(sublime_plugin.TextCommand):
    """Simple test command"""
    
    def run(self, edit):
        current_line = self.view.line(self.view.sel()[0])
        line_text = self.view.substr(current_line).strip()
        
        if not line_text:
            sublime.status_message("No text on line")
            return
        
        try:
            applescript = 'tell application "Google Chrome" to execute active tab of front window javascript "alert(\'Found text: ' + line_text.replace("'", "\\'").replace('"', '\\"') + '\');"'
            result = subprocess.call(['osascript', '-e', applescript])
            
            if result == 0:
                sublime.status_message("Test successful!")
            else:
                sublime.status_message("Test failed")
                
        except Exception as e:
            sublime.status_message("Error: {}".format(str(e)))
    
    def is_enabled(self):
        return True


def plugin_loaded():
    print("ScrollToText plugin loaded successfully")


def plugin_unloaded():
    print("ScrollToText plugin unloaded")