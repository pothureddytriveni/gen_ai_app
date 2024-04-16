import streamlit as st
import openai

# Read OpenAI API key from file
with open('newkey_open_ai.txt', 'r') as f:
    open_api_key = f.read().strip()

# Initialize OpenAI client with the API key
openai.api_key = open_api_key

# Function to call OpenAI API for code review
def code_review(code):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a Python code reviewer."},
            {"role": "user", "content": code}
        ]
    )
    return response.choices[0].message["content"].strip()

# Streamlit UI
def main():
    st.title("✨GenAI App - AI Code Reviewer")
    st.write("Welcome to the GenAI App! Submit your Python code below for review.")

    # Text area for user to input Python code
    user_code = st.text_area("Enter your Python code here:", height=300)

    # Button to trigger code review
    if st.button("Review Code"):
        if user_code.strip() != "":
            st.write("Reviewing your code...")
            feedback = code_review(user_code)
            st.subheader("🤷‍♀️Code Review Feedback:")
            st.code(feedback, language="python")
        else:
            st.warning("Please enter some Python code.")

if __name__ == "__main__":
    main()
