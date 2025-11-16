def daily_reminder():
    """
    Prompts the user for a single task's details and provides a customized
    reminder based on priority and time-sensitivity, using match-case and if statements.
    """
    print("--- Personal Daily Reminder Generator ---")

    # 1. Prompt for a Single Task
    task = input("Enter your task: ")
    
    # Prompt for the task’s priority
    priority = input("Priority (high/medium/low): ").lower().strip()
    
    # Prompt if the task is time-bound
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

    # Variable to hold the final reminder message
    final_reminder = ""

    # 2. Process the Task Based on Priority and Time Sensitivity
    
    # Check if the task is time-bound (using an if statement)
    if time_bound == 'yes':
        # Time-bound tasks require the 'Reminder:' prefix and 'immediate attention' message
        
        # Use Match Case to incorporate the priority into the message
        match priority:
            case 'high':
                base_text = f"'{task}' is a high priority task"
            case 'medium':
                base_text = f"'{task}' is a medium priority task"
            case 'low':
                base_text = f"'{task}' is a low priority task"
            case _:
                base_text = f"'{task}' has an unrecognized priority ({priority}) but is time-bound"

        # Construct the final reminder for immediate action
        final_reminder = f"Reminder: {base_text} that requires immediate attention today!"

    else:
        # Non-time-bound tasks use the 'Note:' prefix and soft advice.
        
        # Use Match Case to determine the appropriate softer reminder based on priority.
        match priority:
            case 'high':
                final_reminder = f"Note: '{task}' is a high priority task. Plan to complete it early in the day."
            case 'medium':
                final_reminder = f"Note: '{task}' is a medium priority task. Schedule time for it soon."
            case 'low':
                # Matches the example output for non-time-bound low priority
                final_reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
            case _:
                final_reminder = f"Warning: Priority '{priority}' not recognized. Please focus on task: '{task}'."

    # 3. Print the final reminder
    print("\n" + final_reminder)

# Run the function
if __name__ == "__main__":
    daily_reminder()