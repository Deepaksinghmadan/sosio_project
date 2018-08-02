from django.shortcuts import render
from .models import *
from .forms import *
from django.http import *
from django.db.models import Sum

def Personal1(request):
	""" form validation for new input expenses and fetching all entries for report"""
	if request.method=='POST':
		form = Expense_form1(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/ramexpenses/')
	else:
		form = Expense_form1()
	r_obj=Ram.objects.all()
	return render(request,"ram_expenses.html",{'my_expenses':r_obj,'form':form})
	

def Personal2(request):
	""" form validation for new input expenses and fetching all entries for report"""
	if request.method=='POST':
		form = Expense_form2(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/shyamexpenses/')
	else:
		form = Expense_form2()
	s_obj=Shyam.objects.all()
	return render(request,"shyam_expenses.html",{'my_expenses':s_obj,'form':form})


def Dashboard(request):
	"""fetching sum of sharing_exp """
	ram_share_exp=Ram.objects.aggregate(Sum('sharing_exp'))
	shyam_share_exp=Shyam.objects.aggregate(Sum('sharing_exp'))
	for k in ram_share_exp:
		for m in shyam_share_exp:
			#comparing for difference and rendering
			if ram_share_exp[k]>shyam_share_exp[m]:
				shyam_dues=((ram_share_exp[k]-shyam_share_exp[m])//2)
				ram_dues=0
			else:
				ram_dues=((shyam_share_exp[m]-ram_share_exp[k])//2)
				shyam_dues=0
	return render(request,"split.html",{'ram_dues':ram_dues,'shyam_dues':shyam_dues})