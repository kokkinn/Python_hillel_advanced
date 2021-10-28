def get_avg_data():
    file = open("../Flask_1/hw-1.csv", encoding="UTF8")
    next(file)
    weight = 0
    height = 0
    count = 0
    for line in file:
        b = line.split(", ")
        b = [float(i) for i in b]
        count += 1
        weight += b[2]
        height += b[1]
    return (f"The average wight is {round(weight / count * 0.45359237, 1)} kg \n"
            f"The average height is {round((height / count * 2.54), 1)} cm")


print(get_avg_data())

