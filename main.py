from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wlexpr
from dotenv import load_dotenv
import os

isLoaded = load_dotenv()

# get kernel path and the function to be evaluated
path = os.getenv("KERNEL_PATH")
multiVarFunc = os.getenv("MULTIVAR_FUNC")

try:
    # start session
    session = WolframLanguageSession(path)

    variables = ["x", "y"]
    valuesVar = ["0", "0.19602"]
    errValues = ["0", "0.00001"]

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

        resultToString = session.evaluate(
            wlexpr("ToString[s[{0}]]".format(variables[i]))
        )

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
            sumFunction = sumFunction + "+{0}*{1}".format(
                resultTextString, errValues[i]
            )

    session.evaluate(wlexpr(sumFunction))

    # evaluate g[] function with variables' values
    print(
        "\n\n\n resultado da soma: {0}".format(
            session.evaluate(wlexpr("g[{0},{1}]".format(valuesVar[0], valuesVar[1])))
        )
    )
except:
    session.terminate()
    print("An error has occurred")

finally:
    session.terminate()
