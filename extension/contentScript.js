chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action === 'nlp-summarize') {
        generateSummary('http://127.0.0.1:5000/api/summarize?youtube_url=' + window.location.href);
    } else if (request.action === 'lsa-summarize') {
        generateSummary('http://127.0.0.1:5000/api/summarize-lsa?youtube_url=' + window.location.href);
    }
});

function generateSummary(url) {
    chrome.storage.local.get(['minLength', 'maxLength'], function(options) {
        var minLength = options.minLength || 120;  // use default value if not set
        var maxLength = options.maxLength || 160;  // use default value if not set

        // Modify the url to include the options
        url += '&min_length=' + minLength + '&max_length=' + maxLength;
        
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var summary = xhr.responseText;
                chrome.runtime.sendMessage({ action: 'result', summary: summary });
            }
        };
        xhr.open('GET', url, true);
        xhr.send();
    });
}

