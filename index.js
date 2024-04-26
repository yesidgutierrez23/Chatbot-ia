function sendMessage() {
    var userInput = document.getElementById('user-input').value;
    var chatBody = document.getElementById('chat-body');

    // Agregar mensaje del usuario al chat
    var userMessage = '<div class="user-message">' + userInput + '</div>';
    chatBody.innerHTML += userMessage;

    // Obtener la respuesta del chatbot
    var botResponse = getBotResponse(userInput);

    // Agregar respuesta del chatbot al chat
    var botMessage = '<div class="bot-message">' + botResponse + '</div>';
    setTimeout(function() {
        chatBody.innerHTML += botMessage;
        chatBody.scrollTop = chatBody.scrollHeight;
    }, 1000);

    // Limpiar campo de entrada
    document.getElementById('user-input').value = '';
}

function getBotResponse(userInput) {
    var botResponse = "";

    // Lógica para responder a las preguntas del usuario sobre la Segunda Guerra Mundial
    switch (userInput.toLowerCase()) {
        case "causas de la segunda guerra mundial":
            botResponse = "Las causas de la Segunda Guerra Mundial incluyen el Tratado de Versalles, la expansión territorial de Alemania y el surgimiento del nazismo.";
            break;
        case "batallas importantes de la segunda guerra mundial":
            botResponse = "Algunas batallas importantes de la Segunda Guerra Mundial fueron Stalingrado, Normandía y El Alamein.";
            break;
        case "personajes destacados de la segunda guerra mundial":
            botResponse = "Entre los personajes destacados de la Segunda Guerra Mundial se encuentran Adolf Hitler, Winston Churchill y Franklin D. Roosevelt.";
            break;
        default:
            botResponse = "Lo siento, no tengo información sobre ese tema. ¿Puedes preguntarme algo relacionado con la Segunda Guerra Mundial?";
            break;
    }

    return botResponse;
}


