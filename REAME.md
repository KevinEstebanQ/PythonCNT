# IoT Data Generator (wxPython App)

This is a wxPython-based desktop application that generates artificial IoT sensor data for 1,000 users. Each user is associated with 1,000 sensor readings generated using the Faker library.


- Generate 1,000 fake users with:
  - First name, last name, age, gender, username, address, and email
- Generate 1,000 IoT sensor records per user, including:
  - Date, Time (every 6 hours from Jan 1, 2015)
  - Outside Temperature (70–95°F)
  - Room Temperature (lower by 0–10°F)
  - Outside Humidity (50–95%)
  - Room Humidity (lower by 0–10%)
- Save data as:
  - JSON
  - CSV
- Display:
  - Descriptive statistics
  - Histogram of outside temperatures (Plot A)
  - Line graph of outside vs room temperature (Plot B)
  - Combined histogram of all temperature and humidity values (Plot C)

How to Run

**Install dependencies**:

pip install wxPython pandas matplotlib faker
