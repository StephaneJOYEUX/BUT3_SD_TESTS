import pandas as pd


a = pd.DataFrame({"a" : ["N", "J", "N", "G"], "b" : [5,6,7,8]})
b= a[a.a=="A"]

print(len(b))

