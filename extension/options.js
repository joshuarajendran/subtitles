document.getElementById('optionForm').addEventListener('submit', function(event) {
    event.preventDefault();  // prevent form from being submitted normally
    var minLength = document.getElementById('minLength').value;
    var maxLength = document.getElementById('maxLength').value;

    // Save the options to local storage
    chrome.storage.local.set({
        minLength: minLength,
        maxLength: maxLength
    });
});
