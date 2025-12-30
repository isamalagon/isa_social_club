from django.urls import path
from . import filename
from . import stories
from . import places

urlpatterns = [
    path("", filename.welcome),
    path("tips/", filename.show_tips),
    path("add-tip/", filename.add_tip),
    path("stories/add/", stories.add_story),
    path("places/", places.list_places),

]
