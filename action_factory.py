# from write_email_action import WriteEmailAction
# from schedule_appointment_action import ScheduleAppointmentAction

# class ActionFactory:
#     def __init__(self, smtp_details, notification_service):
#         # smtp_details might be a dictionary containing SMTP server info
#         # notification_service is an instance of a class for sending notifications
#         self.smtp_details = smtp_details
#         self.notification_service = notification_service

#     def create_action(self, action_type, **params):
#         if action_type == 'write_email':
#             # Pass SMTP details to the WriteEmailAction class
#             return WriteEmailAction(smtp_server=self.smtp_details['server'],
#                                     smtp_port=self.smtp_details['port'],
#                                     smtp_username=self.smtp_details['username'],
#                                     smtp_password=self.smtp_details['password'])

#         elif action_type == 'schedule_appointment':
#             # Pass the notification service to the ScheduleAppointmentAction class
#             return ScheduleAppointmentAction(notification_service=self.notification_service)

#         else:
#             raise ValueError("Unknown action type")


from add_numbers_action import AddNumbersAction
from concatenate_strings_action import ConcatenateStringsAction

class ActionFactory:
    def create_action(self, action_type, **params):
        if action_type == 'add_numbers':
            return AddNumbersAction()
        elif action_type == 'concatenate_strings':
            return ConcatenateStringsAction()
        else:
            raise ValueError("Unknown action type")
