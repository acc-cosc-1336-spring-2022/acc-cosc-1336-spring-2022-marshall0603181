#main program
import lists

#nums = [99,100,101,102]

#print("---------")

#lists.loop_list_w_for(nums)
#lists.loop_list_w_while(nums)

#print("---------")
#for n in nums:
#    print(n)
    
#lists.collect_home_values()

list1 = []

add_more = "y"

while(add_more) == "y":
    item1 = input("enter item ")
    list1.append_item_to_list(item1, list1)
    add_more = input("Enter y to continue")

for item in list1:
    print(item)