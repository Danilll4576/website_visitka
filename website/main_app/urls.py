from django.urls import path
from main_app.views import *


urlpatterns = [
	path('', main),
	path('<path:error_rout>', main),

]

