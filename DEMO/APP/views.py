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

def MenuMain(request):
	context	= {
		'str_titulo':'MENU PRINCIPAL'
	}
	return render_to_response('demo.html',context)

def MntApoderado(request):
	apotupla = ({'tid':1,'tdoc':'DNI','nrodoc':'46484104','nomco':'KELVIN ARNOLD FLORES TICONA','estado':'A','pagpen':'NO','nrohijos':3},
				{'tid':2,'tdoc':'DNI','nrodoc':'46484104','nomco':'KELVIN ARNOLD FLORES TICONA','estado':'A','pagpen':'NO','nrohijos':3},
				{'tid':3,'tdoc':'DNI','nrodoc':'46484104','nomco':'KELVIN ARNOLD FLORES TICONA','estado':'A','pagpen':'NO','nrohijos':3},
				{'tid':4,'tdoc':'DNI','nrodoc':'46484104','nomco':'KELVIN ARNOLD FLORES TICONA','estado':'A','pagpen':'NO','nrohijos':3},
				{'tid':5,'tdoc':'DNI','nrodoc':'46484104','nomco':'KELVIN ARNOLD FLORES TICONA','estado':'A','pagpen':'NO','nrohijos':3},
				{'tid':6,'tdoc':'DNI','nrodoc':'46484104','nomco':'KELVIN ARNOLD FLORES TICONA','estado':'A','pagpen':'NO','nrohijos':3},
				{'tid':7,'tdoc':'DNI','nrodoc':'46484104','nomco':'KELVIN ARNOLD FLORES TICONA','estado':'A','pagpen':'NO','nrohijos':3},
				{'tid':8,'tdoc':'DNI','nrodoc':'46484104','nomco':'KELVIN ARNOLD FLORES TICONA','estado':'A','pagpen':'NO','nrohijos':3},
				{'tid':9,'tdoc':'DNI','nrodoc':'46484104','nomco':'KELVIN ARNOLD FLORES TICONA','estado':'A','pagpen':'NO','nrohijos':3},
				{'tid':10,'tdoc':'DNI','nrodoc':'46484104','nomco':'KELVIN ARNOLD FLORES TICONA','estado':'A','pagpen':'NO','nrohijos':3},
				{'tid':11,'tdoc':'DNI','nrodoc':'46484104','nomco':'KELVIN ARNOLD FLORES TICONA','estado':'A','pagpen':'NO','nrohijos':3},
				{'tid':12,'tdoc':'DNI','nrodoc':'46484104','nomco':'KELVIN ARNOLD FLORES TICONA','estado':'A','pagpen':'NO','nrohijos':3},
				{'tid':13,'tdoc':'DNI','nrodoc':'46484104','nomco':'KELVIN ARNOLD FLORES TICONA','estado':'A','pagpen':'NO','nrohijos':3},
				{'tid':14,'tdoc':'DNI','nrodoc':'46484104','nomco':'KELVIN ARNOLD FLORES TICONA','estado':'A','pagpen':'NO','nrohijos':3}
		)
	context	= {
		'ar_apoderados':apotupla,
		'str_titulo':'PERSONAS - APODERADOS'
	}
	return render_to_response('demo2.html',context)

		