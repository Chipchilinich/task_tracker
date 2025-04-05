from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name


class Task(models.Model):
    title = models.CharField(max_length=200)
    parent_task = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True
    )
    assignee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="tasks"
    )
    due_date = models.DateTimeField()
    status = models.CharField(max_length=50)  # Например, 'in_progress', 'completed'
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
