def daily_reminder():
    """
    Prompts the user for a single task's details and provides a customized
    reminder based on priority and time-sensitivity.
    """
    print("--- Personal Daily Reminder Generator ---")

    # 1. Prompt for a Single Task
    task = input("Enter your task: ")
    
    # Standardize priority input for the match case
    priority = input("Priority (high/medium/low): ").lower().strip()
    
    # Standardize time_bound input for the if statement
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

    # Variable to hold the final reminder message
    final_reminder = ""

    # 2. Process the Task Based on Priority and Time Sensitivity
    
    if time_bound == 'yes':
        # If the task is time-bound, it requires the "immediate attention" message
        # and the "Reminder:" prefix, regardless of priority level.
        
        # Use Match Case to build the core task description
        match priority:
            case 'high':
                base_text = f"'{task}' is a high priority task"
            case 'medium':
                base_text = f"'{task}' is a medium priority task"
            case 'low':
                base_text = f"'{task}' is a low priority task"
            case _:
                base_text = f"'{task}' has an unrecognized priority ({priority}) and is time-bound"

        # Construct the final reminder string for immediate action
        # The required message should be 'that requires immediate attention today!'
        final_reminder = f"Reminder: {base_text} that requires immediate attention today!"

    else:
        # If the task is NOT time-bound, use the "Note:" prefix and soft advice.
        # Use Match Case to determine the appropriate softer reminder based on priority.
        match priority:
            case 'high':
                advice = "Plan to complete it early in the day."
                final_reminder = f"Note: '{task}' is a high priority task. {advice}"
            case 'medium':
                advice = "Schedule time for it soon."
                final_reminder = f"Note: '{task}' is a medium priority task. {advice}"
            case 'low':
                # Matches the example output for non-time-bound low priority
                advice = "Consider completing it when you have free time."
                final_reminder = f"Note: '{task}' is a low priority task. {advice}"
            case _:
                final_reminder = f"Warning: Priority '{priority}' not recognized. Please focus on task: '{task}'."

    # 3. Print the final reminder
    print("\n" + final_reminder)

# Run the function
if __name__ == "__main__":
    daily_reminder()