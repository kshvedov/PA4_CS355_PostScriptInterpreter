# PA4_CS355_PostScriptInterpreter
Project 4 from CS 355 PostScript interpreter made using Python 3

This whole project was split between different assignments. The whole idea behind it was
to learn python by creating an interpreter for Post Script, which in turn taught me how
postcript works.

Part 1 was mostly just the most important functions that a post script interpreter may
need, with test for each one, that tested if all function works and write if an error
occurs.

Part 2 was the development of the project so it would be able to do loops and if
statements, but most importantly a string to function calling interpreter. We were
given a regex expression that was intended to be able to do everything, but unfortunately
it didnt and through some editing it became a more advanced version. The function that
interprets the top is not the best version that could be, but due to how small the program
is, the time it takes to go through every if statement is not noticabel. If I would do this
again I would use hash table for ease of access. In python that would be the same as using a
dictionary.

Part 3 was primarly to learn the difference between a static scope and a dynamic scope and
how to implement each one within the python language to allow the Post Script interpreter to
act accordingly.
