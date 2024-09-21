# Taxi Bus Locator

Taxi Bus Locator is a Django-based web application for managing and displaying information about taxi and bus stops in various communes.

## Features

- List view of all stops
- Detailed view of individual stops
- Search functionality for finding stops by name or commune
- Responsive design for desktop, tablet, and mobile devices

## Installation

1. Clone the repository:
   git clone https://github.com/TugoMC/taxi_bus_locator

2. Navigate to the project directory:
   cd taxi_bus_locator

3. Create a virtual environment and activate it:
   python -m venv venv source venv/bin/activate # On Windows, use venv\Scripts\activate

4. Install the required dependencies:
   pip install -r requirements.txt

5. Run migrations:
   python manage.py migrate

6. Create a superuser:
   python manage.py createsuperuser

7. Run the development server:
   python manage.py runserver

8. Access the application at `http://localhost:8000`

## Usage

- Use the admin interface (`http://localhost:8000/admin/`) to add, edit, or delete stops.
- Browse the list of stops on the home page.
- Click on a stop to view its details.
- Use the search bar to find stops by name or commune.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
