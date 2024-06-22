from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wlexpr
from dotenv import load_dotenv
import os

isLoaded = load_dotenv()

# get kernel path and the function to be evaluated
path = os.getenv("KERNEL_PATH")

# start session
session = WolframLanguageSession(path)

multiVarFunc = "f[]:="

variables = []
variablesValues = []
variablesErr = []
variablesNumber = 0

print("Enter how many variables you need than type 0:")

isActive = 1

while isActive != 0:

    print("Choose an option:\n")
    print("Insert expression --------- 0\n")
    print("Insert variables  --------- 1\n")
    print("Calculate         --------- 2\n")
    print("exit              --------- 3\n")
    temp = input("R.: ")
    
    match temp:
        case "0": 
            temp0 = input("\n\nInsert your expression: ")
            multiVarFunc += temp0
        case "1":
            temp1 = 1
            while temp1 != 0:
                variables.append(input("var number {0}: ".format(temp1)))
                variablesValues.append(input("value of var number {0}: ".format(temp1)))
                variablesErr.append(input("error associated to var number {0}: ".format(temp1)))
        case "2":
            
        case "3":
            session.terminate()
            

    if temp == "_":
        # varNumber = isActive - 1
        isActive = 0
    else:
        variables.append(temp)
        isActive += 1



# evaluate the multivar funcion and s[] function (to be made dynamic) that generates the elements of g[] later on
session.evaluate(wlexpr(multiVarFunc))
session.evaluate(wlexpr("s[k_]:=Abs[D[f[x,y], k]]"))

# build g[] from the array of variables dynamically
sumFunction = "g["

for i in variables:
    sumFunction += "," + i + "_"
sumFunction += "]:="
sumFunction = sumFunction.replace("[,", "[")

# evaluate each s[i] expression and store it inside g[] function
for i in range(len(variables)):

    resultToString = session.evaluate(wlexpr("ToString[s[{0}]]".format(variables[i])))

    resultTextString = session.evaluate(
        wlexpr("TextString[s[{0}]]".format(variables[i]))
    )

    print(
        "derivada em relacao a {0} com erro associado {1}:\n {2} \n".format(
            variables[i],
            errValues[i],
            resultToString,
        )
    )
    if variables[i] == variables[0]:
        sumFunction = sumFunction + "{0}*{1}".format(resultTextString, errValues[i])
    else:
        sumFunction = sumFunction + "+{0}*{1}".format(resultTextString, errValues[i])

session.evaluate(wlexpr(sumFunction))

# evaluate g[] function with variables' values
print(
    "\n\n\n resultado da soma: {0}".format(
        session.evaluate(wlexpr("g[{0},{1}]".format(valuesVar[0], valuesVar[1])))
    )
)

session.terminate()
