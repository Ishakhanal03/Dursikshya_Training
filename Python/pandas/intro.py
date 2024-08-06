# pandas is a python libraray used to analyze the data and manipulating data.

import pandas as pd
x=[1,3,5,9]
reslut=pd.Series(x)
print(reslut)

y=pd.Series(x,index=["a","b","c","d"])
print(y)
print(y['b'])



# dataFrame
dataset={
    "subjects":["html","css","js","Python"],
    "marks":[20,30,50,90]
}
reslut=pd.DataFrame(dataset)
print(reslut)


