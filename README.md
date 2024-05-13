# Faculty_Scholar_Site

## Overview
The Faculty Performance Management System is a comprehensive web application designed to facilitate the evaluation and management of faculty members' performance in an academic institution. This system streamlines the process of collecting, analyzing, and storing performance data, providing administrators, heads of departments (HODs), and staff members with a centralized platform for performance assessment.

### Key Features
1. **User Authentication**: The system offers secure user authentication mechanisms to ensure that only authorized personnel can access and interact with the application. Different user roles, such as administrators, HODs, and staff members, have distinct privileges and access levels within the system.

2. **Performance Evaluation Form**: Staff members can input their performance data through a comprehensive evaluation form. The form includes fields for various performance metrics, such as academic results, student feedback, innovation in teaching, research activities, contribution to the college, attendance, guest lectures delivered, certifications obtained, placements arranged, and more.

3. **Calculation of Total Points**: Based on the submitted performance data, the system automatically calculates the total points accrued by each staff member. The point calculation process considers the weighted values assigned to different performance metrics, ensuring a fair and accurate assessment of each faculty member's contributions.

4. **View Scores**: Administrators, HODs, and staff members can access a dedicated page to view the performance scores of all staff members. This page presents a comprehensive overview of each staff member's performance, including their total points earned across various metrics.

## Project Structure
The project follows a modular structure, with distinct components responsible for different functionalities:

- **Backend (Flask)**: The backend of the application is built using the Flask web framework, which provides routing, request handling, and data processing capabilities. Flask enables the seamless integration of Python code with HTML templates, facilitating dynamic content generation.

- **Database (SQLite)**: The SQLite database management system is used to store user authentication data, performance metrics, and other relevant information. Separate databases are maintained for users, HODs, and staff members to ensure data organization and security.

- **Frontend (HTML/CSS)**: The frontend of the application is developed using HTML for markup and CSS for styling. Jinja2, a template engine for Python, is utilized to render dynamic content within HTML pages, enabling the presentation of user-specific data and interactions.

## Setup and Installation
To set up the Faculty Performance Management System on your local machine, follow these steps:

1. **Clone the Repository**: Use Git to clone the project repository to your local environment:
    ```
    git clone <repository-url>
    ```

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies using pip:
    ```
    pip install -r requirements.txt
    ```

3. **Initialize Databases**: Run the initialization scripts to create and initialize the main database and user-specific databases:
    - `python init_db.py`: Initialize the main database for users.
    - `python init_hod_db.py`: Initialize the database for HODs.
    - `python init_staff_db.py`: Initialize the database for staff members.

4. **Run the Application**: Start the Flask application by running the following command:
    ```
    python app.py
    ```

5. **Access the Application**: Open your web browser and navigate to `http://localhost:5000` to access the Faculty Performance Management System.

## Usage
Upon accessing the application, users can perform the following actions:

- **Login**: Users must log in with their credentials (username and password) to access the system. Different user roles have different access permissions and functionalities.

- **View Performance Scores**: Administrators, HODs, and staff members can view performance scores on the dedicated page. The scores are updated dynamically based on the latest performance data submitted by staff members.

- **Submit Performance Data**: Staff members can submit their performance data through the performance evaluation form. After submission, the system calculates their total points and updates the performance scores accordingly.

## Technologies Used
The Faculty Performance Management System leverages the following technologies and frameworks:

- **Flask**: Flask is a lightweight and versatile web framework for Python, providing the foundation for building web applications with minimal boilerplate code.

- **SQLite**: SQLite is a self-contained, serverless, and lightweight database engine ideal for small to medium-scale applications. It offers simplicity, reliability, and compatibility without the need for a separate database server.

- **HTML/CSS**: HTML (Hypertext Markup Language) is used for creating the structure and content of web pages, while CSS (Cascading Style Sheets) is used for styling and formatting the presentation of HTML elements.

- **Jinja2**: Jinja2 is a powerful and flexible template engine for Python, used in conjunction with Flask to generate dynamic HTML content based on data and logic from the backend.



![Screenshot 2024-05-13 125111](https://github.com/Tharun0568/Faculty_Scholar_site/assets/104981195/5d9cc13a-7e89-49d4-9187-bf63ebd1e9a9)
![Screenshot 2024-05-13 125139](https://github.com/Tharun0568/Faculty_Scholar_site/assets/104981195/c0877c9c-8319-44de-88a3-42dbfa399dcc)
![Screenshot 2024-05-13 125158](https://github.com/Tharun0568/Faculty_Scholar_site/assets/104981195/072b1a7a-8c1f-4919-a3b5-ba13e4d5add1)
![Screenshot 2024-05-13 125241](https://github.com/Tharun0568/Faculty_Scholar_site/assets/104981195/34c1534d-7503-4d60-b05e-8cbfe184ea8f)
![Screenshot 2024-05-13 125309](https://github.com/Tharun0568/Faculty_Scholar_site/assets/104981195/eb5bcc47-661b-4e0a-862a-731e97b07d1c)
![Screenshot 2024-05-13 125350](https://github.com/Tharun0568/Faculty_Scholar_site/assets/104981195/12d5cd2b-7e97-48d1-a691-721ca44ad60a)
![Screenshot 2024-05-13 125501](https://github.com/Tharun0568/Faculty_Scholar_site/assets/104981195/ee765993-f3e8-4ae8-9702-026f76a20e53)
![Screenshot 2024-05-13 123714](https://github.com/Tharun0568/Faculty_Scholar_site/assets/104981195/f5219668-fd4a-4d90-a17d-442164da7731)
![Screenshot 2024-05-13 123736](https://github.com/Tharun0568/Faculty_Scholar_site/assets/104981195/e55bec4a-bc08-4cd8-9f6b-f7eba2d16126)
![Screenshot 2024-05-13 123748](https://github.com/Tharun0568/Faculty_Scholar_site/assets/104981195/49b06c6c-c56d-4ac9-8fb7-96f14198ddda)
![Screenshot 2024-05-13 123807](https://github.com/Tharun0568/Faculty_Scholar_site/assets/104981195/54268272-69be-4a2e-a09c-b65f7721f530)
![Screenshot 2024-05-13 123826](https://github.com/Tharun0568/Faculty_Scholar_site/assets/104981195/0cbb7d1e-e0f5-4443-92ab-7b578dd4dda7)
![Screenshot 2024-05-13 123912](https://github.com/Tharun0568/Faculty_Scholar_site/assets/104981195/bcbee93a-4f39-4746-9ec5-510b0e3750bb)
![Screenshot 2024-05-13 123923](https://github.com/Tharun0568/Faculty_Scholar_site/assets/104981195/26e61bb6-b98f-41cb-bb4d-144e1cde69b7)
![Screenshot 2024-05-13 124014](https://github.com/Tharun0568/Faculty_Scholar_site/assets/104981195/f71a4613-50dc-4b92-9b00-caeefac68f9a)
![Screenshot 2024-05-13 124024](https://github.com/Tharun0568/Faculty_Scholar_site/assets/104981195/ff01da54-2911-4220-bda5-32c2d3722641)
![Screenshot 2024-05-13 124036](https://github.com/Tharun0568/Faculty_Scholar_site/assets/104981195/514c4f3e-9f56-4fe5-b4aa-bc0d20536cf7)
![Screenshot 2024-05-13 124211](https://github.com/Tharun0568/Faculty_Scholar_site/assets/104981195/cf1508ae-0819-487a-8114-9dfe6ac11cb8)
![Screenshot 2024-05-13 124219](https://github.com/Tharun0568/Faculty_Scholar_site/assets/104981195/7ac7240e-eeaf-43c8-abf9-270f3b95bee4)
![Screenshot 2024-05-13 124451](https://github.com/Tharun0568/Faculty_Scholar_site/assets/104981195/77625f53-a5bb-46a7-bec6-cc2c44d395d9)
![Screenshot 2024-05-13 124709](https://github.com/Tharun0568/Faculty_Scholar_site/assets/104981195/7587200d-d77b-4381-aa0a-782956971e26)
