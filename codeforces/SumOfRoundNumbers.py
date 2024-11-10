def minimum_round_numbers(n):
    round_numbers = []
    place_value = 1
    
    while n > 0:
        digit = n % 10
        if digit != 0:
            round_numbers.append(digit * place_value)
        n //= 10
        place_value *= 10
    
    return round_numbers

def process_test_cases(test_cases):
    results = []
    for n in test_cases:
        round_numbers = minimum_round_numbers(n)
        results.append((len(round_numbers), round_numbers))
    return results


t = int(input())
test_cases = [int(input()) for i in range(t)]


results = process_test_cases(test_cases)


for count, round_numbers in results:
    print(count)
    print(' '.join(map(str, round_numbers)))