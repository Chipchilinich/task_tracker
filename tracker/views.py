from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from employee.models import Employee
from tracker.filters import TrackerFilter
from tracker.models import Tracker
from tracker.serializer import TrackerSerializer


class TrackerViewset(viewsets.ModelViewSet):
    """ViewSet для модели TRACKER"""

    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = TrackerFilter
    ordering_fields = ('id', 'status')

    def list(self, request, *args, **kwargs):
        """Вывод информации списка согласно шаблона"""

        # Получаем отфильтрованный список
        queryset = self.filter_queryset(self.get_queryset())

        # Сериализация
        serializer = self.get_serializer(queryset, many=True)

        # Список заданных параметров на фильтрацию в поисковой строке
        filter_params = request.query_params

        # Проверяем наличие фильтра в запросе
        if filter_params.get("important_trackers") == "true":

            # Формируем ответ, если есть отфильтрованные задачи
            formatted_response = []

            for item in serializer.data:

                # Получаем ID сотрудников
                employee_ids = item['employees']

                # Фильтруем сотрудник по ID
                employee_info = Employee.objects.filter(id__in=employee_ids)

                # Достаем ФИО каждого необходимого сотрудника
                employee_names = [employee.fio for employee in employee_info]

                # Создаем необходимый формат ответа
                formatted_response.append({

                    "Важная задача": item['title'],
                    "Срок выполнения": item['time'],
                    "Выполняющие": employee_names,
                })

            return Response(formatted_response)

        return Response(serializer.data)
