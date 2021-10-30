import matplotlib.pyplot as plt
import numpy as np

divisions = ["Cột A", "Cột B", "Cột C", "Cột D", "Cột E"]
division_average_marks = [70,82,73,65,68]
varlance = [5,8,7,6,4]

plt.barh(divisions, division_average_marks, xerr=varlance, color = "Blue")
plt.title("Biểu đồ cột")
plt.xlabel("Divisions")
plt.ylabel("Marks")
plt.show()

