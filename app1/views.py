
from django.shortcuts import render

# Create your views here.
def index(request):
    c1 = ['Alia Bhat (Famous Actress)' , 'I am so glad that I stumbled across Photography. I can’t say enough about how professional is and the quality of work that he provides. I was so pleased with my session and final photographs, that I will continue to use him in the future.']
    c2 = ['Virat Kholi (professional Cricketer)' , 'creates magic. he has captured the most special moments of my family’s life. I would never hesitate to recommend him to anyone who wants a true professional to create a customized photography experience.']
    c3 = ['Rohit Sharma (Indian Cricket Team Captain)' , 'Easily the best experience with a photographer to date! is super personable and very talented at his craft. He made sure everyone was comfortable and enjoying the experience. Thanks ']
    l = [c1 , c2 , c3]
    return render(request , 'index.html' , {'li' : l , 'heading' : 'PBG_SHOOTS Bolte publix'})

def about(request):
    return render(request ,'about.html')

def portfolio(request):
    return render(request ,'portfolio.html')

def contact(request):
    context = {}
    if request.method == 'POST':
        n = request.POST['name']
        p = request.POST['pno']
        e = request.POST['eml']
        m = request.POST['msg']
        print(request.POST)
        context = {'n' : n , 'p' : p , 'e' : e , 'm' : m} 
    return render(request ,'contact.html' , context)

