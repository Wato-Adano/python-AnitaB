def add(a, b):
    answer = a+b
    return answer


def subsract(a, b):
    answer = a-b
    return answer


def mutplication(a, b):
    answer = a*b
    return answer


def divide(a, b):
    answer = a/b
    return answer


def sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number
        return result
    
      
def creat__sentence(**words):
    print(words)
    sentence = ""
    for words in words.vaues():
        sentence += words
        sentence += " "
        return sentence
    
    
def sum_and_greet(*args, **kwargs):
    total = 0
    for number in args:
        total += number
        first_name = kwargs["first_name"]
        last_name = kwargs["last_name"]
        greeting = f"Hello{first_name}{last_name}, the sum is {total}"
        return greeting    
    
    
                                            