from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="請問一個星期有幾天？"
)

print(interaction.output_text)