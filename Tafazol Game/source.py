def game(number):
    MyList=[number//10,number%10]
    MyList.sort(reverse=True)
    return (MyList[0]-MyList[1])