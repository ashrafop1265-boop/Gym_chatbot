# response for a static input
# import os
# from dotenv import load_dotenv
# from google import genai

# # Load environment variables
# load_dotenv()

# # Create Gemini client
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# # Generate text
# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents="Say hello in one line"
# )

# print(response.text)



# response for a user input from terminal
# import os
# from dotenv import load_dotenv
# from google import genai

# # Load environment variables
# load_dotenv()

# # Create Gemini client
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# # Take input from user
# user_input = input("You: ")

# # Send input to Gemini
# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents=user_input
# )

# # Print Gemini response
# print("Gemini:", response.text)

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("🤖 Gemini Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Gemini: Bye! 👋")
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
    )

    print("Gemini:", response.text)
