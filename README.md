# **StatPhi (Beta V1.8)**
[![Estado del Proyecto](https://img.shields.io/badge/Estado-En%20Desarrollo-blue)]()
[![Licencia](https://img.shields.io/github/license/JunixOs/app_escritorio_estadistica)]()
[![Última actualización](https://img.shields.io/github/commit-activity/w/JunixOs/app_escritorio_estadistica/develop)]()

<div style="display:flex;justify-content:center;border-radius:50%;margin: 0 auto;">
    <img src="./Images/icon.png" alt="Logo de StatPhi" width="200" style=""></img>
</div>
<br>

**StatPhi** es una aplicacion de escritorio que permite a los usuarios realizar calculos estadisiticos basados en los diferentes datos obtenidos de una investigacion estadistica a una muestra.

---

## **Tabla de Contenidos**

- [Descripcion](#descripcion)
- [Licencia](#licencia)
- [Caracteristicas](#features)
- [Caracteristicas proximas](#features-to-add)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Instalacion](#instalacion)
- [Guia de Uso](#guia-de-uso)

---
## Licencia

Este proyecto está bajo la Licencia GNU GPLv3 - consulta el archivo [LICENSE](./LICENSE) para más detalles.

---

## Descripcion

**StatPhi** es un programa desarrollado en el lenguaje de programacion `Python`, usando la libreria `tkinter` como base para desarrollar la UI, asi como la libreria `numpy`, `pandas`, `matplotlib` y `openpyxl` para los calculos, exportacion e importacion de archivos y datos.

Este proyecto es el producto final del curso de ***Estadistica General*** correspondiente al ciclo ***2025-0*** el cual tiene por objetivo brindar una forma facil y amigable de calcular y analizar datos a personas que no estan familiarizadas con software avanzado como RStudio.

Con **StatPhi**, podras ingresar los datos obtenidos de una investigacion y obtener informacion relevante sobre esta, como la distribucion de frecuencias , graficos y medidas de resumen. 
 
Tienes la posibilidad de ingresar datos por tu cuenta, o de importarlos de un archivo `.xlsx` (Excel) externo.
Al importar multiples columnas de un archivo `.xlsx` y al calcular la tabla de frecuencias y las medidas de resumen de cada una, tendras la posibilidad de visualizar los resultados por separado, ademas de que podras exportar solo las tablas y los graficos que consideres necesarios.

---

## **DEMO**
### ***Ventana Principal***
![Ventana Principal](./Images/DEMO/Principal_StatPhi.png)

### ***Crear Tabla de Frecuencias***
![Ventana Calcular Tabla de Frecuencias](./Images/DEMO/Calc_Table_Frecuences_DEMO_1.png)
<div style="margin:0 auto;">
    <h3 style="text-align:center;font-size:14px;font-style:italic;">Variables Cuantitativas</h3>
    <div style="display:flex; flex-wrap:wrap;gap:15px;justify-content:center">
        <img src="./Images/DEMO/Calc_Table_Frecuences_DEMO_2_Cuantitative_Table.png" alt="Calculo con Variables Cuantitativas" width="200"></img>
        <img src="./Images/DEMO/Calc_Table_Frecuences_DEMO_2_Cuantitative_Graph.png" alt="Grafico de las Frecuencias Obtenidas" width="200"></img>
        <table>
            <tr>
                <th>Grafico de Barras para fi</th>
                <th>Grafico de Barras para hi</th>
                <th>Grafico de Barras para hi%</th>
                <th>Grafico de Pastel</th>
                <th>Grafico de Cajas</th>
            <tr>
            <tr>
                <td><img src="./Images/DEMO/Calc_Table_Frecuences_DEMO_2_Cuantitative_Graph_fi.png" alt="Grafico de Barras fi para Variables Cuantitativas"></img></td>
                <td><img src="./Images/DEMO/Calc_Table_Frecuences_DEMO_2_Cuantitative_Graph_hi.png" alt="Grafico de Barras hi para Variables Cuantitativas"></img></td>
                <td><img src="./Images/DEMO/Calc_Table_Frecuences_DEMO_2_Cuantitative_Graph_hi_percent.png" alt="Grafico de Barras hi% para Variables Cuantitativas"></img></td>
                <td><img src="./Images/DEMO/Calc_Table_Frecuences_DEMO_2_Cuantitative_Graph_Pie.png" alt="Grafico de Pastel para Variables Cuantitativas"></img></td>
                <td><img src="./Images/DEMO/Calc_Table_Frecuences_DEMO_2_Cuantitative_Graph_Box.png" alt="Grafico de Cajas para Variables Cuantitativas"></img></td>
            </tr>
        </table>
    </div>
    <h3 style="text-align:center;font-size:14px;font-style:italic;">Variables Cualitativas</h3>
    <div style="display:flex; flex-wrap:wrap;gap:15px;justify-content:center">
        <img src="./Images/DEMO/Calc_Table_Frecuences_DEMO_2_Cualitative_Table.png" alt="Calculo con Variables Cualitativas" width="200"></img>
        <img src="./Images/DEMO/Calc_Table_Frecuences_DEMO_2_Cualitative_Graph.png" alt="Grafico de las Frecuencias Obtenidas" width="200"></img>
        <table>
            <tr>
                <th>Grafico de Barras para fi</th>
                <th>Grafico de Barras para hi</th>
                <th>Grafico de Barras para hi%</th>
                <th>Grafico de Pastel</th>
            </tr>
            <tr>
                <td><img src="./Images/DEMO/Calc_Table_Frecuences_DEMO_2_Cualitative_Graph_fi.png" alt="Grafico de Barras fi para Variables Cualitativas"></img></td>
                <td><img src="./Images/DEMO/Calc_Table_Frecuences_DEMO_2_Cualitative_Graph_hi.png" alt="Grafico de Barras fi para Variables Cualitativas"></img></td>
                <td><img src="./Images/DEMO/Calc_Table_Frecuences_DEMO_2_Cualitative_Graph_hi_percent.png" alt="Grafico de Barras fi para Variables Cualitativas"></img></td>
                <td><img src="./Images/DEMO/Calc_Table_Frecuences_DEMO_2_Cualitative_Graph_Pie.png" alt="Grafico de Barras fi para Variables Cualitativas"></img></td>
            </tr>
        </table>
    </div>
    <h3 style="text-align:center;font-size:14px;font-style:italic;">Datos Importados de un Excel</h3>
    <img src="./Images/DEMO/Calc_Table_Frecuences_DEMO_3_ImportDataFromExcel.png" alt="Ventana de Importacion de Datos de un Excel"></img>
    <div style="display:flex; flex-wrap:wrap;gap:15px;justify-content:center">
        <img src="./Images/DEMO/Calc_Table_Frecuences_DEMO_3_ImportDataFromExcel_Prev.png" alt="Previsualizacion de un Excel" width="200"></img>
        <img src="./Images/DEMO/Calc_Table_Frecuences_DEMO_3_ImportDataFromExcel_Import.png" alt="Importar Datos de un Excel" width="200"></img>
        <img src="./Images/DEMO/Calc_Table_Frecuences_DEMO_3_ImportDataFromExcel_Table.png" alt="Tabla Para Multiples Variables de un Excel" width="200"></img>
        <img src="./Images/DEMO/Calc_Table_Frecuences_DEMO_3_ImportDataFromExcel_Graph.png" alt="Grafico Para Multiples Variables de un Excel" width="200"></img>
    </div>
</div>

---

### ***Calcular Tamaño de Muestra***
![Ventana Calcular Tamaño de Muestra](./Images/DEMO/MAS_Calc_DEMO_1.png)
<table style="margin: 0 auto;">
    <tr>
        <th>Calculo de Tamaño de Muestra para una Poblacion Finita</th>
        <th>Calculo de Tamaño de Muestra para una Poblacion Infinita</th>
    </tr>
    <tr>
        <td><img src="./Images/DEMO/MAS_Calc_DEMO_2_Finite_Population.png" alt="Calculo de Tamaño de Muestra para una Poblacion Finita"></img></td>
        <td><img src="./Images/DEMO/MAS_Calc_DEMO_2_Infinite_Population.png" alt="Calculo de Tamaño de Muestra para una Poblacion Infinita"></img></td>
    </tr>
</table>

---

## **Caracteristicas**
Algunas caracteristicas importantes de StatPhi son:
* Trabaja con variables cuantitativas y cualitativas.

* Posibilidad de importar datos de un archivo Excel (.xlsx) externo, correspondientes a una o varias columnas.

* Obten un archivo Excel con las tablas de frecuencias generada.

* Muestra un grafico sobre la distribucion de frecuencias.

* Obten las imagenes de los graficos en baja o alta calidad (hasta 1200 DPI).

---

## **Caracteristicas proximas**
- [x] Posibilidad de importar multiples columnas de un Excel.

- [x] Calculo de cuantiles.

- [x] Visualizacion de grafico de cajas.

- [ ] Creacion de Diagramas de Venn.

- [ ] Creacion y exportacion de multiples graficos en una sola imagen.

- [ ] Importacion de datos de archivos .csv .txt .sql

- [ ] Implementacion de librerias para acelerar la importacion y analisis de miles de datos.


---

## **Estructura del proyecto**
El proyecto tiene la siguiente estructura de carpetas
```bash
Statphi/
├── Calcs/
│   ├── MAS/
│   │   └── MAS_Calc.py
│   ├── Table_of_Frecuency/
│   │   ├── Exports/
│   │   │   ├── Export_Excel.py
│   │   │   └── Export_Graph.py
│   │   ├── Frecuences/
│   │   │   ├── Calc_Frecuences_Cualitative.py
│   │   │   ├── Calc_Frecuences_Cuantitative_Grouped.py
│   │   │   └── Calc_Frecuences_Cuantitative_Not_Grouped.py
│   │   ├── Graphs/
│   │   │   ├── Calc_Bar_Pie_Graphs.py
│   │   │   ├── Calc_Boxplot.py
│   │   │   └── Calc_Multiple_Graphs.py
│   │   ├── Quantiles/
│   │   │   └── Quantil.py
│   │   ├── Summary_Measures/
│   │   │   ├── Calc_For_Grouped_Data.py
│   │   │   └── Calc_For_Not_Grouped_Data.py
│   │   └── Calc_Values_Tables.py
│   ├── Venn/
│   │   └── Calc_Venn_Diagram.py
│   └── Center_Window.py
├── Images/
│   ├── DEMO/
│   ├── icon.png
│   └── normal_distribution.png
├── Views/
│   ├── MAS/
│   │   └── Window_MAS.py
│   ├── Table_of_Frecuency/
│   │   ├── Window_Calc_Table_of_Frecuency.py
│   │   ├── Window_Export_Excel.py
│   │   ├── Window_Export_Graph.py
│   │   ├── Window_Import_Excel.py
│   │   └── Window_Show_Graph.py
│   ├── Venn_Diagram/
│   │   └── Window_Create_Venn_Diagram.py
│   ├── Main_Window.py
│   ├── Window_Create_Multiple_Graphs.py
│   └── Window_Progress_Bar.py
├── .gitignore
└── README.md
```

## **Instalacion**

Por el momento, no esta disponible un ejecutable que facilite su instalacion y uso, esto debido a que el proyecto todavia esta en fase de construccion y pruebas.

### ***Requisitos previos***
 Si deseas probar StatPhi en tu ordenador, deberas tener intalado los siguientes programas:
- Un editor de codigo como `VSCode`.
- `Python 3.11.X`
- El sistema de control de versiones de `GIT`.

### ***Librerias Necesarias***
Ademas, deberas contar con las siguientes librerias de **python** (puedes usar `pip` o `conda`),
1. `tkinter`
2. `pandas 2.2.3`
3. `matplotlib 3.10.0`
4. `openpyxl 3.1.5`
5. `scipy 1.15.1`

> [!WARNING]
> Si ya tienes librerias instaladas, es recomendable crear un entorno virtual para evitar conflictos con las diferentes librerias de tu sistema.

### ***Pasos para la Instalacion***
1. Clonar el repositorio.
    ```bash
    https://github.com/JunixOs/app_escritorio_estadistica.git
    ```
2. Navegar hasta el directorio app_escritorio_estadistica:
    ```bash
    cd app_escritorio_estadistica
    ```

3. Crear el entorno virtual. Si no sabes como, ingresa los siguientes comandos dentro de la terminal:
    ```bash
    python -m venv nombre_del_entorno
    python -m venv venv
    ```

4. Activar el entorno virtual:
    ```bash
    .\venv\Scripts\activate
    ```

5. Instalar las librerias necesarias.

6. Ejecutar el programa con el comando:
    ```bash
    python .\Windows\Main_Window.py
    ```

---

## **Guia de Uso**
### ***Pantalla de Inicio***

En la pantalla de inicio te encontraras con dos botones, uno para dirigirte a la seccion de calculo de tablas de frecuencias y otro para abrir una pequeña ventana donde podras calcular el tamaño de muestra usando el Muestreo Aleatorio Simple.

#### ***Calculo de Tablas de Frecuencias***

Aqui te encontraras con los siguientes elementos:
- **Campo de texto**: 
    Aqui puedes ingresar datos de manera manual, para un calculo correcto y sin errores, asegurate de separar cada uno de los datos por un espacio y de usar puntos decimales en lugar de comas.

- **Precision**:
    Permite ajustar la cantidad de decimales que se mostraran en valores como las Medidas de Resumen , los Quantiles , Deciles , Percentiles , la Frecuencia Relativa (hi) , la Frecuencia Relativa Acumulada (Hi) y sus respectivos valores porcentuales (hi% y Hi%).

- **Importar datos**:
    Permite importar datos de una o varias columnas de un archivo `.xlsx` externo. Para ello, sigue los siguientes pasos:
    
    1. Primero selecciona la ubicacion de tu archivo Excel con los datos a importar.
    2. Posteriormente, se cargara tu archivo en la parte superior de la ventana a modo de previsualizacion.
    3. Una vez cargado tu archivo, selecciona el rango de celdas que contienen tus datos, algunos ejemplos de como seleccionar los datos son:
        - *Para una sola columna de datos*: `A1:A1001`

        - *Para multiples columnas de datos consecutivas*: `A1:C1001`

        - *Para multiples columnas de datos no consecutivas*: `A1:C1001;E1:E1001;G1:H1001`

    4. Finalmente, si no ocurre ningun error, podras ver los datos seleccionados en el cuadro de previsualizacion y en la ventana de calculo. Si lo deseas puedes salir de la ventana de importacion o corregir la seleccion actual.
> [!WARNING]
> Evite ingresar rangos de celdas como A1:C1001;B1:D1001.

> [!CAUTION]
> Dentro del Excel con los datos a importar, asegurese de que el formato de los datos sea correcto, que cada columna de datos cuente un nombre y que los datos se encuentren en la primera fila.

- **Mostrar Grafico**:

---

#### ***Calculo de Diagramas de Venn***

---

#### ***Calculo de Tamaño de Muestra por M.A.S.***
Aqui te encontraras con los siguientes elementos:
- **Seleccion de tipo de poblacion**: Permite especificar el tamaño de la poblacion a investigar, si es finita (Cantidad Conocida) o infinita (Cantidad no conocida).

- **Poblacion (N)**: Si la poblacion a añalizar es finita, podras ingresar el tamaño de la poblacion del cual se calculara el tamaño de muestra.

- **Nivel de Confianza (1 - α)**:

- **Probabilidad de Exito (p)**:

- **Error (e)**:

- **Muestreo Inicial (n_o)**:

- **Muestreo Final Corregido (n_f)**:

---