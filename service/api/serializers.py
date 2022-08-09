from rest_framework import serializers
from api.models import Client, Mailing, Message


class MailingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mailing
        fields = '__all__'
    

class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = '__all__'
        
        
class StatisticsSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'datetime_start': instance.datetime_start,
            'message': instance.message,
            'datetime_end': instance.datetime_end,
            'sent_true_count': Message.objects.filter(mailing=instance.id).filter(is_sent=True).count(),
            'sent_false_count': Message.objects.filter(mailing=instance.id).filter(is_sent=False).count(),
        }