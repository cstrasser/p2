from django.shortcuts import render
from sto.models import Tblservicetask



def sto_list(request):
        context = {}
        sto_list = Tblservicetask.objects.filter(ststatus ='Active')
        #testlist = Tblservicetask.objects.all().filter(ststatus = 'Active').order_by('-check_in')
        context ={'list': sto_list}
        return render(request, 'sto/listview.html', context)