from django import forms
from .models import Test

class Studentform(forms.ModelForm):
	class Meta:
		model=Test
		fields='__all__'



# while True:
# 	apn_type = input('Enter the MPLS or VPN APN type: ')
# 	x = apn_type.upper()
# 	if x == 'MPLS' or apn_type == 'VPN':
# 		if x == 'MPLS':
# 			print('The CONTEXT-NAME for MPLS: gi-citizensenergy-3328')
# 			break
# 		else:
# 			print('The CONTEXT-NAME for VPN: gi-iot-asr2')
# 			break
# 	else:
# 		continue
