from mail.models import *
from pages.models import *



def messageCount(request):
	unread_messages = 0
	if request.user.is_authenticated:
		current_user = OurUser.objects.get(user = request.user)
		unread_messages = Message.objects.filter(to_user = current_user, seen = False).count()   

	return {
		'unread_messages': unread_messages,
	}