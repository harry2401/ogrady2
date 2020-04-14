#from django.utils                   import timezone
from django.contrib.auth.models     import User
from django.shortcuts               import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls                    import reverse_lazy
from .models                        import Site
from .models                        import Photo
from .models                        import EnquiryB
from users.models                   import Person
from .forms                         import advertUpdateForm
from .forms                         import noteUpdateForm
from .forms                         import PhotoInsertForm
#from .forms                         import PhotoauthorUpdateForm
from .forms                         import PhotopriorityUpdateForm
from .forms                         import PhototitleUpdateForm
from .forms                         import EnquiryInsertForm
from .forms                         import EnquirypriorityUpdateForm
#from django.views.generic           import ListView
from django.views.generic           import CreateView
from django.views.generic           import UpdateView
#from django.views.generic           import DeleteView


def fromlogin(request):
      return redirect('eventlist', 'current')
      #return redirect('homepage')

def logout(request):
    logout(request)

@login_required
def notice_update(request):
    activeuser                                                          =     User.objects.get(id=request.user.id)
    activeperson                                                        =     Person.objects.get(username=activeuser.username)
    site                                                                =      get_object_or_404(Site)

    if request.method                                                   != 	"POST":
        form 				= 	                                            advertUpdateForm(instance=site)
        context				                                            =	{'form': form, 'site': site}
        return render				                                        (request, 'mysite/advert_update.html', context)
    else:
        form                                                            = 	advertUpdateForm(request.POST, instance=site)
        if form.is_valid and activeperson.status >= 60:
            site                                                        =   form.save(commit=False)
            site.save()
            return redirect                                                 ('eventlist' ,'current')
        else:
            context                                                     =   {'form': form, 'site': site}
            return render                                                   (request, 'mysite/advert_update.html', context)

@login_required
def notice_delete(request):
    activeuser                                                          =     User.objects.get(id=request.user.id)
    activeperson                                                        =     Person.objects.get(username=activeuser.username)
    site                                                                =      get_object_or_404(Site)

    if  activeperson.status >= 60:
        site.notice                                                 =   ''
        site.save()
        return redirect                                                 ('eventlist' ,'current')
    else:
        context                                                     =   {'form': form, 'site': site}
        return render                                                   (request, 'mysite/advert_update.html', context)

@login_required
def note_update(request):
    activeuser                                                                      =  User.objects.get(id=request.user.id)
    activeperson                                                                    =  Person.objects.get(username=activeuser.username)
    site                                                                            =  Site.objects.get()
    if request.method                                                               != 'POST':
        form                                                                        = noteUpdateForm(instance=site)
        context                                                                     =   {'form': form}
        return render                                                               (request, 'mysite/note_update.html', context)
    else:
        form                                                                        = noteUpdateForm(request.POST, instance=site)
        if form.is_valid():
            note                                                                    = form.save(commit=False)
            if request.user.is_authenticated and activeperson.status                >=  60:
                note.save()
                form.save_m2m()
                return redirect('eventlist', 'current')
            else:
                context                                                              =      {'form': form}
                return render                                                               (request, 'mysite/note_update.html', context)
        else:
            context                                                                 =   {'form': form}
            return render                                                               (request, 'mysite/note_update.html', context)


@login_required
def photo_list(request):
  activeuser                                                                      =     User.objects.get(id=request.user.id)
  activeperson                                                                    =     Person.objects.get(username=activeuser.username)
  photos                                                                          =     Photo.objects.filter(is_live=True).order_by('-priority')
  context                                                                         =    {'photos': photos, 'activeperson' : activeperson}
  return render                                                                         (request, 'mysite/photo_list.html', context)

@login_required
def photo_list_deleted(request):
  activeuser                                                                      =     User.objects.get(id=request.user.id)
  activeperson                                                                    =     Person.objects.get(username=activeuser.username)
  photos                                                                          =     Photo.objects.filter(is_live=False).order_by('-priority')
  context                                                                         =    {'photos': photos, 'activeperson' : activeperson}
  return render                                                                         (request, 'mysite/photo_list_deleted.html', context)


class PhotoInsert(CreateView):
    model = Photo
    form_class = PhotoInsertForm
    template_name = 'mysite/photo_insert.html'
    success_url = reverse_lazy('photolist')



"""
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
"""

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

@login_required
def photo_delete(request, pk):
    activeuser                                                                      =  User.objects.get(id=request.user.id)
    activeperson                                                                    =  Person.objects.get(username=activeuser.username)
    photo                                                                           = get_object_or_404(Photo, pk=pk)
    if activeperson.status >=  60:
        photo.is_live                                                               = False
        photo.save()
    return redirect('photolist')

@login_required
def photo_restore(request, pk):
    activeuser                                                                      =  User.objects.get(id=request.user.id)
    activeperson                                                                    =  Person.objects.get(username=activeuser.username)
    photo                                                                           = get_object_or_404(Photo, pk=pk)
    #if activeperson.status >=  55 or activeperson.username == photo.author:
    if activeperson.status >=  60:
        photo.is_live                                                               = True
        photo.save()
    return redirect('photolist')

@login_required
def photo_delete_perm(request, pk):
    activeuser                                                                      =  User.objects.get(id=request.user.id)
    activeperson                                                                    =  Person.objects.get(username=activeuser.username)
    photo                                                                           = get_object_or_404(Photo, pk=pk)
    #if activeperson.status >=  55 or activeperson.username == photo.author:
    if activeperson.status >=  60:
        photo.delete()
    return redirect('photolistdeleted')

@login_required
def enquiry_list(request):
    activeuser                                                                      =  User.objects.get(id=request.user.id)
    activeperson                                                                    =  Person.objects.get(username=activeuser.username)
    if activeperson.status >=  60:
        enquirys                                                                    =   EnquiryB.objects.filter(is_live=True).order_by('-created_date')
        context                                                                     =   {'enquirys': enquirys, 'activeperson' : activeperson}
        return render                                                                   (request, 'mysite/enquiry_list.html', context)
    else:
        return redirect('eventlist')

@login_required
def enquiry_list_deleted(request):
    activeuser                                                                      =  User.objects.get(id=request.user.id)
    activeperson                                                                    =  Person.objects.get(username=activeuser.username)
    if activeperson.status >=  60:
        enquirys                                                                    =   EnquiryB.objects.filter(is_live=False).order_by('-created_date')
        context                                                                     =   {'enquirys': enquirys, 'activeperson' : activeperson}
        return render                                                                   (request, 'mysite/enquiry_list_deleted.html', context)
    else:
        return redirect('eventlist')

def enquiry_insert(request):
    if request.method                                                               != 'POST':
        form                                                                        =   EnquiryInsertForm()
        context                                                                     =   {'form': form}
        return render                                                                   (request, 'mysite/enquiry_insert.html', context)
    else:
        form                                                                        =   EnquiryInsertForm(request.POST)
        if form.is_valid():
            enquiry                                                                 =   form.save(commit=False)
            enquiry.save()
            form.save_m2m()
            return redirect('eventlist', 'current')
        else:
            context                                                                 =   {'form': form}
            return render                                                               (request, 'mysite/enquiry_insert.html', context)

@login_required
def enquirypriority_update(request, pk):
    activeuser                                                                      =  User.objects.get(id=request.user.id)
    activeperson                                                                    =  Person.objects.get(username=activeuser.username)
    enquiry                                                                           = get_object_or_404(EnquiryB, pk=pk)
    if request.method                                                               != 'POST':
        form                                                                        = EnquirypriorityUpdateForm(instance=enquiry)
        context                                                                     =   {'form': form}
        return render                                                               (request,'mysite/enquirypriority_update.html' , context)
    else:
        form                                                                        = EnquirypriorityUpdateForm(request.POST, instance=enquiry)
        if form.is_valid() and activeperson.status >=  60:
            enquiry                                                                   = form.save(commit=False)
            enquiry.save()
            form.save_m2m()
        return redirect('enquirylist')

@login_required
def enquiry_delete(request, pk):
    activeuser                                                                      =  User.objects.get(id=request.user.id)
    activeperson                                                                    =  Person.objects.get(username=activeuser.username)
    enquiry                                                                           = get_object_or_404(EnquiryB, pk=pk)
    if activeperson.status >=  60:
        enquiry.is_live                                                               = False
        enquiry.save()
    return redirect                                                                         ('enquirylist')

@login_required
def enquiry_deleteperm(request, pk):
    activeuser                                                                      =  User.objects.get(id=request.user.id)
    activeperson                                                                    =  Person.objects.get(username=activeuser.username)
    enquiry                                                                           = get_object_or_404(EnquiryB, pk=pk)
    if activeperson.status >=  60:
        enquiry.delete()
    return redirect                                                                         ('enquirylistdeleted')

@login_required
def enquiry_restore(request, pk):
    activeuser                                                                      =  User.objects.get(id=request.user.id)
    activeperson                                                                    =  Person.objects.get(username=activeuser.username)
    enquiry                                                                           = get_object_or_404(EnquiryB, pk=pk)
    #if activeperson.status >=  55 or activeperson.username == enquiry.author:
    if activeperson.status >=  60:
        enquiry.is_live                                                               = True
        enquiry.save()
    return redirect('enquirylist')

