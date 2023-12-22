import os
import json
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define your local function
def get_weather_info(location):
    return {
        "location": location,
        "forecast": "Sunny",
        "temperature": "75°F"
    }
def get_news_summary(topic):
    """Simulate getting a news summary about a topic."""
    return {
        "topic": topic,
        "summary": "Today in news, major events include..."
    }

def get_recipe(ingredient):
    """Simulate getting a recipe that includes a specific ingredient."""
    return {
        "ingredient": ingredient,
        "recipe": "Delicious dish involving " + ingredient
    }

def calculate_tax(income):
    """Simulate calculating tax based on income."""
    # This is a simplistic calculation and should be replaced with actual tax logic
    tax_rate = 0.3  # Example tax rate
    calculated_tax = income * tax_rate
    return {
        "income": income,
        "tax": calculated_tax
    }

def translate_text(text, target_language):
    """Simulate translating text into a target language."""
    # This is a mock translation and should be replaced with actual translation logic
    translated = "Translated text of '" + text + "' into " + target_language
    return {
        "original_text": text,
        "translated_text": translated
    }


# Define your function descriptions
function_descriptions = [
    {
        "name": "get_weather_info",
        "description": "Get weather information for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The location for the weather forecast, e.g. New York"
                }
            },
            "required": ["location"],
        },
    },
    {
        "name": "get_news_summary",
        "description": "Get a summary of news about a topic",
        "parameters": {
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "The topic for the news summary, e.g. Technology"
                }
            },
            "required": ["topic"],
        },
    },
    {
        "name": "get_recipe",
        "description": "Get a recipe involving a specific ingredient",
        "parameters": {
            "type": "object",
            "properties": {
                "ingredient": {
                    "type": "string",
                    "description": "The primary ingredient for the recipe, e.g. Chicken"
                }
            },
            "required": ["ingredient"],
        },
    },
    {
        "name": "calculate_tax",
        "description": "Calculate tax based on income",
        "parameters": {
            "type": "object",
            "properties": {
                "income": {
                    "type": "number",
                    "description": "The income to calculate tax on, e.g. 50000"
                }
            },
            "required": ["income"],
        },
    },
    {
        "name": "translate_text",
        "description": "Translate text into a specified language",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "string",
                    "description": "The text to be translated, e.g. Hello, world!"
                },
                "target_language": {
                    "type": "string",
                    "description": "The target language for translation, e.g. Spanish"
                }
            },
            "required": ["text", "target_language"],
        },
    },
    
]

def ask_and_reply(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[{"role": "user", "content": prompt}],
        functions=function_descriptions,
        function_call="auto",
    )
    return completion

def execute_function(function_name, arguments):
    # Match the function name to your local functions and execute
    if function_name == "get_weather_info":
        location = json.loads(arguments)['location']
        return get_weather_info(location)
    elif function_name == "get_news_summary":
        topic = json.loads(arguments)['topic']
        return get_news_summary(topic)
    elif function_name == "get_recipe":
        ingredient = json.loads(arguments)['ingredient']
        return get_recipe(ingredient)
    elif function_name == "calculate_tax":
        income = json.loads(arguments)['income']
        return calculate_tax(income)
    elif function_name == "translate_text":
        text = json.loads(arguments)['text']
        target_language = json.loads(arguments)['target_language']
        return translate_text(text, target_language)

example_prompts = [
    "What's the weather like in Paris today?",
    "Give me the latest news on space exploration.",
    "I have chicken, suggest a recipe.",
    "How much tax do I owe on $50,000?",
    "Translate 'Hello, world!' to Spanish."
]

# Loop through each prompt and get a response
for prompt in example_prompts:
    print("\nAsking: ", prompt)
    completion = ask_and_reply(prompt)
    # print(completion.choices[0].message.function_call)
    function_call = completion.choices[0].message.function_call
    # print(function_call.name, function_call.arguments)
    if function_call:
        function_name = function_call['name']
        arguments = function_call['arguments']
        function_result = execute_function(function_name, arguments)
        print("Function Result:", function_result)
    else:
        print("Response: ", completion.choices[0].message['content'])

# prompt = input("Enter: ")
# print("Asking: ", prompt)
# completion = ask_and_reply(prompt)
# print(completion.choices[0].message.function_call)

# # Check if there is a function call in the response
# function_call = completion.choices[0].message.function_call
# print(function_call.name, function_call.arguments)
# if function_call:
#     function_name = function_call['name']
#     arguments = function_call['arguments']
#     function_result = execute_function(function_name, arguments)
#     print("Function Result:", function_result)
# else:
#     print("Response: ", completion.choices[0].message['content'])
