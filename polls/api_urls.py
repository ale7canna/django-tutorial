from rest_framework import routers
from .api_views import ChoiceViewSet, QuestionViewSet

router = routers.DefaultRouter()
router.register(r'choices', ChoiceViewSet)
router.register(r'questions', QuestionViewSet)

urlpatterns = router.urls