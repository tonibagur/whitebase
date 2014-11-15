from chessdb.models import Game
from chessdb.serializers import GameSerializer
from rest_framework import generics
from django.views.generic import TemplateView


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class TemplateChessView(TemplateView):
    def get_template_names(self):
        return [self.kwargs.get('template_name') + ".html"]

    def get_context_data(self,**kwargs):
        context=super(TemplateChessView,self).get_context_data()
        if 'pk' in self.kwargs:
            context['id'] = int(self.kwargs['pk'])
        return context