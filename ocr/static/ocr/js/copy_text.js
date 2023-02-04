window.onload = function() {

    function copyText(textElementId, messageElementId) {
        var message = document.getElementById(messageElementId);
        message.className = 'hidden';

        /* Get the text field */
        var text = document.getElementById(textElementId);

        /* Select the text field */
        text.select();

        /* Copy the text inside the text field */
        document.execCommand("copy");

        message.className = '';
    }

    function genRandomString(length) {
        var chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890';
        var charLength = chars.length;
        var result = '';
        for (var i = 0; i < length; i++) {
            result += chars.charAt(Math.floor(Math.random() * charLength));
        }
        return result;
    }

    const roomName = genRandomString(16);
    console.log('Connecting to', roomName);

    const chatSocket = new WebSocket(
        'ws://'
        + window.location.host
        + '/ws/ocr/'
        + roomName
        + '/'
    );

    chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        document.querySelector('#chat-log').value += (data.message + '\n');
    };

    chatSocket.onclose = function (e) {
        console.error('Chat socket closed unexpectedly');
    };

    // document.querySelector('#chat-message-input').focus();
    // document.querySelector('#chat-message-input').onkeyup = function (e) {
    //     if (e.keyCode === 13) {  // enter, return
    //         document.querySelector('#chat-message-submit').click();
    //     }
    // };
    //
    // document.querySelector('#chat-message-submit').onclick = function (e) {
    //     const messageInputDom = document.querySelector('#chat-message-input');
    //     const message = messageInputDom.value;
    //     chatSocket.send(JSON.stringify({
    //         'message': message
    //     }));
    //     messageInputDom.value = '';
    // };

};
