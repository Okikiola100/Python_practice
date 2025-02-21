import sqlite3
from datetime import datetime

# Database setup
def init_db():
    conn = sqlite3.connect("fitness_tracker.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            exercise TEXT,
            duration INTEGER,
            calories INTEGER,
            date TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Add a new workout
def add_workout(exercise, duration, calories, date):
    conn = sqlite3.connect("fitness_tracker.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO workouts (exercise, duration, calories, date) VALUES (?, ?, ?, ?)",
                   (exercise, duration, calories, date))
    conn.commit()
    conn.close()
    print("Workout added successfully!")

# Retrieve all workouts
def get_all_workouts():
    conn = sqlite3.connect("fitness_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM workouts")
    workouts = cursor.fetchall()
    conn.close()
    return workouts

# Retrieve a single workout by ID
def get_workout_by_id(workout_id):
    conn = sqlite3.connect("fitness_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM workouts WHERE id = ?", (workout_id,))
    workout = cursor.fetchone()
    conn.close()
    return workout

# Main function
def main():
    init_db()
    while True:
        print("\nFitness Tracker Menu:")
        print("1. Add Workout")
        print("2. View All Workouts")
        print("3. View Single Workout")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            exercise = input("Enter exercise name: ")
            duration = int(input("Enter duration (minutes): "))
            calories = int(input("Enter calories burned: "))
            date = input("Enter date (YYYY-MM-DD): ") or datetime.now().strftime("%Y-%m-%d")
            add_workout(exercise, duration, calories, date)
        
        elif choice == "2":
            workouts = get_all_workouts()
            for w in workouts:
                print(f"ID: {w[0]}, Exercise: {w[1]}, Duration: {w[2]} mins, Calories: {w[3]}, Date: {w[4]}")
        
        elif choice == "3":
            workout_id = int(input("Enter workout ID: "))
            workout = get_workout_by_id(workout_id)
            if workout:
                print(f"ID: {workout[0]}, Exercise: {workout[1]}, Duration: {workout[2]} mins, Calories: {workout[3]}, Date: {workout[4]}")
            else:
                print("Workout not found.")
        
        elif choice == "4":
            print("Exiting Fitness Tracker. Stay fit!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()