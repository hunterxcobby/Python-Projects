#!/usr/bin/python3

"""Data abstraction is the process of hiding the implementation details of an object
and exposing only the relevant information to the user. 
This allows the user to interact with the object without needing to understand how it works internally.
Abstraction helps in managing complexity by providing a simple and clear interface to the user."""

"""Example:

Consider a car. As a driver, you don't need to know how the engine, transmission, or other components work internally. 
You interact with the car using a simplified interface: the steering wheel, pedals, and gear shift.
This is an example of data abstraction."""

class Smartphone:
    def __init__(self):
        # Initialize a Screen object and an empty list to store apps
        self.screen = Screen()
        self.apps = []

    def add_app(self, app):
        # Add an app to the list of installed apps
        self.apps.append(app)

    def display_apps(self):
        # Display the list of installed apps on the screen
        self.screen.display("Apps: " + ", ".join(self.apps))

class Screen:
    def display(self, message):
        # Display a message on the screen
        print(message)

# Create a Smartphone object
phone = Smartphone()

# Add some apps to the phone
phone.add_app("Calculator")
phone.add_app("Contacts")

# Display the list of installed apps
phone.display_apps()

"""As a user of the Smartphone class,
you interact with the phone through methods like add_app and display_apps,
without needing to understand the internal workings of the phone. 
This is an example of data abstraction, where the complex details 
are hidden behind a simplified interface."""