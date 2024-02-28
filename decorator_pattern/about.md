# Decorator Design Pattern

The Decorator Design Pattern is a structural pattern that allows behavior to be added to individual objects, either statically or dynamically, without affecting the behavior of other objects from the same class. It is useful for extending the functionality of classes in a flexible and reusable manner.

## Intent

- Attach additional responsibilities to objects dynamically.
- Provide a flexible alternative to subclassing for extending functionality.

## Structure

The key components of the Decorator Design Pattern are:

1. **Component**: Defines the interface for objects that can have responsibilities added to them dynamically.
   
2. **ConcreteComponent**: Represents the base object to which additional responsibilities can be added.
   
3. **Decorator**: Maintains a reference to a Component object and defines an interface that conforms to Component's interface.
   
4. **ConcreteDecorator**: Adds responsibilities to the component.

## Example

Let's consider a simple example of decorating a `Coffee` object with additional condiments.

### Component

```python
interface Coffee {
    cost(): number;
}
