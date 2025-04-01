# Import necessary libraries
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv("groq_api_key")

# Retrieve the API key from Streamlit secrets
api_key = st.secrets["groq"]["groq_api_key"]

client = Groq(api_key=api_key)

def generate_prompt(full_name, years_of_experience, desired_positions, tech_stack):
    """
    Generates a prompt for the Groq API to create AI/ML interview questions.
    
    Args:
    full_name (str): Full name of the user.
    years_of_experience (int): Number of years of experience in the field.
    desired_positions (str): Desired job positions.
    tech_stack (str): Tech stack the user is proficient in.
    
    Returns:
    str: A formatted prompt for generating interview questions.
    """
    return (f"Generate an AI/ML interview prompt based on the following details:\n"
            f"Name: {full_name}\n"
            f"Experience: {years_of_experience} year(s)\n"
            f"Desired Positions: {desired_positions}\n"
            f"Tech Stack: {tech_stack}\n\n"
            "Generate 15 interview questions based on the overall experience level and skill set, not skill-wise. "
            "Format the questions as follows:\n"
            "1.\n\n"
            "2.\n\n"
            "3.\n\n"
            "...\n"
            "15.")

def get_interview_questions(prompt):
    """
    Calls the Groq API to generate interview questions based on the given prompt.
    
    Args:
    prompt (str): The prompt to send to the Groq API.
    
    Returns:
    list: A list of interview questions.
    """
    stream = client.chat.completions.create(
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
        temperature=0.2,
        max_completion_tokens=1024,
        top_p=1,
        stop=None,
        stream=True
    )
    
    questions = []
    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content:  # Ensure content is not None
            questions.append(content)
    
    return "".join(questions)

def main():
    """
    Streamlit app to collect user input, generate AI/ML interview questions,
    and display the generated questions.
    """
    # App title
    st.title("AI/ML Interview Question Generator")

    # User input fields
    full_name = st.text_input("Full Name")
    email_address = st.text_input("Email Address")
    phone_number = st.text_input("Phone Number", max_chars=10)

    # Validate phone number length and check if it's numeric
    if phone_number and (len(phone_number) != 10 or not phone_number.isdigit()):
        st.error("Phone number must be 10 digits")

    years_of_experience = st.number_input("Years of Experience", min_value=0)
    desired_positions = st.text_input("Desired Positions")
    current_location = st.text_input("Current Location")
    tech_stack = st.text_area("Tech Stack")

    # Submit button to trigger question generation
    if st.button("Generate Interview Questions"):
        if full_name and years_of_experience is not None and desired_positions and tech_stack:
            # Generate prompt based on the user inputs
            prompt = generate_prompt(full_name, years_of_experience, desired_positions, tech_stack)
            st.write("Generating Interview Questions... Please wait.")
            
            # Get the interview questions from Groq API
            interview_questions = get_interview_questions(prompt)
            
            # Display the generated questions
            st.subheader("Generated AI/ML Interview Questions:")

            # Custom CSS for width
            st.markdown(
                """
                <style>
                .stTextArea {
                    width: 800px;  /* Adjust the width as needed */
                }
                </style>
                """, unsafe_allow_html=True
            )

            # Text area with specific height
            st.text_area("Interview Questions", interview_questions, height=300)
        else:
            st.error("Please fill all fields before generating the questions.")

## Calling the main function
main()
