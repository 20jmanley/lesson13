# lesson13
File I/O

Complete the program in the video and take notes on how to perform file I/O.

### Enhancements

1. Change the menu so that there is a "save as" and "save" options

2. "Save as" should do exactly what it did in the video

3. "Save" should not open the asksaveasdialog, instead just check to see if the length of the app.filename is greater than zero and if it is, use that filename to open the file and write.  If the length is zero, meaning that there is not a file name yet, do exactly what "save as" does by opening up the asksaveasdialog etc.

4. When exiting the app, it should check to see if app.filename is empty.  If so, ask the user if she wants to exit without saving (like it does now).  If the filename is not empty (meaning that it has been saved).  Ask the user if he wants to save changes.  If yes, run the same function that "save" points to, else, just exit.

### Discussion Questions:

1. What are some limitations to your word processor?

2. What do you think it would take to modify your word processor to overcome one of those limitations?

3. How are menu items similar to PushButtons?  How are menu items different than PushButtons?

4. When you Save a file you have to use open(filename, "w").  Explain why you have to do this.
