import os
import openai
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, ChatMessage

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-3.5-turbo-0613", temperature=0)

# Start a conversation with multiple requests
function_descriptions_multiple = [
    {
        "name": "get_flight_info",
        "description": "Get flight information between two locations",
        "parameters": {
            "type": "object",
            "properties": {
                "loc_origin": {
                    "type": "string",
                    "description": "The departure airport, e.g. DUS",
                },
                "loc_destination": {
                    "type": "string",
                    "description": "The destination airport, e.g. HAM",
                },
            },
            "required": ["loc_origin", "loc_destination"],
        },
    },
    {
        "name": "book_flight",
        "description": "Book a flight based on flight information",
        "parameters": {
            "type": "object",
            "properties": {
                "loc_origin": {
                    "type": "string",
                    "description": "The departure airport, e.g. DUS",
                },
                "loc_destination": {
                    "type": "string",
                    "description": "The destination airport, e.g. HAM",
                },
                "datetime": {
                    "type": "string",
                    "description": "The date and time of the flight, e.g. 2023-01-01 01:01",
                },
                "airline": {
                    "type": "string",
                    "description": "The service airline, e.g. Lufthansa",
                },
            },
            "required": ["loc_origin", "loc_destination", "datetime", "airline"],
        },
    },
    {
        "name": "file_complaint",
        "description": "File a complaint as a customer",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The name of the user, e.g. John Doe",
                },
                "email": {
                    "type": "string",
                    "description": "The email address of the user, e.g. john@doe.com",
                },
                "text": {
                    "type": "string",
                    "description": "Description of issue",
                },
            },
            "required": ["name", "email", "text"],
        },
    },
]

user_prompt = """
This is Jane Harris. I am an unhappy customer that wants you to do several things.
First, I neeed to know when's the next flight from Amsterdam to New York.
Please proceed to book that flight for me.
Also, I want to file a complaint about my missed flight. It was an unpleasant surprise. 
Email me a copy of the complaint to jane@harris.com.
Please give me a confirmation after all of these are done.
"""

# Returns the function of the first request (get_flight_info)

first_response = llm.predict_messages(
    [HumanMessage(content=user_prompt)], functions=function_descriptions_multiple
)

# print(first_response)

print("\n----------------------------------------------------\n")

second_response = llm.predict_messages(
    [
        HumanMessage(content=user_prompt),
        AIMessage(content=str(first_response.additional_kwargs)),
        AIMessage(
            role="function",
            additional_kwargs={
                "name": first_response.additional_kwargs["function_call"]["name"]
            },
            content=f"Completed function {first_response.additional_kwargs['function_call']['name']}",
        ),
    ],
    functions=function_descriptions_multiple,
)

# print(second_response)
third_response = llm.predict_messages(
    [
        HumanMessage(content=user_prompt),
        AIMessage(content=str(first_response.additional_kwargs)),
        AIMessage(content=str(second_response.additional_kwargs)),
        AIMessage(
            role="function",
            additional_kwargs={
                "name": second_response.additional_kwargs["function_call"]["name"]
            },
            content=f"Completed function {second_response.additional_kwargs['function_call']['name']}",
        ),
    ],
    functions=function_descriptions_multiple,
)

print(third_response)