from django import forms

from apps.teacher.models import TeacherApplication


class MultipleFileInput(forms.FileInput):
    """FileInput widget that allows selecting multiple files at once."""
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    """FileField that accepts multiple files and returns a list."""

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('widget', MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class TeacherApplicationForm(forms.ModelForm):
    """Form used on the public-facing 'join as teacher' page."""

    # Multi-file upload handled separately via request.FILES.getlist()
    attachments = MultipleFileField(
        label='المرفقات',
        required=False,
        widget=MultipleFileInput(attrs={
            'accept': 'image/*,video/*,.pdf,.doc,.docx,.ppt,.pptx',
            'class': (
                'block w-full cursor-pointer text-sm text-slate-600 '
                'file:ml-4 file:rounded-full file:border-0 '
                'file:bg-brand-50 file:px-4 file:py-2 '
                'file:text-sm file:font-semibold file:text-brand-700 '
                'hover:file:bg-brand-100'
            ),
        }),
        help_text='يمكنك رفع أكثر من ملف (صور، فيديوهات، ملفات PDF، شهادات، الخ)',
    )

    class Meta:
        model = TeacherApplication
        fields = [
            'full_name',
            'phone',
            'email',
            'specialization',
            'experience',
            'courses',
            'description',
        ]
        labels = {
            'full_name': 'الاسم الكامل',
            'phone': 'رقم الهاتف',
            'email': 'البريد الإلكتروني (اختياري)',
            'specialization': 'التخصص',
            'experience': 'سنوات الخبرة',
            'courses': 'الكورسات التي تستطيع تدريسها',
            'description': 'نبذة عنك',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'مثال: محمد أحمد العمري',
                'class': 'form-input',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'مثال: 0512345678',
                'type': 'tel',
                'class': 'form-input',
                'dir': 'ltr',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'example@email.com',
                'class': 'form-input',
                'dir': 'ltr',
            }),
            'specialization': forms.TextInput(attrs={
                'placeholder': 'مثال: رياضيات - ثانوي',
                'class': 'form-input',
            }),
            'experience': forms.Select(attrs={
                'class': 'form-input',
            }),
            'courses': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'مثال:\nرياضيات الصف الأول ثانوي\nرياضيات القدرات\nتحصيلي رياضيات',
                'class': 'form-input',
            }),
            'description': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'أخبرنا عن نفسك، خبراتك، وأسلوبك في التدريس...',
                'class': 'form-input',
            }),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()
        digits = ''.join(filter(str.isdigit, phone))
        if len(digits) < 9:
            raise forms.ValidationError('رقم الهاتف يجب أن يحتوي على 9 أرقام على الأقل.')
        return phone
