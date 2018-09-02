from beckett import resources


class Invoice(resources.BaseResource):
    class Meta:
        name = 'Invoice'
        resource_name = 'invoices'
        identifier = 'id'
        pagination_key = 'invoices'
        attributes = (
            'archived_at',
            'closed_at',
            'created_at',
            'deleted_at',
            'discounted_amount',
            'id',
            'invoice_to',
            'issue_date',
            'net_amount',
            'notes',
            'number',
            'patient_extra_information',
            'status',
            'status_description',
            'tax_amount',
            'total_amount',
            'updated_at',
        )
        subresources = {
            # 'patient': Patient
            # 'appointment',
            # 'business',
            # 'practitioner',
        }
        valid_status_codes = (
            200,
        )
        methods = (
            'get',
        )
