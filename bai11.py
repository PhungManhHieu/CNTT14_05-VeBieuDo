import matplotlib.pyplot as plt
import numpy as np

divisions = ["Cột A", "Cột B", "Cột C", "Cột D", "Cột E"]
division_average_marks = [70,82,73,65,68]
boys_average_marks = [68,67,77,61,70]

index = np.arange(5)
width = 0.30

plt.bar(index, division_average_marks, width, color = "green" , label = "division marks")
plt.bar(index+width, boys_average_marks, width, color = "blue" , label = "boys marks")
plt.title("Horizontally Stacked bar graphs")

plt.xlabel("Marks")
plt.ylabel("divisions")
plt.xticks(index+ width/2, divisions)

plt.legend(loc="best")

plt.show()