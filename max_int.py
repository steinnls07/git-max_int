num_int = int(input("Input a number: "))   
#While a postive number is input it is added to the list of numbers
#When a negative nr. is entered it prints out the max of the list
lst = []
while  num_int >= 0:
   lst.append(num_int)
   num_int = int(input("Input a number: "))

else:

    print("The maximum is", max(lst))   

