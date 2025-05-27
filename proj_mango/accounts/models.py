from django.db import models
from django.contrib.auth import get_user_model
from survey.models import Farm  # Make sure Farm model exists and is importable

User = get_user_model()

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memberships')
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='memberships')
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'farm')

    def __str__(self):
        return f"{self.user.username} is a member of {self.farm.name}"
