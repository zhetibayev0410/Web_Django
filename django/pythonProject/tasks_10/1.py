def is_weird(n):
    if n % 2 != 0:
        return "Weird"
    else:
        if n >= 2 and n <= 5:
            return "Not Weird"
        elif n >= 6 and n <= 20:
            return "Weird"
        else:
            return "Not Weird"

n = int(input().strip())

print(is_weird(n))
