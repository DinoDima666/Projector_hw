
def is_admin(func):
    def wrapper(*args, **kwargs):
        user_type = kwargs.get('user_type')
        if user_type != 'admin':
            raise ValueError('Permission denied')
        return func(*args, **kwargs)
    return wrapper





@is_admin
def show_customer_receipt(user_type: str):
    print("Your receipt number is 42")

show_customer_receipt(user_type='user')

show_customer_receipt(user_type='admin')