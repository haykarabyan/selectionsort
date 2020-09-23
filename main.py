def selection_sort(array):
    initial_length = len(array)
    for current_length in range(initial_length, 0, -1):
        max_index = 0
        for i in range(current_length):
            if array[i] > array[max_index]:
                max_index = i

        temp = array[max_index]
        array[max_index] = array[current_length - 1]
        array[current_length - 1] = temp



def main():
    mylist = input("Enter the number of array members, seperated by coma  ")
    mylist = mylist.split(',')
    for i in range(len(mylist)):
        mylist[i] = int(mylist[i])

    selection_sort(mylist)
    print(mylist)


main()
