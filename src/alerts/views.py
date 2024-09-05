from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import IntegrityError
from django.views.generic import ListView, DetailView
from .models import Alert
from .serializers import AlertSerializer

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    http_method_names = ['get', 'post', 'patch', 'head']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
        except IntegrityError:
            return Response(
                {"error": "An alert with this identifier already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_update(serializer)
        except IntegrityError:
            return Response(
                {"error": "An alert with this identifier already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

class AlertListView(ListView):
    model = Alert
    template_name = 'alerts/alert_list.html'
    context_object_name = 'alerts'

class AlertDetailView(DetailView):
    model = Alert
    template_name = 'alerts/alert_detail.html'
    context_object_name = 'alert'
