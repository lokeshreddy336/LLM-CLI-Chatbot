import google.generativeai as genai

api_key = "Gemini-API_KEY"  
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-pro")

def is_math_question(prompt):
    math_keywords = ["+", "-", "*", "/", "add", "sum", "multiply", "divide", "math", "calculate", "=", "times", "product"]
    return any(word in prompt.lower() for word in math_keywords)

def main():
    print("Gemini Chatbot (No Math Solver)")
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Gemini: Goodbye!")
            break

        if is_math_question(user_input):
            print("I don't solve math problems, please refer to a calculator!!.")
            continue

        try:
            response = model.generate_content(user_input)
            print("Gemini:", response.text)
        except Exception as e:
            print(" Error talking to Gemini:", e)

if __name__ == "__main__":
    main()
