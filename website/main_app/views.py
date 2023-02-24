from django.shortcuts import render
from django.http import HttpResponse
from urllib.parse import unquote
from main_app.send_in_bot import send_message



def main(request, error_rout="-"):
	if(request.GET):
		print(request.GET)
		try:
			name = unquote(request.GET['name'])
		except:
			name = ''
		try:
			emeil = unquote(request.GET['email'])
		except:
			emeil = ''
		try:
			submite = unquote(request.GET['submite'])
		except:
			submite = ''

		text_for_bot = """
			Имя: {name}
		Телефон: {phone}
		Текст: {submite}
		""".format(name=name, phone=emeil, submite=submite)

		send_message(text_for_bot)


	return render(request, 'main_app/index.htm')




