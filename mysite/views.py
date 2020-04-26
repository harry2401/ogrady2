#from django.utils                   import timezone
from django.contrib.auth.models     import User
from django.shortcuts               import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls                    import reverse_lazy
from .models                        import Site
from .models                        import Photo
from .models                        import Bookmark
from .models                        import EnquiryB
from users.models                   import Person
from .forms                         import SiteadvertForm
from .forms                         import SitenoteForm
from .forms                         import PhotoInsertForm
from .forms                         import PhotopriorityForm
from .forms                         import PhototitleForm
from .forms                         import BookmarkInsertForm
from .forms                         import BookmarkpriorityForm
from .forms                         import BookmarktitleForm
from .forms                         import EnquiryInsertForm
from .forms                         import EnquirypriorityForm
#from django.views.generic           import ListView
from django.views.generic           import CreateView
from django.views.generic           import UpdateView
#from django.views.generic           import DeleteView


def fromlogin(request):
      return redirect('eventlist', 'current')

def logout(request):
    logout(request)

def homepage(request):
    photos                                  =  Photo.objects.all()
    for photo in photos:
        photo.already_liked                 =  False
        photo.save()
    bookmarks                               =  Bookmark.objects.all()
    for bookmark in bookmarks:
        bookmark.already_liked              =  False
        bookmark.save()
    return redirect                            ('eventlist', 'current')

@login_required
def notice_update(request):
    activeuser                                                          =     User.objects.get(id=request.user.id)
    activeperson                                                        =     Person.objects.get(username=activeuser.username)
    site                                                                =      get_object_or_404(Site)

    if request.method                                                   != 	"POST":
        form 				= 	                                            SiteadvertForm(instance=site)
        context				                                            =	{'form': form, 'site': site}
        return render				                                        (request, 'mysite/advert_update.html', context)
    else:
        form                                                            = 	SiteadvertForm(request.POST, instance=site)
        if form.is_valid and activeperson.status >= 60:
            site                                                        =   form.save(commit=False)
            site.save()
            return redirect                                                 ('eventlist' ,'current')
        else:
            context                                                     =   {'form': form, 'site': site}
            return render                                                   (request, 'mysite/advert_update.html', context)

@login_required
def notice_delete(request):
    activeuser                                                      =     User.objects.get(id=request.user.id)
    activeperson                                                    =     Person.objects.get(username=activeuser.username)
    if  activeperson.status <  60:
        return redirect                                                   ('eventlist', 'current')
    site                                                            =     get_object_or_404(Site)
    site.notice                                                     =     ''
    site.save()
    return redirect                                                       ('eventlist' ,'current')

@login_required
def note_update(request):
    activeuser                                                                      =  User.objects.get(id=request.user.id)
    activeperson                                                                    =  Person.objects.get(username=activeuser.username)
    if  activeperson.status <  60:
        return redirect                                                                ('eventlist', 'current')
    site                                                                            =  Site.objects.get()
    if request.method                                                               != 'POST':
        form                                                                        = SitenoteForm(instance=site)
        context                                                                     =   {'form': form}
        return render                                                               (request, 'mysite/note_update.html', context)
    else:
        form                                                                        = SitenoteForm(request.POST, instance=site)
        if form.is_valid():
            note                                                                    = form.save(commit=False)
            note.save()
            form.save_m2m()
            return redirect('eventlist', 'current')
        else:
            context                                                                 =   {'form': form}
            return render                                                               (request, 'mysite/note_update.html', context)


@login_required
def photo_list(request):
    activeuser                                         =     User.objects.get(id=request.user.id)
    activeperson                                       =     Person.objects.get(username=activeuser.username)
    if  activeperson.status <  60:
        return redirect                                      ('eventlist', 'current')
    photos                                             =     Photo.objects.filter(is_live=True).order_by('-priority','-created_date')
    context                                            =     {'photos': photos, 'activeperson' : activeperson}
    return render                                            (request, 'mysite/photo_list.html', context)

@login_required
def photo_list_deleted(request):
    activeuser                                         =     User.objects.get(id=request.user.id)
    activeperson                                       =     Person.objects.get(username=activeuser.username)
    if  activeperson.status <  60:
        return redirect                                      ('eventlist', 'current')
    photos                                             =     Photo.objects.filter(is_live=False).order_by('-priority','-created_date')
    context                                            =     {'photos': photos, 'activeperson' : activeperson}
    return render                                            (request, 'mysite/photo_list_deleted.html', context)

class PhotoInsert(CreateView):
    model = Photo
    form_class = PhotoInsertForm
    template_name = 'mysite/photo_insert.html'
    success_url = reverse_lazy('photolist')

@login_required
def photo_update(request, pk, mode):
    activeuser                                         =  User.objects.get(id=request.user.id)
    activeperson                                       =  Person.objects.get(username=activeuser.username)
    if  activeperson.status <  60:
        return redirect                                   ('eventlist', 'current')
    photo                                              = get_object_or_404(Photo, pk=pk)
    if request.method                                  != 'POST':
        if mode                                        ==  'priority':
            form                                       = PhotopriorityForm      (instance=photo)
        elif mode                                      ==  'title':
            form                                       = PhototitleForm         (instance=photo)
        else:
            return redirect                              ('eventlist', 'current')
        return render                                    (request, 'mysite/photo_update.html', {'form': form})                   
    else:
        if mode                                        ==  'priority':
            form                                       = PhotopriorityForm      (request.POST,instance=photo)
        elif mode                                      ==  'title':
            form                                       = PhototitleForm         (request.POST,instance=photo)
        else:
            return redirect                              ('eventlist', 'current')
        if form.is_valid():
            photo                                      = form.save(commit=False)
            photo.save()
            form.save_m2m()
            return redirect                              ('photolist')
        else:                                                                                  
            return render                                (request, 'mysite/photo_update.html', {'form': form})

#@login_required
def photo_change(request, pk, mode):
    #activeuser                                         =   User.objects.get(id=request.user.id)
    #activeperson                                       =   Person.objects.get(username=activeuser.username)
    #if activeperson.status <   60:
            #return redirect                              ('eventlist', 'current')
    photo                                              =   get_object_or_404(Photo, pk=pk)
    if mode                                            ==  "deletetemp":
        photo.is_live                                  =   False
        photo.save()
        return redirect                                    ('photolist')
    elif mode                                          ==  "uptick":
        photo.upticks                                  =   photo.upticks + 1
        photo.already_liked                            =   True
        photo.save()
        #return redirect                                    ('photolist')
        return redirect                                    ('eventlist', 'current')
    elif mode                                          ==  "deleteperm":
        photo.delete()
        return redirect                                    ('photolistdeleted')
    elif mode                                          ==  "restore":
        photo.is_live                                  =   True
        photo.save()
        return redirect                                    ('photolistdeleted')




@login_required
def enquiry_list(request):
    activeuser                                           =  User.objects.get(id=request.user.id)
    activeperson                                         =  Person.objects.get(username=activeuser.username)
    if activeperson.status >=  60:
        enquirys                                         =   EnquiryB.objects.filter(is_live=True).order_by('-priority','-created_date')
        context                                          =   {'enquirys': enquirys, 'activeperson' : activeperson}
        return render                                        (request, 'mysite/enquiry_list.html', context)
    else:
        return redirect                                      ('eventlist', 'current')

@login_required
def enquiry_list_deleted(request):
    activeuser                                           =  User.objects.get(id=request.user.id)
    activeperson                                         =  Person.objects.get(username=activeuser.username)
    if activeperson.status <   60:
        return redirect                                      ('eventlist', 'current')
    enquirys                                             =   EnquiryB.objects.filter(is_live=False).order_by('-priority','-created_date')
    context                                              =   {'enquirys': enquirys, 'activeperson' : activeperson}
    return render                                            (request, 'mysite/enquiry_list_deleted.html', context)

def enquiry_insert(request):
    if request.method                                                               != 'POST':
        form                                                                        =   EnquiryInsertForm()
        context                                                                     =   {'form': form}
        return render                                                                   (request, 'mysite/insert_update.html', context)
    else:
        form                                                                        =   EnquiryInsertForm(request.POST)
        if form.is_valid():
            enquiry                                                                 =   form.save(commit=False)
            enquiry.save()
            form.save_m2m()
            return redirect('eventlist', 'current')
        else:
            context                                                                 =   {'form': form}
            return render                                                               (request, 'mysite/insert_update.html', context)

@login_required
def enquiry_update(request, pk):
    activeuser                                                                      =  User.objects.get(id=request.user.id)
    activeperson                                                                    =  Person.objects.get(username=activeuser.username)
    if activeperson.status <   60:
        return redirect                                                                ('eventlist', 'current')
    enquiry                                                                           = get_object_or_404(EnquiryB, pk=pk)
    if request.method                                                               != 'POST':
        form                                                                        = EnquirypriorityForm(instance=enquiry)
        context                                                                     =   {'form': form}
        return render                                                               (request,'mysite/insert_update.html' , context)
    else:
        form                                                                        = EnquirypriorityForm(request.POST, instance=enquiry)
        if form.is_valid():
            enquiry                                                                   = form.save(commit=False)
            enquiry.save()
            form.save_m2m()
        return redirect('enquirylist')


@login_required
def enquiry_change(request, pk, mode):
    activeuser                                           =   User.objects.get(id=request.user.id)
    activeperson                                         =   Person.objects.get(username=activeuser.username)
    if activeperson.status <   60:
        return redirect('enquirylist')
    enquiry                                              =   get_object_or_404(EnquiryB, pk=pk)
    if mode                                              ==  "deletetemp":
        enquiry.is_live                                  =   False
        enquiry.save()
        return redirect                                      ('enquirylist')
    elif mode                                            ==  "deleteperm":
        enquiry.delete()
        return redirect                                      ('enquirylistdeleted')
    elif mode                                            ==  "restore":
        enquiry.is_live                                  =   True
        enquiry.save()
        return redirect                                      ('enquirylistdeleted')

"""
@login_required
def bookmark_list(request):
    activeuser                                             =  User.objects.get(id=request.user.id)
    activeperson                                           =  Person.objects.get(username=activeuser.username)
    if activeperson.status <   60
        return redirect                                      ('eventlist', 'current')
    bookmarks                                              =   Bookmark.objects.filter(is_live=True).order_by('-priority','-created_date')
    context                                                =   {'bookmarks': bookmarks, 'activeperson' : activeperson}
    return render                                              (request, 'mysite/bookmark_list.html', context)
"""

def bookmark_list(request):
    if request.user.is_authenticated == True:
        activeuser                                =   User.objects.get(id=request.user.id)
        activeperson                              =   Person.objects.get(username=activeuser.username)
    else:
        activeperson                              =   Person.objects.get(username='notloggedin')
    bookmarks                                     =   Bookmark.objects.filter(is_live=True).order_by('-priority','-created_date')
    context                                       =   {'bookmarks': bookmarks, 'activeperson' : activeperson, 'logged_in' : request.user.is_authenticated}
    return render                                     (request, 'mysite/bookmark_list.html', context)

@login_required
def bookmark_list_deleted(request):
    activeuser                                             =  User.objects.get(id=request.user.id)
    activeperson                                           =  Person.objects.get(username=activeuser.username)
    if activeperson.status >=  60:
        bookmarks                                          =   Bookmark.objects.filter(is_live=False).order_by('-priority','-created_date')
        context                                            =   {'bookmarks': bookmarks, 'activeperson' : activeperson}
        return render                                          (request, 'mysite/bookmark_list_deleted.html', context)
    else:
        return redirect('eventlist')

@login_required
def bookmark_insert_update(request, pk, mode):
    activeuser                                         =  User.objects.get(id=request.user.id)
    activeperson                                       =  Person.objects.get(username=activeuser.username)
    if  activeperson.status <  60:
        return redirect                                   ('eventlist', 'current')
    if mode                                            !=  'insert':
        bookmark                                       = get_object_or_404(Bookmark, pk=pk)
    if request.method                                  != 'POST':
        if mode                                        ==  'insert':
            form                                       = BookmarkInsertForm        ()
        elif mode                                      ==  'priority':
            form                                       = BookmarkpriorityForm      (instance=bookmark)
        elif mode                                      ==  'title':
            form                                       = BookmarktitleForm         (instance=bookmark)
        else:
            return redirect                              ('eventlist', 'current')
        return render                                    (request, 'mysite/insert_update.html', {'form': form})                   
    else:
        if mode                                        ==  'insert':
            form                                       = BookmarkInsertForm        (request.POST)
        elif mode                                      ==  'priority':
            form                                       = BookmarkpriorityForm      (request.POST,instance=bookmark)
        elif mode                                      ==  'title':
            form                                       = BookmarktitleForm         (request.POST,instance=bookmark)
        else:
            return redirect                              ('eventlist', 'current')
        if form.is_valid():
            bookmark                                      = form.save(commit=False)
            bookmark.save()
            form.save_m2m()
            return redirect                              ('bookmarklist')
        else:                                                                                  
            return render                                (request, 'mysite/insert_update.html', {'form': form})

@login_required
def bookmark_change(request, pk, mode):
    activeuser                                         =   User.objects.get(id=request.user.id)
    activeperson                                       =   Person.objects.get(username=activeuser.username)
    if activeperson.status <   60:
        return redirect                                    ('bookmarklist')
    bookmark                                           =   get_object_or_404(Bookmark, pk=pk)
    if mode                                            ==  "deletetemp":
        bookmark.is_live                               =   False
        bookmark.save()
        return redirect                                    ('bookmarklist')
    elif mode                                          ==  "deleteperm":
        bookmark.delete()
        return redirect                                    ('bookmarklistdeleted')
    elif mode                                          ==  "restore":
        bookmark.is_live                               =   True
        bookmark.save()
        return redirect                                    ('bookmarklistdeleted')


"""
@login_required
def photo_change(request, pk, mode):
    photo                                                =   get_object_or_404(Photo, pk=pk)
    if mode                                              ==  "deletetemp":
        photo.is_live                                    =   False
        photo.save()
    elif mode                                            ==  "deleteperm":
        photo.delete()
    else:                                                                                                       # i.e. mode = "restore"
        photo.is_live                                    =   True
        photo.save()
    return redirect                                      ('photolist')      

@login_required
def photo_update(request, pk, mode):
    photo                                     = get_object_or_404(Photo, pk=pk)
    if request.method                           != 'POST':
        if mode                                         ==  'priority':
            form = PhotopriorityForm(instance=photo)
        elif mode                                         ==  'title':
            form = PhototitleForm(instance=photo)
        else:
            return redirect('photolist')
        return render(request, 'mysite/photo_insert_update.html', {'form': form})                   # ask user for photo details
    else:
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            photo                                   = form.save(commit=False)
            photo.save()
            form.save_m2m()
            return redirect('photolist')
        else:                                                                                  # i.e. form is not valid, ask user to resubmit it
            return render(request, 'mysite/photo_insert_update.html', {'form': form})

@login_required
def enquiry_change(request, pk, mode):
    enquiry                                                =   get_object_or_404(EnquiryB, pk=pk)
    if mode                                              ==  "deletetemp":
        enquiry.is_live                                    =   False
        enquiry.save()
    elif mode                                            ==  "deleteperm":
        enquiry.delete()
    else:                                                                                                       # i.e. mode = "restore"
        enquiry.is_live                                    =   True
        enquiry.save()
    return redirect                                      ('enquirylist')      

def enquiry_insert(request, pk, mode):
    enquiry                                     = get_object_or_404(EnquiryB, pk=pk)
    if request.method                           != 'POST':
        form = EnquiryBForm()
        return render(request, 'mysite/enquiry_insert_update.html', {'form': form})                   # ask user for enquiry details
    else:
        form = EnquiryBForm(request.POST)
        if form.is_valid():
            enquiry                                   = form.save(commit=False)
            enquiry.save()
            form.save_m2m()
            return redirect('enquirylist')
        else:                                                                                  # i.e. form is not valid, ask user to resubmit it
            return render(request, 'mysite/enquiry_insert_update.html', {'form': form})

@login_required
def bookmark_list(request):
    activeuser                                                                      =  User.objects.get(id=request.user.id)
    activeperson                                                                    =  Person.objects.get(username=activeuser.username)
    if activeperson.status >=  60:
        bookmarks                                                                    =   Bookmark.objects.filter(is_live=True).order_by('-created_date')
        context                                                                     =   {'bookmarks': bookmarks, 'activeperson' : activeperson}
        return render                                                                   (request, 'mysite/bookmark_list.html', context)
    else:
        return redirect('eventlist')

@login_required
def bookmark_list_deleted(request):
    activeuser                                                                      =  User.objects.get(id=request.user.id)
    activeperson                                                                    =  Person.objects.get(username=activeuser.username)
    if activeperson.status >=  60:
        bookmarks                                                                    =   Bookmark.objects.filter(is_live=False).order_by('-created_date')
        context                                                                     =   {'bookmarks': bookmarks, 'activeperson' : activeperson}
        return render                                                                   (request, 'mysite/bookmark_list_deleted.html', context)
    else:
        return redirect('eventlist')

@login_required
def bookmark_change(request, pk, mode):
    bookmark                                                =   get_object_or_404(Bookmark, pk=pk)
    if mode                                              ==  "deletetemp":
        bookmark.is_live                                    =   False
        bookmark.save()
    elif mode                                            ==  "deleteperm":
        bookmark.delete()
    else:                                                                                                       # i.e. mode = "restore"
        bookmark.is_live                                    =   True
        bookmark.save()
    return redirect                                      ('bookmarklist')      

@login_required
def bookmark_insert(request, pk, mode):
    if request.method                           != 'POST':
        form = BookmarkInsertForm()
        return render(request, 'mysite/bookmark_insert_update.html', {'form': form})                   # ask user for bookmark details
    else:
        form = BookmarkInsertForm(request.POST)
        if form.is_valid():
            bookmark                                   = form.save(commit=False)
            bookmark.save()
            form.save_m2m()
            return redirect('bookmarklist')
        else:                                                                                  # i.e. form is not valid, ask user to resubmit it
            return render(request, 'mysite/bookmark_insert_update.html', {'form': form})

@login_required
def photoauthor_update(request, pk):
    activeuser                                                                      =  User.objects.get(id=request.user.id)
    activeperson                                                                    =  Person.objects.get(username=activeuser.username)
    photo                                                                           = get_object_or_404(Photo, pk=pk)
    if request.method                                                               != 'POST':
        form                                                                        = PhotoauthorUpdateForm(instance=photo)
        context                                                                     =   {'form': form}
        return render                                                               (request,'mysite/photoauthor_update.html' , context)
    else:
        form                                                                        = PhotoauthorUpdateForm(request.POST, instance=photo)
        if form.is_valid() and activeperson.status >= 60:
            photo                                                                   = form.save(commit=False)
            photo.save()
            form.save_m2m()
        return redirect('photolist')

@login_required
def photopriority_update(request, pk):
    activeuser                                                                      =  User.objects.get(id=request.user.id)
    activeperson                                                                    =  Person.objects.get(username=activeuser.username)
    photo                                                                           = get_object_or_404(Photo, pk=pk)
    if request.method                                                               != 'POST':
        form                                                                        = PhotopriorityUpdateForm(instance=photo)
        context                                                                     =   {'form': form}
        return render                                                               (request,'mysite/photopriority_update.html' , context)
    else:
        form                                                                        = PhotopriorityUpdateForm(request.POST, instance=photo)
        if form.is_valid() and activeperson.status >=  60:
            photo                                                                   = form.save(commit=False)
            photo.save()
            form.save_m2m()
        return redirect('photolist')

@login_required
def phototitle_update(request, pk):
    activeuser                                                                      =  User.objects.get(id=request.user.id)
    activeperson                                                                    =  Person.objects.get(username=activeuser.username)
    photo                                                                           = get_object_or_404(Photo, pk=pk)
    if request.method                                                               != 'POST':
        form                                                                        = PhototitleUpdateForm(instance=photo)
        context                                                                     =   {'form': form}
        return render                                                               (request,'mysite/phototitle_update.html' , context)
    else:
        form                                                                        = PhototitleUpdateForm(request.POST, instance=photo)
        #if form.is_valid() and (activeperson.status >=  55 or activeperson.username == photo.authorname):
        if form.is_valid and activeperson.status >=  60:
            photo                                                                   = form.save(commit=False)
            photo.save()
            form.save_m2m()
        return redirect('photolist')

"""
