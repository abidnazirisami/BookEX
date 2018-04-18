from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from pages.models import *
from .forms import *
from django.shortcuts import redirect

class SignUp(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'

def showUserProfile(request):
	current_user = request.user
	if OurUser.objects.filter(user=current_user).exists():
		current_profile = OurUser.objects.get(user=current_user)
	else:
		newUser = OurUser.objects.create(user = current_user,user_name = current_user.username)
		current_profile = OurUser.objects.get(user=current_user)
	new_list = list()
	author_name_list = list()
	book = list()
	book = Boiii.objects.all()
	for books in book:
		if books.id == current_profile:
			print(books.isbn.isbn)
			if Book.objects.filter(isbn = books.isbn.isbn).exists():
				curBook = Book.objects.get(isbn = books.isbn.isbn)
				new_list.append(curBook)
			if Author.objects.filter(author_id = curBook.author_id.author_id).exists():
				author = Author.objects.get(author_id = curBook.author_id.author_id)
				cur_author_string=''
				isOdd=True
				isFirst=True
				for c in author.author_name:
					if c is '[':
						pass
					elif c is ']':
						pass
					else:
						if isFirst and c is '\'':
							isFirst=False
							isOdd=False
						elif c is '\'' and isOdd and not isFirst:
							cur_author_string+=','
							isOdd=False
						elif c is '\'' and not isOdd:
							isOdd=True
						else:
							cur_author_string+=c
				author_name_list.append(cur_author_string)
	donated = False
	if(int(float(current_profile.donate_count))>0):
		donated=True
	return render(request, 'registration/profile.html', context={'user':current_user,'profile':current_profile,'book':zip(new_list,author_name_list),'donated':donated})


def showProfile(request,username):
	if OurUser.objects.filter(user_name = username):
		current_user = OurUser.objects.get(user_name= username)
		if OurUser.objects.filter(user=current_user.user_id).exists():
			current_profile = OurUser.objects.get(user=current_user.user_id)
		current_user = User.objects.get(id=current_user.user_id)
		new_list = list()
		author_name_list = list()
		book = list()
		book = Boiii.objects.all()
		for books in book:
			if books.id == current_profile:
				print(books.isbn.isbn)
				if Book.objects.filter(isbn = books.isbn.isbn).exists():
					curBook = Book.objects.get(isbn = books.isbn.isbn)
					new_list.append(curBook)
				if Author.objects.filter(author_id = curBook.author_id.author_id).exists():
					author = Author.objects.get(author_id = curBook.author_id.author_id)
					cur_author_string=''
					isOdd=True
					isFirst=True
					for c in author.author_name:
						if c is '[':
							pass
						elif c is ']':
							pass
						else:
							if isFirst and c is '\'':
								isFirst=False
								isOdd=False
							elif c is '\'' and isOdd and not isFirst:
								cur_author_string+=','
								isOdd=False
							elif c is '\'' and not isOdd:
								isOdd=True
							else:
								cur_author_string+=c
					author_name_list.append(cur_author_string)
		donated = False
		if(int(float(current_profile.donate_count))>0):
			donated=True
		return render(request, 'registration/profileOthers.html', context={'cur_user':current_user,'profile':current_profile,'book':zip(new_list,author_name_list),'donated':donated})
	return render(request,'home.html')

def editUserProfile(request):
	current_user = request.user
	if OurUser.objects.filter(user=current_user).exists():
		current_profile = OurUser.objects.get(user=current_user)
	else:
		newUser = OurUser.objects.create(user = current_user,user_name = current_user.username)
		current_profile = OurUser.objects.get(user=current_user)
	if request.method=="POST":
		form_user = EditUser(request.POST, instance=current_user)
		form_profile = EditProfile(request.POST,request.FILES, instance=current_profile)
		if form_profile.is_valid() and form_user.is_valid:
			profile = form_profile.save(commit=False)
			profile.user = current_user
			
			userprofile = form_user.save(commit=False)
			userprofile.email = profile.mail_id
			if 'photo' in request.FILES:
				userprofile.photo = request.FILES['photo']
			profile.save()
			userprofile.save()
			return redirect('profile')
	else:
		form_user = EditUser(instance=current_user)
		form_profile = EditProfile(instance=current_profile)
	return render(request, 'registration/edit_profile.html', {'form_profile':form_profile,'form_user':form_user})
