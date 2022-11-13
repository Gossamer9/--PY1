# TODO решить с помощью list comprehension и распечатать его
import pprint
ans = []
for i in range(16):
    dict = {}
    dict["dec"] = i
    dict["bin"] = bin(i)
    dict["oct"] = oct(i)
    dict["hex"] = hex(i)
    ans.append(dict)
pprint.pprint(ans)
