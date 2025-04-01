## Project Overview
The **Interview Question Generator** is a Streamlit-based web application designed to assist in generating AI/ML interview questions. By gathering user input such as years of experience, desired positions, and tech stack, the app uses the Groq API to create a customized set of interview questions tailored to the user’s profile. It is especially useful for candidates preparing for AI/ML job interviews or companies looking to create interview questions based on specific skills and experience levels.

## Installation Instructions
To run the **Interview Question Generator** locally, follow the steps below:

### Prerequisites:
1. **Python 3.7+**
2. **Streamlit** for creating the web application.
3. **Groq API** key for generating interview questions.
4. **.env file** for securely storing environment variables (API keys).

### Steps:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/interview-question-generator.git
   cd interview-question-generator
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scriptsctivate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the environment variables**:
   - Create a `.env` file in the root directory.
   - Add your **Groq API key** in the `.env` file:
     ```bash
     groq_api_key=YOUR_API_KEY
     ```

5. **Configure Streamlit secrets**:
   - Create a `secrets.toml` file in the `.streamlit` folder.
   - Add your **Groq API key**:
     ```toml
     [groq]
     groq_api_key = "YOUR_API_KEY"
     ```

6. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

7. Open a web browser and navigate to `http://localhost:8501` to access the app.

## Usage Guide
1. **Open the Application**: Once the app is running, you will be greeted with a form asking for the following details:
   - **Full Name**
   - **Email Address**
   - **Phone Number**
   - **Years of Experience** (Numeric input)
   - **Desired Positions**
   - **Current Location**
   - **Tech Stack** (List the technologies you're proficient in)

2. **Generate Interview Questions**:
   - After filling in the form, click the **Generate Interview Questions** button.
   - The application will generate customized AI/ML interview questions based on the provided inputs (experience, desired position, and tech stack).
   - The generated interview questions will be displayed in a text area for easy review.

3. **Follow-up**: The user can use the context to check the previous conversation or review the generated questions. The session maintains the conversation flow, ensuring a coherent and context-aware interaction.

## Technical Details

### Libraries Used:
- **Streamlit**: For building the interactive web interface.
- **Groq**: To interact with the Groq API for generating customized AI/ML interview questions.
- **dotenv**: To manage environment variables securely.
- **os**: For managing system-level tasks like reading environment variables.
  
### Model Details:
- **Groq API**: The app uses Groq’s API (through the `groq` Python package) to generate AI/ML interview questions. The model used is **llama-3.3-70b-versatile** with a temperature of 0.2 and a maximum completion token of 1024. This ensures that the generated questions are relevant, diverse, and well-formatted.
  
### Architectural Decisions:
- **Streamlit** was chosen for rapid prototyping and easy deployment of the web application.
- The app uses **session_state** to maintain context across user interactions, ensuring a coherent conversation flow for follow-up queries.
- The **Groq API** is leveraged to generate interview questions dynamically based on the user’s profile and desired job role.

## Prompt Design

The interview question generation is based on the following approach:
- **Inputs**: The system uses user-provided details such as years of experience, desired positions, and tech stack to generate a relevant set of interview questions.
- **Prompt Structure**: The prompt is structured to ensure all provided tech stack technologies are covered and that the questions are appropriate for the candidate's experience level.
  
Here’s an example of how the prompt is crafted:

```text
Generate an AI/ML interview prompt based on the following details:
Experience: 5 year(s)
Desired Positions: Data Scientist, Machine Learning Engineer
Tech Stack: Python, TensorFlow, SQL, Scikit-learn

Generate 15 interview questions based on the overall experience level and Tech Stack and strictly ensure that all Tech Stack are covered.
Format the questions as follows:
1.
2.
3.
...
15.
```

This prompt ensures that the questions are directly relevant to the user’s tech stack and experience.

## Challenges & Solutions

### Challenge 1: **Dynamic Question Generation**
- **Problem**: Ensuring that the questions are dynamically generated based on the user’s specific inputs and tech stack.
- **Solution**: We leveraged the **Groq API**'s flexibility in generating context-aware responses. By formatting a detailed prompt that includes the user’s input data, we can guide the model to produce relevant and diverse interview questions.

### Challenge 2: **Maintaining Conversation Context**
- **Problem**: Managing a coherent flow of conversation, especially if the user asks follow-up questions or wants to adjust their inputs.
- **Solution**: We used **Streamlit’s session state** to store the conversation context, allowing the app to retain the previously generated questions and ensure follow-up interactions remain contextually relevant.

### Challenge 3: **User Input Validation**
- **Problem**: Validating the user’s phone number and ensuring that all required fields are filled correctly before generating the questions.
- **Solution**: We added input validation, especially for the phone number, ensuring it’s exactly 10 digits long and numeric, and included error handling for any missing fields.

---
