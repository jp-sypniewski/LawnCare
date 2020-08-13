from lawn_care.services import user_service
from lawn_care.viewmodels.shared.viewmodelbase import ViewModelBase


class RegisterViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.username = self.request_dict.username
        self.password = self.request_dict.password
        self.email = self.request_dict.email
        self.first_name = self.request_dict.first_name
        self.last_name = self.request_dict.last_name

    def validate(self):
        if not self.username:
            self.error = 'Username required.'
        elif not self.password:
            self.error = 'Username required.'
        elif not self.email:
            self.error = 'Username required.'
        elif user_service.find_user_by_email(self.email):
            self.error = 'A user with this email address already exists.'
