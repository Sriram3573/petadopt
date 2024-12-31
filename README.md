# Pet Adoption Platform

## Overview
The Pet Adoption Platform is a web application designed to connect potential pet adopters with animals in need of homes. The platform provides users with features such as viewing available pets, reading informative blogs, and learning how to get involved in the adoption process. Users can register, log in, and manage their interactions securely.

---

## Features
- **User Authentication**: Users can register, log in, and log out securely.
- **Personalized Experience**: The homepage greets users by name upon login.
- **Pet Search**: Find pets available for adoption.
- **Informative Content**: Access blogs and resources about pet care and adoption.
- **Community Engagement**: Learn about opportunities to get involved with the platform.
- **Contact Us**: Allows users to send inquiries or messages directly to the platform's team using Email.js.
- **Pet Filtering**: Users can filter pets by type, breed, gender, and age on the "Adopt" page.
- **Logout Feature**: Ensures users can securely log out of their accounts.

---

## Frontend
The frontend of the Pet Adoption Platform is built with HTML, CSS, and JavaScript to ensure a clean, responsive, and interactive user interface.

### Technologies Used
- **HTML5**: Structure of the web pages.
- **CSS3**: Styling for a visually appealing and user-friendly experience.
- **JavaScript**: Adds interactivity, such as form validation, dynamic content updates, and integration with Email.js.
- **Email.js**: Enables users to send messages from the "Contact Us" page directly to the admin's email without requiring server-side email configurations.

### Key Components
1. **Navigation Bar**: Provides easy access to different sections of the platform such as Home, Adopt, Get Involved, Blog, About Us, and Contact Us.
2. **Homepage**:
   - Greets logged-in users with a personalized message.
   - Includes a call-to-action button for starting the adoption process.
3. **Adopt Page**:
   - Displays a list of available pets for adoption.
   - Includes details such as the pet's name, breed, age, and a brief description.
   - Allows users to filter pets by type, breed, gender, and age to find their perfect match.
   - Features a "Contact to Adopt" button for users to express interest in specific pets.
4. **Contact Us Page**:
   - Provides a form for users to enter their name, email, subject, and message.
   - Integrates with Email.js to send messages directly to the admin's email address.

---

## Backend
The backend is built using **Flask**, a lightweight and flexible Python web framework. Flask handles routing, server-side logic, and user authentication.

### Key Features
1. **User Authentication**:
   - Passwords are securely hashed using the `werkzeug.security` module.
   - Users are authenticated via email and password.
2. **Dynamic Routing**:
   - Routes like `/adopt` and `/blog` render pages dynamically based on user interaction.
   - A secure session mechanism ensures users stay logged in during their interaction.
3. **Logout Feature**:
   - Provides a secure way for users to end their session and protect their account.
4. **Email.js Integration**:
   - The "Contact Us" page leverages Email.js for message delivery.
   - Provides a seamless way for users to communicate with the platform's team without requiring complex backend email configurations.

### API Endpoints
- `/`: Homepage
- `/login`: User login
- `/register`: User registration
- `/adopt`: View and filter pets available for adoption
- `/blog`: Access informative articles
- `/get-involved`: Learn about community engagement
- `/contact-us`: Send inquiries using Email.js

---

## Database
The platform uses an SQLite database to store user and platform data.

### Database Schema
- **Table: `users`**
  - `id`: Primary key
  - `username`: Stores the user's name
  - `email`: Unique email for user identification
  - `password`: Hashed password for secure login

### Initialization
The database is initialized using the `init_db()` function, which creates the necessary tables if they do not already exist.

### Security
- Passwords are hashed using `generate_password_hash()` for secure storage.
- User sessions are managed with Flask's session management to prevent unauthorized access.

---

## How to Run the Project

1. **Setup Environment**:
   - Install Python 3.x.
   - Install required dependencies:
     ```bash
     pip install flask werkzeug
     ```

2. **Initialize Database**:
   - Run the application once to create the database automatically:
     ```bash
     python app.py
     ```

3. **Start the Server**:
   - Launch the Flask development server:
     ```bash
     python app.py
     ```

4. **Access the Application**:
   - Open a web browser and go to `http://127.0.0.1:5000/`.

---

## Future Enhancements
- Add user profiles for managing adoption preferences.
- Integrate a payment gateway for donations.
- Use a more scalable database like PostgreSQL or MySQL.
- Add image uploads for pets on the "Adopt" page.
- Enhance the "Contact Us" page with auto-reply functionality.
- Implement advanced pet filtering options using JavaScript and AJAX for real-time updates.

---

## Contact
For questions or support, please reach out to:
- **Developer**: Sriram Senthil
- **Email**: sriramsenthil6@gmail.com

---

## License
This project is open-source and available for use under the MIT License.

