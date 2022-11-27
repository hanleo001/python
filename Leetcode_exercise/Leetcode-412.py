def some(n):    
    for i in range(n-1):
        if (i+2)%15==0:
            answer=answer+["FizzBuzz"]
        elif(i+2)%3==0:
            answer=answer+["Fizz"]
        elif(i+2)%5==0:
            answer=answer+["Buzz"]
        else:
            answer=answer+[i+2]
    return answer