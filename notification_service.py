# Example of a simple notification service (to be implemented)
class NotificationService:
    def notify(self, recipient, subject, message):
        # In a real implementation, this might send an email or SMS
        print(f"Notification sent to {recipient}: {subject} - {message}")
