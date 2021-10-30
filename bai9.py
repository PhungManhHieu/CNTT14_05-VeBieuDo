import matplotlib.pyplot as plt
import numpy as np

divisions = ["Cột A", "Cột B", "Cột C", "Cột D", "Cột E"]
division_average_marks = [70,82,73,65,68]

plt.bar(divisions, division_average_marks, color = "Blue")
plt.title("Biểu đồ cột")
plt.xlabel("Divisions")
plt.ylabel("Marks")
plt.show()

