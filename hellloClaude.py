import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

conversations = []
while True:
    user_input = input("Your message: ")
    if user_input.lower() in ["quit", "exit", "bye", "ciao", "merci"]:
        break
    conversations.append({"role": "user", "content": user_input})
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        system="You are a helpful assistant that can answer questions and help with tasks. Your answer are short and concise with as much details as possible.",
        messages= conversations
    )
    conversations.append({"role": "assistant", "content": message.content[0].text})
    print(message.content[0].text)