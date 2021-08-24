
from .views import PersonagenViewSet, LivroViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('personagens', PersonagenViewSet)
router.register('livros', LivroViewSet)