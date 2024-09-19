from datetime import datetime

def validate_date(date_str):
    """Validate date format (YYYY-MM-DD) and return a datetime object."""
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format.")

def calculate_progress(current: int, target: int) -> int:
    """Calculate progress percentage."""
    if target <= 0:
        raise ValueError("Target must be greater than zero.")
    return (current / target) * 100

def format_nutrition_log(date, food_item, calories):
    """Format a nutrition log entry for display."""
    return f"{date}: {food_item} - {calories} calories"

def format_fitness_metric(weight, performance):
    """Format a fitness metric entry for display."""
    return f"Weight: {weight} kg, Performance: {performance} units"

def prompt_user_for_input(prompt: str) -> str:
    """Prompt the user for input with a message."""
    return input(prompt)
