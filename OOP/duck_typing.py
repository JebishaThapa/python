class Duck:
    def swim(self):
        return "Swimming gracefully in the pond."

    def quack(self):
        return "Quack, quack!"


class Person:
    def swim(self):
        return "Swimming laps using freestyle stroke."

    def quack(self):
        return "I am mimicking a duck! Quack!"


class Car:
    def drive(self):
        return "Vroom! Driving down the highway."


# This function demonstrates Duck Typing
def perform_duck_actions(animal_like_obj):
    # The function does not check if the object is an instance of Duck.
    # It only cares if the object has the required 'swim' and 'quack' methods.
    try:
        print(animal_like_obj.swim())
        print(animal_like_obj.quack())
    except AttributeError as e:
        print(f"Error: Object lacks required duck behaviors. Details: {e}")
    print("-" * 40)


if __name__ == "__main__":
    # Instantiate the objects
    donald = Duck()
    john = Person()
    tesla = Car()

    print("--- Testing the Duck ---")
    perform_duck_actions(donald)

    print("--- Testing the Person (Duck Typing in action) ---")
    # Even though John is a Person and doesn't inherit from Duck,
    # he behaves like a duck, so Python allows it!
    perform_duck_actions(john)

    print("--- Testing the Car (Missing expected behaviors) ---")
    # The Car class does not have swim() or quack(), so it fails gracefully.
    perform_duck_actions(tesla)
