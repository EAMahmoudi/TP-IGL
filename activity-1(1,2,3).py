import unittest
import random


class StringHelper:
    '''
       la class de TP
    '''
    def __init__(self):
        return self
    def Joindre(self,list,sp):
        '''

        :param list: list de chaine de caractere
        :param sp: le separateur
        :return: la chaine de caractere construit avec les element de la list separer avec le sp
        '''
        str =""
        for l in list:
            if l == list[-1]:
                sp = ''
            str += l +sp
        return  str





class TP_Test(unittest.TestCase):

    def test_join(self):
        list = ['rouge','vert','blanc']
        self.assertEqual(StringHelper.Joindre(self,list,'-'),'rouge-vert-blanc')
