# Sheldon
Sheldon, the AI-powered chatbot, is here to help you craft an exceptional portfolio. Sheldon brings his unique personality to assist you in creating a stellar portfolio that stands out. Get expert guidance and witty insights from Sheldon for a remarkable portfolio-building experience!

## Skills
- Frameworks - Flask
- Languages  - JavaScript, Python, HTML, CSS
- Developer Tools - VS Code, pip, AWS Elastic Beanstalk

## Installation
Follow the steps below to set up and run the project:
1. Clone the Repository
    `git clone https://github.com/ShevinuM/Sheldon`
2. Change to the project directory
3. Create a virtual environment
    `python3 -m venv env`
4. Activate the virtual environment
    `source env/bin/activate`
5. Install the required dependencies
    `pip3 install -r requirement.txt`
6. Obtain an API key from the OpenAI website
7. Create a file called hidden.env in the root directory of the project and type the following in the file
    `OPENAI_API_KEY=your-api-key`
8. Run the project. 
    `python3 app.py`
Please note that I haven't yet tested running this by cloning from the repository. If you encounter any issues during the setup process or have further questions, please feel free to reach out at MShevinu#5358 on Discord or shevinu2002@gmail.com in email.

## How to navigate the repository
- The main application file, `application.py`, can be found in the root directory.
- The `templates` folder within the root directory contains HTML files, including the main UI file.
- The `static` folder contains static assets such as CSS and JavaScript files for the front-end.
- The `backend` folder contains files related to the application's backend, which currently includes the chatbot implementation.

## How and Why I Built It

This project was built as a part of a 2 day hackathon and I expanded upon it after the hackathon. The theme of the hackathon was to build a tool to assist students in building a portfolio and what other way to assist students than building a fancy portfolio generator. Project involved the integration of various technologies and a comprehensive development process. Here's an overview of how the project was built:

### ChatBot
- An earlier version of the application used an existing open-source repository to train a custom dataset, however the large dependency size restricted me from hosting the application.
- The next version used the Chatterbot library to solve the issue, however, the responses were inconsistent and inaccurate.
- Hence, the current version uses the OpenAI API to generate responses.
- The ChatBot is tailored to sound like Sheldon Cooper, from Big Bang Theory and it provides responses to any query related to portfolio building
- It uses persistent caching using a dictionary stored in a JSON file to increase response speed and reduce API calls.

### Backend Development with Flask
- The core functionality of the application was implemented using the Flask web framework. Flask allowed me to handle HTTP requests, route them to the appropriate endpoints, and facilitate seamless communication between the frontend and backend.

### Frontend User Interface
- The frontend user interface was built using JavaScript, HTML, and CSS. These web technologies were used to create an interactive and visually appealing UI for users to engage with the chatbot. The interface enabled smooth communication between the user and the backend Flask server.

### Hosting
- I used AWS Elastic Beanstalk to host the application for public access. 
