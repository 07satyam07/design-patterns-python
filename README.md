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

## Usage

To run the examples, simply execute each Python file using a Python interpreter.

```bash
python ./strategy_pattern/main.py
python ./observer_pattern/main.py
python ./factory_pattern/main.py
