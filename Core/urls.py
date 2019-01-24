from django.urls import path
#from Core.views import home_cards, home, consultar, encerrar, editar
from Core.views import (
ChamadoListView,
ChamadoCreateView,
ChamadoUpdateView,
ChamadoDetailView,
content_details,

)


# teste usando genericViews

urlpatterns = [
    path('', ChamadoListView.as_view(), name='home'),
    path('add/', ChamadoCreateView.as_view(), name='create'),
    path('<int:pk>/update/', ChamadoUpdateView.as_view(), name='change'),
    path('<int:pk>/detail/', ChamadoDetailView.as_view(), name='detail'),
    path('content_details/', content_details, name='ajax_content_details'),
    

    # path('ajax/load-problemas/', load_problemas, name='ajax_load_problemas'),
    # path('ajax/load-cat-problemas/', load_cat_problemas, name='ajax_load_cat_problemas'),
]


#############################
#   PRIMIERO MODO DE VIEWS  #
############################
# urlpatterns = [

#     path('', home, name='home'),
#     path('home_cards', home_cards, name='home_cards'),
#     path('consultar', consultar, name='Consultar'),
#     path('editar', editar, name='Editar'),
#     path('encerrar', encerrar, name='Encerrar'),

# ]
