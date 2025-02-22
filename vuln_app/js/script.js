setInterval(() => {
  fetch('/api/read.php?file=cpu.txt')
      .then(response => {
          if (!response.ok) {
              throw new Error('Network response was not ok: ' + response.statusText);
          }
          return response.text()
      })
      .then(data => {
          console.log(data);
      })
      .catch(error => {
          console.error('There has been a problem with your fetch operation:', error);
      });
}, 10000);