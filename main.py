from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wlexpr


session = WolframLanguageSession(
    "C:\\Program Files\\Wolfram Research\\Wolfram Engine\\14.0\\WolframKernel.exe"
)

variables = ["x", "y", "z", "m", "a", "b"]
valuesVar = ["0.9", "1.888", "0.313", "0.12275", "3.15", "1.097"]
errValues = ["0.5", "0.001", "0.001", "0.00001", "0.11", "0.001"]


varDict = {
    "x_": {"value": "", "errValue": ""},
    "y_": {"value": "", "errValue": ""},
    "z_": {"value": "", "errValue": ""},
    "m_": {"value": "", "errValue": ""},
    "a_": {"value": "", "errValue": ""},
    "b_": {"value": "", "errValue": ""},
}

expression = "D[((x(y-z)^2)/2) + (m*(a)^2)/2 + m*9.81*b, "


multiVarFunc = "f[x_,y_,z_,m_,a_,b_]:=((x*(y-z)^2)/2)+(m*(a)^2)/2+m*9.81*b"

session.evaluate(wlexpr(multiVarFunc))

sumFunction = ""

for i in range(len(variables)):

    diffExp = "D[f[x_,y_,z_,m_,a_,b_],{0}]".format(variables[i] + "_")

    resultToString = session.evaluate(wlexpr("ToString[{0}]".format(diffExp)))
    resultTextString = session.evaluate(wlexpr("TextString[{0}]".format(diffExp)))

    print(
        "derivada em relacao a {0}_ com erro associado {1}:\n {2} \n".format(
            variables[i],
            errValues[i],
            resultToString,
        )
    )
    if variables[i] == variables[0]:
        sumFunction = sumFunction + "Abs[{0}]*{1}".format(
            resultTextString, errValues[i]
        )
    else:
        sumFunction = sumFunction + "+Abs[{0}]*{1}".format(
            resultTextString, errValues[i]
        )

for i in range(len(variables)):
    sumFunction = sumFunction.replace(
        ("Pattern[{0}, Blank[]]".format(variables[i])), valuesVar[i]
    )

print("\n\n\n resultado da soma: {0}".format(session.evaluate(wlexpr(sumFunction))))

session.terminate()
