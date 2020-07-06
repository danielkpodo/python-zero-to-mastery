# A return keyword automatically exits the function

def aggregator(num1, num2):
    def evaluator(n1, n2):
        return n1 + n2
    return evaluator(num1, num2)


total = aggregator(10, 90)
print(total)
