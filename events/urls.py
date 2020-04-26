#from django.conf             import settings
#from django.conf.urls.static import static
#from django.conf.urls        import url
#from django.urls              import  re_path
#from .views                   import EventInsert, EventUpdate, EventDelete
from django.urls              import  path
from django.conf              import settings
from django.conf.urls.static  import static
from .                        import views
from .views                   import EventInsert, EventUpdate

urlpatterns = [
    path('eventlist/<slug:periodsought>/)',               views.event_list,                   name='eventlist'),
    #path('eventdetail/,int:pk>/)',                        views.event_detail,                 name='eventdetail'),
#
    path('Z3E4ttud124rv6eventinsert',                     EventInsert.as_view(),                name='eventinsert'),
    path('eventrestore/<int:pk>/)',                       views.restore,                      name='eventrestore'),
    #path('eventrepeat/<int:pk>/)',                        views.event_repeat,                 name='eventrepeat'),
#
    path('eventupdate/<int:pk>/)',                        EventUpdate.as_view(),                 name='eventupdate'),
    #path('bookinto/<int:pk>/)',                           views.bookinto,                     name='bookinto'),
    #path('leave/<int:pk>/)',                              views.leave,                        name='leave'),
    #path('hostsupdate/<int:pk>/)',                        views.hosts_update,                 name='hostsupdate'),
    #path('attendeesupdate/<int:pk>/)',                    views.attendees_update,             name='attendeesupdate'),
#
    path('eventdelete/<int:pk>/)',                        views.event_delete,                name='eventdelete'),
    path('eventdeleteperm/<int:pk>/)',                    views.event_deleteperm,             name='eventdeleteperm'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
