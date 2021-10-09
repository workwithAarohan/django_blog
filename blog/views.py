from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data = {
        'title': 'Home Page',
    }
    return render(request,'home.html',data)

# def aboutUs(request):
#     return HttpResponse("Welcome everyone.")

def blog(request):
    data = {
        'webTitle' : 'Blog Index',
        'blogs' : [
            {
                'title': 'Artificial Intelligence Future', 
                'description' : 'This is the future of AI.'
            },
            {
                'title': 'Coding', 
                'description' : 'This is the blog of coding.'
            }
        ]
    }
    return render(request, 'blog.html', data)

def blogDetails(request, blog_id):
    return HttpResponse(blog_id)