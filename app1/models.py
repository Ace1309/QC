from django.contrib.auth.models import User
from django.db import models


class Operator(models.Model):
    user_name = models.CharField(max_length=30, blank=False)
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()


class Project(models.Model):
    project_code = models.IntegerField(blank=False)
    project_name = models.CharField(max_length=35, blank=False)

    def __str__(self):
        return self.project_name


class CallType(models.Model):
    call_type_name = models.CharField(max_length=10)

    def __str__(self):
        return self.call_type_name


class Team(models.Model):
    team_name = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return self.team_name


class CallCheck(models.Model):
    operator = models.ForeignKey(Operator, on_delete=models.PROTECT)
    qc_manager = models.ForeignKey(User, on_delete=models.PROTECT)
    op_team = models.ForeignKey(Team, on_delete=models.PROTECT, blank=True)
    call_date = models.DateField(blank=True)
    check_up_date = models.DateField(blank=True)
    call_type = models.ForeignKey(CallType, on_delete=models.PROTECT)
    call_duration = models.IntegerField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    phone_number = models.IntegerField(blank=True)
    record_name = models.CharField(max_length=30, blank=True)
    intro = models.CharField(max_length=10, blank=True)
    presentation = models.IntegerField(blank=True)
    purpose = models.IntegerField(blank=True)
    info_to_debtor = models.IntegerField(blank=True)
    payment_options = models.IntegerField(blank=True)
    objections_handling = models.IntegerField(blank=True)
    commitment_closing = models.IntegerField(blank=True)
    farewell = models.IntegerField(blank=True)
    ant_event_result = models.IntegerField(blank=True)
    ant_info = models.IntegerField(blank=True)
    call_model_following = models.IntegerField(blank=True)
    voice_tone = models.IntegerField(blank=True)
    prohibited_phrases = models.IntegerField(blank=True)
    comments = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.record_name

