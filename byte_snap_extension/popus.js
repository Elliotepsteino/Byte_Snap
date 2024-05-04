document.addEventListener('DOMContentLoaded', function () {
    var saveButton = document.getElementById('saveButton');
    saveButton.addEventListener('click', function () {
      chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        chrome.scripting.executeScript({
          target: { tabId: tabs[0].id },
          function: saveText
        });
      });
    });
  });
  
  function saveText() {
    var text = document.body.innerText;
    // Save the text to local storage
    chrome.storage.local.set({ 'savedText': text }, function () {
      console.log('Text saved locally.');
    });
  }
  
  