from django.shortcuts import render, get_object_or_404
from .models import Company

def index(request):
    all_companies = Company.objects.all();
    return render(request,'tutorialApp/index.html',{'all_companies':all_companies})

def detail(request,company_id):
    #try:
    #    company = Company.objects.get(id=company_id)
    #except Company.DoesNotExist:
    #    raise Http404("Company does not exist!")
    #return render(request,'tutorialApp/detail.html',{'company' : company})

    #same code as above, but cleaner

    company=get_object_or_404(Company, id=company_id)
    return render(request,'tutorialApp/detail.html',{'company' : company})
