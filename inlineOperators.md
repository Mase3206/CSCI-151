# Inline Operators in Unix, macOS, and Linux

In Unix, macOS, and Linux, inline operators are often used in command-line interfaces to perform various operations on data streams, files, or commands. 

These inline operators provide powerful ways to manipulate and process data in Unix-like operating systems, allowing for efficient command chaining, file manipulation, and error handling.

Here's a brief explanation of some common inline operators:

## Pipe (`|`)
The pipe operator (`|`) is used to redirect the output of one command as input to another command. It allows you to chain commands together, creating a pipeline where the output of one command serves as the input to the next command.

**Example:**

```bash
# This is a roundabout way to print "hello" on the screen
cat "echo 'hello'" | bash
```

## Input Redirection (`<`)
The input redirection operator (`<`) is used to redirect the contents of a file to serve as input to a command. It tells the command to read input from the specified file instead of from the keyboard.

**Example:**

```bash
# This uses the practice code we had in class one day
python plotfilter.py < usa.txt
```

## Output Redirection (`>` and `>>`)
The output redirection operators (`>` and `>>`) are used to redirect the output of a command to a file instead of the standard output (usually the terminal):

- `>` overwrites the contents of the file if it exists or creates a new file if it doesn't exist.
- `>>` appends the output to the end of the file if it exists or creates a new file if it doesn't exist.

**Examples:**

```bash
# Puts random integers to a file, making it if it does not exist, *overwrighting it* if it does.
python randomintseq.py > random.txt

# *Appends* some text to a file, making it if it does not exist.
python appendthis.py >> file_to_append.txt
```

## Error Redirection (`2>` and `2>>`)
Similar to output redirection, error redirection operators (`2>` and `2>>`) are used to redirect error messages (stderr) to a file instead of the standard error output (usually the terminal).

**Examples:**

```bash
# This will hide the errors generated.
wget "http://tcfvygbhjdferg.com/" 2> /dev/null

# This can be handy for logging errors
wget "http://tcfvygbhjdferg.com/" 2>> error.log
```
