""" Table of Squares and cubes (0-5) """

print(f'{"number":>6} {"square":>6} {"cube":>6}') # Table header.
for number in range(6):
    # Calculate/display squares and cubes, right-aligned,
    # formatted to 6 character width.
    print(f'{number:>6} {number ** 2:>6} {number ** 3:>6}') 