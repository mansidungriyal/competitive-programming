def final_value(n, statements):
    x = 0  
    for statement in statements:
        if '++' in statement:
            x += 1
        elif '--' in statement:
            x -= 1
    return x


n = int(input().strip())


statements = [input().strip() for _ in range(n)]


result = final_value(n, statements)


print(result)