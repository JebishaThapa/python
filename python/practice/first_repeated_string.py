def repeated_letter(string):
    count = {}

    for i in string:
        if i in count:
            count[i] +=1
        else:
            count[i] = 1

    result = []
    for i in range(len(string)):
        store = string[i]
        if count[store] == 1:
            result.append(i)

    return result