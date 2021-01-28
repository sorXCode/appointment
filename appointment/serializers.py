from rest_framework import serializers
from .models import Appointment, BlockedTime


class AppointmentSerializer(serializers.ModelSerializer):
    duration = serializers.DurationField(read_only=True)

    class Meta:
        model = Appointment
        fields = ["doctor", "patient", "time_in", "duration"]

    def create(self, validated_data):
        if not (BlockedTime.is_time_blocked(doctor_id=validated_data["doctor"],
                                            time=validated_data["time_in"])
                or Appointment.is_time_in_taken(time_in=validated_data["start_time"])):
            return Appointment.objects.create(**validated_data)
        raise serializers.ValidationError({"time_in": "Time occupied, pick another time"})


class BlockTimeSerializer(serializers.ModelSerializer):
    end_time = serializers.DateTimeField(read_only=False)

    class Meta:
        model = BlockedTime
        fields = '__all__'
