import matplotlib.pyplot as plt
import numpy as np

divisions = ["Cột A", "Cột B", "Cột C", "Cột D", "Cột E"]
boys_average_marks = [68,67,77,61,70]
girls_average_marks = [72,97,69,69,66]


index = np.arange(5)
width = 0.30

plt.bar(index, boys_average_marks, width, color = "blue" , label = "boys marks")
plt.bar(index, girls_average_marks, width, color = "red" , label = "girls marks", bottom=boys_average_marks)
plt.title("Horizontally Stacked bar graphs")

plt.xlabel("Marks")
plt.ylabel("divisions")
plt.xticks(index+ width/2, divisions)

plt.legend(loc="best")

plt.show()