# Fitness Management System CLI

This Fitness Management System is a command-line interface (CLI) application designed to help users manage their fitness goals, workouts, nutrition logs, and overall health metrics. The application allows for easy interaction through prompts, providing a user-friendly experience.

## Features

### User Management
- **Add User**: Add a new user with their name and fitness level.
- **View Goals**: Retrieve and display fitness goals for a specified user.

### Workout Management
- **Add Workout**: Add a workout plan for a specific user.
- **Generate Workout Plan**: Generate a customized workout plan based on the user's fitness level.
- **Schedule Workout**: Schedule a workout for a user on a specified date.
- **Adjust Workout Plan**: Modify the workout plan based on the user's fitness level.

### Nutrition Management
- **Log Nutrition**: Log nutrition data including food items and calories consumed.

### Fitness Tracking
- **Log Fitness Metrics**: Log fitness metrics such as weight and performance.
- **Check Progress**: Calculate progress toward fitness goals and provide motivational feedback.

### Injury Prevention
- **Injury Tips**: Provide tips for injury prevention during workouts.

### Schedule Recommendations
- **Recommend Workout Schedule**: Suggest a workout schedule based on the number of workouts per week.

## Dependencies

This project requires the following Python packages:
- `Click`: For creating command-line interfaces.
- `SQLAlchemy`: For database interactions.
- `SQLite`: As the database backend (comes with Python).

To install the dependencies, run:

```bash
pip install click sqlalchemy

Getting Started

    Clone the Repository:

    bash

git clone https://github.com/yourusername/fitness-management-system.git
cd fitness-management-system

Initialize the Database: To set up the SQLite database, run:

bash

python -m app.cli init

Run the CLI: You can access the CLI commands using:

bash

python -m app.cli [COMMAND]

Replace [COMMAND] with one of the following:

    add-user
    add-workout
    log-nutrition
    add-goal
    log-fitness_metric
    check-progress
    view-goals
    injury-tips
    generate-plan
    recommend-workout-schedule
    schedule-workout-command
    adjust-plan

Example Usage:

bash

    python -m app.cli add-user

    Follow the prompts to add a user.

Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request to enhance the functionality of the application.
License

This project is licensed under the MIT License - see the LICENSE file for details.