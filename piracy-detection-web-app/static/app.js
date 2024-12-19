document.getElementById('piracyForm').addEventListener('submit', function(e) {
    e.preventDefault();  // Prevent the default form submission
    let text = document.getElementById('text').value;
    
    // Show loading spinner
    document.getElementById('loading').style.display = 'block';
    document.getElementById('submitBtn').disabled = true;  // Disable button to prevent multiple submissions

    fetch('/check_piracy', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('loading').style.display = 'none';  // Hide loading spinner
        document.getElementById('submitBtn').disabled = false;  // Enable button

        if (data.result) {
            document.getElementById('result-container').innerHTML = `<h2>Result: ${data.result}</h2>`;
        } else {
            document.getElementById('result-container').innerHTML = '<h2>Result: No piracy detected</h2>';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('loading').style.display = 'none';
        document.getElementById('submitBtn').disabled = false;
        document.getElementById('result-container').innerHTML = '<h2>Something went wrong. Please try again.</h2>';
    });
});
