ones      = '(I[VX]|V?I{0,3})'
tens      = '(X[LC]|L?X{0,3})'
hundreds  = '(C[DM]|D?C{0,3})'
thousands = '(M{0,3})'

regex_pattern = r"%s%s%s%s$" % (thousands, hundreds, tens, ones)

import re
print(str(bool(re.match(regex_pattern, input()))))
