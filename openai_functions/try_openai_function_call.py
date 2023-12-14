# Import Modules
import os
import json
import openai
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Load OpenAI API Token From the .env File
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
messages = [{"role": "user", "content": "What's the weather like in Tokoyo and San Francisco."}]
tools = [
    {       "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. Tokoyo, CA",
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["location"],
            },
        }
    
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=messages,
    functions=tools,
)
response_message = response.choices[0].message
print(response_message )

def get_current_weather(location, unit="fahrenheit"):
    """Get weather information of any locations."""
    """Get the current weather in a given location"""
    if "tokyo" in location.lower():
        return json.dumps({"datetime": str(datetime.now()), "location": "Tokyo", "temperature": "10", "unit": unit})
    elif "san francisco" in location.lower():
        return json.dumps({"datetime": str(datetime.now()), "location": "San Francisco", "temperature": "72", "unit": unit})
    elif "paris" in location.lower():
        return json.dumps({"datetime": str(datetime.now()), "location": "Paris", "temperature": "22", "unit": unit})
    else:
        return json.dumps({"datetime": str(datetime.now()), "location": location, "temperature": "unknown"})


place = json.loads(response_message.function_call.arguments).get("location")
params = json.loads(response_message.function_call.arguments)
type(params)

print(place)
print(params)
# Call the function with arguments fo magic
chosen_function = eval(response_message.function_call.name)
Weather = chosen_function(**params)
print(Weather)
