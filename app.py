from flask import Flask, render_template, request, redirect, url_for, session,flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database initialization for main users
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    
    # Check if the user already exists
    c.execute("SELECT * FROM users WHERE username = ?", ('tharun',))
    user = c.fetchone()
    if not user:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('tharun', '12345'))
    
    conn.commit()
    conn.close()

# Database initialization for HOD
def init_hod_db():
    conn = sqlite3.connect('hod.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

# Database initialization for staff
def init_staff_db():
    conn = sqlite3.connect('staff.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

# Route for login page
@app.route('/')
def login():
    return render_template('login.html')
@app.route('/chat')
def Chat():
    return render_template('chat.html')
# Route for handling login form submission
@app.route('/login', methods=['POST'])
def login_submit():
    username = request.form['username']
    password = request.form['password']
    user_type = request.form['user-type']  
    
    # Connect to the appropriate database based on user type
    if user_type == 'admin':
        db_name = 'database.db'
    elif user_type == 'hod':
        db_name = 'hod.db'
    elif user_type == 'staff':
        db_name = 'staff.db'
    else:
        flash('Invalid user type', 'error')  
        return redirect(url_for('login'))  
    
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()

    if user:
        session['logged_in'] = True
        session['username'] = username  
        if user_type == 'hod':
            return redirect(url_for('categories', username=username))  
        elif user_type == 'staff':
            return redirect(url_for('staff_result'))
        else:
            return redirect(url_for('dashboard'))
    else:
        flash('Invalid username or password.', 'error')  
        return redirect(url_for('login'))


# Route for academics page
@app.route('/academics')
def academics():
    return render_template('academics.html')

# Route for dashboard
@app.route('/dashboard')
def dashboard():
    if 'logged_in' in session:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))

# Route for creating new user
@app.route('/create_user', methods=['POST'])
def create_user():
    if 'logged_in' in session:
        new_username = request.form['new_username']
        new_password = request.form['new_password']
        
        # Check if the username already exists in any of the databases
        conn_main = sqlite3.connect('database.db')
        c_main = conn_main.cursor()
        c_main.execute("SELECT * FROM users WHERE username = ?", (new_username,))
        user_main = c_main.fetchone()
        conn_main.close()
        
        conn_hod = sqlite3.connect('hod.db')
        c_hod = conn_hod.cursor()
        c_hod.execute("SELECT * FROM users WHERE username = ?", (new_username,))
        user_hod = c_hod.fetchone()
        conn_hod.close()
        
        conn_staff = sqlite3.connect('staff.db')
        c_staff = conn_staff.cursor()
        c_staff.execute("SELECT * FROM users WHERE username = ?", (new_username,))
        user_staff = c_staff.fetchone()
        conn_staff.close()
        
        
        if user_main or user_hod or user_staff:
            flash( 'Username already exists. Please choose another username.','info')
            return redirect(url_for('hod_dashboard'))
        else:
            #
            conn_main = sqlite3.connect('hod.db')
            c_main = conn_main.cursor()
            c_main.execute("INSERT INTO users (username, password) VALUES (?, ?)", (new_username, new_password))
            conn_main.commit()
            conn_main.close()
            return redirect(url_for('hod_dashboard'))
    else:
        return redirect(url_for('login'))

# Route for creating new staff user
@app.route('/create_staff_user', methods=['POST'])
def create_staff_user():
    if 'logged_in' in session:
        new_username = request.form['new_username']
        new_password = request.form['new_password']
        
        # Check if the username already exists in any of the databases
        conn_main = sqlite3.connect('database.db')
        c_main = conn_main.cursor()
        c_main.execute("SELECT * FROM users WHERE username = ?", (new_username,))
        user_main = c_main.fetchone()
        conn_main.close()
        
        conn_hod = sqlite3.connect('hod.db')
        c_hod = conn_hod.cursor()
        c_hod.execute("SELECT * FROM users WHERE username = ?", (new_username,))
        user_hod = c_hod.fetchone()
        conn_hod.close()
        
        conn_staff = sqlite3.connect('staff.db')
        c_staff = conn_staff.cursor()
        c_staff.execute("SELECT * FROM users WHERE username = ?", (new_username,))
        user_staff = c_staff.fetchone()
        conn_staff.close()
        
        # If the username exists in any of the databases, return an error message
        if user_main or user_hod or user_staff:

            flash( 'Username already exists. Please choose another username.','info')
            return redirect(url_for('staff_dashboard'))
        else:
            # Otherwise, proceed to create the user in the staff database
            conn_staff = sqlite3.connect('staff.db')
            c_staff = conn_staff.cursor()
            c_staff.execute("INSERT INTO users (username, password) VALUES (?, ?)", (new_username, new_password))
            conn_staff.commit()
            conn_staff.close()
            return redirect(url_for('staff_dashboard'))
    else:
        return redirect(url_for('login'))

# Route for categories page
@app.route('/categories')
def categories():
    if 'logged_in' in session:
        username = session.get('username')
        if username:
            return render_template('categories.html', username=username)
        else:
            flash( 'Username not provided','info')
    else:
        return redirect(url_for('login'))


# Route for HOD dashboard
@app.route('/hod_dashboard')
def hod_dashboard():
    if 'logged_in' in session:
        conn_hod = sqlite3.connect('hod.db')
        c_hod = conn_hod.cursor()
        c_hod.execute("SELECT * FROM users")
        users = c_hod.fetchall()
        conn_hod.close()
        return render_template('hod_dashboard.html', users=users)
    else:
        return redirect(url_for('login'))


# Route for deleting user
@app.route('/delete_user/<int:user_id>', methods=['GET', 'POST'])
def delete_user(user_id):
    if 'logged_in' in session:
        if request.method == 'POST':
            conn_hod = sqlite3.connect('hod.db')
            c_hod = conn_hod.cursor()
            c_hod.execute("DELETE FROM users WHERE id = ?", (user_id,))
            conn_hod.commit()
            conn_hod.close()
            flash('User deleted successfully!','info')
            return redirect(url_for('hod_dashboard'))
    else:
        return redirect(url_for('login'))

# Route for changing user password
@app.route('/change_password/<int:user_id>', methods=['POST'])
def change_password(user_id):
    if 'logged_in' in session:
        new_password = request.form['new_password']
        conn_hod = sqlite3.connect('hod.db')
        c_hod = conn_hod.cursor()
        c_hod.execute("UPDATE users SET password = ? WHERE id = ?", (new_password, user_id))
        conn_hod.commit()
        conn_hod.close()
        flash( 'Password changed successfully!','info')
        return redirect(url_for('hod_dashboard'))
    else:
        return redirect(url_for('login'))

# Route for Staff Dashboard
@app.route('/staff_dashboard')
def staff_dashboard():
    if 'logged_in' in session:
        conn_staff = sqlite3.connect('staff.db')
        c_staff = conn_staff.cursor()
        c_staff.execute("SELECT * FROM users")
        users = c_staff.fetchall()
        conn_staff.close()
        return render_template('staff_dashboard.html', users=users)
    else:
        return redirect(url_for('login'))
    

# Route for deleting staff user
@app.route('/delete_staff/<int:user_id>', methods=['POST'])
def delete_staff(user_id):
    if 'logged_in' in session:
        conn_staff = sqlite3.connect('staff.db')
        c_staff = conn_staff.cursor()
        c_staff.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn_staff.commit()
        conn_staff.close()
        flash('User deleted successfully!','info')
        return redirect(url_for('staff_dashboard'))
    else:
        return redirect(url_for('login'))

# Route for changing staff password
@app.route('/change_staff_password/<int:user_id>', methods=['POST'])
def change_staff_password(user_id):
    if 'logged_in' in session:
        new_password = request.form['new_password']
        conn_staff = sqlite3.connect('staff.db')
        c_staff = conn_staff.cursor()
        c_staff.execute("UPDATE users SET password = ? WHERE id = ?", (new_password, user_id))
        conn_staff.commit()
        conn_staff.close()
        flash( 'Password changed successfully!','info')
        return redirect(url_for('staff_dashboard'))
    else:
        return redirect(url_for('login'))


# Function to calculate points
def calculate_points(form_data):
    # Calculate points based on each field
    academics_points = int(form_data['academics'])
    feedback_points = int(form_data['Feedback'])
    innovation_points = int(form_data['innovation'])
    ug_points = int(form_data['ug']) * 3
    pg_points = int(form_data['pg']) * 4
    curriculum_points = int(form_data['curriculum']) * 3
    students_cleared_points = 0
    if int(form_data['studentsClearedAll']) == 100:
        students_cleared_points = 5
    elif int(form_data['studentsClearedAll']) >= 90:
        students_cleared_points = 4
    elif int(form_data['studentsClearedAll']) >= 80:
        students_cleared_points = 3
    attendance_points = 0
    if float(form_data['Attendance']) > 96:
        attendance_points = 5
    elif float(form_data['Attendance']) >= 90:
        attendance_points = 3
    guest_lecture_points = int(form_data['Guest_Lecture']) * 2
    guest_lecture_industry_points = int(form_data['Guest_Lecture_1']) * 3
    online_certification_points = int(form_data['Online_Certification']) * 0.75
    placement_points = int(form_data['Placements']) * 5
    applied_points = 5 if form_data['Applied'] == '>10lakhs' else 3
    received_points = 0  # Assuming no points for this field
    grant_applied_points = int(form_data['Workshop'])
    international_conference_points = int(form_data['International']) * 5
    national_conference_points = int(form_data['National']) * 3
    other_conference_points = int(form_data['Other Events']) * 2
    department_events_points = int(form_data['Department'])  

    # Calculate total points
    total_points = (academics_points + feedback_points + innovation_points + ug_points +
                    pg_points + curriculum_points + students_cleared_points + attendance_points +
                    guest_lecture_points + guest_lecture_industry_points + online_certification_points +
                    placement_points + applied_points + received_points + grant_applied_points +
                    international_conference_points + national_conference_points + other_conference_points +
                    department_events_points)
    
    return total_points

# Route to handle form submission and calculate points
@app.route('/calculate', methods=['POST'])
def calculate():
    # Get form data
    form_data = request.form
    
    # Calculate total points
    total_points = calculate_points(form_data)
    
    # Store staff information and points in the database
    store_staff_info(form_data, total_points)
    
    # Redirect to a new route to display total points
    return redirect(url_for('display_total_points', total_points=total_points))

# New route to display total points
@app.route('/total_points')
def display_total_points():
    total_points = request.args.get('total_points')
    return render_template('total_points.html', total_points=total_points)

# New route to handle linking back to categories page
@app.route('/back_to_categories')
def back_to_categories():
    if 'username' in session:
        username = session['username']
        return redirect(url_for('categories', username=username))
    else:
        flash('Username not provided','info')


# Route to view scores
@app.route('/view_scores')
def view_scores():
    # Fetch staff information from the database
    staff_info = fetch_staff_info()
    
    # Render the scores page template with staff information
    return render_template('view_scores.html', staff_info=staff_info)


# Function to initialize the staff_info database
def init_staff_info_db():
    conn = sqlite3.connect('staff_info.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS staff_info 
                 (id INTEGER PRIMARY KEY, name TEXT UNIQUE, total_points INTEGER)''')
    conn.commit()
    conn.close()

# Call this function to initialize the staff_info database
init_staff_info_db()

def store_staff_info(form_data, total_points):
    staff_name = form_data['staffName']
    
    # Connect to the database
    conn = sqlite3.connect('staff_info.db')
    c = conn.cursor()
    
    # Check if the staff member already exists in the database
    c.execute("SELECT * FROM staff_info WHERE name=?", (staff_name,))
    existing_staff = c.fetchone()
    
    if existing_staff:
        # If the staff member exists, update their total points
        c.execute("UPDATE staff_info SET total_points=? WHERE name=?", (total_points, staff_name))
        conn.commit()
        conn.close()
        return f"Total points updated successfully for {staff_name}!"
    
    # Insert staff information and total points into the database
    c.execute("INSERT INTO staff_info (name, total_points) VALUES (?, ?)", (staff_name, total_points))
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    
    flash( "Staff information stored successfully!",)


# Route for Staff Result Page
@app.route('/staff_result')
def staff_result():
    if 'logged_in' in session:
        # Retrieve the logged-in staff member's username
        username = session['username']
        
        # Connect to the staff_info database to retrieve the staff member's score
        conn_staff_info = sqlite3.connect('staff_info.db')
        c_staff_info = conn_staff_info.cursor()
        c_staff_info.execute("SELECT total_points FROM staff_info WHERE name = ?", (username,))
        total_points = c_staff_info.fetchone()
        conn_staff_info.close()
        
        if total_points:
            # If the total points are available, render the result page with the score
            return render_template('staff_result.html', username=username, total_points=total_points[0])
        else:
            # If the total points are not available, display a message indicating that the score is not calculated yet
            return render_template('staff_result.html', username=username, total_points="Your score is not calculated yet.")
    else:
        return redirect(url_for('login'))

# Function to fetch staff information from the database
def fetch_staff_info():
    try:
        conn = sqlite3.connect('staff_info.db')
        c = conn.cursor()
        c.execute("SELECT * FROM staff_info")
        staff_info = c.fetchall()
        conn.close()
        return staff_info
    except sqlite3.Error as e:
        print("Error fetching staff information:", e)
        return None

@app.route('/view_form/<int:form_id>')
def view_form_by_id(form_id):
    # Your logic to fetch and render a specific form based on form_id
    pass

# Route for logging out
@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove username from the session
    # Your logout logic here
    return redirect(url_for('login'))  # Redirect to the login page after logout


if __name__ == '__main__':
    init_db()
    init_hod_db()
    init_staff_db()
    app.run(debug=True, host="0.0.0.0")

