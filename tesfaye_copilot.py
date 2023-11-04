import openai
from flask import Flask, request, render_template, jsonify

app = Flask("AI_Assistant")

# Set your OpenAI API key (if using GPT-3)
openai.api_key = 'your_openai_api_key_here'

# Data science dataset
data_science_dataset = [
    # Your data science questions and answers here...
]

# Physics dataset
physics_dataset = [
    # Your physics questions and answers here...
]

# Your TeacherAssistant class and ai_hook function here...

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.form['user_question']
    response = ai_hook(user_question)
    return render_template('index.html', user_question=user_question, response=response)

if __name__ == '__main__':
    app.run(debug=True)
import random

class TeacherAssistant:
    def __init__(self):
        self.schedule = {}  # Dictionary to store schedules
        self.grades = {}    # Dictionary to store student grades

    def add_schedule(self, day, subject, time):
        if day not in self.schedule:
            self.schedule[day] = {}
        self.schedule[day][time] = subject

    def add_grade(self, student, subject, grade):
        if student not in self.grades:
            self.grades[student] = {}
        self.grades[student][subject] = grade

    def get_schedule(self, day):
        if day in self.schedule:
            return self.schedule[day]
        return "No classes scheduled for this day."

    def get_student_grade(self, student, subject):
        if student in self.grades and subject in self.grades[student]:
            return f"{student}'s grade in {subject}: {self.grades[student][subject]}"
        return f"No grade found for {student} in {subject}."
def ai_hook(question):
    # Simulated AI response based on a few predefined queries
    predefined_queries = {
        "What is my schedule for Monday?": "You have Math at 9:00 AM and Science at 11:00 AM.",
        "What is my grade in Math?": "Your grade in Math is 95%.",
   }
   # Check if the AI can answer the query based on predefined queries
    if question in predefined_queries:
     return predefined_queries[question]
    else:
        return "I'm sorry, I don't have an answer for that right now."


# Example usage:
assistant = TeacherAssistant()

# Add schedules
assistant.add_schedule("Monday", "Math", "9:00 AM")
assistant.add_schedule("Monday", "Science", "11:00 AM")

# Add grades
assistant.add_grade("Alice", "Math", 95)
assistant.add_grade("Alice", "Science", 88)

# Sample AI queries
query1 = "What is my schedule for Monday?"
query2 = "What is my grade in Math?"

# Get responses
response1 = assistant.get_schedule("Monday")
response2 = assistant.get_student_grade("Alice", "Math")
print(response1)
print(response2)

# Sample data science queries
query1 = "What is data science?"
query2 = "Explain the CRISP-DM process."
query3 = "Tell me about machine learning."

# Get responses
response1 = ai_hook(query1)
response2 = ai_hook(query2)
response3 = ai_hook(query3)

import openai

# Set your OpenAI API key (if using GPT-3)
openai.api_key = 'your_openai_api_key_here'

# Data science dataset
data_science_dataset = [
    {
        "question": "What is data science?",
        "answer": "Data science is an interdisciplinary field that uses scientific methods, algorithms, processes, and systems to extract knowledge and insights from structured and unstructured data."
    },
    {
        "question": "What is the CRISP-DM process in data science?",
        "answer": "CRISP-DM (Cross-Industry Standard Process for Data Mining) is a widely-used process model for data mining and data science projects. It consists of six phases: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, and Deployment."
    },
    {
        "question": "Explain the concept of machine learning.",
        "answer": "Machine learning is a subset of artificial intelligence that involves developing algorithms and models that allow computers to learn and make predictions or decisions without being explicitly programmed. It uses data to improve its performance over time."
    },
    {
        "question": "What is the difference between supervised and unsupervised learning?",
        "answer": "Supervised learning is a type of machine learning where the model is trained on a labeled dataset, meaning it is provided with input-output pairs. Unsupervised learning, on the other hand, involves learning from unlabeled data to discover patterns or relationships in the data."
    },
    {
        "question": "What is the role of data preprocessing in data science?",
        "answer": "Data preprocessing is the process of cleaning and transforming raw data into a suitable format for analysis. It involves tasks like data cleaning, missing value imputation, feature scaling, and more to ensure data quality."
    },{
        "question": "What are some popular data science programming languages?",
        "answer": "Popular data science programming languages include Python, R, and Julia. Python is widely used for its versatility and a rich ecosystem of libraries."
    },
    {
        "question": "Explain overfitting in machine learning.",
        "answer": "Overfitting occurs when a machine learning model performs very well on the training data but fails to generalize to new, unseen data. It's a result of the model learning the noise in the training data."
    },
    {
        "question": "What is feature engineering?",
        "answer": "Feature engineering is the process of creating new features or transforming existing ones to improve the performance of a machine learning model. It involves selecting, combining, or modifying features to capture relevant information."
    },
    {
        "question": "What is the purpose of cross-validation in machine learning?",
        "answer": "Cross-validation is a technique used to assess the generalization performance of a machine learning model. It helps estimate how well the model will perform on unseen data by splitting the data into training and testing sets multiple times."
    },
    {
        "question": "What is the difference between a data scientist and a data analyst?",
        "answer": "Data scientists are responsible for in-depth data analysis, model building, and often work with unstructured data. Data analysts focus on summarizing and visualizing data to support decision-making."
    }
]
#physics dataset
physics_dataset = [
    {
        "question": "What is Newton's first law of motion?",
        "answer": "Newton's first law of motion, also known as the law of inertia, states that an object at rest tends to stay at rest, and an object in motion tends to stay in motion with the same speed and in the same direction unless acted upon by an external force."
    },
    {
        "question": "What is the formula for calculating gravitational force?",
        "answer": "The formula for calculating gravitational force between two objects is given by Newton's law of universal gravitation: F = (G * m1 * m2) / r^2, where F is the gravitational force, G is the gravitational constant, m1 and m2 are the masses of the objects, and r is the distance between them."
    },
    {
        "question": "Explain the concept of electromagnetic waves.",
        "answer": "Electromagnetic waves are a form of energy that propagate through space as oscillating electric and magnetic fields. They include various types of waves, such as radio waves, microwaves, visible light, and X-rays, each with different wavelengths and frequencies."
    },
    {
        "question": "What is the first law of thermodynamics?",
        "answer": "The first law of thermodynamics, also known as the law of conservation of energy, states that energy cannot be created or destroyed in an isolated system. It can only change forms from one to another."
    },
    {
        "question": "Explain the theory of relativity.",
        "answer": "The theory of relativity, developed by Albert Einstein, includes both the special theory of relativity and the general theory of relativity. It fundamentally changes our understanding of space, time, and gravity. The special theory deals with objects in motion at constant velocity, while the general theory extends this to include gravity and acceleration."
    },
    {
        "question": "What are the fundamental particles in the Standard Model of particle physics?",
        "answer": "The Standard Model of particle physics describes the fundamental particles of the universe. It includes quarks, which make up protons and neutrons, and leptons, such as electrons and neutrinos. It also includes bosons, like the Higgs boson, which are responsible for mediating fundamental forces."
    },
    {
        "question": "Explain the concept of wave-particle duality in quantum mechanics.",
        "answer": "Wave-particle duality is a fundamental principle of quantum mechanics, suggesting that particles like electrons exhibit both wave-like and particle-like behaviors. This duality is described by mathematical wave functions and is essential for understanding quantum phenomena."
    },
    {
        "question": "What is the Heisenberg Uncertainty Principle?",
        "answer": "The Heisenberg Uncertainty Principle, formulated by Werner Heisenberg, states that it is impossible to simultaneously know the exact position and momentum of a particle with absolute certainty. The more precisely one property is known, the less precisely the other can be determined."
    }
]



def ai_hook(question):
    # Check for data science-related questions and provide answers from the dataset (case-insensitive)
    question_lower = question.lower()
    for entry in data_science_dataset:
        if entry["question"].lower() in question_lower:
            return entry["answer"]
        
    # Check for physics-related questions and provide answers from the physics dataset (case-insensitive)
    for entry in physics_dataset:
        if entry["question"].lower() in question_lower:
            return entry["answer"]

    # If the question is related to physics, use GPT-3 to generate an answer (case-sensitive)
    if "physics" in question:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=question,
            max_tokens=50  # Adjust the max_tokens as needed
        )
        return response.choices[0].text

    # For non-physics and non-data science questions, use predefined responses (case-insensitive)
    predefined_queries = {
        "What is my schedule for Monday?": "You have Math at 9:00 AM and Science at 11:00 AM.",
        "What is my grade in Math?": "Your grade in Math is 95%.",
    }
    if question_lower in predefined_queries:
        return predefined_queries[question_lower]

    # If no suitable answer is found, return a generic response
    return "I'm sorry, I don't have an answer for that right now."

def get_user_input():
    # Function to get user input
    return input("Ask a question: ")

# Example usage with user input
while True:
    user_question = get_user_input()
    if user_question.lower() == "exit":
        break
    response = ai_hook(user_question)
    print(response)




