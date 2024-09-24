import sys
from tabulate import tabulate
from colorama import Fore, Style

# Logical operators
def And(p,q):
    return True if p and q else False
def Or(p,q):
    return True if p or q else False
def Not(p):
    return not p
def Xr(p,q):
    return True if p != q else False
def Imp(p,q):
    return False if (p and (not q)) else True
def Bim(p,q):
    return not Xr(p,q)

# Counts how many propositions are in a statement
def GetPropositions(statement:str) -> str:

    # Replacement list that stores all substring 
    # that are to be removed from the statement
    replacement_list = ["not","and","or","xr","imp","bim"," ","(",")","="]

    # Remove substrings from statement
    for replacement in replacement_list:
        statement = statement.replace(replacement,"")

    # Remove duplicates
    statement = "".join(dict.fromkeys(statement))

    return statement
    
# Checks if a statement is able to be converted
# to an evaluateable statement
def Convertable(statement:str) -> bool:
    if "and" in statement:
        return True
    
    if "or" in statement:
        return True
    
    if "not" in statement:
        return True
    
    if "xr" in statement:
        return True
    
    if "imp" in statement:
        return True
    
    if "bim" in statement:
        return True
    
    return False

# Extracts (compound)propositions from either side
# of a logical operator
def ExtractPropositions(statement:str, split_from:str) -> tuple:
    
    # Get the index of the split point
    split_index = statement.find(split_from)

    # Remove logical operator from split point
    statement = statement.replace(split_from,"",1)

    # Check left side
    if statement[split_index-1] not in "()":
        left = statement[split_index-1]
    
    else:
        parenthesis_counter = 0
        left_index = split_index-1
        while True:
            if statement[left_index] == ")":
                parenthesis_counter += 1
            elif statement[left_index] == "(":
                parenthesis_counter -= 1

            if parenthesis_counter == 0:
                left = statement[left_index:split_index]
                break
            
            left_index -= 1
    

    # Check right side
    if statement[split_index] not in "()":
        right = statement[split_index]
    
    else:
        parenthesis_counter = 0
        right_index = split_index
        while True:
            if statement[right_index] == ")":
                parenthesis_counter += 1
            elif statement[right_index] == "(":
                parenthesis_counter -= 1

            if parenthesis_counter == 0:
                right = statement[split_index:right_index]
                break
            
            right_index += 1
    
    
    return left,right

# Converts statement to evaluateable format
def MakeEvaluateable(statement:str) -> str:
    if not Convertable(statement):
        return statement

    if "(not)" in statement:
        left,right = ExtractPropositions(statement, "(not)")
        statement = statement.replace("(not)"+right,f"(Not({right}))")

    elif "(and)" in statement:
        left,right = ExtractPropositions(statement, "(and)")
        statement = statement.replace(left+"(and)"+right,f"(And({left},{right}))")

    elif "(xr)" in statement:
        left,right = ExtractPropositions(statement, "(xr)")
        statement = statement.replace(left+"(xr)"+right,f"(Xr({left},{right}))")

    elif "(or)" in statement:
        left,right = ExtractPropositions(statement, "(or)")
        statement = statement.replace(left+"(or)"+right,f"(Or({left},{right}))")

    elif "(imp)" in statement:
        left,right = ExtractPropositions(statement, "(imp)")
        statement = statement.replace(left+"(imp)"+right,f"(Imp({left},{right}))")
    
    elif "(bim)" in statement:
        left,right = ExtractPropositions(statement, "(bim)")
        statement = statement.replace(left+"(bim)"+right,f"(Bim({left},{right}))")

    return MakeEvaluateable(statement)

# Format statement by surrounding functions with ()
def Format(statement:str) -> str:

    # A list of all available functions
    functions = ["not", "and", "xr", "or", "imp", "bim"]

    # Replace everything
    for function in functions:
        if function in statement:
            statement = statement.replace(function,f"({function})")
    
    # Lastly remove spaces
    statement = statement.replace(" ", "")

    return statement

# Replaces the first valid occurence of a proposition in a statement
# with a value, and returns that new statement
def ReplacePropositionWithValueInStatement(statement:str, prop:str,val:str) -> str:
    # This method was neccesarry because the program sometimes
    # flagged characters that were part of a function as propositions and changed them

    stat = statement

    # If there is only a single proposition
    # just return the value
    if len(stat) == 1:
        return val

    # First check if the propsition even existst
    if prop in stat:

        # Then iterate though all characters in the statement
        for i in range(len(stat)-1,-1,-1):

            char = stat[i]

            # If the characters is a proposition
            # and the index is within usable bounds
            if char == prop and 0 < i < len(stat)-1:

                # Make sure it is a valid proposition by checking
                # That it is inside a function
                if stat[i-1] in "(," and stat[i+1] in "),":

                    # Then change that proposition to the value
                    # and return statement
                    stat = stat[:i] + val + stat[i+1:]
        
        return stat
 
    return statement

def GetLastColumn(table:list):
    col = []
    table.pop(0)
    for row in table:
        col.append(row[-1])
    
    return col

# Generates truthtable
def GenerateTruthTable(statement:str, custom_propositions:str="None") -> list:
    # Save a copy of the original statement for final print
    og_statement = statement

    # Format statement by adding parenthesis around functions
    statement = Format(statement)

    # Get propositions if no custom propositions are used
    if custom_propositions == "None":
        propositions = GetPropositions(statement)
    else:
        propositions = custom_propositions
    
    # If no propositions are given, return None
    if len(propositions) == 0:
        print("No propositions given")
        return None
    
    # Convert statement to an evaluateable form
    evaluateable_statement = MakeEvaluateable(statement)

    # Table list for kepping track of all the data
    table = []

    # Create header with propositions and statement
    # and add it to the table
    header = list(propositions)+[og_statement]
    table.append( header )

    for _ in range( 2**len(propositions) ):
        # Convert _ to binary number with length of propositions
        binary = format(_, f'#0{ len(propositions)+2 }b') 
        binary = binary[2:]

        # Create a body, which is just a row of the table
        body = []

        # Make a copy of evaluateableStatement
        # to not modify original one
        es = evaluateable_statement

        # Go through each bit of binary number
        for i, digit in enumerate(binary):

            digit = True if digit == "1" else False

            # Add True to body if the digit is 1
            # otherwise add False
            body.append( digit )

            # Replace propositions with 0's and 1's from binary number
            es = ReplacePropositionWithValueInStatement(es,propositions[i],str(digit))

        # Evaluate the constructed evaluateableStatement
        # and add it to the body
        es = eval(str(es))
        body.append( es )

        # If coloring is enabled
        # color False red, and True blue
        if coloring:
            for i, col in enumerate(body):
                if col == False:
                    body[i] = Fore.RED+"False"
                elif col == True:
                    body[i] = Fore.BLUE+"True"

        # Add the body to the table
        table.append( body )
    
    # Add some personal space
    print("")

    # Tabulate the table with the first row
    # being a header, and print it
    print(tabulate(table,headers="firstrow"))

    if coloring:
        # Reset styling
        print(Style.RESET_ALL)
    
    return GetLastColumn(table)

def GetPropositionType(data:list) -> str:
    """ Get the proposition type from the last columns of a statement
    """
    proposition_type = ""

    rights = 0
    wrongs = 0

    for i in range(len(data[0])):
        sub_rights = 0
        for index in range(len(data)):
            if data[index][i] != data[(index+1)%len(data)][i]:
                wrongs += 1
                break
            else:
                sub_rights += 1
        if len(data) == sub_rights:
            rights += 1        
    
    if wrongs == 0:
        proposition_type  = "Tautology"
    elif rights == 0:
        proposition_type = "Contradiction"
    else:
        proposition_type = "Contingency"

    return proposition_type

def CheckEquivilance(statement:str):
    compound_propositions = statement.split("==")
    all_propositions = GetPropositions(statement)

    data = []

    for compound_proposition in compound_propositions:
        col = GenerateTruthTable(compound_proposition,all_propositions)
        data.append(col)

    proposition_type = GetPropositionType(data)

    return proposition_type

# Example usage:  filepath\python evaluator.py True
if __name__ == "__main__":
    # If the first argument is used, its for coloring
    # check if it is True, otherwise let it be False
    global coloring
    coloring = False
    if len(sys.argv) == 2:
        if sys.argv[1] == "True":
            coloring = True
    
    # Start continuing statement evaluation
    running = True
    while running:
        statement = input("-> ")

        # Check if statement is a logical equivilence
        if "==" in statement:
            proposition_value = CheckEquivilance(statement)

            # Print what kind of statement is made
            # with coloring the type
            print("The statement is",
                  Fore.GREEN+proposition_value+Style.RESET_ALL 
                  if coloring else proposition_value)

        else:
            # Generate the truthtable from a statement
            GenerateTruthTable(statement)
