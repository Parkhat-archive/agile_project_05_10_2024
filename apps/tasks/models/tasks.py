from django.db import models
from django.contrib.auth.models import User

from apps.project.models.project import Project
from apps.tasks.choises.priority import Priority
from apps.tasks.choises.statuses import Statuses
from apps.tasks.models.tag import Tag
from apps.tasks.utils.set_datetime import last_day_of_the_month

class Task(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=Statuses.choices, default=Statuses.New)
    priority = models.SmallIntegerField(choices=Priority.choices, default=Priority.MEDIUM[0])
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deadline = models.DateTimeField(default=last_day_of_the_month)
    assignee = models.ForeignKey(User, on_delete=models.PROTECT, related_name='assigned_tasks', null=True, blank=True)

    def __str__(self):
        return self.name, self.status

    class Meta:
        ordering = ['-deadline']
        unique_together = (('name', 'project'),)





