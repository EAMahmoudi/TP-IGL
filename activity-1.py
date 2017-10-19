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
    def __init__(self):
        return 0

    def nb_occur(self, String, Mot):
        '''

        :param String: la chaine de caractere
        :param Mot: le Mot a chercher
        :return: cherche le nombre d'occurence de Mot dans chaine
        '''
        c = 0
        if len(String) == 0:
            raise StringVide
        list = StringHelper.fractionner(0, String, ' ')
        for w in list:
            if w == Mot:
                c += 1
        return c

    def incr_char(self, String):
        '''
        :param String: La chaine de caractere
        :return: la chaine String mais touts les lettre sont incrementer
        '''
        str = ""
        for c in String:
            if c.isalpha():
                str += chr(ord(c) + 1)
            else:
                str += c
        return str
    def Magiscule(self,String):
     '''
     :param String: La chaine de caractere
     :return: la chaine String en mettant au majiscule toutes les premier lettre de chaque phrase
     '''
     cap = True
     for c,i in enumerate(String) :
         if cap and String[c] != ' ':
             String = String[:c] +String[c:].capitalize()
             cap = False
         if String[c] == '.' :
             cap = True
     return String
class error(Exception):
    pass

class StringVide(error):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message







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

    def test_nboc(self):
        str=" penser a acheter 3 kilo pomme de tere , 2 kilo tomate et 1 kilo courgette ."
        self.assertEqual(StringHelper.nb_occur(0,str,'kilo'),3)

    def test_Mag(self):
        str1="bonJour . ce Message a Ete fais dans le BUT de tester la fonction . Enjoy it !"
        str2="Bonjour . Ce message a ete fais dans le but de tester la fonction . Enjoy it !"
        self.assertEqual(StringHelper.Magiscule(0,str1),str2)

        str="asde poij"
        str2="btef qpjk"
        self.assertEqual(StringHelper.incr_char(0,str),str2)


