def sort(values):
    for i in range(len(values)):
        for j in range(i):
            if values[i] < values[j]:
                values[i], values[j] = values[j], values[i]
