task = input ("Enter your task: ")
priority = input ("Priority (high/medium/low): ").lower()
time_bound = input ("Is it time-bound? (yes/no): ").lower()

match priority:
  case _:
    if time_bound == "yes":
      print(f"'{task}' is a {priority} priority task that requires immediate attention today!")
    else:
      print(f"'{task}' is a {priority} priority task. Consider completing it when you have free time.")