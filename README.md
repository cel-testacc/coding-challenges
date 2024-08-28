# coding-challenges
This is made to store my solutions to the coding problems on the coding challenges blog.

## wc tool
The first challenge is to implement your own version of Linux's wc CLI tool.
My initial implementation is in Python.
To run code, simply navigate to the wc_tool directory, then run:
```sh
python ccwc.py
```
Enter variations of the wc tool, with the slight difference that the command is now prefaced with 'ccwc' instead. For example, here are several commands you can run:
```sh
ccwc -c <filename>
ccwc -l <filename>
ccwc -w <filename>
ccwc -m <filename>
ccwc <filename>
cat <filename> | ccwc -l
```
The output should match results you get while running the wc tool. The input accepts prompts infinitely. To exit, use a keyboard shortcut to denote eof or type 'exit'.
