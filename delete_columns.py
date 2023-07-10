import pandas as pd
f = pd.read_csv("cut_test.csv")
keep_col = ['Zeit','ETOTAL','PAC','PDC']
new_f = f[keep_col]
new_f.to_csv("usable_data.csv", index = False)
