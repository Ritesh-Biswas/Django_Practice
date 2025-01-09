from django.shortcuts import render
from .models import Article


#Creating Article Search View
def artcile_search_view(request):
    #print(dir(request))

    query_dict = request.GET #This is a dictionary -> dict(request.GET)
    query = query_dict.get("q") #<input type="text" name="q">
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)



    context = {
        "object" : article_obj,
    }

    return render(request,'articles/search.html',context=context)



#Cretae Form
def article_create_view(request):
    #print(request.POST)
    title = request.POST.get("title")
    content = request.POST.get("content")
    print(title,content)
    Article.objects.create(title=title,content=content)
    context = {}
    return render(request, "articles/create.html"
    ,context=context)
    
     

# Create your views here.
def article_detail_view(request, id=None):
    artcle_obj = None

    if id is not None:
        article_obj = Article.objects.get(id=id)

    context = {
        "object" :article_obj,

    }
    return render(request, "articles/details.html",context=context)
