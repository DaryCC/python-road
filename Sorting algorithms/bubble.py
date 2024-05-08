def bubble(data):

    for _ in range(len(data)-1):
        # print(i)
        for i in range(len(data)-1):
            if data[i]>data[i+1]:
                data[i],data[i+1]=data[i+1],data[i]
    return data

# datos=[12,10,3,7,4]
datos=[12,3,6,6,10,3,7,4,4,90]
print(bubble(datos))