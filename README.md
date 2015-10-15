CS 325 Project 1

To test the programs against the MSS_Problems.txt:
  Ensure that all of the required files are in the same directory. 
  The required files are:
    maxSumSubarray.py		    (contains the four algorithms)
    main.py				        (runs max subarray algorithms on arrays in MSS_Problems.txt) 
    MSS_Problems.txt		    (contains test sets of data (arrays of integers))
  From the command line, run the program by entering:   python main.py

Once the program has completed execution, a file called MSS_Results.txt will 
have been generated. This text file contains the results of the runs of each 
algorithm on the provided arrays from MSS_TestProblems.txt.

Additionally, to generate timing statistics for the program you can 
run the "python expStats2.py". This command will output average times 
for different sizes of n (based on hard coded values of n) to 4 
different csv files. The following file names correspond to the defined algorithms:
  stats1.csv = enumeration
  stats2.csv = better enumeration
  stats3.csv = recursive
  stats4.csv = linear
  
