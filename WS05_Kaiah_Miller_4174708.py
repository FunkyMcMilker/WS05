import numpy as np
import math

graph = {0 : [0, 1, 2, 3, 4],
         1 : [0, 1, 3],
         2 : [0, 2, 4],
         3 : [],
         4 : [],}

weights = { (0, 0) : 3/8,
            (0, 1) : 1/4,
            (0, 2) : 3/16,
            (0, 3) : 1/16,
            (0, 4) : 1/8,
            (1, 0) : 1/4,
            (1, 1) : 1/2,
            (1, 3) : 1/4,
            (2, 0) : 1/4,
            (2, 2) : 1/4,
            (2, 4) : 1/2 }

#question1a
#function creates the state diagram M from the corresponding maps 
def AdjMatrix(graph, weights):
    M = np.zeros((len(graph),len(graph[0]))) 
    # iterate with int values through graph
    for i in range(len(graph)):
        #target the nodes k, and their weights j
        for k, j in weights.items():
            #at a node k result matrix M will apply the node weight, j 
            M[k] = j
    return M;

#question 1b    
#funciton multiplies two matricies  
def mul(X,Y) :
    Z = np.zeros((len(X),len(Y[0]))) # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y 
            for k in range(len(Y)):
                Z[i][j] += X[i][k] * Y[k][j]
    return Z

#question 1c
#function to find the probibility of a win in n number games
def prob_win(n):
    probibility = 0
    #matrix of state changes will hold probibility after multiplication
    M1 = AdjMatrix(graph,weights)
    #initialize probibility in 1 game
    probibility = M1[0][3]
    #const version to multply M by
    M2 = AdjMatrix(graph,weights)
    #multiplying our probibility of state changes with its self
    moves = 0
    #setting initial probibility of 1 move to default A->D
    while moves <= n:
        #this will cause the probability of A->D (1/16) too add upp
        M1 = mul(M1,M2)
        probibility += M1[0][3]
        moves += 1
        #print(probibility)
        #print(m1)
    #divide the added probibility by the number of moves to yeild the converging probibility
    return probibility 

#questionTwo
# count is integers incrementing by 1, n is its upper limit
# a is divisible by 3 and is the difference between a square number and 1 
def questionTwo( n ):
    a = 0 
    count = 0
    while count <= n :
        #a mod 3 to find if a is divisable by 3
        if ( a % 3 == 0):
            #find if that values satifies a square minus 1
            if( math.sqrt(a + 1) % 1 == 0):
                #print(a)
                a += 1
            a += 1
        #if not we increment
        else:
            a += 1
        #finding the 2021st term
        if( count == 2021 ):
            print("The remainder of the 2021st term divided by 1000 is : ")
            print( a % 1000)
        count += 1

def gcd(x, y):
  
   while(y):
       x, y = y, x % y
  
   return x
  
#question3
#Determine the number of fractions in the pattern 
#below that are expressed in lowest terms
def questionThree( ):
    # n is the numerator 
    n = 1
    # d is the denominator 
    d = 2019
    # counter will be result
    counter = 0
    # x will hold GCD value
    x = 0
    #increment n while decrementing d
    while( d != n):
        #evaluate if n and d is in lowest terms if the gcd of n and d is 1
        x = gcd(n,d)
        #if in lowest terms increment the counter
        if  x == 1 :
            counter += 1
           # print(n, "/",d)
        n += 1
        d -= 1    
    print("The number of fractions in reduced form is : ", counter)    

   
#Driver Code below

X = AdjMatrix(graph,weights)
print("Self constructed state diagram is : ")
print(X)
probn = prob_win(200)
print("\nProbability of winning = ",probn,".")
print("\nExpected number of winning in 840 games = ",int(round(probn*840,0)),".")
print("\n")
questionTwo( 2021 )
print("\n")
questionThree()
