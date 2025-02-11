function toggleChatbot(event) {
    event.stopPropagation();
    const chatbot = document.getElementById("chatbot");
    chatbot.style.right = chatbot.style.right === "-400px" ? "20px" : "-400px";
}

function closeChatbot(event) {
    const chatbot = document.getElementById("chatbot");
    if (chatbot.style.right === "20px") {
        chatbot.style.right = "-400px";
    }
}

function handleKeyPress(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}

function sendMessage() {
    const inputField = document.getElementById("userInput");
    const chatbox = document.getElementById("chatbox");
    const message = inputField.value.trim();

    if (message) {
        const userMessageElement = document.createElement("div");
        userMessageElement.textContent = "You: " + message;
        userMessageElement.classList.add("message", "user-message");
        chatbox.appendChild(userMessageElement);
        
        fetch("https://jaideep-singh-portfolio.onrender.com/api/chat/", { 
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: message }),
        })
        .then(response => response.json())
        .then(data => {
            const botMessageElement = document.createElement("div");
            botMessageElement.textContent = "Bot: " + data.response;
            botMessageElement.classList.add("message", "bot-message");
            chatbox.appendChild(botMessageElement);
            chatbox.scrollTop = chatbox.scrollHeight;
        })
        .catch(error => console.error("Error:", error));

        inputField.value = "";
    }
}





function toggleMenu() {
    const menu = document.querySelector(".menu-links");
    const icon = document.querySelector(".hamburger-icon");
    menu.classList.toggle("open");
    icon.classList.toggle("open");
  }
  