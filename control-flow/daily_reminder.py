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

    # 2. Process the Task Based on Priority and Time Sensitivity
    
    # Initialize a base reminder message
    base_message = f"Note: '{task}' is a {priority} priority task."
    
    # 3. Provide a Customized Reminder using Match Case
    match priority:
        case 'high':
            # High priority tasks often need more urgency.
            if time_bound == 'yes':
                # Time-bound high priority task requires immediate attention
                final_reminder = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
            else:
                final_reminder = f"Reminder: '{task}' is a high priority task. Plan to complete it early."
                
        case 'medium':
            # Medium priority tasks are important but can wait a moment.
            if time_bound == 'yes':
                final_reminder = f"Reminder: '{task}' is a medium priority task that requires immediate attention today!"
            else:
                final_reminder = f"Note: '{task}' is a medium priority task. Schedule time for it soon."

        case 'low':
            # Low priority tasks are flexible.
            if time_bound == 'yes':
                # Even low priority time-bound tasks need that specific message
                final_reminder = f"Reminder: '{task}' is a low priority task that requires immediate attention today!"
            else:
                final_reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."

        case _:
            # Handle unrecognized priority input
            final_reminder = f"Warning: Priority '{priority}' not recognized. Please focus on task: '{task}'."

    # Print the final reminder
    print("\n" + final_reminder)

# Run the function
if __name__ == "__main__":
    daily_reminder()