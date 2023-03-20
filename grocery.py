list = {"milk":0,"strawberry":0, "mango":0,"mango":0 , "tortilla":0,
        "sweet potato":0,"apple":0 ,"banana":0,"ice cream":0, "lettuce":0,"tomato":0,"carrot":0}
while True:
    try:
       item = input()
       list[item]=list[item] + 1
    except(KeyError,ValueError,NameError):
        pass
    except EOFError:
        for x in list:
            if list[x] != 0:
                print(list[x], x.upper())        
        break        