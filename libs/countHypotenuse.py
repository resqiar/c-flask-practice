import math 

def countHypotenuse(inputA, inputB):
    result = math.sqrt(inputA**2 + inputB**2)
    return {
        "status": 200,
        "result": result
    }