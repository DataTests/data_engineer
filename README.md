Data Engineer Test
==================

1. Fork and clone this repo.

2. Start the Vagrant environment and log in.

        $ vagrant up
        $ vagrant ssh

3. Write a program to get the dataset available [here] and save it to a TSV
file. Use the tools available in the Vagrant environment. If you want to use
something else, then update this document to include the installation steps.

4. Push your code back to your fork at GitHub and submit a Pull Request to the
original repo.



[here]: https://www.random.org/integers/?num=100&min=1&max=100&col=4&base=10&format=plain&rnd=new

# Observaciones de la prueba:

Sinceramente no había utilizado Vagrant, según leí se utiliza para crear ambientes virtuales para tener todas las herramientas necesarias para realizar un proyecto. Como una caja de arena. Y debido a que no poseía mi computadora. Tomé la decisión de utilizar las herramientas que poseía actualmente.
Para llevar a cabo el objetivo de la prueba utilice únicamente python. Con la utilización de librerías para descargar la data (requests) y para hacer algunas validaciones (re).

# Instalación
Para la ejecución del código se debe descargar únicamente la librería requests:
        
        pip install requests
        
La librería re viene por defecto en la instalación de python.

# Ejecución:
Basta con ejecutar el archivo prueba.py

        python prueba.py

        
