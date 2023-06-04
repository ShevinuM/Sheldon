# Sheldon
Sheldon, the AI-powered chatbot, is here to help you craft an exceptional portfolio. From generating customized resumes to answering queries, Sheldon brings his unique personality to assist you in creating a stellar portfolio that stands out. Get expert guidance and witty insights from Sheldon for a remarkable portfolio-building experience!

# Skills
- Frameworks - NLTK, PyTorch, Flask
- Languages  - JavaScript, Python, HTML5, CSS3

# How I Built It

This project was built as a part of a 2 day hackathon.Sheldon project involved the integration of various technologies and a meticulous development process. Here's an overview of how the project was built:

### Dataset Creation
- During the hackathon, I curated a dataset specifically tailored for portfolio building prompts. This dataset served as the foundation for training the chatbot's responses.

### Deep Learning Algorithm
- To train the dataset and generate responses, I leveraged an existing deep learning algorithm sourced from an open-source repository. The algorithm was carefully chosen, ensuring it was appropriately licensed for personal use.

### OpenAI Integration
- The dataset covered a wide range of prompts; however, for prompts that required more context or weren't adequately handled, I made use of the OpenAI API. By integrating the API, I could seamlessly generate responses that aligned with the tone and style of the dataset.

### Backend Development with Flask
- The core functionality of the application was implemented using the Flask web framework. Flask allowed me to handle HTTP requests, route them to the appropriate endpoints, and facilitate seamless communication between the frontend and backend.

### Frontend User Interface
- The frontend user interface was built using JavaScript, HTML, and CSS. These web technologies were used to create an interactive and visually appealing UI for users to engage with the chatbot. The interface enabled smooth communication between the user and the backend Flask server.

### API Key Management
- To securely utilize the OpenAI API, I implemented a mechanism for storing the API key. Users were instructed to obtain an API key from the OpenAI website and place it in a file called `hidden.txt`. This ensured that the API key remained confidential while being easily accessible for the application. (Please note that I'm aware storing a key as .txt file is not the most secure, this is a temporary fix and I'll update it as soon as I can)

### Deployment and Testing
- During development, I thoroughly tested the application locally to ensure its functionality and address any issues or bugs.


## Installation
Follow the steps below to set up and run the project:
1. Clone the Repository
    git clone https://github.com/your-username/your-repository.git
2. Change to the project directory
    cd your-repository
3. Create a virtual environment
    python3 -m venv env
4. Activate the virtual environment
    source env/bin/activate
5. Install the required libraries
    pip3 install -r requirement.txt
6. Obtain an API key from the OpenAI website
7. Create a file called hidden.txt and place the API Key
8. Run the project. 
    python3 app.py
Please note that I haven't yet tested running this by cloning from the repository. If you encounter any issues during the setup process or have further questions, please feel free to reach out at MShevinu#5358 on Discord or shevinu2002@gmail.com in email.

## Constrains
- Time was a constraint which led to
  1. Lack of time to host the application on AWS.
  2. Couldn't implement the resume generator.
  3. DataSet is not large enough since I had to write the dataset.
