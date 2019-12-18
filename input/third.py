import input.second_copy
from input.second_copy import F_ERRORE


print("third")

input = input.second_copy.manage_input()
d = input.second_copy.validate_display(input)


if F_ERRORE in d:
    print(d[F_ERRORE])
else:
    print(d)


# second.validate_display('a b c d e r')
# second.validate_display('elvis presley')
