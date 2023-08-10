# Sheldon
Sheldon is here to help you craft an exceptional portfolio. Sheldon brings his unique personality to assist you in creating a stellar portfolio that stands out. Get expert guidance and witty insights from Sheldon for a remarkable portfolio-building experience!

## Demo (Click to Play)
[![YouTube Video Link](http://img.youtube.com/vi/7qI0Be5LZXY/0.jpg)](https://www.youtube.com/watch?v=7qI0Be5LZXY)

## How and Why I Built It

This project was built as a part of a 2 day hackathon and I expanded upon it after the hackathon. The theme of the hackathon was to build a tool to assist students in building a portfolio and what other way to assist students than building a fancy portfolio generator. Project involved the integration of various technologies and a comprehensive development process. Here's an overview of how the project was built:

### ChatBot

#### Version 1
- The first version of the application used open-source machine learning and natural language processing algorithm to train a custom dataset.
- The custom dataset was a 68 input JSON based dataset which I wrote to train the algorithm.
- I extracted the probabilty of match for each input and used OpenAI API to fetch responses for inputs with a low probabiliy.
- The implementation for this can be seen in the earliest commits to the repository.

#### Version 2
- The large dependency size prevented me from hosting the application. So I needed an alternative and decided to use the Chatterbot library.
- However, the responses were very inconsistent and innacurate and the library needed a much larger dataset to be accurate.

#### Version 3
- The current version only uses the OpenAI API for responses because I wanted to host the application.
- It uses a JSON based persistent caching mechanism to increase response speed and reduce API calls.

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
8. This application is configured to fetch data from the public address. If you want to run this application locally, you will need to change the fetch URL in app.js. Replace line 43 in app.js `fetch('http://sheldon.ap-south-1.elasticbeanstalk.com/predict', { ` with `fetch('http://localhost:5000/predict', {`.
9. Run the project. 
    `python3 app.py`
If you encounter any issues during the setup process or have further questions, please feel free to reach out at MShevinu#5358 on Discord or shevinu2002@gmail.com in email.

## How to navigate the repository
- The main application file, `application.py`, can be found in the root directory.
- The `templates` folder within the root directory contains HTML files, including the main UI file.
- The `static` folder contains static assets such as CSS and JavaScript files for the front-end.
- The `backend` folder contains files related to the application's backend, which currently includes the chatbot implementation.

### Backend Development with Flask
- The core functionality of the application was implemented using the Flask web framework. Flask allowed me to handle HTTP requests, route them to the appropriate endpoints, and facilitate seamless communication between the frontend and backend.

### Frontend User Interface
- The frontend user interface was built using JavaScript, HTML, and CSS. These web technologies were used to create an interactive and visually appealing UI for users to engage with the chatbot. The interface enabled smooth communication between the user and the backend Flask server.

### Hosting
- I used AWS Elastic Beanstalk to host the application for public access. 
- The link is not working right now because I have exceeded the free-tier limits for Amazon EC2 hence it's no longer deployed.
