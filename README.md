# eggcode
Extended Grammar GCODE. Adds control flow and variable options and then translates it to basic gcode.

Basic usage:
```
// Use C-style comments

G0 X0Y0; // Your basic GCODE command except it has a semicolon now

// Variables:

var i = 0; // Variable declaration
var s = 1;
i = 3+2;    // Variables work like you expect them to.
i += 5;     // += and -= are implemented too and you can use a variable to 

// Note that order of operations isn't accounted for so a*b+c is treated as a*(b+c) since it's always read left to right and resolved right to left.

// Using variables in gcode:
G0X<i>;     // Anything inside the angle brackets is treated as an expression and resolved as such so calculations are valid too.

// Control flow statements:
while(i>0){
    G1 Y<3*s>; // This is the main reason why I made eggcode.
    s = -s;    // To easily make a back and forth going path on a CNC machine.
    G1 X1;     // Was it worth the effort of learning to use a lexer? No comment...
};

// I'm planning to implement for loops and if-elif-else statements in the future.
// Maybe I'll add functions as well but I'm not sure yet.
```
