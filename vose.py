# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 16:52:38 2012

@author: seveibar
"""

#Based on Vose's Alias Method
#http://www.keithschwarz.com/darts-dice-coins/

import random

class Vose():
    
    """
    Example plist
    
    [
        ('A':25),
        ('B':65),
        ('C':10)
    ]
    
    *The probabilites do not have to add up to 100
    
    """
    def __init__(self,plist):
        probs = [[p[0],float(p[1])] for p in plist]
        
        
        #Normalize probabilites
        probSum = sum([i[1] for i in probs])

        for prob in probs:
            prob[1] = prob[1]/probSum
        
        #Setup
        
        n = len(probs)

        Alias = []#Tuples with coin flip result
        Prob = []#Unfair coin probability
        
        Small = []
        Large = []
        
        
        #Scale Probabilies
        
        for prob in probs:
            prob[1] *= n
            if (prob[1] < 1):
                Small.append(prob)
            else:
                Large.append(prob)
                
        if Large == []:
            #fix for the issue that Large is empty caused by bad luck in calculations
            Large = Small[:]
            Small = []
        
        #Sort into board
        while Small!=[] and Large!=[]:
            l = Small.pop(0)
            g = Large.pop(0)
            Prob.append(l[1])
            Alias.append((l[0],g[0]))
            g[1] -= (1 - l[1])
            if (g[1] >= 1):
                Large.append(g)
            else:
                Small.append(g)
        while Large!=[]:
            g = Large.pop(0)
            Prob.append(1)
            Alias.append((g[0],g[0]))
            g[1] -= 1
            if (g[1] >= 1):
                Large.append(g)
            else:
                Small.append(g)
        
        #Numerical inaccuracy may leave Small with items,
        #I'm going to ignore them for now (they are negligible)
        
        self.Prob = Prob
        self.Alias = Alias
        self.n = n
        self.probs = probs
    
    #Get a random weighted value
    def get(self):
        i = random.randint(0,len(self.Prob) - 1)
        if self.Prob[i] >= random.random():
            return self.Alias[i][0]
        else:
            return self.Alias[i][1]
        

#Uncomment the following lines to see test

#vose = Vose([('a',25),('b',65),('c',10)])
#accuracy = 10000 #increase for better results
#d = {'a':0,'b':0,'c':0}
#for i in range(accuracy):
#    d[vose.get()] += 1./accuracy
#print "\n".join([v + " : " + str(round(k*1000)/1000.) for v,k in d.items()])
