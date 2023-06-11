class ShowResumeGenerator {
    constructor() {
        this.args = {
            chatBox: document.querySelector('.chatbox'),
            resumeGenerator: document.querySelector('.resume_generator'),
        }
        const {chatBox, resumeGenerator} = this.args;
        chatBox.style.display = 'none';
        resumeGenerator.style.display = 'block';
    }
}

class Chatbox {
    constructor() {
        this.args = {
            sendButton: document.querySelector('.send__button'),
            chatBox: document.querySelector('.chatbox')
        }

        this.messages = []; // array to keep track of the chat history
    }

    display() {
        const {sendButton, chatBox} = this.args;

        sendButton.addEventListener('click', ()=> this.onSendButton(chatBox));
        
        // select the first <input> element within the 'chatBox' element
        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({key}) => {
            if (key == "Enter") {
                this.onSendButton(chatBox)
            }
        });

        const introMessage = {name: "Sheldon", message: "Greetings, I am Sheldon Cooper, and I welcome your inquiries pertaining to the art of portfolio construction. I am at your disposal, prepared to offer my profound expertise. However, I must insist that you refrain from divulging any classified information. Now, feel free to pose your inquiries, and I shall assist you with utmost diligence." };
        this.messages.push(introMessage);
        this.updateChatText(chatBox);

    }

    onSendButton(chatbox) {
        let textField = chatbox.querySelector('input');
        let text = textField.value
        if (text == "") {
            return;
        }

        let msg = {name: "user", message: text}
        this.messages.push(msg)

        // Show loading indicator
        this.showLoadingIndicator(chatbox);

        fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            body: JSON.stringify({message: text }), //convert the object to JSON
            headers: {
                'Content-Type': 'application/json' // indicate the server that the data in the request body is formatted in json
            }
        })
        .then(response => response.json())
        .then(response => {
            let reply = {name: "Sheldon", message: response.answer };
            this.messages.push(reply)
            this.updateChatText(chatbox)
            textField.value = ''

            // Hide loading indicator
            this.hideLoadingIndicator(chatbox);
        })
        .catch((error) => {
            console.error('Error:', error);
            this.updateChatText(chatbox)
            textField.value = ''

            // Hide loading indicator
            this.hideLoadingIndicator(chatbox);
        });
    }

    showLoadingIndicator(chatbox) {
        const chatMessage = chatbox.querySelector('.chatbox__messages');
        const loadingIndicator = '<div class="message__item loading">' + '...' + '</div>';
        chatMessage.insertAdjacentHTML('afterbegin', loadingIndicator);
    }

    hideLoadingIndicator(chatbox) {
        const chatMessage = chatbox.querySelector('.chatbox__messages');
        const loadingIndicator = chatMessage.querySelector('.loading');
        if (loadingIndicator) {
            loadingIndicator.remove();
        }
    }

    updateChatText(chatbox) {
        let html = ''
        this.messages.slice().reverse().forEach(function(item, index) {
            if (item.name == "Sheldon") {
                html += '<div class="message__item visitor">' + item.message.replace(/\n/g, '<br>') + '</div>'
            } else {
                html += '<div class="message__item operator">' + item.message.replace(/\n/g, '<br>') + '</div>'
            }
        });
        
        const chatMessage = chatbox.querySelector('.chatbox__messages');
        chatMessage.innerHTML = html;
    }
}

const chatbox = new Chatbox();
chatbox.display();

const generateResumeButton = document.querySelector('.generate_resume_button');
generateResumeButton.addEventListener('click', () => {
    const showResumeGenerator = new ShowResumeGenerator();
    showResumeGenerator.display();
});