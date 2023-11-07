# Flight Deals Finder App

Welcome to the Flight Deals Finder web application ! This application helps users find cheap flights using the Kiwi API, receive flight information in an XLSX file, and subscribe to weekly deals via email.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Features

### 1. Flight Search
- Search for flight deals using your preferred criteria.
- Retrieve flight information from various sources (e.g., Expedia, Skyscanner).

### 2. Automatic XLSX Conversion
- Automatically convert flight deals results to XLSX format.
- The XLSX file includes details such as flight options, prices, and departure/arrival times.

### 3. Sheety API Integration
- Utilize the Sheety API to store and manage flight deal data.
- Easily access and share flight deals through a web interface.

### 4. Subscription Option
- Allow users to subscribe to receive weekly flight deal updates via email.
- Keep users informed about the latest travel discounts and offers.
- Stay updated with the latest discounts and travel offers.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed
- Required Python packages installed (specified in requirements.txt)
- Kiwi API key (sign up at https://partners.kiwi.com/)
- Sheety APi (sign up at https://sheety.co/)

## Configuration
1. fill the auth.py with your details.
2. copy the FlightDeals.xlsx i provided to your sheety.

## Installation

1. Clone the repository:
  - git clone https://github.com/AintSmurf/Flights_Finder.git

2. Navigate to the project directory:
  - cd Flights_Finder


3. Install the required libraries:
  - pip install -r requirements.txt

## Usage
1. python app.py

## Contributing
Contributions are welcome! If you have any suggestions, bug fixes, or improvements, please open an issue or create a pull request.
