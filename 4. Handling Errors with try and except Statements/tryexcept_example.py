def div42by(divisor):
    try:
        return 42 / divisor
    except ZeroDivisionError:
        print('You tried to divide by zero.')
        
print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))
