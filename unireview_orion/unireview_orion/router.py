from unireview_app.viewsets import CourseViewset, RatingViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('Course',CourseViewset)
router.register('Rating',RatingViewSet)