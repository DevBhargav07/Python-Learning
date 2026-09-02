#sum of the divisors of a number is called as aliquot sum
#should not be negative
#not be zero
#a positive integer

def find_aliquot(number):
    if not isinstance(number, int):
        raise ValueError(f"Number should be an integer but got: {type(number)}")
    
    if number < 0:
        raise ValueError("Number must be a Positive Integer")
    
    return sum(
        value for value in range(1, number//2 +1 ) if number % value == 0
    )

print(find_aliquot(91))
