import math

def perfect_square(n):
    root = int(math.sqrt(n))
    return n == root * root

def eval_num(num):

    result = f'{num} '

    # Primo
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                result += 'no es primo, '
                break
        else:
            result += 'es primo, '

    else:
        result += 'no es primo, '

    # Fibonacci
    if perfect_square(5 * num * num + 4) or perfect_square(5 * num * num - 4) and num > 0:
        result += 'es Fibonacci '
    else:
        result += 'no es Fibonacci '

    # Par
    if num % 2 == 0:
        result += 'y es par'
    else:
        result += 'y es impar'

    return result

print(eval_num(4))
print(eval_num(8))
print(eval_num(7))
print(eval_num(10))

