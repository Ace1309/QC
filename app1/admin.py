from django.contrib import admin
from .models import Operator
from .models import Project
from .models import CallType
from .models import Team
from .models import CallCheck


admin.site.register(Operator)
admin.site.register(Project)
admin.site.register(CallType)
admin.site.register(Team)
admin.site.register(CallCheck)
