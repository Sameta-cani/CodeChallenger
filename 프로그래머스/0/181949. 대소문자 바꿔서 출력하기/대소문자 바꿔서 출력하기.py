str = input()

print(''.join([c.upper() if c.islower() else c.lower() for c in str]))