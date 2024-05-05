document.addEventListener('DOMContentLoaded', function () {
  var saveButton = document.getElementById('saveButton');
  saveButton.addEventListener('click', function () {
      chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
          chrome.tabs.sendMessage(tabs[0].id, { action: "getText" }, function () {
              sendTextToServer(document.body.innerText);
              
          });
      });
  });
});

function sendTextToServer(text) {
  fetch('http://localhost:5003/', { // Change to your localhost URL
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: text }),
  })
      .then(response => response.text())
      .then(data => {
          console.log('Response from server:', data);
          // Handle the response as needed
      })
      .catch(error => {
          console.error('Error:', error);
      });
}


/*

document.addEventListener('DOMContentLoaded', function () {
  var saveButton = document.getElementById('saveButton');
  saveButton.addEventListener('click', function () {
      console.log('Button clicked!');
  });
});
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
    // Save the text to local storage http://127.0.0.1:5003
    chrome.storage.local.set({ 'savedText': text }, function () {
      console.log('Text saved locally.');
    });
  }
  */
  