# Program Specifications

## Inputs
Inputs to the program will be made using command-line option flags. The program must take the appropriate run-time actions as follows:

  -h, --help   show this help message and exit
  -i INPUT     specify clear text password from command line
  -f FILENAME  specify a CSV file to read and process 

If no options are specified, print the usage overview and exit.

### CSV file format

The CSV file must have at least two columns, for URL and clear text password. Password Corral 
        http://www.cygnusproductions.com/freeware/pc.asp
can be used to export a clear text CSV file, but it will not include column headers. Add them manually if required for processing.

## Output
When processing a clear text password from the command line, print text indicating if the password is safe or not from dictionary attacks.
When processing a CSV file, print the value from the URL column and if the password is safe or not.
If the CSV file contains blank lines, ignore them.
Print a message indicating how many rows were processed when the input is a CSV file.

## Application Programming Interface

Use the https://www.passable.io/ API to check the password strength of the password. Use any supported hash algorithm.

# Test cases
Test the following conditions:

* Connection failure to the API host
* Execution without any command-line option flags
* Execution with an unrecognized argument
* Execution specifying -h and --help
* Specify the -f option with no filename, and an invalid filename
* Specify the -i option with no 
* Execute using a valid -i and -f arguments
* CSV file with blank lines

Print out appropriate error messages for failure test cases.
