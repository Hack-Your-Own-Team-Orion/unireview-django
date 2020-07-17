from unireview_app.viewsets import CourseViewset
from rest_framework import routers

router = routers.DefaultRouter()

router.register('Course',CourseViewset)