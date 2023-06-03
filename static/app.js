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

        sendButton.addEventListener('click', ()=> this.onSendButton(chatBox))
        
        // select the first <input> element within the 'chatBox' element
        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({key}) => {
            if (key == "Enter") {
                this.onSendButton(chatBox)
            }
        })
    }

    onSendButton(chatbox) {
        let textField = chatbox.querySelector('input');
        let text = textField.value
        if (text == "") {
            return;
        }

        let msg = {name: "user", message: text}
        this.messages.push(msg)

        fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            body: JSON.stringify({message: text }), //convert the object to JSON
            headers: {
                'Content-Type': 'application/json' // indicate the server that the data in the request body is formatted in json
            }
        })
        .then(response => response.json()) // extract the JSON data from a response object and parse it into a JavaScript object.
        .then(response => {
            let reply = {name: "Sheldon", message: response.answer };
            this.messages.push(reply)
            this.updateChatText(chatbox)
            textField.value = ''
        }).catch((error) => {
            console.error('Error:', error);
            this.updateChatText(chatbox)
            textField.value = ''
        });
    }

    updateChatText(chatbox) {
        let html = ''
        this.messages.slice().reverse().forEach(function(item, index) {
            // slice() is used to make a shallow copy of the messages array to make sure that the original array is not modified
            // reverse() is used to reverse the order of the elements in the array so that the latest message is displayed at the bottom
            // forEach() is used to iterate over the reversed array and execute the callback function for each element
            if (item.name == "Sam") {
                html += '<div class="message__item visitor">' + item.message + '</div>'
            } else {
                html += '<div class="message__item operator">' + item.message + '</div>'
            }
        });
        
        // select the first 'chatbox_messages' element within the 'chatBox' element
        const chatMessage = chatbox.querySelector('.chatbox__messages');
        chatMessage.innerHTML = html;
    }
}

const chatbox = new Chatbox();
chatbox.display();