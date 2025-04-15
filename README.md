# TP2 - ACSO

## Ejecución con Docker

Este proyecto incluye configuración de Docker para asegurar un entorno de desarrollo y ejecución consistente.

### Requisitos previos

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Scripts disponibles

1. **Ejecutar tests en Docker**

   ```bash
   ./run-docker-tests.sh
   ```

   Este script construye la imagen Docker y ejecuta las pruebas del ejercicio 1 automáticamente.

2. **Ingresar a una shell interactiva en el contenedor**

   ```bash
   ./run-docker-shell.sh
   ```

   Este script inicia una sesión interactiva en el contenedor donde puedes ejecutar comandos manualmente.

### Comandos útiles dentro del contenedor

Una vez dentro del contenedor, puedes ejecutar:

```bash
# Navegar al directorio del ejercicio 1
cd ej1

# Compilar el ejercicio
make

# Ejecutar pruebas cortas
./runMain.sh

# Ejecutar pruebas completas
./runTester.sh
```

### Ejecución manual con Docker

También puedes ejecutar comandos individuales directamente con Docker:

```bash
# Construir la imagen
docker build --platform linux/amd64 -t tp2-acso .

# Iniciar una shell interactiva montando el directorio actual
docker run -it --platform linux/amd64 -v "<ruta-absoluta-del-proyecto>:/app" tp2-acso
```

(PARA MI CASO: docker run -it --platform linux/amd64 --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -v "/Users/juanfra/Documents/Facultad/3er año - 1er Cuatri/Arq y Sist./TPS/tp2-acso":/app tp2-acso   )

## Estructura del proyecto

- **ej1/**: Contiene el código fuente del ejercicio 1
  - **ej1.c**: Implementación en C de las funciones requeridas
  - **ej1.asm**: Implementación en Assembly de las funciones requeridas
  - **ej1.h**: Definiciones de estructuras y prototipos de funciones
  - **main.c**: Código para pruebas personalizadas
  - **runTester.sh**: Script para ejecutar las pruebas completas
  - **runMain.sh**: Script para ejecutar pruebas cortas
  - **tester.c**: Implementación de las pruebas automáticas
  - **Makefile**: Configuración de compilación del proyecto
  - **salida.catedra.ej1.txt**: Salida esperada para las pruebas

## Ejercicio 1

El ejercicio 1 implementa un conjunto de funciones para manejar una lista doblemente enlazada, tanto en C como en Assembly.

### Archivos importantes

En el directorio de este ejercicio encontrarán los siguientes archivos:

- **Makefile**: Configuración para compilar el proyecto
- **ej1.asm**: Implementación en Assembly de las funciones requeridas
- **ej1.c**: Implementación en C de las funciones requeridas
- **ej1.h**: Definiciones de estructuras y prototipos de funciones
- **main.c**: Archivo para pruebas personalizadas
- **runMain.sh**: Script para ejecutar pruebas cortas
- **runTester.sh**: Script para ejecutar pruebas completas
- **tester.c**: Implementación de las pruebas automáticas
- **salida.catedra.ej1.txt**: Salida esperada para las pruebas

### Configuración C vs Assembly

El archivo **ej1.h** contiene la directiva que determina qué implementación usar:

```c
#define USE_ASM_IMPL 0  // 0 para C, 1 para Assembly
```

Para cambiar entre la implementación de C y Assembly, modifica este valor:
- `0` para usar la implementación en C
- `1` para usar la implementación en Assembly

### Compilación y ejecución

Para compilar el código:

```bash
make
```

Para ejecutar las pruebas básicas (definidas en main.c):

```bash
./runMain.sh
```

Para ejecutar las pruebas completas:

```bash
./runTester.sh
```

## Ejercicio 2

Este ejercicio está pendiente de implementación.



