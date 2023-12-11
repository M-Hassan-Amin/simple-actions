# from actions_worker import ActionsWorker
# from queue import Queue
# from notification_service import NotificationService
# import threading

# class ChatGPTAgent:
#     def __init__(self, smtp_details, notification_service):
#         self.input_queue = Queue()
#         self.output_queue = Queue()
#         self.actions_worker = ActionsWorker(self.input_queue, self.output_queue, smtp_details, notification_service)
#         self.worker_thread = threading.Thread(target=self.actions_worker.run, daemon=True)  # daemon thread for graceful exit
#         self.worker_thread.start()


#     def process_input(self, user_input):
#         # Process the user input and dynamically determine the action
#         # This is a placeholder logic. Implement your own logic to parse user_input and decide the action.
#         action_request = {
#             "action_type": "write_email",  # Placeholder action type
#             "params": {
#                 "recipient": "example@example.com",
#                 "subject": "Test Email",
#                 "body": "This is a test email from ChatGPTAgent."
#             }
#         }
#         self.input_queue.put(action_request)

#     def check_for_action_output(self):
#         if not self.output_queue.empty():
#             result = self.output_queue.get()
#             return result
#         return None

#     def run(self):
#         try:
#             while True:
#                 user_input = input("You: ")
#                 self.process_input(user_input)
#                 action_result = self.check_for_action_output()
#                 if action_result:
#                     print("Agent:", action_result)
#         except KeyboardInterrupt:
#             print("Shutting down the agent...")

# # # Example initialization
# smtp_details = {'server': 'your_smtp_server', 'port': 587, 'username': 'username', 'password': 'password'}
# notification_service = NotificationService()  # Replace with your actual notification service instance

# agent = ChatGPTAgent(smtp_details, notification_service)
# agent.run()


from actions_worker import ActionsWorker
from queue import Queue
import threading

class ChatGPTAgent:
    def __init__(self):
        self.input_queue = Queue()
        self.output_queue = Queue()
        self.actions_worker = ActionsWorker(self.input_queue, self.output_queue)
        self.worker_thread = threading.Thread(target=self.actions_worker.run)
        self.worker_thread.daemon = True
        self.worker_thread.start()

    def process_input(self, user_input):
            # Process the user input to decide the action
            if "add" in user_input:
                numbers = [int(s) for s in user_input.split() if s.isdigit()]
                action_request = {"action_type": "add_numbers", "params": {"num1": numbers[0], "num2": numbers[1]}}
                self.input_queue.put(action_request)
            elif "concat" in user_input:
                strings = user_input.split()[1:]
                action_request = {"action_type": "concatenate_strings", "params": {"string1": strings[0], "string2": strings[1]}}
                self.input_queue.put(action_request)



    def check_for_action_output(self):
        if not self.output_queue.empty():
            result = self.output_queue.get()
            return result
        return None

    def run(self):
        while True:
            user_input = input("You: ")
            self.process_input(user_input)
            action_result = self.check_for_action_output()
            if action_result is not None:
                print("Agent:", action_result)

# Example usage
agent = ChatGPTAgent()
agent.run()
