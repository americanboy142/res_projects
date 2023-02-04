import asyncio
import time


# split split the number into the two biggest divisors
# will be used for all numbers multiple times until in form (1,prime)
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


#%{
# if split[i][0] == 1 then print split[i][1]
# else check( split( tuple[0] and tuple[1] ) )
#
# recursive function continues untill all prime factors are printed
#}
async def check(tuple):
    #print(tuple)
    if tuple[0] == None:
        print("given empty tuple")
    else:
        lowest_split = tuple[0]
        if lowest_split == 1:
            # star added to check work at end
            print(tuple[1], "*")
            return
            #factors = factors + str(tuple[1]) + ","
        else:
            await asyncio.gather(*[check(tup) for tup in (await asyncio.gather(split(int(tuple[0])),split(int(tuple[1]))))])


#%{
#   where everything is ran
#       - calls check() with split(n)
#   n is number that needs to be factored
#   Start, Ends and Prints timer to see how long factoring took
#}
async def main(n):
    s = time.perf_counter()

    #first_Split = await split(44215651515)
    #print("first split" , first_Split)
    #await check(first_Split)

    await check(await split(n))

    elapsed = time.perf_counter() - s
    print(f"Time: {elapsed:0.3f} seconds.")
    


asyncio.run(main(41165562616156165156165))




