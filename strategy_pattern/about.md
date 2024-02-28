## Strategy Pattern

The Strategy Pattern is a behavioral design pattern that enables an algorithm's behavior to be selected at runtime. It defines a family of algorithms, encapsulates each one, and makes them interchangeable. This pattern allows the algorithm to vary independently of the clients that use it, promoting flexibility and extensibility.

### Key Components:

1. **Context**: The class that maintains a reference to the chosen strategy object. It acts as a client to the strategy objects and delegates the algorithm implementation to the current strategy.

2. **Strategy**: The interface or abstract class that defines a set of methods representing the algorithm's contract. It serves as the base class for all concrete strategy implementations.

3. **Concrete Strategies**: The concrete implementations of the strategy interface. Each concrete strategy encapsulates a specific algorithm and provides its own implementation for the defined methods.

### Usage:

- The Strategy Pattern is used when multiple algorithms exist for performing a specific task, and the appropriate algorithm needs to be selected dynamically at runtime.
  
- It promotes encapsulation by isolating the algorithm's implementation details from the client code, allowing algorithms to be added, removed, or modified without affecting the client's code.

- This pattern is particularly useful in scenarios where the same set of operations need to be performed in different contexts or environments, with each context requiring a different algorithm.

### Example Scenario:

In a document processing application, the application needs to support multiple file compression algorithms such as ZIP, RAR, and GZIP. Rather than embedding the compression logic directly into the application, the Strategy Pattern can be used. The application defines a common compression interface (Strategy) with methods like `compress()` and `decompress()`. Concrete strategy classes (ZIPCompressionStrategy, RARCompressionStrategy, etc.) implement these methods with their specific compression algorithms. At runtime, the application can dynamically switch between different compression strategies based on user preferences or file types without modifying the core application logic.
