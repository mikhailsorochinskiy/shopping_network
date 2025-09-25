from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, NetworkNodeViewSet


app_name = 'shop_net'

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'network-node', NetworkNodeViewSet, basename='network_node')

urlpatterns = [

] + router.urls
