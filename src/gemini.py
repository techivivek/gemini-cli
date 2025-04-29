import os
import sys
from google.generativeai import GenerativeModel, configure

# Configure API
configure(api_key=os.getenv("GOOGLE_API_KEY"))  # Set your key in environment variables

def search_gemini(query):
    model = GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"Tell me about: {query}")
    return response.text

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Command-line mode: handle arguments
        query = " ".join(sys.argv[1:])
        result = search_gemini(query)
        print(result)
    else:
        # Interactive mode: ask for input repeatedly
        print("Gemini Search Interactive Mode. Type your query or 'exit' to quit.")
        while True:
            query = input("Search: ").strip()
            if query.lower() in {"exit", "quit"}:
                print("Goodbye!")
                break
            if query:
                try:
                    result = search_gemini(query)
                    print(result)
                except Exception as e:
                    print(f"An error occurred: {e}")
