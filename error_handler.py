file = open("youtube.txt", "w")

try:
    file.write("learning python")
finally:
    file.close()

with open("youtube.txt", "w") as file:
    file.write("Hello")
