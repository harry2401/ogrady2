from django.contrib             import admin
from django.urls                import path, include
from django.conf                import settings
from django.conf.urls.static    import static
from .                          import views
from .views                     import PhotoInsert
urlpatterns = [
    path('',                                    views.homepage,                                   name='homepage'),
    path('logout/',                             views.logout,                    {'next_page': settings.LOGOUT_REDIRECT_URL},  name='logout'),
    path('accounts/',                           include('django.contrib.auth.urls')),
    path('accounts/profile/' ,                  views.fromlogin ),
    path('admin/',                              admin.site.urls),
#
#
    path('noticeupdate',             	        views.notice_update,                                                           name='noticeupdate'),
    path('noticedelete',             	        views.notice_delete,                                                           name='noticedelete'),
#
    path('noteupdate',                          views.note_update,                                                             name='noteupdate'),
#
#
#
    path('photolist',                                    views.photo_list,                        name='photolist'),
    path('photolistdeleted',                             views.photo_list_deleted,                name='photolistdeleted'),
#
    path('qawsd345d7u',                                  PhotoInsert.as_view(),                   name='photoinsert'),
    path('photoupdate/<int:pk>/<slug:mode>/)',           views.photo_update,                      name='photoupdate'),
#
    path('photochange/<int:pk>/<slug:mode>/)',           views.photo_change,                      name='photochange'),
#
    path('bookmarklist',                                 views.bookmark_list,                     name='bookmarklist'),
    path('bookmarklistdeleted',                          views.bookmark_list_deleted,             name='bookmarklistdeleted'),
#
    path('bookmarkinsertupdate/<int:pk>/<slug:mode>/)',  views.bookmark_insert_update,            name='bookmarkinsertupdate'),
#
    path('bookmarkchange/<int:pk>/<slug:mode>/)',        views.bookmark_change,                   name='bookmarkchange'),
#
#
#
    path('enquirylist',                                     views.enquiry_list,                                name='enquirylist'),
    path('enquirylistdeleted',                              views.enquiry_list_deleted,                        name='enquirylistdeleted'),
#
    path('enquiryinsert',                                   views.enquiry_insert,                              name='enquiryinsert'),
    path('enquiryupdate/<int:pk>/',                         views.enquiry_update,                              name='enquiryupdate'),
#
    path('enquirychange/<int:pk>/<slug:mode>/)',            views.enquiry_change,                              name='enquirychange'),
#
#
    path('',                                    include('events.urls')),
    path('',                                    include('users.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
    path('photoBlist',                           views.photoB_list,                                                              name='photoBlist'),
    path('photoBlistdeleted',                    views.photoB_list_deleted,                                                      name='photoBlistdeleted'),
#
    path('photoBinsert',                         PhotoBInsert.as_view(),                                                         name='photoBinsert'),
#
    path('photoBauthorupdate/<int:pk>/',         views.photoBauthor_update,                                                      name='photoBauthorupdate'),
    path('photoBpriorityupdate/<int:pk>/',       views.photoBpriority_update,                                                    name='photoBpriorityupdate'),
    path('photoBtitleupdate/<int:pk>/',          views.photoBtitle_update,                                                       name='photoBtitleupdate'),
    path('photoBrestore/<int:pk>/',              views.photoB_restore,                                                           name='photoBrestore'),
    path('photoBdelete/<int:pk>/',               views.photoB_delete,                                                            name='photoBdelete'),
#
    path('photoBdeleteperm/<int:pk>/',           views.photoB_delete_perm,                                                       name='photoBdeleteperm'),
#
#
"""
