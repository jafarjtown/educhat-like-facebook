from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_field

class UserAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.avatar = data.get('avatar')
        user.cover = data.get('cover')
        user.save()
        return user
    