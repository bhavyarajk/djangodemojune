from django.shortcuts import render

from shop.models import Product

from django.db.models import Q

def search_products(request):
     if(request.method=="POST"):
          query=request.POST['q']  #reads the query value
          if query:
               p=Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query)) #filter the records matching with query
          context={'pro':p,'query':query}
     return render(request,'search.html',context)