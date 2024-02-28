## Factory Pattern

The Factory Pattern is a creational design pattern used to create objects without specifying the exact class of object that will be created. It provides a way to delegate the instantiation logic to child classes.

### Key Components:

1. **Product**:
   - Defines the interface of objects the factory method creates.
   
2. **Concrete Product**:
   - Implements the Product interface.

3. **Factory**:
   - Declares the factory method, which returns an object of type Product.
   - May implement a default behavior for creating objects or provide a default implementation of the factory method.

4. **Concrete Factory**:
   - Overrides the factory method to create specific types of products.
   
### How It Works:

1. **Client**:
   - Invokes the factory method to create objects without knowing the concrete type of object that will be created.
   
2. **Factory Method**:
   - Abstract method declared in the Factory class or interface.
   - Returns an object of the Product type.
   
3. **Concrete Factory Implementation**:
   - Concrete subclasses of the Factory class override the factory method to create specific types of products.
   
### Example Scenario:

Consider a pizza restaurant:
- **Product**: Pizza (with different types such as Margherita, Pepperoni, etc.).
- **Concrete Products**: MargheritaPizza, PepperoniPizza, etc.
- **Factory**: PizzaFactory with a method `create_pizza()`.
- **Concrete Factory**: MargheritaPizzaFactory, PepperoniPizzaFactory, etc. each implementing `create_pizza()` to create the respective pizzas.

### Benefits:

- **Decoupling**: Clients are decoupled from the specific classes of objects they create, as they only interact with the factory method.
- **Flexibility**: Allows adding new products or changing the implementation of existing products without modifying client code.
- **Encapsulation**: Encapsulates the object creation logic, promoting code maintainability and readability.

### When to Use:

- Use the Factory Pattern when a class cannot anticipate the class of objects it must create.
- Use it when you want to centralize the creation logic to avoid duplication and promote maintainability.
- Use it to abstract the object creation process, making it easier to extend and customize object creation.
