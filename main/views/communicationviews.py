from django.contrib.auth.decorators import login_required
from django.shortcuts import  render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.db.models.functions import Concat
from django.db.models import Value, Q
from django.http import JsonResponse
from django.utils import timezone
from django.conf import settings
import json, datetime
# get model
from main.models import User, Official_Letter

# -------------------------------------------------------------------------------------------------------------------------------------

@login_required(login_url = 'main:sign_page')
def communication_list_page(request):
    official_letter_list = Official_Letter.objects.filter(Q(fk_sender = request.user) | Q(fk_receiver = request.user)).order_by('-create_date')\
        .annotate(receiver = Concat('fk_receiver__first_name', Value(' '), 'fk_receiver__last_name'), sender = Concat('fk_sender__first_name',\
        Value(' '), 'fk_sender__last_name')).values('id', 'title', 'sender', 'receiver', 'status', 'create_date')

    context = {
        'OfficialLetterList': official_letter_list
    }
    
    return render(request, 'main/communication/communication-list.html', context)


@login_required(login_url = 'main:sign_page')
def communication_create_page(request):
    return render(request, 'main/communication/communication-create.html')


def create_official_letter(request):
    response_data = {}
    if request.user.is_authenticated:
        try:
            # get data
            this_title = request.POST.get('title')
            this_description = request.POST.get('description')
            this_receiver_id = request.POST.get('receiver_id')
            try:
                this_attached_file = request.FILES['attached_file']
            except:
                this_attached_file = None
            # create official_letter
            this_receiver = User.objects.get(id = this_receiver_id)
            this_official_letter = Official_Letter.objects.create(title = this_title, description = this_description,\
                fk_receiver = this_receiver, fk_sender = request.user)
            # check other fields
            if this_attached_file is not None:
                this_official_letter.attached_file = this_attached_file
            this_official_letter.save()

            response_data['status'] = '201'
            return JsonResponse(response_data)
        except Exception as e:
            response_data['status'] = '500'
            response_data['error'] = str(e)
            return JsonResponse(response_data)
    else:
        response_data['status'] = '401'
        response_data['error'] = 'شما وارد سیستم نشده اید.'
        return JsonResponse(response_data)


def get_official_letter_details(this_official_letter):
    this_official_letter_details = {
        'title': this_official_letter.title,
        'description': this_official_letter.description,
        'sender': this_official_letter.fk_sender.get_fullname(),
        'receiver': this_official_letter.fk_receiver.get_fullname(),
        'attached_file': this_official_letter.attached_file,
        'status': this_official_letter.status,
        'answer': this_official_letter.answer,
        'create_date': this_official_letter.create_date
    }
    return this_official_letter_details


@login_required(login_url = 'main:sign_page')
def official_letter_details_page(request, pk):
    this_official_letter =  get_object_or_404(Official_Letter, id = pk)

    context = {
        'OfficialLetter': get_official_letter_details(this_official_letter)
    }

    return render(request, 'main/communication/communication-detail.html', context)


def answer_official_letter(request):
    response_data = {}
    if request.user.is_authenticated:
        try:
            # get data
            this_official_letter_id = request.POST.get('official_letter_id')
            this_description = request.POST.get('description')
            try:
                this_attached_file = request.FILES['attached_file']
            except:
                this_attached_file = None
            # get official_letter
            if Official_Letter.objects.filter(id = this_official_letter_id, fk_receiver = request.user).exists():
                this_official_letter = Official_Letter.objects.get(id = this_official_letter_id)
                # upload files
                file_url = None
                if this_attached_file is not None:
                    file_storage = FileSystemStorage(location = settings.MEDIA_ROOT + '/media/files/official_letter/answer', base_url = '/media/files/official_letter/answer')
                    data = file_storage.save(this_attached_file.name, this_attached_file)
                    file_url = file_storage.url(data)
                this_official_letter.answer['description'] = this_description
                this_official_letter.answer['datetime'] = timezone.localtime(datetime.datetime.now()).strftime('%Y-%m-%d %H:%M')
                if this_attached_file is not None:
                    this_official_letter.answer['file'] = file_url
                this_official_letter.save()

                response_data['status'] = '200'
                return JsonResponse(response_data)
            else:
                response_data['status'] = '404'
                response_data['error'] = 'مکاتبه ای با این شناسه که شما دریافت کننده آن باشید، در سیستم موجود نیست.'
                return JsonResponse(response_data)
        except Exception as e:
            response_data['status'] = '500'
            response_data['error'] = str(e)
            return JsonResponse(response_data)
    else:
        response_data['status'] = '401'
        response_data['error'] = 'شما وارد سیستم نشده اید.'
        return JsonResponse(response_data)