function convertCurrency() {
    const from_currency = document.getElementById('from_currency').value;
    const to_currency = document.getElementById('to_currency').value;
    const amount = document.getElementById('amount').value;

    fetch('/convert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ from_currency, to_currency, amount })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `Converted Amount: ${data.result.toFixed(2)} ${to_currency}`;
        document.getElementById('result-window').style.display = 'block';
    });
}

function closeResultWindow() {
    document.getElementById('result-window').style.display = 'none';
}

function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
}
