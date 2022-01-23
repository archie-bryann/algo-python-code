def laptopRentals(times):
    laptops = 0
    main = []
    intersections = []
    for i in times:
        start = i[0]
        end = i[1]
        for j in times:
            if (j[0] >= start and j[0] < end) and (j[0] != start and j[1] != end):
                if i in main:
                    laptops += 0
                else:
                    main.append(i)
                intersections.append([j[0],j[1]])
    
    # main
    if main != []:
        for i in main:
            laptops+=1
            for j in main:
                if j[0] > i[1]:
                    laptops-=1
    
    # others
    if intersections == []:
        laptops = 1
    else:
        others = [i for i in times if i not in main]
        for i in others:
            laptops += 1
            for j in others:
                 if j[0] > i[1]:
                    laptops-=1
    
       
   

        
    return "" + str(times) + " = " + str(laptops)
        
            
            

print(laptopRentals([[0,2], [1,4], [4,6], [0,4], [7,8], [9,11], [3,10]])) # 3
print(laptopRentals([[0,4], [2,3], [2,3], [2,3]])) # 4
print(laptopRentals([[1,5], [5,6], [6,7], [7,9]])) # 1
