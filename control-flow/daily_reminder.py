while True:
    task_description = input("Enter your task: ")
    
    priority = input("Priority (high/medium/low): ").lower()
    
    if priority in ['high', 'medium', 'low']:
        break
    else:
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    if time_bound in ['yes', 'no']:
        break
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")

base_reminder = ""
note_message = ""

match priority:
    case 'high':
        base_reminder = f"'{task_description}' is a high priority task"
    case 'medium':
        base_reminder = f"'{task_description}' is a medium priority task"
    case 'low':
        base_reminder = f"'{task_description}' is a low priority task. Consider completing it when you have free time."
        
        note_message = f"Note: {base_reminder}"
        base_reminder = ""

if base_reminder and time_bound == 'yes':
    base_reminder += " that requires immediate attention today!"
elif base_reminder and time_bound == 'no':
    base_reminder += ". Focus on it soon."
    
if base_reminder:
    print(f"\nReminder: {base_reminder}")
elif note_message:
    print(f"\n{note_message}")
