# MARKDOWN
## Estilos de texto

Configurar en negrita: **negrita**, __negrita__ <** **> o <__ __>  
Configurar en cursiva: *cursiva* <* *>  
Configurar subrayado: This is an <ins>underlined</ins> text    
poner un comentario con ">texto"
>este es un comentario  
Asi se resalta algo `hola`  

Para poner una lista se hace de la sig manera (con 3 comillas invertidas al inicio y final del texto)
```
esta  [] 
es una   
lista   
```  
Puede crear un vínculo en línea escribiendo su texto entre corchetes [ ] y escribiendo la URL entre paréntesis ( ). También puede usar el método abreviado de teclado Command+K para crear un vínculo. Cuando haya seleccionado texto, puede pegar una dirección URL del Portapapeles para crear automáticamente un vínculo a partir de la selección.  
por ejemplo:
[(https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)] `Link para aprender mas sobre markdown ` 

# Python 
## GENERAL THEORY
### Pilares de OOP (OBJEC-ORIENTED PROGRAMMING PILLARS)
`----1.-Encapsulation----`

El encapsulamiento es el principio que permite proteger los datos y ocultar la información interna de un objeto, de manera que solo se pueda acceder a ellos a través de métodos públicos y seguros.


`Código Ejemplo encapsulamiento`
```
public:
    void deposit(double amount) {
        // Code to handle the deposit operation
        balance += amount;
    }

    void withdraw(double amount) {
        // Code to handle the withdrawal operation
        if (balance >= amount) {
            balance -= amount;
        } else {
            // Handle insufficient funds error
            // Display an error message or throw an exception
        }
    }

    double getBalance() const {
        // Code to retrieve the account balance
        return balance;
    }
};
```

`----2.-Abstraction----`

Abstraction is breaking down complex systems into manageable and reusable components to simplify them. It enables us to construct classes and objects that accurately replicate real-world entities while disregarding superfluous feature

`Code example abstraction`
```
abstract class Animal {
    abstract void hacerSonido();
}

class Perro extends Animal {
    void hacerSonido() {
        System.out.println("Guau");
    }
}

class Gato extends Animal {
    void hacerSonido() {
        System.out.println("Miau");
    }
}
```

`----3.-Inheritance----`

Inheritance creates an "is-a" relationship between classes by allowing a derived or child class to inherit characteristics from a parent or base class. This relationship allows the derived class to access and utilize the base class's properties and methods, boosting code reuse and decreasing redundancy.

`Code example inheritance`
```
# Clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

# Clase derivada
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

# Clase derivada
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Crear instancias de las clases derivadas
mi_perro = Perro("Fido")
mi_gato = Gato("Whiskers")

# Usar los métodos de las clases derivadas
print(f"{mi_perro.nombre} dice: {mi_perro.hacer_sonido()}")
print(f"{mi_gato.nombre} dice: {mi_gato.hacer_sonido()}")

```

`----4.-Polymorphism---`

Polymorphism in the context of OOP allows objects of different kinds to be treated consistently when they share a common superclass.

`Code example polymorphism`
```


class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

def hacer_sonido_animal(animal):
    print(animal.hacer_sonido())

# Crear instancias de Perro y Gato
mi_perro = Perro()
mi_gato = Gato()

# Llamar a la función con diferentes tipos de animales
hacer_sonido_animal(mi_perro)  # Salida: Guau
hacer_sonido_animal(mi_gato)   # Salida: Miau

```

## REPASO EJERCICIOS PYTHON
Ejercicio: Define una clase llamada Persona.  
Inicializa los atributos nombre y edad.  
Agrega un metodo saludar
```
class Persona: 
      
     def __init__(self,nombre, edad):
            self.nombre =nombre
            self.edad = edad
     def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

persona1= Persona("César",24)

persona1.saludar()  
``` 

```
git add -u  
esto es para agregar los cambios a la zona de preparacion  

Una vez que hayas añadido los cambios, puedes hacer un commit para registrar esos cambios:

git commit -m "Eliminados archivos innecesarios"      
  

Finalmente, si todo está listo y quieres reflejar las eliminaciones en tu repositorio remoto, puedes hacer un git push:

git push origin main

class BankAccount {
private:
    double balance;
```

### RECURSIÓN:

 Ejercicio 1 (Fácil):
Escribe una función recursiva que calcule el factorial de un número entero positivo.
```
def factorial(n):
    if n == 0 or n == 1:  # Consideramos 0! = 1 también
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Salida: 120

```

 Ejercicio 2 (Medio):
Escribe una función recursiva que invierta una cadena de texto.

```
def invertir(cadena):
    if len(cadena) <= 1:  # Condición base: si la cadena tiene 0 o 1 caracteres, se regresa igual
        return cadena
    else:
        return invertir(cadena[1:]) + cadena[0]  # Llamada recursiva con el resto de la cadena

print(invertir("python"))  # Salida: "nohtyp"
```
