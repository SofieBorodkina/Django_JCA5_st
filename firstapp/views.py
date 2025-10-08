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
def test(request):
        return render(request,'hl_staranka.html')
        
def dalsineco(request: HttpRequest) -> HttpResponse:
        return HttpResponse("Dalsi stranka ktera neco ukazuje")

"""Tohle jsou articles"""   

def unique(request: HttpRequest) -> HttpResponse:
        return HttpResponse("Tohle je unikatni article :d")

def article_main(request: HttpRequest) -> HttpResponse:
        return HttpResponse("Tohle je hlavni article stranka")


def articles(request: HttpRequest,article_id: int, article_name: str="") ->HttpResponse:
        return HttpResponse(
                "This is article n.{}, {}".format(article_id,"Name of this article is {}".format(
                        article_name) if article_name else "This is unnamed article"))