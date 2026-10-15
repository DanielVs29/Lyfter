from datetime import date

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth
        

    @property
    def age(self):
        today = date.today()
        return (
            today.year 
            - self.date_of_birth.year 
            - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        )


def adult_required(func):
    def wrapper(user, *args, **kwargs):
        
        if user.age < 18:
            raise ValueError(f"Access denied. User age is {user.age}, must be at least 18 years old.")
        
        return func(user, *args, **kwargs)
        
    return wrapper


@adult_required
def buy_alcohol(user, beverage_name):
    print(f"Successfully purchased {beverage_name}!")


adult_user = User(date(1995, 5, 15))
minor_user = User(date(2012, 10, 20))

print(f"Adult user age: {adult_user.age}")
buy_alcohol(adult_user, "Wine")


print(f"Minor user age: {minor_user.age}")
buy_alcohol(minor_user, "Beer") 