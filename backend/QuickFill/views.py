from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import QuickFill.Algorithmes.InteractQuickFill as IFF
import os
import time
import json
import psutil
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
            Montuple = []
            
            Maformuledecoupe = []

        
            
            
            for elt in DataGlobal:
                    for elt2 in elt:
                        MonElment[elt2] =  elt[elt2]
                        break
            
            
            for ett in MonElment:
                    Formuletest = Test.ExpressionConcatenate(Entrer,MonElment[ett])
                    Formuletest = Formuletest[-1][0]
                    Formuletest = "Concatenate(" + "˅".join(Formuletest) + ")"
                    Maformuledecoupe.append(Formuletest)
                    
            for elt in DataEntreeBrute:
                    Traite1 = {}
                    i = 0
                    for ett in Maformuledecoupe:
                        i=i+1
                        Traite1["b"+str(i)] = Test.ExecuteElementFromExpressSustr2(elt["Entrer"],ett)
                    
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
            print("Afaire ici mmmmmm : " , s) 
            programme = list(Test.GenerateStringProgram(s))
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

            return Response(datas)
    
    
    @classmethod
    def get_extra_actions(cls):
        return []