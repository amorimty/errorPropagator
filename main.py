from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wlexpr


session = WolframLanguageSession(
    "C:\\Program Files\\Wolfram Research\\Wolfram Engine\\14.0\\WolframKernel.exe"
)

variables = ["constEl", "Lb", "Lzero", "massaZinha", "velocidade", "hb"]
valuesVar = ["0.9", "1.888", "0.313", "0.12275", "3.15", "1.097"]
errValues = ["0.5", "0.001", "0.001", "0.00001", "0.11", "0.001"]

expression = (
    "D[((constEl(Lb-Lzero)^2)/2) + (massaZinha*(velocidade)^2)/2 + massaZinha*9.81*hb, "
)

sum = ""

for i in range(len(variables)):

    # expressionManipulated = expression.replace("err", errValues[i])

    completeExp = expression + "{0}]".format(variables[i])

    resultToString = session.evaluate(wlexpr("ToString[{0}]".format(completeExp)))
    resultTextString = session.evaluate(wlexpr("TextString[{0}]".format(completeExp)))

    print(
        "derivada em relacao a {0} com erro associado {1}:\n {2} \n".format(
            variables[i],
            errValues[i],
            resultToString,
        )
    )
    if variables[i] == variables[0]:
        sum = sum + "Abs[{0}]*{1}".format(resultTextString, errValues[i])
    else:
        sum = sum + "+ Abs[{0}]*{1}".format(resultTextString, errValues[i])
    # results.append(resultTextString)

for i in range(len(variables)):
    sum = sum.replace(variables[i], valuesVar[i])

print("\n\n\n resultado da soma: {0}".format(session.evaluate(wlexpr(sum))))

# print(session.evaluate(wlexpr("ToString[{0}]".format(sum))))


# expressionParse = session.evaluate(wlexpr("ToString[{0}]".format("(y*x^(2/3))")))

# print("Função a ser derivada parcialmente: \n", expressionParse, "\n")

# result = session.evaluate(wlexpr(expression))

# parse = "TextString[{0}]".format(result)
# parseX = "ToString[{0}]".format(expressionX)
# parseY = "ToString[{0}]".format(expressionY)

# print("Resultado sem parsing: \n", result, "\n")
# print("Resultado com parsing: \n", session.evaluate(wlexpr(parse)), "\n")
# print("Resultado da derivada parcial em x: \n ", session.evaluate(wlexpr(parseX)), "\n")
# print("Resultado da derivada parcial em y: \n ", session.evaluate(wlexpr(parseY)), "\n")

session.terminate()
