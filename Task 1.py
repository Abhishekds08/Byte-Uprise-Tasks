# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
database = pd.read_csv("svm_data.csv")
print(database)

# %%
database.head()

# %%
database.tail()

# %%
database.info()

# %%
database.drop_duplicates

# %%
database.describe()

# %%
database.plot(kind='hist')

# %%
database.plot(kind='bar')
database.sort_values(by='x1',ascending=False, axis=0, inplace=True)

plt.xlabel


# %%
datatop15 = database.tail(15)

# %%
datatop15.plot(kind='bar')

# %%



