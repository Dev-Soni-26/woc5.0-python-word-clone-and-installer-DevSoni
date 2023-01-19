#lists 

courses = ["history", "math", "eng", "phy"]

print(len(courses))   #length of list 
print(courses[0])     #particular index
print(courses)        #whole list 
print(courses[-1]) #last index is -1   
print(courses[0:2])  #print index 0 and 1
print(courses[2:])  #slicing prints indexes 2 till end


new_course = ["new"]
#list methods
# adding a word at the end
courses.append("art")

#adding a word at specific index
courses.insert(1,"modern")
#instead of a word an entire list can be inseerted
courses.insert(0, new_course) #alternative using append

#remove command
courses.remove("math")
last_word = courses.pop() #removes last value from list 
print(last_word)

#reversing 
courses.reverse()
print(courses)

#sorting 
#courses.sort() #ascending order

number_list= [1,2,35,32,12,6]
number_list.sort()
print(number_list)
number_list.sort(reverse = True ) #descending sort 

#sorted function sorts without changing the list 
#other function 

nums=[1,5,4,3,78,65,34,1]
print(min(nums), max(nums), sum(nums))


#checking index of an element
print(nums.index(34))

print( 34 in nums) #returns boolean value 




#looping in lists 
woc_5 = ["html", "python", "css", "java"]

for i, lang in enumerate(woc_5, start =1):
    print(i, lang)



#joining values of a list
names= ['Victor', 'Allen', 'lisa']
str_names= '|-|'.join(names)
print(str_names)

#splitting a string
split_str_names = str_names.split('|-|')
print(split_str_names)