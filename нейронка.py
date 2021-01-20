import numpy as np

# Сигмоида 
def  nonlin(x):
    return 1/(1+np.exp(-x))
    

X = np.array([  [0,0,0,1,0],
                [1,0,1,0,0],
                [0,1,0,0,1],
                [1,1,1,0,0],
                [0,0,0,1,0],
                [1,0,0,1,1],
                [0,1,0,1,1],
                [0,0,0,0,0]])
               
    
            
y = np.array([[0,1,1,1,0,0,0,1]]).T


np.random.seed(1)


syn0 = 2 * np.random.random((5,1)) - 1

for iter in range(100000):

  
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))

    
    l1_error = y - l1

   
    l1_delta = l1_error * nonlin(l1) 

    syn0 += np.dot(l0.T,l1_delta) 


new = np.array([1,0,1,0,1])
outputs = nonlin(np.dot(new,syn0))
c = nonlin(-15)
print(c)
  
    
