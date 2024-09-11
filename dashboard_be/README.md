# Dashboard Backend

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Janithbimsara/dashboard-be.git
   cd dashboard_be
   ```

2. **Install dependencies:**
   Make sure you have `pip` installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations to set up the database:**
   ```bash
   python manage.py migrate
   ```

4. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Open the application in your browser**:
   Navigate to `http://localhost:8000/` to view the dashboard backend.

## Libraries and Tools Used

- **Django**: For handling backend logic, URLs, and models.
- **Django REST Framework** (if applicable): For building APIs.
- **Charts Module**: Handles chart-related views and logic.
- Other dependencies are listed in the `requirements.txt` file.

## Project Structure

Here's a brief overview of the key modules and files:

```
dashboard_be/
├── dashboard_be/                   
│   ├── __init__.py                
│   ├── asgi.py                    
│   ├── wsgi.py                    
│   ├── settings.py                
│   ├── urls.py                     
│   └── charts/   
│       ├── __init__.py            
│       ├── urls.py 
│       ├── views.py                
├── manage.py                      
```

## Approach and Thought Process

- **Modular Structure**: The project is structured to keep different components isolated, such as placing all chart-related logic inside the `charts` module for better maintainability.
- **Django's Core**: Used Django’s built-in features like routing, templating, and ORM for managing URL patterns, database interactions, and application logic.
- **Extensibility**: Designed the project to be easily extendable. For example, the `charts` module can be expanded to include more complex charting features without affecting the rest of the application.
