"""
 * DO NOT ALTER OR REMOVE THIS  NOTICES OR THIS FILE HEADER FROM THE CODE.
 * This code is free software you can redistribute it and/or modify it
   published by the Good will of the author.

 * This code is distributed in the hope that it will be useful,Therefore
   use this code for your need or purpose and you can inform Error or part
   to modify or add.
 * Modifiying this code in a part or as Whole is possible and incremental modification is
   suggested please inform the author any modification you have done.
 * Please contact the Author,if you need additional information or have any questions.
     *Author:Duressa Shukuri
     *Email:duressashukuri2022@gmail.com
"""
def evaluate(array,player):
    return player
def minimaxFunctionI(array,player):
    if evaluate(array,player):
        return evaluate(array)*player
    score=-2
    move=-1
    for i in range(len(array)):
        if array[i]==0:
            array[i]=player
            current=-functionName(array,-player)
            if current>score:
                score=current
                move=i
            array[i]=0
    if move==-1:
        return 0
    return score
def minimaxFunctionII(array,player,depth):
    if evaluate(array,player):
        return evaluate(array)*player
    score=-2
    move=-1
    for i in range(len(array)):
        if array[i]==0:
            array[i]=player
            current=-functionName(array,-player,depth-1)
            if current>score:
                score=current
                move=i
            array[i]=0
    if move==-1:
        return 0
    return score
def minimaxFunctionIII(array,player):
    stack=[(array,player)]
    maxScore=None
    while stack:
        currentA,currentp=stack.pop()
        currentScore=evaluate(currentA)
        if currentScore!=0:
            if maxScore is None:
                maxScore=currentScore
            elif player==1:
                maxScore=max(maxScore,currentScore)
            else:
                maxScore=min(maxScore,currentScore)
        else:
            if player==1:
                for i in range(len(array)):
                    if array[i]==0:
                        array[i]=player
                        stack.append((array,-player))
                        array[i]=0
            else:
                for i in range(len(array)):
                    if array[i]==0:
                        array[i]=player
                        stack.append(array[i],-player)
                        array[i]=0
    return maxScore
def minimaxFunctionIV(array,player,depth):
    stack = [(array, player,depth)]
    maxScore = None
    while stack:
        currentA,currentp,depth=stack.pop()
        currentScore=evaluate(currentA)
        if currentScore!=0:
            if maxScore is None:
                maxScore=currentScore
            elif player==1:
                maxScore=max(maxScore, currentScore)
            else:
                maxScore=min(maxScore, currentScore)
        else:
            if player==1:
                for i in range(len(array)):
                    if array[i]==0:
                        array[i]=player
                        stack.append((array,-player,depth-1))
                        array[i]=0
            else:
                for i in range(len(array)):
                    if array[i]==0:
                        array[i]=player
                        stack.append(array[i],-player,depth-1)
                        array[i] = 0
    return maxScore
def minimaxFunctionV(array,player):
    queue=[(array, player)]
    maxScore=None
    while queue:
        currentA,current=stack.pop(0)
        currentScore=evaluate(currentA)
        if currentScore!=0:
            if maxScore is None:
                maxScore=currentScore
            elif player==1:
                maxScore=max(maxScore, currentScore)
            else:
                maxScore=min(maxScore, currentScore)
        else:
            if player==1:
                for i in range(len(array)):
                    if array[i]==0:
                        array[i]=player
                        queue.append((array,-player))
                        array[i]=0
            else:
                for i in range(len(array)):
                    if array[i]==0:
                        array[i]=player
                        queue.append(array[i], -player)
                        array[i]=0
    return maxScore





