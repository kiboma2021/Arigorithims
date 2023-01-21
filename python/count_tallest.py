'''
You are in charge of the cake for a child's birthday. You have decided 
the cake will have one candle for each year of their total age. 
They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

Example

candles=[1,8,4,5,8,2,6,8]

should return 3
'''
def birthdayCakeCandles(candles):
    # Write your code here
    candles=sorted(candles,reverse=True)
    tallest_candle=candles[0]
    count=0
    for i in candles:
        if i==tallest_candle:
            count+=1
    return count
