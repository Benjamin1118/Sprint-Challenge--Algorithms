#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) a(n*n*n)/ a(n*n) == a(n) 
    So this is O(n)


b) this calls n 2x 1: in the for loop, 2: in the while loop
but in the while loop j is incremented 2x
    So this one is O(n log n)


c) This one calls bunnies, when bunnies is 0 it ends
 so this one is O(n)
 

## Exercise II
start = n[0]
end = len(n)
middle = range(start, len(n)) //2
#while start <= end:
    test = drop_egg(middle)
        #if egg breaks too high take off last half of #floors
        if egg breaks:
            end = middle
            middle = range(0, end)//2
            print(middle)
            test.drop_egg(middle)


        #if egg survives try a higher height, remove # #    first half

        else:
            start = middle
            middle = range(start, len(n))//2
            print(middle)
            test. drop_egg(middle)

runtime complexity is worst case O(n)

