from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import timedelta
from django.contrib.auth.models import User
from django.db.models import Q

# Create your models here.
class Appointment(models.Model):
    doctor = models.ForeignKey(User, verbose_name=_("Doctor"), on_delete=models.CASCADE, related_name="appointments")
    patient = models.ForeignKey(User, verbose_name=_("Patient"), on_delete=models.CASCADE, related_name="my_appointments")
    time_in = models.DateTimeField(_("time_in"), auto_now=False, auto_now_add=False)
    duration = models.DurationField(_("duration"), default=timedelta(hours=1))
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('doctor', 'time_in')
        ordering = ['time_in']

    def book_appointment(self, doctor, patient, time_in, date):
        pass

    @classmethod
    def view_appointments(cls, owner_id):
        return cls.objects.filter(Q(doctor=owner_id) | Q(patient=owner_id))
    
    @classmethod
    def is_time_in_taken(cls, time_in):
        return cls.objects.filter(time_in=time_in).first()


    def __repr__(self):
        return f"Appointment btw Dr. {self.doctor} and {self.patient} at {self.time_in} for {self.duration}"


class BlockedTime(models.Model):
    doctor = models.ForeignKey(User, verbose_name=_("Doctor"), on_delete=models.CASCADE)
    start_time = models.DateTimeField(_("start"), auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField(_("end"), auto_now=False, auto_now_add=False)
    
    class Meta:
        unique_together = ('doctor', 'start_time')
        ordering = ['start_time']
    
    @classmethod
    def get_blocked_time(cls, doctor_id):
        return cls.objects.filter(doctor=doctor_id)
    
    @classmethod
    def is_time_blocked(cls, doctor_id,time):
        return cls.objects.filter(doctor=doctor_id, start_time=time).first()
    
    def __repr__(self):
        return f"Dr. {self.doctor} blocked {self.start_time} to {self.end_time}"