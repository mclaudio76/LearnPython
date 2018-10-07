import pandas as pd
import matplotlib.pyplot as plt

data = [ [1,2,3], [4,5,6], [7,8,9]]
cols = [ 'Alfa', 'Beta', 'Gamma']
idx  = [ 'R1', 'R2', 'R3']

df = pd.DataFrame(data=data, index=idx, columns=cols)

#my_df = pd.DataFrame(data=[4,5,6,7], index=range(0,4), columns=['A'])
#print(my_df)

dati = [ ["Francia", 2], ["Italia", 4] , ["Germania",4] , ["Austria", 0]]
palmares = pd.DataFrame(data=dati, index=range(0, len(dati)), columns=["Nazione","Vittorie"])
#print(palmares)

#for n in palmares["Vittorie"]:
#    print(n)

print(palmares.loc[1,'Nazione'])

palmares.plot()
#plt.show()