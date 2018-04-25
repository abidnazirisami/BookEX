from django.shortcuts import render
from pages.models import *
from rating.models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def mail(request,receiver):
	sender_list = []
	mail_list = []
	sender = OurUser.objects.get(user = request.user)
	receiver = OurUser.objects.get(user_id = receiver)
	if request.method == "POST":
		cur_message = request.POST
		text = Message(text = cur_message['text'],to_user = receiver, from_user = sender)
		text.save()
	mail_list1 = Message.objects.filter(to_user=receiver ,from_user= sender)
	mail_list2 = Message.objects.filter(to_user=sender ,from_user=receiver)
	mail_list = mail_list1|mail_list2
	seen = False
	mail_list.order_by('sent_on')
	last_object = Message()
	for mail in mail_list:
		cur_user = mail.from_user
		sender_list.append(cur_user)
		if mail.to_user == sender:
			mail.seen = True
			mail.save()
		if mail.seen:
			seen = True
			#if(mail.sent_on >):
				#mail.delete()
		else:
			seen = False
	if mail_list[len(mail_list)-1].to_user == sender:
		seen = False
	return render(request, 'mail/mail.html', context={'mail_list':zip(mail_list,sender_list),'seen':seen,'chat':receiver})

@login_required
def messages(request):
	cur_user = OurUser.objects.get(user=request.user)
	users = OurUser.objects.all()
	mail_list=[]
	for user in users:
		if Message.objects.filter(to_user=cur_user, from_user=user).exists() or Message.objects.filter(from_user=cur_user, to_user=user).exists():
			mails_to = Message.objects.filter(to_user=cur_user, from_user=user)
			mails_from = Message.objects.filter(from_user=cur_user, to_user=user)
			mails = mails_to|mails_from
			mails.order_by('sent_on').reverse()
			mail_list.append(mails[len(mails) - 1])

	return render(request, 'mail/messages.html', context={'mail_list' : mail_list})