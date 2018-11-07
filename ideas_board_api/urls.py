from django.conf.urls import url, include
from django.contrib import admin

from ideas.views import ideas, idea_new, idea_delete, idea_update

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^api/v1/ideas/new$', idea_new, name="idea_new"),
    url(r'^api/v1/ideas$', ideas, name="ideas"),
    url(r'^api/v1/idea/delete$', idea_delete, name="idea_delete"),
    url(r'^api/v1/idea/update$', idea_update, name="idea_update"),
    url(r'^admin/', admin.site.urls),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
