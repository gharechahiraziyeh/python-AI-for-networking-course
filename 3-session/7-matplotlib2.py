import matplotlib.pyplot as plt   
x = [1, 2, 3, 4, 5]
y1 = ["a", "b", "c", "d", "e"]
y2 = ["F", "G", "H", "I", "J"]

plt.plot(x, y1, marker="o", color="black", linestyle="-.", label="y1 data")
plt.plot(x, y2, marker="o", color="green", linestyle="--", label="y2 data")

plt.xlabel("Numbers")
plt.ylabel("Alphabet")
plt.title("alpha-numeric plot")
plt.legend()

# set background
plt.grid(True, linestyle=":", linewidth=0.5, color="blue")
plt.gca().set_facecolor("lightblue")

# add note
plt.text(3, -3, "This is test plot", fontsize=12, color="red")
plt.show()