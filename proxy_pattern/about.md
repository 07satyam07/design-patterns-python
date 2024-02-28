## Proxy Pattern

The Proxy Pattern is a structural design pattern that provides a surrogate or placeholder for another object to control access to it. It allows you to create an intermediary that acts as an interface to another resource, such as a network connection, a large object in memory, or a complex computation. The proxy controls access to the original object, allowing you to perform additional tasks before or after accessing it, such as logging, caching, or authentication.

### Key Components:

1. **Subject**: Represents the common interface for both the RealSubject and Proxy, allowing the client to interact with either object interchangeably.

2. **RealSubject**: The real object that the proxy represents. It performs the actual work.

3. **Proxy**: Controls access to the RealSubject and forwards requests to it, performing additional tasks if needed (e.g., creating the RealSubject on demand, caching results, logging).

### Usage:

- The Proxy Pattern is used when you need to control access to an object, providing a surrogate or placeholder to control its creation, access, and lifecycle.

- It is useful for implementing lazy initialization, caching, access control, logging, and monitoring.

- This pattern is also applicable in scenarios where you want to add additional functionalities or control access to the real object without modifying its code directly.

### Example Scenario:

Consider a scenario where you have a large image file that needs to be loaded into memory for processing. Loading the entire image into memory at once may consume a significant amount of resources. Instead, you can use a proxy to lazily load the image into memory only when it is actually needed. The proxy can act as a placeholder for the image, loading it from disk or a remote server only when requested by the client. This improves memory efficiency and reduces loading time, especially for large files.
