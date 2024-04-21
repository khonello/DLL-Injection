# DLL Injection

#### Requirement
1. Psutil
2. Pywin32

If for testing purpose you intend to inject a different process with my DLL, make sure the process reads and writes to an I/O [ stdin, stdout ] and replace the `console` in the main module.py with the name of the program.
If you intend to use your own DLL, make sure your `C` source file that will be used to create the DLL has a definition for the DLLMain. Refer to the deps/source.c file. What you specify in the DLLMain is what will be performed in the target process in this case print a 🍩.

I think by now you know this is a windows only project.
