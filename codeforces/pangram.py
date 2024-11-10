def is_pangram(s):
    s_lower = s.lower()
    letters = set()

    for char in s_lower:
        if 'a' <= char <= 'z':
            letters.add(char)

    return len(letters) == 26


n = int(input().strip())
string = input().strip()


if is_pangram(string):
    print("YES")
else:
    print("NO")