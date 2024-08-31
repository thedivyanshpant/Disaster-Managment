document.getElementById('getWeatherButton').addEventListener('click', getWeather);

function getWeather() {
    const apiKey = "906e9450851e85944b4a293e5c8162b7";
    const cityName = document.getElementById('cityName').value;
    const apiUrl = `http://api.openweathermap.org/data/2.5/weather?q=${cityName}&appid=${apiKey}`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            if (data.cod !== 200) {
                showError("City Not Found");
                return;
            }

            displayWeather(data);
            checkForAlerts(data);
        })
        .catch(error => {
            console.error('Error fetching the weather data:', error);
            showError("Unable to fetch data");
        });
}

function displayWeather(data) {
    const { temp, pressure, humidity } = data.main;
    const weatherDescription = data.weather[0].description;

    document.getElementById('weatherDisplay').innerHTML = `
        <p>Temperature: ${(temp - 273.15).toFixed(2)}°C</p>
        <p>Pressure: ${pressure} hPa</p>
        <p>Humidity: ${humidity}%</p>
        <p>Description: ${weatherDescription}</p>
    `;
}

function checkForAlerts(data) {
    const temp = data.main.temp - 273.15; // Convert Kelvin to Celsius
    const humidity = data.main.humidity;
    const weatherDescription = data.weather[0].description;

    let alertMessage = "";

    if (temp > 40) {
        alertMessage += "Alert: Extreme heat detected!<br>";
    }
    if (humidity > 80) {
        alertMessage += "Alert: High humidity levels detected!<br>";
    }
    if (weatherDescription.includes("rain") || weatherDescription.includes("storm")) {
        alertMessage += "Alert: Severe weather detected!<br>";
    }

    document.getElementById('alertDisplay').innerHTML = alertMessage || "No alerts";
}

function showError(message) {
    document.getElementById('weatherDisplay').innerHTML = "";
    document.getElementById('alertDisplay').innerHTML = `<p>${message}</p>`;
}
