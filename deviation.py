# Calculate the mean and standard deviation of the following list:
# Numbers = [1,2,3,5,88,99,55,33,41,52]
import math
import numpy

Numbers = [1,2,3,5,88,99,55,33,41,52]
empty_List = []

total_Numbers = len(Numbers)
print(f"There are {total_Numbers} numbers in the list ")

for i in range(total_Numbers):
    empty_List.append(Numbers)
print(f"The sum of the given numbers in the list is", sum(Numbers))

# doing mean deviation

mean_deviation = sum(Numbers) / 10
print(f"*********The mean deviation of the numbers in the list is {mean_deviation}")

# finding out standard deviation

first_element0 = (Numbers[0] - mean_deviation)**2
second_element1 = (Numbers[1] - mean_deviation)**2
third_element2 = (Numbers[2] - mean_deviation)**2
fourth_element3 = (Numbers[3] - mean_deviation)**2
fifth_element4 = (Numbers[4] - mean_deviation)**2
sixth_element5 = (Numbers[5] - mean_deviation)**2
seventh_element6 = (Numbers[6] - mean_deviation)**2
eight_element7 = (Numbers[7] - mean_deviation)**2
ninth_element8 = (Numbers[8] - mean_deviation)**2
last_element9 = (Numbers[9] - mean_deviation)**2

#adding all the elements of the list
add_all_elements = first_element0 + second_element1 + third_element2 + fourth_element3 + \
                   fifth_element4 + sixth_element5 + seventh_element6 + eight_element7 + \
                   ninth_element8 + last_element9
#print(f"The sum of square of every element in the list is {add_all_elements}")

divide_sum = add_all_elements / total_Numbers

#print(f"The sum of square i.e {divide_sum} divided my number of elements i.e {total_Numbers} is",divide_sum)

standard_deviation = math.sqrt(divide_sum)
print(f"*************The standard deviation of the elements of the list is {standard_deviation}")



