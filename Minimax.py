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
def evaluate(state,player):
    """
       This is Evaluation method Which identify winner in board game and its implementation depends on game type.
       :param:state(usally one dimensional array and player by 1 or -1
       :return:player if player wins the game else 0
    """
    return player or 0
def minimaxFunctionI(state,player):
    """
        This is main method of the game and returns max Score of the player and dont use stack and search until
         the ends of the game tree.
        :param:state(usally one dimensional array and player by 1 or -1
        :return:maxScore of player
    """
    if evaluate(state,player):
        return evaluate(state)*player
    score=-2
    move=-1
    for i in range(len(state)):
        if state[i]==0:
            state[i]=player
            current=-functionName(state,-player)
            if current>score:
                score=current
                move=i
            state[i]=0
    if move==-1:
        return 0
    return score
def minimaxFunctionII(state,player,depth):
    """
        This is main method of the game and returns max Score of the player and dont use stack and search until
        untill given depth is reached.
        :param:state(usally one dimensional array and player by 1 or -1 and max depth to search
        :return:maxScore of player
    """
    if evaluate(state,player):
        return evaluate(array)*player
    score=-2
    move=-1
    for i in range(len(array)):
        if state[i]==0:
            array[i]=player
            current=-functionName(state,-player,depth-1)
            if current>score:
                score=current
                move=i
            state[i]=0
    if move==-1:
        return 0
    return score
def minimaxFunctionIII(state,player):
    """
        This is main method of the game and returns max Score of the player and use stack and search until
        the ends of the game tree.
        :param:state(usally one dimensional array and player by 1 or -1
        :return:maxScore of player
    """
    stack=[(state,player)]
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
                    if state[i]==0:
                        state[i]=player
                        stack.append((state,-player))
                        state[i]=0
            else:
                for i in range(len(array)):
                    if state[i]==0:
                        state[i]=player
                        stack.append(state[i],-player)
                        state[i]=0
    return maxScore
def minimaxFunctionIV(state,player,depth):
    """
        This is main method of the game and returns max Score of the player and use stack and search until
        depth of the become zero.
        :param:state(usally one dimensional array and player by 1 or -1 and depth
        :return:maxScore of player
    """
    stack = [(state, player,depth)]
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
                for i in range(len(state)):
                    if state[i]==0:
                        array[i]=player
                        stack.append((state,-player,depth-1))
                        array[i]=0
            else:
                for i in range(len(state)):
                    if state[i]==0:
                        state[i]=player
                        stack.append(state[i],-player,depth-1)
                        array[i] = 0
    return maxScore
def minimaxFunctionV(state,player):
    """
        This is main method of the game and returns max Score of the player and use queue and search until
        the ends of the game tree.
        :param:state(usally one dimensional array and player by 1 or -1
        :return:maxScore of player
    """
    queue=[(state, player)]
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
                for i in range(len(state)):
                    if state[i]==0:
                        state[i]=player
                        queue.append((state,-player))
                        state[i]=0
            else:
                for i in range(len(state)):
                    if state[i]==0:
                        state[i]=player
                        queue.append(state[i], -player)
                        state[i]=0
    return maxScore
def minimaxFunctionVI(state,player,depth):
    """
        This is main method of the game and returns max Score of the player and use queue and search until
        given depth become zero.
        :param:state(usally one dimensional array and player by 1 or -1 and depth.
        :return:maxScore of player
    """
    queue=[(state, player,depth)]
    maxScore=None
    while queue:
        currentA,current,depth=stack.pop(0)
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
                    if state[i]==0:
                        state[i]=player
                        queue.append((state,-player,depht-1))
                        state[i]=0
            else:
                for i in range(len(array)):
                    if state[i]==0:
                        state[i]=player
                        queue.append(state[i], -player,depth-1)
                        state[i]=0
    return maxScore





