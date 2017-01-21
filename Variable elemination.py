


import numpy as np
import math

class variable_elemination:
   def __init__(self, Vs, Ps, O, Q):

       self.observations = O
       self.Fs = Ps
       self.Vs = [element for element in Vs if element not Q]



       for X in Vs:


class node:
   def __init__(self, name, parents, obs=None):
       self.name = name
       self.observed = obs
       self.matrix = np.zeros((1+parents,math.exp(2,1 + parents)))

   def getvalue(self, truth_values):
       length = len(truth_values)
       liste = []

        # Hello future us:
        # for anzahl der reihen
        # wenn truth values == erste elemente matrix
        # index der reihe für prob summierung
       for i in range(len(self.matrix[:,length-1])):
           if(np.array_equal(self.matrix[i,0:length],truth_values)):
               liste.append(i)

    # Nächste Schritte, jedes listen element (index) nimm letztes
    # element der jeweiligen row (Probability) und summiere diese auf


   def setobserved(self, boolean):
       self.observed = boolean


def probability(self, variables):
    if


    numerator =
    divisor

def computed(self, node)






    return



if __name__ == "__main__":
        influenza = node("influenza")
        wheezing = node("wheezing")
        coughing = node("coughing")
        bronchitis = node("bronchitis")
        sore_throat = node("sore_throat")

        Vs = [influenza, coughing, wheezing, bronchitis]
        Ps = [0.6 , 0.4 , 0.8 , 0.2]
        O = [(sore_throat, true)]

        for x in O :
            x[0].setobserved(x[1])


        variable_elemination(Vs, Ps, O, Q)









