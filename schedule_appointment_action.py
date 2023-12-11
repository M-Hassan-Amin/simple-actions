from base_action import BaseAction
import datetime

class ScheduleAppointmentAction(BaseAction):
    def __init__(self, notification_service):
        # Assuming notification_service is an instance of a class responsible for sending notifications
        self.notification_service = notification_service

    def run(self, date, time, participant):
        # Combine date and time into a single datetime object
        appointment_datetime = datetime.datetime.strptime(f'{date} {time}', '%Y-%m-%d %H:%M')

        # Logic to schedule the appointment
        # For example, saving to a file or database (not implemented here)
        appointment_details = f"Appointment scheduled on {appointment_datetime} with {participant}"

        # Logic to notify the participant
        # This could be an email, SMS, etc. Here, we'll just print the details
        self.notification_service.notify(participant, "Appointment Scheduled", appointment_details)

        return appointment_details

