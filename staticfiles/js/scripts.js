/*!
* Start Bootstrap - Clean Blog v6.0.9 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if (currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            mainNav.classList.remove('is-visible');
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });
});

// Функция для автоматической прокрутки чата вниз
function scrollChat() {
    const chatBox = document.getElementById('chat-box');
    if (chatBox) {
        chatBox.scrollTop = chatBox.scrollHeight - chatBox.clientHeight;
    }
}

// Проверка перед инициализацией WebSocket
if (typeof username === 'undefined' || username === '') {
    console.error("Ошибка: username не определен. Проверь, передается ли он в шаблоне.");
} else if (typeof roomName === 'undefined' || roomName === '') {
    console.error("Ошибка: roomName не определен. Проверь, передается ли он в шаблоне.");
} else {
    initChatSocket(roomName, username);
}

// Инициализация WebSocket
function initChatSocket(roomName, username) {
    console.log("DEBUG: username =", username);
    console.log("DEBUG: roomName =", roomName);

    const chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
    );

    chatSocket.onopen = function () {
        console.log('WebSocket connected');
    };

    chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        const message = data['message'];
        const user = data['username'];

        const chatBox = document.getElementById('chat-box');
        const messageElement = document.createElement('div');
        messageElement.classList.add('message');
        if (user === username) {
            messageElement.classList.add('parker');
        }
        messageElement.innerHTML = `<b>${user}:</b> ${message}`;
        chatBox.appendChild(messageElement);
        scrollChat(); // Прокручиваем чат вниз после добавления сообщения
    };

    chatSocket.onclose = function (e) {
        console.error('Chat socket closed unexpectedly', e);
    };

    chatSocket.onerror = function (e) {
        console.error('WebSocket error:', e);
    };

    // Отправка сообщения
    const messageInput = document.querySelector('#chat-message-input');
    const sendButton = document.querySelector('#send-button');

    if (messageInput && sendButton) {
        sendButton.onclick = function () {
            const message = messageInput.value.trim();
            if (message) {
                chatSocket.send(JSON.stringify({
                    'message': message,
                    'username': username,
                }));
                messageInput.value = '';
            }
        };

        messageInput.onkeyup = function (e) {
            if (e.key === 'Enter') {
                sendButton.click();
            }
        };
    }
}
