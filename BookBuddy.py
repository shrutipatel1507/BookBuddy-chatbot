from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY_HERE",  
    base_url="https://api.groq.com/openai/v1"
)

while True:
    user_input = input("you: ")
    if user_input == "quit":
        print("bot: Happy reading! Goodbye :)")
        break

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are a friendly book recommendation bot. Suggest books based on genre, mood, or author's name. Don't answer anything unrelated to books."},
            {"role": "user", "content": user_input}
        ]
    )

    print("bot:", response.choices[0].message.content)
