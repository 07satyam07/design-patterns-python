# Python Design Patterns

This repository contains examples of design patterns implemented in Python.

## Table of Contents

1. [Introduction](#introduction)
2. [Design Patterns](#design-patterns)
    - [1. Strategy Pattern](#1-strategy-pattern)
    - [2. Observer Pattern](#2-observer-pattern)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [License](#license)

## Introduction

Design patterns are reusable solutions to commonly occurring problems in software design. They provide a way to structure and organize code, making it more maintainable, scalable, and understandable. This repository demonstrates various design patterns implemented in Python, along with explanations and examples.

## Design Patterns

### 1. Strategy Pattern

The Strategy Pattern is a behavioral design pattern that enables an algorithm's behavior to be selected at runtime. It defines a family of algorithms, encapsulates each one, and makes them interchangeable. This pattern allows the algorithm to vary independently of the clients that use it, promoting flexibility and extensibility.

[Strategy Pattern](./strategy_pattern)

### 2. Observer Pattern

The Observer Pattern is a behavioral design pattern where an object, known as the subject, maintains a list of its dependents, called observers, and notifies them of any changes in its state, usually by calling one of their methods. This allows for a loosely coupled system where changes in one object can trigger actions in other objects without them being directly coupled.

[Observer Pattern](./observer_pattern)

### 3. Factory Pattern

The Factory Pattern is a creational design pattern used to create objects without specifying the exact class of object that will be created. It provides a way to delegate the instantiation logic to child classes.

[Factory Pattern](./factory_pattern)

### Proxy Pattern

The Proxy Pattern is a structural design pattern that provides a surrogate or placeholder for another object to control access to it. It allows you to create an intermediary that acts as an interface to another resource, such as a network connection, a large object in memory, or a complex computation. The proxy controls access to the original object, allowing you to perform additional tasks before or after accessing it, such as logging, caching, or authentication.

[Proxy Pattern](./proxy_pattern)


### Singelton Pattern

The Singleton Pattern is a creational design pattern that ensures a class has only one instance and provides a global point of access to that instance. It is commonly used when exactly one object is needed to coordinate actions across the system.

[Singelton Pattern](./singelton_pattern)


### Builder Patern 

The Builder Pattern is a creational design pattern that separates the construction of a complex object from its representation, allowing the same construction process to create different representations. It aims to solve the problem of telescoping constructor anti-pattern where the number of constructor parameters becomes excessive.

[Builder Pattern](./builder_pattern)

## Usage

To run the examples, simply execute each Python file using a Python interpreter.

```bash
python ./strategy_pattern/main.py
python ./observer_pattern/main.py
python ./factory_pattern/main.py
python ./proxy_pattern/main.py
python ./singelton_pattern/main.py
python ./builder_pattern/main.py
