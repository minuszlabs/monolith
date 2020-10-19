from rest_framework import routers
from api.base.views import users

router = routers.DefaultRouter()
router.register(r'users', users.UserViewSet)
