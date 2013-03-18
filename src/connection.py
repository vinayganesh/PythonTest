'''
Created on Mar 17, 2013

@author: vganesh
'''

class connection():
    '''
    classdocs
    '''
    
    def add(self,a,b):
        return a+b
         
    def setConnectionString(self,connectionString):
        self.connectionString = connectionString
        return self
         
    def getConnectionString(self):
        return self.connectionString

