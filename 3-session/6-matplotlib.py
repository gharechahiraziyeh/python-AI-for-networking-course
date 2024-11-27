import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = ["a", "b", "c", "d", "e"]
plt.plot(x , y, marker = "+")
plt.xlabel("Numbers")
plt.ylabel("Alphabet")
plt.title("alpha-numeric plot")
plt.annotate("middle value", xy=(3, "c"), xytext=(3, 4), arrowprops=dict(facecolor= "red", arrowstyle="->"))
plt.show()