
###############################################################################
# Tasks
# 1 - Create a training set
###############################################################################

###############################################################################
# CONSTANTS
# For use as dictionary keys in training/testing sets and sums
###############################################################################
DATE = "Date"
NAME = "Name"
AMOUNT = "Amount"

###############################################################################
# 1. Create a  set
# - Read in file
###############################################################################
def makeSet(filename):
    # DONE - Do not modify.
    newSet = []

    fin = open(filename,'r')

    # Read in file
    for line in fin:
        line = line.strip()
        line_list = line.split(',')

        # Create a dictionary for the line
        # ( assigns each attribute of the record (each item in the linelist)
        #   to an element of the dictionary, using the constant keys )
        record = {}
        record[DATE] = float(line_list[0])
        record[NAME] = line_list[1]
        record[AMOUNT] = float(line_list[2])

        # Add the dictionary to a list
        newSet.append(record)        

    fin.close()
    return newSet


###############################################################################
# 2. Generate Income Account
###############################################################################
def incomeAccount(incomeSet, expenditureSet):
    totalin = 0.0;
    totalexp = 0.0;
    print "Generate Income and Expenditure Account\n\n"
    print " Income and Expenditure Account        \n"
    print "---------------------------------------\n"
    print " INCOME                                \n"
    for record in incomeSet:
        totalin = totalin + float(record[AMOUNT])
        print " %s \t %.2f " % (record[NAME], record[AMOUNT])
    print "\n Total Income \t %.2f " % totalin
    print "                                       \n"
    print " EXPENDITURE                           \n"
    for record in expenditureSet:
        totalexp = totalexp + float(record[AMOUNT])
        print " %s \t %.2f " % (record[NAME], record[AMOUNT])
    print "\n Total Expenditure \t %.2f " % totalexp
    print "                                       \n"
    dif = totalin - totalexp
    print " Surplus / Deficit \t %.2f" % dif
    print "---------------------------------------\n"
#  

###############################################################################
# main - starts the program
###############################################################################
def main():
    # TODO
    print "Reading in data..."
    incomeSet = []
    incomeFile = "income.data"
    incomeSet = makeSet(incomeFile)
    print "Done reading income data.\n"

    print "Reading in expenditure data..."
    expenditureFile = "expenditure.data"
    expenditureSet = makeSet(expenditureFile)
    print "Done reading in data.\n"

    incomeAccount(incomeSet, expenditureSet)

    print "Program finished."
    
main()
