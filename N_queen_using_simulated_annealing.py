import random
import numpy as np

#create random board
def create_board(n):
   board = [] 
   for i in range(n):
      board.append(random.randint(0,n-1))     
   return board

def eval(state):
    cnt = 0
    n = len(state)
    for i in range(n):
       for j in range(n):
          if(i == j):
            continue
          if(state[i] == state[j]):
            cnt += 1
          elif(abs(state[i]-state[j]) == abs(i-j)):
            cnt += 1

def random_next(state):
    n = len(state)
    i = random.randint(0,n-1)
    j = random.randint(0,n-1)
    while(state[i] == j):
        j = random.randint(0,n-1)
    return j    

def sigmoid(e1,e0,t):
    return 1/(1 + np.exp((e0 - e1)/t))

#simulated annealing
def simulated_annealing(n):
   curr_state = create_board(n)

   #maintain the best state
   best_state = curr_state
   best_eval = eval(curr_state)
   
   #maintain temperature
   temp = 1000

   #loop for eochs
   for _ in range(1000):
      #move to next state till termination(do 100 iteration)
      for _ in range(1000):
        next_state = random_next(curr_state)
        next_eval = eval(next_state)
        curr_eval = eval(curr_state)

        if(sigmoid(next_eval,curr_eval,t) > random.random()):
          curr_state = next_state
          if(next_eval < best_eval):
            best_eval = next_eval
            best_state = curr_state 
        #reduce the temprature
        temp -= 100

   #print the best state
   print("Solution: ",best_state)

simulated_annealing(4)