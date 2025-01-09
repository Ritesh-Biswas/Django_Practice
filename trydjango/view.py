"""
To Render HTML Web pages
"""
from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string, get_template



name = "Ritesh Biswas"




def home_view(request,id=None, *args, **kwargs):
    #args-> arguments
    #kwargs-> keywordarguments
    """
    Take in a request(Django send request) and
    Return HTML in a response (We pick to return the response)
    """

    #From the Database
    article_obj = Article.objects.get(id=1)
    # print(args,kwargs)
    print(id)

    article_title = article_obj.title
    article_content = article_obj.content
    # my_list = [102,103,342]

    #getting the data in form of list from the database
    article_queryset = Article.objects.all()

    context = {
        "object_list" : article_queryset,
        "title" : article_obj.title,
        "content" : article_obj.content,
        "id" : article_obj.id,
        "name" : name,
    }

    #DJANGO Templates

    #Other way to render the template
    # tmpl = get_template("home-view.html")
    # tmpl_string = tmpl.render(context=context)


    #One way to render the TEMPLATE
    H1_STRING = render_to_string("home-view.html",context=context)



    # H1_STRING = """
    # <h1> Hello {name}, your ID is {id} </h1>
    # <h2> Your Title is {title}, Your Content is {content}</h2>
    
    # """.format(**context)
    
    return HttpResponse(H1_STRING)