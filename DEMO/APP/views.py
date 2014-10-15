from django.shortcuts import render_to_response
# from forms import UserForm
# from django.Http import HttpResponseRedirect

# Create your views here.
def Index(request):
	str_name	= 'Kelvin'
	int_edad	= 24
	tupla	= (1,2,3,4,5,6,7,8,9,10)
	context	= {
		'str_name':str_name,
		'int_edad':int_edad,
		'tupla':tupla
	}
	return render_to_response('index.html',context)