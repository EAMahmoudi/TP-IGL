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
    def fractionner(self, String, sp):
        '''
        :param String: la chaine de caractere
        :param sp: le separateur
        :return: une list des chaine deviser selon par le separateur
        '''
        list = []
        i = 0
        j = 0
        for c in String:
            if c in sp:
                list.append(String[i:j])
                j += 1
                i = j

            else:
                j += 1
        list.append(String[i:j])
        return list

    def eleminermotvide(self, String):
            '''

            :param String: chaine de caractere
            :return: la chaine String on suprimant les mot vide (et,ou,a,non)
            '''
            v = " "
            list = StringHelper.fractionner(0, String, ' ')
            for x in ['ou', 'et', 'a', 'non']:
                if x in list:
                    list.remove(x)
            str = ""
            sp = ' '
            for i in list:
                if i == list[-1]:
                    sp = ''
                str += i + sp

            return str



class TP_Test(unittest.TestCase):

    def test_join(self):
        list = ['rouge','vert','blanc']
        self.assertEqual(StringHelper.Joindre(self,list,'-'),'rouge-vert-blanc')
    def test_fract(self):
        list = ['rouge', 'vert', 'blanc']
        str = 'rouge,vert,blanc'
        self.assertEqual(StringHelper.fractionner(self, str, ','), list)
    def test_elim_V(self):
        str1 = 'rouge et blanc ou vert '
        str2 = "rouge blanc vert "
        self.assertEqual(StringHelper.eleminermotvide(self, str1), str2)
