import asyncio
import time


# split split the number into the two biggest divisors
# will be used for all numbers multiple times
async def split(n):
    biggest_Split = n**(1/2)
    if biggest_Split % 1 == 0:
        return (biggest_Split,biggest_Split)
    else:
        #print(biggest_Split%1)
        #print("bigsdas: ", int(biggest_Split))
        biggest_Split = int(biggest_Split)

        for i in range(biggest_Split-1):
            test_num = n/biggest_Split

            if test_num % 1 == 0:
                #print("thingw: ",biggest_Split,test_num)
                return (biggest_Split,test_num)
            biggest_Split -= 1
    return(1,n)

# if split[i][0] == 1 the add split[i][1] to factors
# else return tuple of two numbers that need to be split


async def check(tuple):
    #print(tuple)
    if tuple == None:
        return
    else:
        lowest_split = tuple[0]
        if lowest_split == 1:
            print(tuple[1])
            #factors = factors + str(tuple[1]) + ","
        else:
            await asyncio.gather(*[check(tup) for tup in (await asyncio.gather(split(int(tuple[0])),split(int(tuple[1]))))])


#%{
#   variables we need
#       first_Split
#           - called every time, tuple of two biggest divisors of n
#               - found with main()
#       nth_Split
#           - return a split of split[i][1] with split[i][0] != 1
#               - found in split()
#       factors
#           - string in form split[1][1],...,split[n][1]
#           - where split[i][0] == 1
#               - found in check
#       split_Needed
#           - tuple (split[0],split[1]) that need to be split
#               - found in check()
#}


# nested function that will conitue untill number is fully splited

async def main():
    s = time.perf_counter()
    #factors = ""
    # first split
    first_Split = await split(56516154546151561654646442646555164684661651615)
    #print("first split" , first_Split)
    # run check for the first split to see if given prime
    
    nth_Split = await check(first_Split)

    elapsed = time.perf_counter() - s
    print(f"executed in {elapsed:0.2f} seconds.")
    #for tuples in second_Split:
        #check(tuples)
    
    #print(factors)


asyncio.run(main())




