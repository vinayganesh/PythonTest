'''
Created on Mar 17, 2013

@author: vganesh
'''
import unittest
import connection


class Test(unittest.TestCase):

    global object
    
    def setUp(self):
        self.object = connection.connection()


    def tearDown(self):
        pass


    def test_add(self):
        value = self.object.add(10, 20)
        self.assertEqual(value,30)
        
    def test_getsetConnectionString(self):
        self.object.setConnectionString("A=B&C=D")
        self.assertEqual(self.object.getConnectionString(),"A=B&C=D")
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()