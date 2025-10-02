from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def main(request):
        jmeno = "Karel"
        cislo = 22
        barva = "modra"
        return render(request,'index.html',{
                'jmeno':jmeno,
                'cislo':cislo,
                'barva':barva,
                'neco':["he","he",],
        })  
        
def dalsineco(request: HttpRequest) -> HttpResponse:
        return HttpResponse("Dalsi stranka ktera neco ukazuje")