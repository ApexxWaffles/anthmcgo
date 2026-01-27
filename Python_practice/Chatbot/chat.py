from openai import OpenAI
client = OpenAI()

user_prompt = input("You: ")
system_prompt = "Limit your response to 100 words. Respond in a friendly and engaging manner. Use simple language and avoid technical jargon. Make sure to include an example of a Caesar Cipher with a shift of 3 in your response."

reponse = client.chat.completions.create(
    model="gpt-5",
    input= user_prompt,
    instructions=system_prompt
)

print("Chatbot: " + reponse.output_text)