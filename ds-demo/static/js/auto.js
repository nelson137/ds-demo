function scrapeURL() {
  url = document.getElementById('url').value;
  $.ajax({
    url: '/scrape-url/',
    data: {url: url},
    success: function(response) {
      console.log(response)
    }
  });
}
