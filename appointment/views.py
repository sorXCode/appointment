from datetime import datetime, timedelta

from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .models import Appointment, BlockedTime
from .serializers import AppointmentSerializer, BlockTimeSerializer


@api_view(["GET",])
@login_required
@permission_required("auth.can_view_appointments")
def appointment_list(request):
    """
    List all Appointment
    """
    appointment = Appointment.view_appointments(owner_id=request.user.id)
    serializer = AppointmentSerializer(appointment, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(["POST",])
@login_required
@permission_required("auth.can_book_appointments")
@csrf_exempt
def book_appointment(request):
    """
    create a new Appointment
    """
    data = JSONParser().parse(request)
    data["time_in"], _ = convert_datetime_to_datehour(data["time_in"])
    data["patient"] = request.user.id
    serializer = AppointmentSerializer(data=data)
    return validate_and_save(serializer=serializer)


@api_view(["POST", "GET"])
@login_required
@permission_required("auth.can_block_off")
@csrf_exempt
def block_time(request):
    if request.method=="POST":
        data = JSONParser().parse(request)
        data["start_time"], data["end_time"] = convert_datetime_to_datehour(data["start_time"])
        data["doctor"] = request.user.id
        serializer = BlockTimeSerializer(data=data)
        return validate_and_save(serializer=serializer)
    elif request.method=="GET":
        blocked_time = BlockedTime.get_blocked_time(doctor_id=request.user.id)
        serializer = BlockTimeSerializer(blocked_time, many=True)
        return JsonResponse(serializer.data, safe=False)


def convert_datetime_to_datehour(time_):
    time_ = datetime.fromisoformat(time_)
    return f"{time_.date()}T{time_.hour}:00:00.0", f"{time_.date()}T{time_.hour+1}:00:00.0"

def validate_and_save(serializer):
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
