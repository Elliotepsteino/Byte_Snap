// popup.js

document.addEventListener('DOMContentLoaded', function () {
  var saveButton = document.getElementById('saveButton');
  saveButton.addEventListener('click', function () {
    sendTextFromCurrentTab();
  });

  // Function to handle sending text from the current tab
  function sendTextFromCurrentTab() {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      chrome.tabs.sendMessage(tabs[0].id, { action: "getText" }, function () {
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
          // Execute a script in the context of the webpage
          chrome.scripting.executeScript({
            target: { tabId: tabs[0].id },
            function: () => {
              return {
                text: document.body.innerText,
                url: window.location.href
              };
            }
          }, function (result) {
            sendTextToServer(result[0].result.text, result[0].result.url);
          });
        });

      });
    });
  }

  // Function to send text to the server
  function sendTextToServer(text_page, url) {
    fetch('http://127.0.0.1:5001/', {
      mode: 'no-cors',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: text_page, url: url }),
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

  // Add an event listener to capture the keyboard shortcut
  document.addEventListener('keydown', function (event) {
      if (event.shiftKey && event.key === 'L') {
        sendTextFromCurrentTab();
    }
  });
});

  