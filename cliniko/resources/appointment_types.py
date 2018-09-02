from beckett import resources


class AppointmentTypes(resources.BaseResource):
    class Meta:
        name = 'Appointment_Types'
        resource_name = 'appointment_types'
        identifier = 'url'
        attributes = (
            'category',
            'color',
            'created_at',
            'description',
            'duration_in_minutes',
            'id',
            'max_attendees',
            'name',
            'show_in_online_bookings',
            'updated_at',
        )
        subresources = {
            # 'billable_item':
            # 'practitioners':
        }
        valid_status_codes = (
            200,
        )
        methods = (
            'get',
        )
