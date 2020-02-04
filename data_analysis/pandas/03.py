import numpy as np
import pandas as pd
if __name__ == '__main__':
     df = pd.DataFrame(np.arange(12).reshape(3,4))
     # print(df)

     df2 = pd.DataFrame(np.arange(12).reshape(3,4), index=list('abc'), columns=list('wxyz'))
     print(df2)

     print(df2.shape)
     print(df2.dtypes)
     print(df2.ndim)
     print(df2.index)
     print(df2.columns)
     print(df2.values)

     print(df2.head(1))
     print(df2.tail(2))
     print(df2.info())
     print(df2.describe())