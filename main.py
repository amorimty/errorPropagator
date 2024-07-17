from sympy import *
import sympy as sympy
import copy

multiVarFunc = ""
diffFuncs = []

variables = []
variablesValues = []

varDict = {}

variablesErr = []
variablesNumber = 0


isActive = 1


while isActive != 0:

    print("Choose an option:\n")
    print("Insert expression --------- 1\n")
    print("Insert variables ---------- 2\n")
    print("Evaluate------------------ 3\n")
    print("exit ---------------------- 4\n")
    temp = input("")

    match temp:
        case "1":
            temp0 = input("\n\nInsert your expression: ")
            multiVarFunc = parse_expr(temp0, evaluate=false)

            for i in multiVarFunc.free_symbols:
                diffFuncs.append(diff(multiVarFunc, i))

        case "2":
            if multiVarFunc != "":
                varDict.clear()
                for i in multiVarFunc.free_symbols:
                    valor = float(input("Valor para {}: ".format(i)))
                    varDict.update({i: valor})

        case "3":
            multivarFuncCopy = copy.deepcopy(multiVarFunc)
            diffFuncsCopy = copy.deepcopy(diffFuncs)

            multivarFuncCopy.subs(varDict)

            errCalc = 0

            for i in diffFuncsCopy:
                i.subs(varDict)
                errCalc += Abs(i)

            print("Valor encontrado foi: {} +/- {}".format(multivarFuncCopy, errCalc))

        case "4":
            isActive = 0

    # if temp == "_":
    #     # varNumber = isActive - 1
    #     isActive = 0
    # else:
    #     variables.append(temp)
    #     isActive += 1


# # evaluate the multivar funcion and s[] function (to be made dynamic) that generates the elements of g[] later on
# session.evaluate(wlexpr(multiVarFunc))
# session.evaluate(wlexpr("s[k_]:=Abs[D[f[x,y], k]]"))

# # build g[] from the array of variables dynamically
# sumFunction = "g["

# for i in variables:
#     sumFunction += "," + i + "_"
# sumFunction += "]:="
# sumFunction = sumFunction.replace("[,", "[")

# # evaluate each s[i] expression and store it inside g[] function
# for i in range(len(variables)):

#     resultToString = session.evaluate(wlexpr("ToString[s[{0}]]".format(variables[i])))

#     resultTextString = session.evaluate(
#         wlexpr("TextString[s[{0}]]".format(variables[i]))
#     )

#     print(
#         "derivada em relacao a {0} com erro associado {1}:\n {2} \n".format(
#             variables[i],
#             errValues[i],
#             resultToString,
#         )
#     )
#     if variables[i] == variables[0]:
#         sumFunction = sumFunction + "{0}*{1}".format(resultTextString, errValues[i])
#     else:
#         sumFunction = sumFunction + "+{0}*{1}".format(resultTextString, errValues[i])

# session.evaluate(wlexpr(sumFunction))

# # evaluate g[] function with variables' values
# print(
#     "\n\n\n resultado da soma: {0}".format(
#         session.evaluate(wlexpr("g[{0},{1}]".format(valuesVar[0], valuesVar[1])))
#     )
# )
