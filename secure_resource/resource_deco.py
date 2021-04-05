from auth import authenticate
from datetime import datetime
from functools import wraps

def resource_deco(email='example@email.com', password='example123'):
    def outer_wrapper(func):
        user = authenticate(email, password)
        @wraps(func)
        def wrapper():
            current_datetime = datetime.now()
            current_date = current_datetime.strftime('%d/%m/%Y')
            current_time = current_datetime.strftime('%H:%M:%S')
            if user:
                if user['role'] in ["admin","superadmin"]:
                    with open('access_granted.txt', 'a') as access_granted_file:
                        access_granted_file.write(f'{user["role"].capitalize()} {user["first_name"]} {user["last_name"]} viewed company resources on {current_date} at {current_time}\n')
                    return func()
                else:
                    with open('access_denied.txt', 'a') as access_denied_file:
                        access_denied_file.write(f'{user["role"].capitalize()} {user["first_name"]} {user["last_name"]} tried to view company most valuable resource on {current_date} at {current_time}\n')
                    return f'You are not authorized to view this'
            else:
                return f"Only staff can access this resource"
        return wrapper
    return outer_wrapper
