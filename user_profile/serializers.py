from rest_framework import serializers

from allauth.account.utils import setup_user_email
from allauth.account.adapter import get_adapter

from rest_auth.registration.serializers import RegisterSerializer

class CustomRegisterSerializer(RegisterSerializer):
	first_name = serializers.CharField(
			required = True,
			max_length = 15
		)
	last_name = serializers.CharField(
			required = True,
			max_length = 15
		)

	def get_cleaned_data(self):
		data_dict = super().get_cleaned_data()
		data_dict['first_name'] = self.validated_data.get('first_name','')
		data_dict['last_name'] = self.validated_data.get('last_name','')
		return data_dict

