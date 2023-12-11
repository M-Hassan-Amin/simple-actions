# from action_factory import ActionFactory

# class ActionsWorker:
#     def __init__(self, input_queue, output_queue, smtp_details, notification_service):
#         self.input_queue = input_queue
#         self.output_queue = output_queue
#         # Initialize ActionFactory with required parameters
#         self.factory = ActionFactory(smtp_details=smtp_details, notification_service=notification_service)

#     def run(self):
#         while True:
#             action_request = self.input_queue.get()
#             # action_request should include the action type and any additional parameters for the action
#             action_type = action_request['action_type']
#             action_params = action_request.get('params', {})
#             action = self.factory.create_action(action_type, **action_params)
#             result = action.run()
#             self.output_queue.put(result)


from action_factory import ActionFactory
from queue import Queue

class ActionsWorker:
    def __init__(self, input_queue, output_queue):
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.factory = ActionFactory()

    def run(self):
        while True:
            action_request = self.input_queue.get()
            action_type = action_request['action_type']
            action_params = action_request.get('params', {})
            action = self.factory.create_action(action_type, **action_params)
            result = action.run(**action_params)
            self.output_queue.put(result)
