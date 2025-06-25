# 🧮 Geometric Shape Area & Perimeter Calculator

A modular Python calculator for computing the **area** and **perimeter (scope)** of various 2D geometric shapes, using clean **Object-Oriented Programming (OOP)** principles.

Designed to be **scalable**, **easy to use**, and **educational**.

---

## 📁 Project Structure

```
.
├── calculator.py     # Central calculator class
├── shape.py          # Abstract base class
├── square.py         # Square shape
├── rectangle.py      # Rectangle shape
├── triangle.py       # Triangle shape
├── circle.py         # Circle shape
├── hexagon.py        # Hexagon shape
```

---

## 🧠 OOP Concepts

| Concept         | Implementation                                      |
|----------------|------------------------------------------------------|
| Inheritance     | All shapes inherit from a base class `Shape`        |
| Polymorphism    | Each shape defines its own area and perimeter logic |
| Encapsulation   | Shape parameters are stored and used internally     |
| Extensibility   | Easy to add more shapes with minimal changes        |

---

## 🚀 Usage Example

```python
from hexagon import Hexagon
from calculator import calculator

hex = Hexagon(5)
calc = calculator(hex)
calc.calculate()
```

You can use the same pattern for:
```python
from square import square
from rectangle import rectangle
from triangle import Triangle
from circle import circle
```

---

## 📊 Shape Comparison Table

| Shape     | Parameters                  | Area Formula                  | Perimeter Formula            |
|-----------|------------------------------|-------------------------------|------------------------------|
| Square    | side (s)                    | s × s                         | 4 × s                        |
| Rectangle | width (w), height (h)       | w × h                         | 2 × (w + h)                  |
| Triangle  | base (b), height (h), side1, side2 | (b × h) / 2          | b + side1 + side2           |
| Circle    | radius (r)                  | π × r²                        | 2 × π × r                    |
| Hexagon   | side (s)                    | (3√3 / 2) × s²                | 6 × s                        |

> All calculations use floating-point precision and the `math` module where needed.

---

## ✅ Requirements

- Python 3.7+
- Standard Library only (uses `math`)

---

## 🖼️ Optional: Demo GIF

To show usage visually, add a demo GIF like this:

```markdown
![Demo](assets/demo.gif)
```

---

## 🛠️ Future Features

- Support for scalene/irregular triangle classification  
- 3D shape extensions (cube, sphere, cylinder)  
- User input CLI or GUI using `Tkinter` or `PyQt`  
- Internationalization (i18n) support for Hebrew or others  
- Unit tests using `pytest`  

---

## 👨‍💻 Created For Learning

This project is an OOP training ground:  
Modular, readable, and fun to expand.

---
