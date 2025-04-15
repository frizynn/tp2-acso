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
cd TP2/src/ej1

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

- **TP2/src/ej1/**: Código fuente y scripts del ejercicio 1
  - **ej1.c**: Implementación en C de las funciones requeridas
  - **ej1.asm**: Implementación en Assembly de las funciones requeridas
  - **ej1.h**: Definiciones de estructuras y prototipos de funciones
  - **main.c**: Código para pruebas personalizadas
  - **runTester.sh**: Script para ejecutar las pruebas completas
  - **runMain.sh**: Script para ejecutar pruebas cortas
  - **tester.c**: Implementación de las pruebas automáticas
  - **Makefile**: Configuración de compilación del proyecto
  - **salida.catedra.ej1.txt**: Salida esperada para las pruebas
  - **salida.caso.propio.ej1.txt**: Salida de pruebas propias

- **TP2/src/bomb3/**: Archivos del ejercicio 2 (bomba binaria)
  - **bomb**: Ejecutable de la bomba binaria
  - **bomb.c**: Código fuente de referencia de la bomba (no modificar)
  - **palabras.txt**: Diccionario de palabras utilizado por la bomba
  - **input.txt**: Archivo de entrada con las claves para desactivar fases
  - **respuestas_descripcion.txt**: Explicación de cada fase desactivada y cómo se resolvió
  - **ID**: Identificador único del alumno
  - **gdb_refcard_gnu.pdf**: Referencia rápida de GDB
  - **.gdbinit**: Configuración recomendada para GDB
  - **bomb_disasm.txt**: Desensamblado completo del ejecutable (generado con objdump)
  - **phase1.py, phase2.py, phase3.py, phase4.py**: Scripts de apoyo para análisis de fases (si aplica)
  - **README**: Información breve de la bomba asignada

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
- **salida.caso.propio.ej1.txt**: Salida de pruebas propias

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

## Ejercicio 2: Bomba Binaria

Este ejercicio consiste en desactivar una bomba binaria mediante ingeniería inversa. La bomba está basada en un proyecto de Carnegie Mellon University y contiene varias fases que deben ser desactivadas proporcionando la entrada correcta.

### Archivos importantes

- **bomb**: Ejecutable de la bomba binaria (NO modificar)
- **bomb.c**: Código fuente de referencia (solo lectura)
- **palabras.txt**: Diccionario de palabras utilizado por la bomba
- **input.txt**: Archivo de entrada con las claves para desactivar fases (debe contener una línea por fase)
- **respuestas_descripcion.txt**: Explicación de cada fase desactivada y cómo se resolvió
- **ID**: Identificador único del alumno
- **gdb_refcard_gnu.pdf**: Referencia rápida de GDB
- **.gdbinit**: Configuración recomendada para GDB
- **bomb_disasm.txt**: Desensamblado completo del ejecutable (puede generarse con `objdump -M intel -d bomb > bomb_disasm.txt`)
- **phase1.py, phase2.py, phase3.py, phase4.py**: Scripts de apoyo para análisis de fases (opcional)

### Ejecución de la bomba

Puedes ejecutar la bomba de la siguiente manera:

```bash
cd TP2/src/bomb3
./bomb < input.txt
```

O bien, para depuración:

```bash
gdb ./bomb
# o
./bomb input.txt
```

### Entrega

Debes entregar todos los archivos proporcionados y generados en la carpeta correspondiente del repositorio. Asegúrate de incluir:
- input.txt
- respuestas_descripcion.txt
- ID
- bomb
- palabras.txt
- bomb.c
- gdb_refcard_gnu.pdf
- .gdbinit

Completa el archivo respuestas_descripcion.txt con tu nombre, email y una breve explicación de cada fase desactivada y cómo la resolviste.

---

Para dudas sobre el uso de herramientas de ingeniería inversa, consulta el enunciado y la referencia rápida de GDB incluida en el proyecto.



