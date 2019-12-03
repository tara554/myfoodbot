#######
#  CMPT120
#  myfoodbot2.py
#  Author: Tianle Zhong

#introduction
print("Welcome to the food bot!!")
initLists = input("\nExecute with new lists (n) or original lists (o)? ==> ")
print()

if initLists == "n":
    print("\nTo start please input the lists exactly using the list format")
    print("Lists should have at least 1 dish and not more than 10 dishes")
    print("Lists with prices correspond exactly to lists with dishes\n")

    vietnamese_dishes = eval(input("List of Vietnamese dishes ==> "))
    vietnamese_dish_prices = eval(input("List of Vietnamese dishes prices ==> "))
    print()
    italian_dishes = eval(input("List of Italian dishes ==> "))
    italian_dish_prices = eval(input("List of Italian dishes prices ==> "))

else:

    print("Now lists are initialized in the program")

    vietnamese_dishes = ["Pho", "Fried rice", "Pancake", "Steamed sticky rice"]
    vietnamese_dish_prices = [7.5, 6.75, 5.15, 8.25]

    italian_dishes = ["Pizza", "Meatball spaghetti", "Pasta"]
    italian_dish_prices = [7.15, 6.25, 5.0]


#trace printing in any case
print ("\n***TRACE Vietnamese ", vietnamese_dishes, vietnamese_dish_prices)
print ("\n***TRACE Italian ", italian_dishes, italian_dish_prices)

print("\nWELCOME TO THE FOOD ORDERING BOT!")

#greet user
def greetUser():
    name=input("\nWhat is your name?-->")
    print("\nHello dear "+name+"!")
    print('''We specialize in Vietnamese and Italian food. 
You will be able to order two dishes
If you are not sure what to ask we will choose for you!''')
    return name
name=greetUser()

#ask the dish
import random
dishRequest="n"
food=(input("\nWhat is your specific dish you want to order? ").capitalize())
if food in vietnamese_dishes:
    print("It seems that you like Vietnamese style of food")
    foodPlace=vietnamese_dishes.index(food)
    cost=vietnamese_dish_prices[foodPlace]
    print("\n***TRACE:dish "+food+" costs "+str(cost))
elif food in italian_dishes:
    print("It seems that you like Italian style of food")
    foodPlace=italian_dishes.index(food)
    cost=italian_dish_prices[foodPlace]
    print("\n***TRACE:dish "+food+" costs "+str(cost))
else:
    print("Since you indicated a dish not available, we are choosing one for you")
    dishRequest=input("But also, would you like to request that this dish is considered for the future? y/n ==>")
    if dishRequest=="y":
        print("\n***TRACE: suggested dish "+food)      
    dishChosen=random.choice(vietnamese_dishes+italian_dishes)
    print()
    print("The dish we chose for you is "+dishChosen)
    if dishChosen in vietnamese_dishes:
        foodPlace=vietnamese_dishes.index(dishChosen)
        cost=vietnamese_dish_prices[foodPlace]
        print("\n***TRACE:dish "+dishChosen+" costs "+str(cost))
    else:
        foodPlace=italian_dishes.index(dishChosen)
        cost=italian_dish_prices[foodPlace]
        print("\n***TRACE:dish "+dishChosen+" costs "+str(cost))

    
    
#show the available dishes with the codes
list1=[]
list2=[]
def printMenu():
    print("\nAll the available dishes are")
    print("============================")    
    var=0
    prefix="v"
    for elem in vietnamese_dishes:
        var+=1
        code1=prefix+str(var)
        list1.append(code1)
        code2="-"+elem
        print(code1+code2)
    print("============================")
    
    var1=0
    prefix2="i"
    for elem in italian_dishes:
        var1+=1
        code3=prefix2+str(var1)
        list2.append(code3)
        code4="-"+elem
        print(code3+code4)
    print("============================")
    return

#show the price
food2=input("\nDo you want to order another dish? y/n ==>")     
if food2=="y":
    printMenu()
    print()
    print('''\nPlease choose another dish by indicating the code that we provide 
You may order the same dish as before, if you want 
If you do not choose an existing dish we will choose one for you''')
    dishCode=input("\nProvide the dish code here (MUST BE a letter and a number) ==>")
    if dishCode in list1:
        position=list1.index(dishCode)
        dishName=vietnamese_dishes[position]
        price=vietnamese_dish_prices[position]
        totalPrice=str(cost+price)
        print("\n***TRACE:dish "+dishName +" costs "+str(price))
        print("\nPlease dear "+name+", pay the delivery person the total $"+totalPrice+", and a nice tip :)!")
        if dishRequest=="y":
            print("Thanks for your suggestion of "+food+"!")
        print("Nice doing business with you!")
    elif dishCode in list2:
        position=list2.index(dishCode)
        dishName=italian_dishes[position]
        price=italian_dish_prices[position]
        totalPrice=str(cost+price)
        print("\n***TRACE:dish "+dishName +" costs "+str(price))
        print("\nPlease dear "+name+", pay the delivery person the total $"+totalPrice+", and a nice tip :)!")
        if dishRequest=="y":
            print("Thanks for your suggestion of "+food+"!")
        print("Nice doing business with you!")
    else:
        print("Since you indicated a code dish not available, we are choosing one for you")
        dishChosen2=random.choice(vietnamese_dishes+italian_dishes)
        print("\nYour dish will be: "+dishChosen2)
        if dishChosen2 in vietnamese_dishes:
            foodPlace=vietnamese_dishes.index(dishChosen2)
            cost2=vietnamese_dish_prices[foodPlace]
            totalPrice=str(cost+cost2)
            print("\n***TRACE:dish "+dishChosen2+" costs "+str(cost2))
            print("\nPlease dear "+name+", pay the delivery person the total $"+totalPrice+", and a nice tip :)!")
            if dishRequest=="y":
                print("Thanks for your suggestion of "+food+"!")
            print("Nice doing business with you!")
        else:
            foodPlace=italian_dishes.index(dishChosen2)
            cost2=italian_dish_prices[foodPlace]
            totalPrice=str(cost+cost2)
            print("\n***TRACE:dish "+dishChosen2+" costs "+str(cost2))
            print("\nPlease dear "+name+", pay the delivery person the total $"+totalPrice+", and a nice tip :)!")
            if dishRequest=="y":
                print("Thanks for your suggestion of "+food+"!")
            print("Nice doing business with you!")

else:
    print("Ok! No more dishes for you")
    print("\nPlease dear "+name+", pay the delivery person the total $"+str(cost)+", and a nice tip :)!")
    if dishRequest=="y":
            print("Thanks for your suggestion of "+food+"!")
    print("Nice doing business with you!")

### END OF CODE


#REFLECTION:
#It took me approximately six hours to complete this assignment.
#From this assignment, I think I learned to use the for loops function and use index to find the location of a string in a list.

