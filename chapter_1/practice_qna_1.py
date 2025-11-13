# Question 1

def g(l):
    s = 0
    for i in range(len(l)):
        if l[i] % 2 == 0:
            s = s + l[i] * 2
    print("Sum is", s)


# my answer
def generate_sum(list_of_nums):
    sum = 0

    for i in range(len(list_of_nums)):
        if list_of_nums[i] % 2==0: # check whether the number is even
            sum = sum + list_of_nums[i] *2
    print("Sum is :", sum)        

# better answer

def sum_of_doubled_evens(numbers: list[int]) -> int:
    """Return the sum of all even numbers doubled."""
    return sum(num * 2 for num in numbers if num % 2 == 0)
