# 🐍 PythonDAW

Ejercicios de **Fundamentos de Programación en Python** realizados durante el primer curso del ciclo de **Desarrollo de Aplicaciones Web (1DAW)**.

El repositorio está organizado por unidades de trabajo (UT) y recoge tanto los ejercicios propuestos en clase como pequeñas pruebas y ejemplos que he ido haciendo para practicar.

---

## 📁 Estructura del repositorio

```
PythonDAW/
├── ut1/        → UT1: variables, tipos, entrada/salida y operadores
├── ut2/        → UT2: funciones
├── Todo el material (PDF) - CMO-313 · Fundamentos de programación.pdf
└── README.md
```

---

## 📘 UT1 · Primeros pasos con Python

Variables con anotaciones de tipo, `input()` / `print()`, f-strings, operadores aritméticos y primeras estructuras de control.

| Archivo | Qué hace |
|---|---|
| `ejemplo.py` | Suma de dos números siguiendo el esquema *Entrada → Proceso → Salida* |
| `ejemplo1.py` | Pide la edad y dice si eres mayor o menor de edad (`if` / `else`) |
| `ejercicio2.py` | Muestra varias variables y su tipo con `type()` (`str`, `int`, `float`, `bool`) |
| `ejercicio3.py` | Intercambio de dos variables en una sola línea (`a, b = b, a`) |
| `Ej1,5.py` | Suma de dos números introducidos por teclado |
| `EjerciciosPropuestos1.py` | Conversión de grados Celsius a Fahrenheit |
| `EjerciciosPropuestos2.py` | Área y perímetro de un rectángulo |
| `EjerciciosPropuestos3.py` | Conversión de segundos a horas, minutos y segundos (`//` y `%`) |
| `EjerciciosPropuestos4.py` | Precio final aplicando un 15 % de descuento |
| `EjerciciosPropuesto5.py` | Función que calcula la media de tres números |
| `EjerciciosPropuestos6.py` | Desglose de céntimos en monedas (mi versión, en progreso) |
| `EjerciciosPropuesto6ejemploProfe.py` | Desglose de céntimos en monedas con un bucle `for` (solución de referencia) |
| `EjerciciosPropuesto7.py` | Línea de ticket formateada con alineación y decimales en f-strings |
| `EjerciciosPropuesto8.py` | Función que devuelve base, IVA y total en una tupla |
| `nose.py` | Mini factura: base, IVA (21 %) y total con formato de tabla |
| `a.py` | Prueba rápida |

---

## 📗 UT2 · Funciones

Definición de funciones, `return` frente a `print`, anotaciones de tipo, parámetros posicionales y por nombre, y valores por defecto.

| Archivo | Qué hace |
|---|---|
| `Ejercicio1.1.py` | Reescribir código repetido usando una sola función `saludo()` |
| `Ejercicio1.2.py` | Reflexión sobre nombres de funciones mal elegidos (`f1`, `hacer_cosas`, `calcular`) |
| `Ejercicio1.3.py` | Función mínima `con_iva()` para no repetir el cálculo del IVA |
| `Ejercicio2.1.py` | Función que indica si un número es par (devuelve `True` / `False`) |
| `Ejercicio2.2.py` | Diferencia entre una función que hace `print` y otra que hace `return` |
| `Ejercicio2.3.py` | `mayor(a, b)` sin usar `max()` (operador ternario) |
| `Ejercicio3.1.py` | `presentar(nombre, ciudad)` llamada por posición y por nombre |
| `Ejercicio3.2.py` | `saludar(nombre, saludo="Hola")` con valor por defecto |
| `Ejercicio3.3.py` | `potencia(base, exponente=2)`: los parámetros con valor por defecto van al final |

---

## ▶️ Cómo ejecutar los ejercicios

Necesitas **Python 3.9 o superior** (algunos ejercicios usan anotaciones como `tuple[float, float, float]`).

```bash
# Clonar el repositorio
git clone https://github.com/AlvaroML19/PythonDAW.git
cd PythonDAW

# Ejecutar cualquier ejercicio
python ut1/EjerciciosPropuestos1.py
python ut2/Ejercicio3.3.py
```

> En Windows puede que el comando sea `py` en lugar de `python`.
> Los archivos con espacios o comas en el nombre conviene escribirlos entre comillas: `python "ut1/Ej1,5.py"`.

---

## 📚 Material del curso

En la raíz del repositorio está el PDF **CMO-313 · Fundamentos de programación**, con todo el material teórico de la asignatura.

---

## 🛠️ Herramientas

- **Python 3**
- **Visual Studio Code**
- **Git y GitHub**

---

## 👤 Autor

**Álvaro Martín López** · Estudiante de 1º de DAW
GitHub: [@AlvaroML19](https://github.com/AlvaroML19)
