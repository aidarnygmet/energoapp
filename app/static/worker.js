self.onmessage = function(event) {
    const messageFromMain = event.data;
    console.log('Message from the main thread:', messageFromMain);
  
    // Perform some computation or task in the background
    const result = performTask(messageFromMain);
  
    // Send the result back to the main thread
    self.postMessage(result);
  };
  
  function performTask(data) {
    // Perform some computation or data processing here
    // ...
    return 'Result from the Web Worker';
  }
  function sendDataToServer() {
    label = document.getElementById("t_total")
    const value = parseFloat(label.textContent); 
    const data = {
      value: value
    };
    fetch('/save-data/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data),
    })
      .then(response => response.json())
      .then(result => {
        if (result.success) {
    console.log('Ugol Data saved successfully!');
  } else {
    console.error('Failed to save data:', result.message);
  }
      })
      .catch(error => {
        console.log('Error:', error.message);
      });
  }