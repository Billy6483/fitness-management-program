import click
from .database import SessionLocal, init_db
from .models import User, WorkoutPlan, NutritionLog, FitnessGoal, FitnessMetric
from .utils import validate_date, format_nutrition_log, format_fitness_metric
from datetime import datetime

@click.group()
def cli():
    """Fitness Management System CLI."""
    pass

@cli.command()
def init():
    """Initialize the database."""
    init_db()
    click.echo("Database initialized.")

@cli.command()
@click.argument('name')
@click.argument('fitness_level')
def add_user(name, fitness_level):
    """Add a new user."""
    db = SessionLocal()
    new_user = User(name=name, fitness_level=fitness_level)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    click.echo(f"Added user: {new_user.name}")

@cli.command()
@click.argument('user_id')
@click.argument('description')
def add_workout(user_id, description):
    """Add a workout plan for a user."""
    db = SessionLocal()
    workout_plan = WorkoutPlan(user_id=user_id, description=description)
    db.add(workout_plan)
    db.commit()
    click.echo(f"Added workout plan: {description}")

@cli.command()
@click.argument('user_id')
@click.argument('date')
@click.argument('food_item')
@click.argument('calories', type=int)
def log_nutrition(user_id, date, food_item, calories):
    """Log nutrition data for a user."""
    validated_date = validate_date(date)
    db = SessionLocal()
    nutrition_log = NutritionLog(user_id=user_id, date=validated_date, food_item=food_item, calories=calories)
    db.add(nutrition_log)
    db.commit()
    click.echo(format_nutrition_log(validated_date, food_item, calories))

@cli.command()
@click.argument('user_id')
@click.argument('goal_description')
@click.argument('target_date')
def add_goal(user_id, goal_description, target_date):
    """Add a fitness goal for a user."""
    validated_date = validate_date(target_date)
    db = SessionLocal()
    goal = FitnessGoal(user_id=user_id, goal_description=goal_description, target_date=validated_date)
    db.add(goal)
    db.commit()
    click.echo(f"Added goal: {goal_description} by {validated_date}")

@cli.command()
@click.argument('user_id')
@click.argument('weight', type=int)
@click.argument('performance', type=int)
def log_fitness_metric(user_id, weight, performance):
    """Log fitness metrics for a user."""
    db = SessionLocal()
    metric = FitnessMetric(user_id=user_id, weight=weight, performance=performance)
    db.add(metric)
    db.commit()
    click.echo(format_fitness_metric(weight, performance))

if __name__ == "__main__":
    cli()
