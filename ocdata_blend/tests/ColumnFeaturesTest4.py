# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

import numpy as np
import pandas as pd
import unittest

from ColumnFeatures_2 import ColFeatures

##data = pd.read_csv('Georgia_AllTenders_D1strow_.csv')




class ColumnfeaturesTest(unittest.TestCase):
    
    

    def test_data_not_zero(self):
    	list_of_list = [('id', 'procurring_entity_id', 'tender_type' , 'tender_registration_number'), ('Brian', 'unladen swallow', 'dead parrot' , '2') ]
    	data = pd.DataFrame(list_of_list)
    	cF = ColFeatures(data)
        ##print cF.get_col_names(data)
        self.assertNotEqual(cF.get_col_names(), 0.0)
        

   
   
    def test_returns_col_names(self):
    	list_of_list = [('id', 'procurring_entity_id', 'tender_type' , 'tender_registration_number'), ('Brian', 'unladen swallow', 'dead parrot' , '2') ]
    	data = pd.DataFrame(list_of_list)
        
        ##  Here the class is instantiated
        cF = ColFeatures(data)
        
        actual = cF.get_col_names()
        
        ##self.assertNotEqual(cF.get_col_names(), 0.0)
        expected = ['id', 'procurring_entity_id', 'tender_type' , 'tender_registration_number']
        
        self.assertListEqual(actual, expected, msg='Lists did not match')
   
