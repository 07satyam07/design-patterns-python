## Observer Pattern

The Observer Pattern is a behavioral design pattern used to establish a one-to-many dependency between objects, ensuring that when one object changes state, all its dependents are notified and updated automatically.

### Key Components:

1. **Subject**:
   - The object being observed, which maintains a list of its dependents (observers).
   - Provides methods to attach, detach, and notify observers.
   - Keeps track of its state and notifies observers when the state changes.

2. **Observer**:
   - Represents the dependent objects interested in receiving updates from the subject.
   - Defines an update method that the subject calls to notify observers of state changes.

### How It Works:

1. **Registration**:
   - Observers register themselves with the subject to receive notifications.
   - Typically done through a registration method in the subject, where observers are added to a list maintained by the subject.

2. **Notification**:
   - When the subject's state changes, it iterates through its list of observers and calls the update method on each observer.
   - The subject passes any necessary information about the state change to the update method.

3. **Update**:
   - Each observer implements the update method to handle the notification from the subject.
   - Observers can retrieve the updated state from the subject and take appropriate actions, such as updating their own state or triggering further behavior.

### Example Scenario:

Consider a weather monitoring system:
- **Subject**: Weather station collects data (temperature, humidity, etc.) and notifies observers when the weather changes.
- **Observers**: Displays (current conditions, forecast, statistics) register with the weather station to receive updates.
  - **Current Conditions Display**: Updates current temperature and humidity.
  - **Forecast Display**: Updates weather forecast.
  - **Statistics Display**: Updates statistical data (average temperature, etc.).

### Benefits:

- **Loose Coupling**: Subjects and observers are loosely coupled, allowing for easier maintenance and scalability.
- **Flexibility**: New observers can be added without modifying the subject, and vice versa.
- **Modularity**: Encourages separation of concerns by decoupling the logic for state changes and the logic for handling those changes.

### When to Use:

- Use the Observer Pattern when you have a one-to-many relationship between objects, where changes in one object require updates to multiple other objects.
- Use it to decouple the subject and observers, enabling easier maintenance and extensibility of the system.
