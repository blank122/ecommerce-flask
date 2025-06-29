🛒 ecommerce-flask
A RESTful eCommerce backend built with Flask, designed for scalability, security, and maintainability. This backend API supports user authentication, product management, and a scheduled system to send sale deals. The project is built with PostgreSQL, SQLAlchemy, and JWT authentication, and uses bcrypt for password hashing.

🚀 Features
🔐 Authentication
Secure user registration and login using JWT (JSON Web Tokens)

Passwords hashed with bcrypt

🛍️ Admin Functionalities
Create and manage products

Create and manage categories and sub-categories

Role-based access control for admin endpoints

📩 Scheduler
A background task that sends sale deals to all users via email or notifications at scheduled intervals

🧠 Future Functionalities
Predictive analytics to analyze sales trends and suggest inventory or marketing strategies

Enhanced Admin Dashboard with analytics like:

Best-selling products

Sales by category

User purchase behavior

Daily/weekly/monthly revenue breakdowns

🧱 Tech Stack
Technology	Purpose
Flask	Web framework
PostgreSQL	Relational database
SQLAlchemy	ORM for managing database models
bcrypt	Password hashing
JWT	Token-based authentication
Celery + Redis (optional)	For scheduling tasks (e.g. sale deal notifications)

📁 Project Structure
bash
Copy
Edit
ecommerce-flask/
│
├── app/
│   ├── models/               # SQLAlchemy models
│   ├── routes/               # API routes
│   ├── utils/                # Utility functions (e.g. auth, bcrypt)
│   ├── scheduler/            # Background task scheduler
│   ├── __init__.py           # App factory
│
├── config.py                 # Configuration (dev/prod)
├── requirements.txt          # Python dependencies
├── run.py                    # Entry point
└── README.md
🔧 Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/ecommerce-flask.git
cd ecommerce-flask
2. Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Configure the Environment
Create a .env file and set up the following:

env
Copy
Edit
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://username:password@localhost:5432/ecommerce_db
JWT_SECRET_KEY=your_jwt_secret
5. Initialize the Database
bash
Copy
Edit
flask db init
flask db migrate
flask db upgrade
6. Run the Application
bash
Copy
Edit
flask run
🧪 API Endpoints (Sample)
Method	Endpoint	Description	Auth Required
POST	/api/auth/register	Register a new user	❌
POST	/api/auth/login	Login and get JWT token	❌
POST	/api/admin/product	Create a product	✅ (admin)
GET	/api/products	Get list of products	❌
POST	/api/admin/category	Create category or sub-category	✅ (admin)

🧠 Planned Enhancements
Predictive Sales Analysis

Use machine learning to forecast demand

Recommend stock levels to the admin

Admin Analytics Dashboard

Graphs and tables to visualize:

Product performance

User purchase patterns

Sales trends over time

Email Notifications

Automated promotional emails

Order confirmations & status updates

Multi-user Roles

Customer, Admin, and Seller roles

💡 Contributing
Pull requests and suggestions are welcome! For major changes, please open an issue first to discuss what you'd like to change.

📄 License
This project is licensed under the MIT License.

