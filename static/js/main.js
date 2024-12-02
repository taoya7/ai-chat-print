document.addEventListener('DOMContentLoaded', function() {
    const messageInput = document.getElementById('messageInput');
    const sendBtn = document.getElementById('sendBtn');
    const chatArea = document.getElementById('chatArea');
    const settingsBtn = document.getElementById('settingsBtn');
    const settingsModal = document.getElementById('settingsModal');
    const saveSettings = document.getElementById('saveSettings');
    const closeSettings = document.getElementById('closeSettings');
    const printerIp = document.getElementById('printerIp');
    const printerPort = document.getElementById('printerPort');

    // Load saved printer settings from localStorage
    const loadSavedSettings = () => {
        const savedIp = localStorage.getItem('printerIp') || '192.168.1.200';
        const savedPort = localStorage.getItem('printerPort') || '9100';
        printerIp.value = savedIp;
        printerPort.value = savedPort;
        return { ip: savedIp, port: savedPort };
    };

    // Save printer settings to localStorage
    const saveSettingsToStorage = (ip, port) => {
        localStorage.setItem('printerIp', ip);
        localStorage.setItem('printerPort', port);
    };

    // Connect printer function
    async function connectPrinter(ip, port) {
        try {
            const response = await fetch('/api/printer/connect', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ ip, port })
            });

            const data = await response.json();

            if (data.success) {
                console.log('Printer connected successfully!');
                settingsModal.style.display = 'none';
                return true;
            } else {
                console.error('Error:', data.error || 'Failed to connect to printer');
                return false;
            }
        } catch (error) {
            console.error('Error connecting to printer:', error.message);
            return false;
        }
    }

    // Send message function
    async function sendMessage() {
        const message = messageInput.value.trim();
        if (!message) return;

        try {
            const response = await fetch('/api/print', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message })
            });

            const data = await response.json();

            if (data.success) {
                addMessageToChat(data.message, data.timestamp);
                messageInput.value = '';
            } else {
                alert('Error: ' + (data.error || 'Failed to send message'));
            }
        } catch (error) {
            alert('Error sending message: ' + error.message);
        }
    }

    // Add message to chat area
    function addMessageToChat(message, timestamp) {
        const messageElement = document.createElement('div');
        messageElement.className = 'message';
        messageElement.innerHTML = `
            <div class="timestamp">${timestamp}</div>
            <div class="content">${message}</div>
        `;
        chatArea.appendChild(messageElement);
        chatArea.scrollTop = chatArea.scrollHeight;
    }

    // Auto-connect on page load
    (async function autoConnect() {
        const settings = loadSavedSettings();
        await connectPrinter(settings.ip, settings.port);
    })();

    // Event Listeners
    sendBtn.addEventListener('click', sendMessage);
    messageInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') sendMessage();
    });

    settingsBtn.addEventListener('click', () => {
        settingsModal.style.display = 'block';
    });

    closeSettings.addEventListener('click', () => {
        settingsModal.style.display = 'none';
    });

    saveSettings.addEventListener('click', async () => {
        const ip = printerIp.value.trim();
        const port = printerPort.value.trim();

        if (!ip || !port) {
            alert('Please enter both IP and port');
            return;
        }

        saveSettingsToStorage(ip, port);
        await connectPrinter(ip, port);
    });

    // Close modal when clicking outside
    window.addEventListener('click', (e) => {
        if (e.target === settingsModal) {
            settingsModal.style.display = 'none';
        }
    });
});