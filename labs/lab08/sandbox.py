# Lab 08 Sandbox - Follow along with the lab instructions

f = open("data/scores.txt", "w")
f.write("85\n")
f.write("92\n")
f.write("78\n")
f.close()

print("Scores saved to file!")

f=open('data/scores,txt', "r")

for line in f:
    print(line)
    f.close()

# Try running this program again - scores will be empty!
