def combo_string(a, b):
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b

print(combo_string('Hello', 'hi'))  # Output: 'hiHellohi'
print(combo_string('hi', 'Hello'))  # Output: 'hiHellohi'
print(combo_string('aaa', 'b'))     # Output: 'baaab'
