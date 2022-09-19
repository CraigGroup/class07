#----------------------------------------------------------------------------
#    PROGRAM NAME:  triangle.py
#    PURPOSE:       Using command line arguments and Math functions.  
#    CREATED:       Craig Group  2022
#
#    Class06
#    UVA Honor Pledge
#   
#    To run me:  python triangle.py
#____________________________________________________________________________

#------------------------------------------------
#                  IMPORTS
#------------------------------------------------


import sys



#------------------------------------------------
#               GLOBAL CONSTANTS
#------------------------------------------------
#None

INPUT1=0
INPUT2=0
INPUT3=0

PROGRAM_NAME=sys.argv[0]

if (len(sys.argv)>1):
    if (len(sys.argv)==4):
        print("User input:\n")
        print(sys.argv)
        print("\n")

        try:
            #argv is a list of strings - convert to floats
            #Use "try" statement to make sure floats were given at the command line
            INPUT1=float(sys.argv[1])
            INPUT2=float(sys.argv[2])
            INPUT3=float(sys.argv[3])
        except:
            #If not, correct the user
            print("\n make sure your 3 inputs are floats!\n")
    else:
        print("\n 3 command-line inputs required (the length of the 3 sides of a triangle)\n")
else:
    print("\n Please include a command-line argument.\n")
    print(">>> python command_line_input.py your_input_goes_here \n")




#------------------------------------------------
#               METHODS
#------------------------------------------------
#None

#------------------------------------------------
#                   MAIN FUNCTION
#------------------------------------------------
def main():

    #To print something to the screen in Python.
    print("\n-->You are running the program: "+PROGRAM_NAME+"\n\n")
    print("-->The use input was: %f, %f, %f \n" %(INPUT1,INPUT2,INPUT3))
    
    
   

#Call the main function if all three INPUTS are filled.

if INPUT3>0 and INPUT2>0 and INPUT3>0:

    main()
else:
    print("all sides must have length greater than zero")
