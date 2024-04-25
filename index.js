function sendMessage() {
    var userInput = document.getElementById('user-input').value;
    var chatBody = document.getElementById('chat-body');

    // Agregar mensaje del usuario al chat
    var userMessage = '<div class="user-message">' + userInput + '</div>';
    chatBody.innerHTML += userMessage;

    // Simular respuesta del chatbot (aquí puedes agregar la lógica de tu chatbot)
    var botMessage = '<div class="bot-message">¡Entendido! Estoy procesando tu solicitud...</div>';
    setTimeout(function() {
        chatBody.innerHTML += botMessage;
        chatBody.scrollTop = chatBody.scrollHeight;
    }, 1000);

    // Limpiar campo de entrada
    document.getElementById('user-input').value = '';
}
