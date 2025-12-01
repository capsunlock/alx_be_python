task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder_content = ""

# Use Match Case to handle priority levels
match priority:
    case "high":
        if time_bound == "yes":
            # High priority AND time-bound -> immediate attention
            reminder_content = f"'{task}' is a {priority} priority task that requires immediate attention today!"
        else:
            # High priority but NOT time-bound -> high importance, but no deadline stress
            reminder_content = f"'{task}' is a {priority} priority task. This should be completed as soon as possible."
            
    case _: # This case handles "medium", "low", and any other input
        if time_bound == "yes":
            # Medium/Low priority AND time-bound -> must be done today
            reminder_content = f"'{task}' is a {priority} priority task that requires immediate attention today!"
        else:
            # Medium/Low priority and NOT time-bound (matches the 'low/no' example output)
            reminder_content = f"'{task}' is a {priority} priority task. Consider completing it when you have free time."

# Provide the customized reminder with the required prefix

if time_bound == "yes":
    print(f"Reminder: {reminder_content}")
else:
    print(f"Note: {reminder_content}")