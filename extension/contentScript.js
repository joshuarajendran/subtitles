chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action === 'generate') {
        console.log('Message received in content script');
        var url = window.location.href;
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                console.log('Summary received from server:', xhr.responseText); // debug from youtube chrome console
                var summary = xhr.responseText;
                chrome.runtime.sendMessage({ action: 'result', summary: summary });
            }
        };
        xhr.open('GET', 'http://127.0.0.1:5000/api/summarize?youtube_url=' + url, true);
        xhr.send();
    }
});
