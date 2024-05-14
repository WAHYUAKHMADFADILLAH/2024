import numpy as np
# buat data jumlah kamar (x)
bedroom = np.array([1,1,2,2,3,4,4,5,5])

# Data harga rumah, Asumsi dalam dolar (y)
house_price = np.array([15000,18000,27000,34000,50000,60000,65000,85000,90000])

# menampilkan scatter plot dari data set
import matplotlib.pyplot as plt
%matplotlib inline
plt.scatter(bedroom,house_price) 
