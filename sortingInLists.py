mylist = [6,2,9,7,1,5]
sortList = mylist.sort()
print(sortList)
#The output for this is 'None' because sort function does not return anything.


#To get the sorted list we can use the following code.
mylist.sort()
my_sorted_list = mylist
print(mylist)

#alternatively we can use a function called sorted
sortedList = sorted(mylist)
print(sortedList)
#The function sorted returns the list unlike the function sort