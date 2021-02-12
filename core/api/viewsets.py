from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.authentication import TokenAuthentication

class PontoTuristicoViewSet(ModelViewSet):

    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    # search_fields = ('nome', 'descricao', 'enderecos__linha1')
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)

        queryset = PontoTuristico.objects.all()
        if id:
            queryset = queryset.filter(pk=id)
        
        if nome:
            queryset = queryset.filter(nome__iexact=nome)
        
        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)
            
        return queryset
    
    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)