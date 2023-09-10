// import wiki from 'wikijs';

// wiki({ apiUrl: 'https://en.wikipedia.org/w/api.php' })
//     .page('Batman')
//     .then(page => page.content())
//     .then(console.log);

// Define the URL for the Wikipedia API
const apiUrl = "https://en.wikipedia.org/w/api.php?action=query&format=json&titles=Antimony&prop=revisions&rvprop=size";

// Use the fetch API to make a GET request to the API
fetch(apiUrl)
  .then(response => {
    // Check if the response status is OK (200)
    if (response.status !== 200) {
      throw new Error(`Request failed with status ${response.status}`);
    }
    
    // Parse the JSON response
    return response.json();
  })
  .then(data => {
    // Do something with the JSON data
    console.log(data);
  })
  .catch(error => {
    // Handle any errors that occurred during the fetch
    console.error(error);
  });