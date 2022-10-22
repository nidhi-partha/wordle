import matplotlib.pyplot as plt
import tkinter as tk
y=['1', '2', '3', '4', '5', '6']
 

root = tk.Tk()

# getting values against each value of y
x=[5,3,5,3,2,1]
plt.barh(y, x, color ='#6AA964')
 
# setting label of y-axis
plt.ylabel("Tries Taken", fontweight = 'bold')
 
# setting label of x-axis
plt.xlabel("Amount of Times", fontweight = 'bold')
plt.title("Guess Distribution", fontweight = 'bold')
plt.show()

