# Missing-PNRs

Description: Script main.py is made to find all missing PNRs between given two. Missing PNRs are stored in Database called PNR.db same as two given PNRs while client get a number of missing PNRs.

# Requirements

 -Python 3.x
 -sqlite3 (built in into python)
 -string  (built in into python)
 -unittest (built in into python)
 (requirements.txt file was made by "pip freeze > requirements.txt" command)

# How to use

  Script main.py can be used in two ways :

  1) It can be run directly which provides interaction with client through the console/terminal 
  2) Script can be importet in another script and all it functionality can be used 

  Script contain class Detector with attributes/metods:
  	1. d_s2n - dict that contain symbols(0-9, A-Z) for keys and numbers(0-35) as values
  	2. d_n2s - dict that contain numbers(0-35) for keys and symbols(0-9, A-Z) as values
  	3. base - nubmber used to convert PNRs to decimal format
  	4. conn - connection to Database
  	5. c - cursor that execute queries 

  	6. __init__ - constructor seting up attributes
  	7. uspostavi_konekciju - function that provide connection to Database
  	8. save_to_db(fist, second, missing) - function that saves first given PNR with isMissing = 0 , second given PNR with isMissing = 0 and each missing PNR from list missing with isMissing = 1
  	9. close_connection - closing connection with Database
  	10. check_order(x, y) - checking if y is greater than x if it is returned value is x,y , if x is greater than returned values is y,x. ValueError will be raised if x and y are the equal
  	11. convert(x) - function convert integer number into PNR or PNR into integer number.ValueError is raised if PNR is in wrong format(less/more than 6 symbols , symbols are not in d_s2n.keys() or symbol equals 0) or if given value x is of a diferent data type except string or integer
  	12. find_missing_PNR (x,y) - function whit a job to count and return how many missing PNRs are between 2 given. After counting, finds the missing PNRs and stores tham in Database. ValueError is raised when number of missing PNRs is greater than 1000

# Testing

 The unittest package was used for testing purposes.Testing was pperformed on convert,check_order and find_missing_PNR.
 The behavior when passing valid values was tested, as well as the behavior when passing values that should raise ValueError. 