document.addEventListener('DOMContentLoaded', function () {
    var summarizeButton = document.getElementById('summarize-button');
    summarizeButton.addEventListener('click', function () {
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            var activeTab = tabs[0];
            console.log('Sending message to generate summary'); // for debugging
            chrome.tabs.sendMessage(activeTab.id, { action: 'generate' });
        });
    });

    chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
        if (request.action == 'result') {
            console.log('Received summary:', request.summary); // for debugging
            outputSummary(request.summary);
        }
    });

    function outputSummary(summary) {
        var summaryDiv = document.getElementById('summaryDiv');
        summaryDiv.innerHTML = summary;
    }
});
