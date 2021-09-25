import copy
import re
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from collections import OrderedDict
import QuickFill.Algorithmes.InteractQuickFill as IFF
import os
import time
import json
import psutil
import random
from backend.settings import BASE_DIR




class QuickFillExecutionList(APIView):    
    def get(self, request, format=None):
            datas = {"Cette requetes montre que tu volais un peu experiment je te comprends mais cette application n'as pas de faille de securite ne pers pas ton temps"}
            return Response(datas)
        
        
    def post(self, request, format=None):
            
            
            DataEntreeBrute = eval(request.data.get("data").get("DataEntreeBrute"))
            DataGlobal = eval(request.data.get("data").get("DataGlobal"))

            Test = IFF.InteractQuickFill()
            Test.GetClassC()
            Entrer = DataGlobal[0]["Entrer"]
            IndiceColoneSortie = len(Entrer.keys())+1
            Sortie = DataGlobal[0]["Output"]
            ListeEntreFormeAtraiter = {}
            MonElment  = {}
            dict1= {}
            Montuple = []
            Maformuledecoupe = []


            for elt in DataGlobal:
                    for elt2 in elt:
                        MonElment[elt2] =  elt[elt2]
                        break
            
            for i in sorted (MonElment.keys()) :
                dict1[i] = MonElment[i]
            
            MonElment =  dict1
   
            for ett in MonElment:
                if MonElment[ett] == "ConstStr":
                        decoupekeyval = ett.split("***")
                        Formuletest = "ConstStr(" + decoupekeyval[1] + ")"
                        
                else:
                        Formuletest = Test.ExpressionConcatenateAbsolute2(Entrer,MonElment[ett])
                        Formuletest = list(Test.flatten(Formuletest[0][0]))
                        Formuletest = "".join(Formuletest)
                        
                        
                
                Maformuledecoupe.append(Formuletest)
            
            
           
            
            for elt in DataEntreeBrute:
                    Traite1 = {}
                    i = 0
                    chaineRetire = []
                    for ett in Maformuledecoupe:
                        i=i+1
                        if(ett.startswith("ConstStr")):
                                Traite1["b"+str(i)] = ett
                        else:
                                if i>1:
                                        TraiementEntrer = copy.deepcopy(elt["Entrer"]) 
                                        if Traite1["b"+str(i-1)].startswith("ConstStr"):
                                                continue
                                        else:
                                                chaineRetire.append(Traite1["b"+str(i-1)])
                                        for ettb in chaineRetire:
                                                for key in TraiementEntrer:
                                                        new_string = TraiementEntrer[key]
                                                        r1 =re.compile(re.escape(ettb))
                                                        indice = re.search(r1,new_string)
                                                        if indice == None:
                                                                continue
                                                        else:
                                                                last_char_index = indice.end()
                                                                new_string = new_string[last_char_index:]
                                                                TraiementEntrer[key] = new_string
                                                
                                        
                                else:
                                        TraiementEntrer = elt["Entrer"]
                                

                                Traite1["b"+str(i)] = Test.ExecuteElementFromExpressRegex(TraiementEntrer,ett)
                    

                    
                    ListeEntreFormeAtraiter[json.dumps(elt)] = [elt["position"],Traite1,elt["Entrer"]]
                            

     
            Montuple.append(json.dumps(MonElment))
            Montuple.append(json.dumps(Entrer))
            Montuple.append(Sortie)
            
            Montuple = tuple(Montuple)
            
            
            chemin = os.path.join(BASE_DIR, 'QuickFill/Algorithmes/interactData.txt')
            
            with open(chemin, 'w') as f:
                f.write(str(Montuple))
                        
                            
            datas = {}
            start = time.time()
            pid = os.getpid()
            ps = psutil.Process(pid)
            
            
            s = Test.GetInteractData()[0]
            programme = list(Test.GenerateStringProgram(s))
            random_index = random.randint(0,len(programme)-1)
            print("Progammme recuperer : " , programme[random_index])
            datas["NombreExemples"] = len(programme)
            datas["IndiceColoneSortie"] = IndiceColoneSortie
            
            
            
            for elt in DataEntreeBrute:
                    elt["Output"] = Test.ExecuteFonction(programme[0],ListeEntreFormeAtraiter[json.dumps(elt)][1],ListeEntreFormeAtraiter[json.dumps(elt)][2])
            
            
            datas["memoryQuickfill"] = ps.memory_info()[0]/1048576
            time.sleep(1)
            end = time.time()
            
            timewastQuickfill = end - start
            
            print("Temps execution  : " , timewastQuickfill)
            
            
            datas["timewastQuickfill"] = timewastQuickfill
            datas["DataFinalToBeReplace"] = DataEntreeBrute
            
            
            datas["indiceduprogrammechoisi"] = random_index
            datas["listedesprogrammes"] = programme
            return Response(datas)
    
    
    @classmethod
    def get_extra_actions(cls):
        return []





class QuickFillExecutionListWithFilter(APIView):    
    def get(self, request, format=None):
            datas = {"Cette requetes montre que tu volais un peu experiment je te comprends mais cette application n'as pas de faille de securite ne pers pas ton temps"}
            return Response(datas)
        
        
    def post(self, request, format=None):
            
            
            DataEntreeBrute = eval(request.data.get("data").get("DataEntreeBrute"))
            DataGlobal = eval(request.data.get("data").get("DataGlobal"))

            Test = IFF.InteractQuickFill()
            Test.GetClassC()
            Entrer = DataGlobal[0]["Entrer"]
            IndiceColoneSortie = len(Entrer.keys())+1
            Sortie = DataGlobal[0]["Output"]
            ListeEntreFormeAtraiter = {}
            MonElment  = {}
            dict1= {}
            Montuple = []
            Maformuledecoupe = []


            for elt in DataGlobal:
                    for elt2 in elt:
                        MonElment[elt2] =  elt[elt2]
                        break
            
            for i in sorted (MonElment.keys()) :
                dict1[i] = MonElment[i]
            
            MonElment =  dict1
   
            for ett in MonElment:
                if MonElment[ett] == "ConstStr":
                        decoupekeyval = ett.split("***")
                        Formuletest = "ConstStr(" + decoupekeyval[1] + ")"
                        
                else:
                        Formuletest = Test.ExpressionConcatenateAbsolute2(Entrer,MonElment[ett])
                        Formuletest = list(Test.flatten(Formuletest[0][0]))
                        Formuletest = "".join(Formuletest)
                        
                        
                
                Maformuledecoupe.append(Formuletest)
            
            
           
            
            for elt in DataEntreeBrute:
                    Traite1 = {}
                    i = 0
                    chaineRetire = []
                    for ett in Maformuledecoupe:
                        i=i+1
                        if(ett.startswith("ConstStr")):
                                Traite1["b"+str(i)] = ett
                        else:
                                if i>1:
                                        TraiementEntrer = copy.deepcopy(elt["Entrer"]) 
                                        if Traite1["b"+str(i-1)].startswith("ConstStr"):
                                                continue
                                        else:
                                                chaineRetire.append(Traite1["b"+str(i-1)])
                                        for ettb in chaineRetire:
                                                for key in TraiementEntrer:
                                                        new_string = TraiementEntrer[key]
                                                        r1 =re.compile(re.escape(ettb))
                                                        indice = re.search(r1,new_string)
                                                        if indice == None:
                                                                continue
                                                        else:
                                                                last_char_index = indice.end()
                                                                new_string = new_string[last_char_index:]
                                                                TraiementEntrer[key] = new_string
                                                
                                        
                                else:
                                        TraiementEntrer = elt["Entrer"]
                                

                                Traite1["b"+str(i)] = Test.ExecuteElementFromExpressRegex(TraiementEntrer,ett)
                    

                    
                    ListeEntreFormeAtraiter[json.dumps(elt)] = [elt["position"],Traite1,elt["Entrer"]]
                            

     
            Montuple.append(json.dumps(MonElment))
            Montuple.append(json.dumps(Entrer))
            Montuple.append(Sortie)
            
            Montuple = tuple(Montuple)
            
            
            chemin = os.path.join(BASE_DIR, 'QuickFill/Algorithmes/interactData.txt')
            
            with open(chemin, 'w') as f:
                f.write(str(Montuple))
                        
                            
            datas = {}
            start = time.time()
            pid = os.getpid()
            ps = psutil.Process(pid)
            
            
            s = Test.GetInteractData()[0]
            programme = list(Test.GenerateStringProgram(s))
            random_index = random.randint(0,len(programme)-1)
            print("Progammme recuperer : " , programme[random_index])
            datas["NombreExemples"] = len(programme)
            datas["IndiceColoneSortie"] = IndiceColoneSortie
            
            
            
            for elt in DataEntreeBrute:
                    elt["Output"] = Test.ExecuteFonction(programme[0],ListeEntreFormeAtraiter[json.dumps(elt)][1],ListeEntreFormeAtraiter[json.dumps(elt)][2])
            
            
            datas["memoryQuickfill"] = ps.memory_info()[0]/1048576
            time.sleep(1)
            end = time.time()
            
            timewastQuickfill = end - start
            
            print("Temps execution  : " , timewastQuickfill)
            
            
            datas["timewastQuickfill"] = timewastQuickfill
            datas["DataFinalToBeReplace"] = DataEntreeBrute
            
            
            datas["indiceduprogrammechoisi"] = random_index
            datas["listedesprogrammes"] = programme
            return Response(datas)
    
    
    @classmethod
    def get_extra_actions(cls):
        return []




class QuickFillExecutionListManyBlock(APIView):    
    def get(self, request, format=None):
            datas = {"Cette requetes montre que tu volais un peu experiment je te comprends mais cette application n'as pas de faille de securite ne pers pas ton temps"}
            return Response(datas)
        
        
    def post(self, request, format=None):
            
            
            DataEntreeBrute = eval(request.data.get("data").get("DataEntreeBrute"))
            DataGlobal = eval(request.data.get("data").get("DataGlobal"))

            Test = IFF.InteractQuickFill()
            Test.GetClassC()
            Entrer = DataGlobal[0]["Entrer"]
            IndiceColoneSortie = len(Entrer.keys())+1
            Sortie = DataGlobal[0]["Output"]
            ListeEntreFormeAtraiter = {}
            MonElment  = {}
            dict1= {}
            Montuple = []
            Maformuledecoupe = []


            for elt in DataGlobal:
                    for elt2 in elt:
                        MonElment[elt2] =  elt[elt2]
                        break
            
            for i in sorted (MonElment.keys()) :
                dict1[i] = MonElment[i]
            
            MonElment =  dict1
   
            for ett in MonElment:
                if MonElment[ett] == "ConstStr":
                        decoupekeyval = ett.split("***")
                        Formuletest = "ConstStr(" + decoupekeyval[1] + ")"
                        
                else:
                        Formuletest = Test.ExpressionConcatenateAbsolute2(Entrer,MonElment[ett])
                        Formuletest = list(Test.flatten(Formuletest[0][0]))
                        Formuletest = "".join(Formuletest)
                        
                        
                
                Maformuledecoupe.append(Formuletest)
            
            
           
            
            for elt in DataEntreeBrute:
                    Traite1 = {}
                    i = 0
                    chaineRetire = []
                    for ett in Maformuledecoupe:
                        i=i+1
                        if(ett.startswith("ConstStr")):
                                Traite1["b"+str(i)] = ett
                        else:
                                if i>1:
                                        TraiementEntrer = copy.deepcopy(elt["Entrer"]) 
                                        if Traite1["b"+str(i-1)].startswith("ConstStr"):
                                                continue
                                        else:
                                                chaineRetire.append(Traite1["b"+str(i-1)])
                                        for ettb in chaineRetire:
                                                for key in TraiementEntrer:
                                                        new_string = TraiementEntrer[key]
                                                        r1 =re.compile(re.escape(ettb))
                                                        indice = re.search(r1,new_string)
                                                        if indice == None:
                                                                continue
                                                        else:
                                                                last_char_index = indice.end()
                                                                new_string = new_string[last_char_index:]
                                                                TraiementEntrer[key] = new_string
                                                
                                        
                                else:
                                        TraiementEntrer = elt["Entrer"]
                                

                                Traite1["b"+str(i)] = Test.ExecuteElementFromExpressRegex(TraiementEntrer,ett)
                    

                    
                    ListeEntreFormeAtraiter[json.dumps(elt)] = [elt["position"],Traite1,elt["Entrer"]]
                            

     
            Montuple.append(json.dumps(MonElment))
            Montuple.append(json.dumps(Entrer))
            Montuple.append(Sortie)
            
            Montuple = tuple(Montuple)
            
            
            chemin = os.path.join(BASE_DIR, 'QuickFill/Algorithmes/interactData.txt')
            
            with open(chemin, 'w') as f:
                f.write(str(Montuple))
                        
                            
            datas = {}
            start = time.time()
            pid = os.getpid()
            ps = psutil.Process(pid)
            
            
            s = Test.GetInteractData()[0]
            programme = list(Test.GenerateStringProgram(s))
            random_index = random.randint(0,len(programme)-1)
            print("Progammme recuperer : " , programme[random_index])
            datas["NombreExemples"] = len(programme)
            datas["IndiceColoneSortie"] = IndiceColoneSortie
            
            
            
            for elt in DataEntreeBrute:
                    elt["Output"] = Test.ExecuteFonction(programme[0],ListeEntreFormeAtraiter[json.dumps(elt)][1],ListeEntreFormeAtraiter[json.dumps(elt)][2])
            
            
            datas["memoryQuickfill"] = ps.memory_info()[0]/1048576
            time.sleep(1)
            end = time.time()
            
            timewastQuickfill = end - start
            
            print("Temps execution  : " , timewastQuickfill)
            
            
            datas["timewastQuickfill"] = timewastQuickfill
            datas["DataFinalToBeReplace"] = DataEntreeBrute
            
            
            datas["indiceduprogrammechoisi"] = random_index
            datas["listedesprogrammes"] = programme
            return Response(datas)
    
    
    @classmethod
    def get_extra_actions(cls):
        return []