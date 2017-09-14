from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from wiki.urls import get_pattern as get_wiki_pattern
from django_nyt.urls import get_pattern as get_nyt_pattern

#Index redirect
urlpatterns = [
    url(r'^', include('index.urls', namespace="main_page"))
]

#Login redirect
urlpatterns += [
    url(r'^user/', include('login.urls', namespace='login_urls'))
]

#Hour manager redirect
urlpatterns += [
    url(r'^hourmanager/', include('hour_manager.urls'))
]

#Wiki redirect
urlpatterns += [
    url(r'^notifications/', get_nyt_pattern()),
    url(r'^wiki/', get_wiki_pattern())
]

#LFP redirect
urlpatterns += [
    url(r'^lfp/', include('lfp_scheduler.urls')),
]

<<<<<<< HEAD
#Evaluation page redirect
urlpatterns += [
    url(r'^evaluations/', include('evaluations.urls'))
]

#Shift manager redirect
urlpatterns += [
    url(r'^shifts/', include('shiftmanager.urls', namespace='shiftmanager'))
]
=======
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> Add a more hard configured path to media
