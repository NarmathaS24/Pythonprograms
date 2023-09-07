import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(5, 4), index='A B C D E'.split(), columns='W X Y Z'.split())
print("Original DataFrame:\n", df)
df['New'] = np.random.randn(5)
print("Modified DataFrame:\n", df)