from lawn_care.viewmodels.shared.viewmodelbase import ViewModelBase


class SubmitQuoteViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.requester_name = self.request_dict.requester_name
        self.dttm_requested = self.request_dict.dttm_requested
        self.contact_phone = self.request_dict.contact_phone
        self.contact_email = self.request_dict.contact_email
        self.preference_contact = self.request_dict.preference_contact

    def validate(self):
        if not self.requester_name:
            self.error = 'You must specify a name.'
