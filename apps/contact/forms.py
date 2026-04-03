from django import forms

from apps.contact.models import ContactSubmission


class ContactSubmissionForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ('full_name', 'email', 'phone', 'subject', 'message')
        error_messages = {
            'full_name': {'required': 'الاسم الكامل مطلوب.'},
            'email': {
                'required': 'البريد الإلكتروني مطلوب.',
                'invalid': 'أدخل بريدًا إلكترونيًا صالحًا.',
            },
            'subject': {'required': 'الموضوع مطلوب.'},
            'message': {'required': 'الرسالة مطلوبة.'},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].label = 'الاسم الكامل'
        self.fields['email'].label = 'البريد الإلكتروني'
        self.fields['phone'].label = 'رقم الجوال'
        self.fields['subject'].label = 'الموضوع'
        self.fields['message'].label = 'الرسالة'

    def clean_message(self):
        message = self.cleaned_data['message'].strip()
        if len(message) < 10:
            raise forms.ValidationError('يجب أن تحتوي الرسالة على 10 أحرف على الأقل.')
        return message
