from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, ListView, DetailView
from basicfunc.models import Participant, TransferHistory
from basicfunc.forms import TransferCredits
import datetime


# Create your views here.


class ParticipantListView(ListView):
	context_object_name = 'p_list'
	model = Participant
	template_name = "basicfunc/participantlist.html"
	# Returns participant_list

class ParticipantDetailView(DetailView):
	model = Participant
	template_name = "basicfunc/participantdetail.html"

class HomeView(TemplateView):
	template_name = "basicfunc/index.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['injected_content'] = datetime.datetime.now()
		return context

def disp_users(request):
	p = Participant.objects.all()
	return render(request, 'basicfunc/display_users.html', {'user_data': p})
	
def single_user(request):
	form_dict = {}
	# We splice the current path to get our link variable for displaying selected user's information
	user_link = request.path.split("/")[-1]
	selected_user = get_object_or_404(Participant, link=user_link)
	other_users = Participant.objects.exclude(link=user_link)
	transfer_form = TransferCredits()
	if selected_user:
		data_dict = {'user': selected_user}
		form_dict['outmail'] = selected_user.email
	else:
		data_dict = {'user': '404'}
	data_dict['others'] = other_users

	if request.method == "POST":
		requested_amount = int(request.POST.get('amount'))
		requested_sender = selected_user.email
		requested_reciever = request.POST.get('reciever_email')
		reciever_object = Participant.objects.filter(email=requested_reciever)[0]
		print("The user " + requested_sender + " is sending " + str(requested_amount) + " to " + requested_reciever)


		# Now to actually send the data
		reduced_amount = selected_user.credit_points - requested_amount
		added_amount = Participant.objects.filter(email=requested_reciever)[0].credit_points + requested_amount
		Participant.objects.filter(email=requested_sender).update(credit_points=reduced_amount)
		Participant.objects.filter(email=requested_reciever).update(credit_points=added_amount)
		print("update done!")
		# update transferhistory table here
		new_transaction = TransferHistory(donor=selected_user, target=reciever_object, weight=requested_amount)
		print("new_transaction added to database")
		new_transaction.save()
		return redirect('index')


	return render(request, 'basicfunc/sendto.html', data_dict)


def history_table(request):
	users = TransferHistory.objects.all()
	disp_dict = {'entity': users}
	if request.method == "POST":
		TransferHistory.objects.all().delete()
		return redirect(request.path_info, context=disp_dict)
	return render(request, 'basicfunc/history.html', context=disp_dict)


def display_table(request):
	users = Participant.objects.all()
	disp_dict = {'users':users}
	return render(request, 'basicfunc/display_data.html', context=disp_dict)
