function scrapeURL() {
  request = new XMLHttpRequest(); 
  request.open('GET', document.getElementById('url').value);
  request.onreadystatechange = function() { 
    if (request.readyState === 4 && request.status === 200) {
      console.log(request);
    }
  }
  request.send(null);
}

