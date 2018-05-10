
try:

    f = open("nene_index.txt", 'r')
    index = f.readline()
    file_index = int(index)


    f.close()

    f = open("nene_index.txt", 'w')
    file_index += 1
    index_number = str(file_index)

    file_index //3


    f.write(index_number)
    print(file_index)

except:
    f = open("nene_index.txt", 'w')
    f.write("1")
    print("1")




f.close()

