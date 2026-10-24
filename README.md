StudyBuddy AI

StudyBuddy AI is a simple AI-powered study assistant that helps students study more effectively. Students enter a topic, choose their available study time, and select their difficulty level. The app generates a personalized study plan, a five-question practice quiz, and useful study tips.

Features

- Personalized study plans based on the topic and available time
- Beginner-friendly and adaptable explanations
- Five multiple-choice quiz questions with answers and explanations
- Practical study tips
- Simple, user-friendly interface

Prompt Engineering Techniques

1. Role-Based Prompting: The system prompt gives the AI the role of a friendly and patient personal tutor. This helps guide the tone and level of the generated content.

2. Structured Output Prompting: The system prompt requests a specific JSON structure containing the study plan, quiz questions, answer options, correct answers, explanations, and tips. This allows the frontend to display the generated content in an organized format.

3. Constraint-Based Prompting: The prompt specifies the number of study steps, exactly five quiz questions, four answer options per question, and a limited number of study tips.

Technologies Used

- Python
- Flask
- Groq API
- HTML, CSS, and JavaScript
- python-dotenv

Setup Instructions

1. Install Python 3.10 or newer.
2. Clone or download this repository.
3. Create and activate a Python virtual environment.
4. Install the required packages:

   pip install flask groq python-dotenv


5. Create a .env file in the project root and add your Groq API key:

   GROQ_API_KEY=your_api_key_here
   

6. Start the application:

   python app.py
   

7. Open http://127.0.0.1:5000 in your browser.

Testing

The application was tested with different subjects, including Photosynthesis and Java Loops, using different study durations and difficulty levels.

Security

The .env file containing the API key should never be uploaded to GitHub. The API key is kept in an environment variable and is used by the Flask backend.

Purpose

This project demonstrates how prompt engineering and a generative AI API can be combined with a web interface to create a practical educational assistant.
