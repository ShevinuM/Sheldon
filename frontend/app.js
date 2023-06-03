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

        let message = {name: "user", message: text}
        this.messages.push(message)

        fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            body: JSON.stringify({message: text1 }),
        })

    }
}