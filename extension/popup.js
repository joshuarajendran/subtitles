document.addEventListener('DOMContentLoaded', function () {
    var nlpSummarizeButton = document.getElementById('nlp-summarize-button');
    var lsaSummarizeButton = document.getElementById('lsa-summarize-button');
    
    nlpSummarizeButton.addEventListener('click', function () {
        sendMessageToContentScript('nlp-summarize');
    });

    lsaSummarizeButton.addEventListener('click', function () {
        sendMessageToContentScript('lsa-summarize');
    });

    chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
        if (request.action === 'result') {
            // Hide the spinner
            document.getElementById('spinner').style.display = 'none';
    
            outputSummary(request.summary);
        }
    });

    function sendMessageToContentScript(action) {
         // Show the spinner
        document.getElementById('spinner').style.display = 'block';
    
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            var activeTab = tabs[0];
            console.log('Sending message to generate summary:', action);
            chrome.tabs.sendMessage(activeTab.id, { action: action });
        });
    }
    

    function outputSummary(summary) {
        var summaryDiv = document.getElementById('summaryDiv');
        summaryDiv.innerHTML = summary;
    }
});
