from beckett import resources


class Patient(resources.BaseResource):
    class Meta:
        name = 'Patient'
        resource_name = 'patients'
        identifier = 'id'
        pagination_key = 'patients'
        attributes = (
            'accepted_privacy_policy',
            'accepted_sms_marketing',
            'address_1',
            'address_2',
            'address_3',
            'archived_at',
            'city',
            'country',
            'created_at',
            'date_of_birth',
            'deleted_at',
            'email',
            'emergency_contact',
            'first_name',
            'gender',
            'id',
            'invoice_default_to',
            'invoice_email',
            'invoice_extra_information',
            'label',
            'last_name',
            'medicare',
            'notes',
            'occupation',
            'old_reference_id',
            'patient_phone_numbers',
            'post_code',
            'referral_source',
            'reminder_type',
            'state',
            'title',
            'updated_at',
        )
        # subresources = {
        #     'medical_alerts',
        #     'invoices',
        #     'appointments',
        # }
        valid_status_codes = (
            200,
        )
        methods = (
            'get',
        )
