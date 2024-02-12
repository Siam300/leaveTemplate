from django.contrib import admin
from django.core.mail import send_mail
from .models import LeaveRequest

class LeaveRequestAdmin(admin.ModelAdmin):
    actions = ['approve_selected', 'decline_selected']

    def approve_selected(self, request, queryset):
        for leave_request in queryset:
            leave_request.approval_status = 'approved'
            leave_request.save()

    def decline_selected(self, request, queryset):
        for leave_request in queryset:
            leave_request.approval_status = 'declined'
            leave_request.save()

            # If the approval status is 'declined', send a decline email
            if leave_request.approval_status == 'declined':
                self.send_decline_email(leave_request)

    approve_selected.short_description = "Approve selected leave requests"
    decline_selected.short_description = "Decline selected leave requests"

    list_display = ('student', 'start_date', 'end_date', 'reason', 'approval_status_display')
    list_filter = ('approval_status',)

    def approval_status_display(self, obj):
        return obj.get_approval_status_display()

    approval_status_display.short_description = 'Approval Status'

    def save_model(self, request, obj, form, change):
        # Save the object
        super().save_model(request, obj, form, change)

        # If the approval status is 'approved', send an email
        if obj.approval_status == 'approved':
            self.send_approval_email(obj)
        else:
            # If the approval status is 'declined', send a decline email
            self.send_decline_email(obj)

    def send_approval_email(self, leave_request):
        subject = "Leave Request Approved"
        message = f"Your leave request has been approved. \nStart Date: {leave_request.start_date}, \nEnd Date: {leave_request.end_date}"
        from_email = 'siam.macos@gmail.com'
        recipient_list = [leave_request.email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

    def send_decline_email(self, leave_request):
        subject = "Leave Request Declined"
        message = f"Your leave request has been declined. \nStart Date: {leave_request.start_date}, \nEnd Date: {leave_request.end_date}"
        from_email = 'siam.macos@gmail.com'
        recipient_list = [leave_request.email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

admin.site.register(LeaveRequest, LeaveRequestAdmin)
