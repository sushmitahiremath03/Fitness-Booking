# Fitness-Booking

---

A simple Django REST API for a fictional fitness studio where users can view available classes (like Yoga, Zumba, and HIIT) and book slots.

---

## 📌 Features

---

- View all upcoming fitness classes
- Book a slot in a class
- View all bookings by email
- Timezone support (IST and conversions)
- Input validation and error handling
- In-memory database using SQLite
- Seed data loading via fixtures

---

## 🚀 Setup Instructions

Follow these steps to run the project locally:

```bash
git clone https://github.com/sushmitahiremath03/Fitness-Booking.git
cd Fitness-Booking

# Create virtual environment
python -m venv venv

# Activate the virtual environment
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Load seed data
python manage.py loaddata seed_data.json

# Run the server
python manage.py runserver


| Method | Endpoint                           | Description                                 |
| ------ | ---------------------------------- | ------------------------------------------- |
| GET    | `/classes`                         | Get list of all upcoming fitness classes    |
| POST   | `/book`                            | Book a class with name, email, and class ID |
| GET    | `/bookings?email=user@example.com` | Get all bookings for a given email          |


## Running Unit Tests
bash
python manage.py test

Project Structure
bash
Fitness-Booking/
├── booking/                  # Main app for class and booking logic
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── tests.py
│   └── urls.py
├── fitness_booking/          # Django project folder
│   ├── settings.py
│   └── urls.py
├── db.sqlite3                # SQLite in-memory database
├── manage.py
├── seed_data.json            # Fixture to populate initial classes
├── requirements.txt
└── README.md



