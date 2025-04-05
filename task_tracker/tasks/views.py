from rest_framework import viewsets
from rest_framework.response import Response
from .models import Employee, Task
from .serializers import EmployeeSerializer, TaskSerializer
from django.db.models import Count, Q
from rest_framework.decorators import action


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=False, methods=["get"])
    def busy_employees(self, request):
        busy_employees = (
            Employee.objects.annotate(task_count=Count("tasks"))
            .filter(task_count__gt=0)
            .order_by("-task_count")
        )
        data = [
            {"id": emp.id, "full_name": emp.full_name, "task_count": emp.task_count}
            for emp in busy_employees
        ]
        return Response(data)

    @action(detail=False, methods=["get"])
    def important_tasks(self, request):
        important_tasks = Task.objects.filter(
            Q(status="not_started") & Q(parent_task__isnull=False)
        )
        result = []
        for task in important_tasks:
            eligible_employees = (
                Employee.objects.annotate(task_count=Count("tasks"))
                .filter(Q(tasks__isnull=True) | Q(tasks__status="completed"))
                .exclude(id__in=[t.assignee.id for t in task.assignee.tasks.all()])
                .order_by("task_count")[:1]
            )

            result.append(
                {
                    "important_task": task.title,
                    "due_date": task.due_date,
                    "employees": [emp.full_name for emp in eligible_employees],
                }
            )
        return Response(result)
