# **StatPhi (Beta V1.9)**
[![Estado del Proyecto](https://img.shields.io/badge/Estado-En%20Desarrollo-blue)]()
[![Licencia](https://img.shields.io/github/license/JunixOs/app_escritorio_estadistica)]()
[![Última actualización](https://img.shields.io/github/commit-activity/w/JunixOs/app_escritorio_estadistica/develop)]()

<div style="margin: 0 auto; width: 80%; text-align: center;">
    <img src="./Images/icon.png" alt="Logo de StatPhi" width="200" style=""></img>
</div>
<br>

**StatPhi** es una aplicacion de escritorio que permite a los usuarios realizar calculos estadisiticos basados en los diferentes datos obtenidos de una investigacion estadistica a una muestra.

---

## **Tabla de Contenidos**

- [Descripcion](#descripcion)

- [Caracteristicas](#features)

- [Caracteristicas proximas](#features-to-add)

- [Estructura del proyecto](#estructura-del-proyecto)

- [Instalacion](#instalacion)

- [Guia de Uso](#guia-de-uso)

- [Autor](#autor)

- [Creditos](#creditos)

- [Licencia](#licencia)

---

## Descripcion

**StatPhi** es un programa desarrollado en el lenguaje de programacion `Python`, usando la libreria `tkinter` como base para desarrollar la UI, asi como las librerias `numpy` , `scipy`, `matplotlib`, `seaborn`, `venn`, `pandas` y `openpyxl` para los calculos, creacion de graficos e importacion y exportacion de archivos y datos.

Este proyecto es el producto final del curso de ***Estadistica General*** correspondiente al ciclo ***2025-0***, el objetivo principal del mismo es el de brindar una forma facil y amigable de calcular y analizar datos a personas que no estan familiarizadas con la programacion en lenguajes especializados para ese campo como `RStudio`.

Con **StatPhi**, podras ingresar los datos obtenidos de una investigacion y obtener informacion relevante sobre esta, como la distribucion de frecuencias , graficos y medidas de resumen. 
 
Si ingresar los datos de manera manual es un problema, o si tienes que analizar varios conjuntos de datos de golpe, tienes la posibilidad de importarlos de un archivo `.xlsx` (Excel) externo.

---

## **DEMO**
### ***Ventana Principal***
![Ventana Principal](./Images/DEMO/Principal_StatPhi.png)

### ***Crear Tabla de Frecuencias***
![Ventana Calcular Tabla de Frecuencias](./Images/DEMO/Table_Of_Frecuency/Calc_Table_Frecuences_DEMO_1.png)
<div style="margin: 0 auto; width: 80%; text-align: center;">
    <h3 style="font-size:14px;font-style:italic;">Variables Cuantitativas Agrupadas en Intervalos</h3>
    <div style="display:flex; flex-wrap:wrap; gap:15px; justify-content:center; margin-bottom:20px;">
        <img src="./Images/DEMO/Table_Of_Frecuency/Cuantitative_Grouped/Table_Frecuences.png" alt="Calculo con Variables Cuantitativas Agrupadas en Intervalos" width="200">
        <img src="./Images/DEMO/Table_Of_Frecuency/Cuantitative_Grouped/Calc_Table_Frecuences_Graph.png" alt="Grafico de las Frecuencias Obtenidas" width="200">
    </div>
    <table style="margin: 0 auto; border-collapse: collapse; width: 80%; text-align: center;">
        <tr>
            <th>Grafico de Barras para fi</th>
            <th>Grafico de Barras para hi</th>
            <th>Grafico de Barras para hi%</th>
            <th>Grafico de Pastel</th>
            <th>Grafico de Cajas</th>
        </tr>
        <tr>
            <td><img src="./Images/DEMO/Table_Of_Frecuency/Cuantitative_Grouped/Calc_Table_Frecuences_Graph_fi.png" alt="Grafico de Barras fi para Variables Cuantitativas Agrupadas en Intervalos" width="100%"></td>
            <td><img src="./Images/DEMO/Table_Of_Frecuency/Cuantitative_Grouped/Calc_Table_Frecuences_Graph_hi.png" alt="Grafico de Barras hi para Variables Cuantitativas Agrupadas en Intervalos" width="100%"></td>
            <td><img src="./Images/DEMO/Table_Of_Frecuency/Cuantitative_Grouped/Calc_Table_Frecuences_Graph_hi_percent.png" alt="Grafico de Barras hi% para Variables Cuantitativas Agrupadas en Intervalos" width="100%"></td>
            <td><img src="./Images/DEMO/Table_Of_Frecuency/Cuantitative_Grouped/Calc_Table_Frecuences_Graph_Pie.png" alt="Grafico de Pastel para Variables Cuantitativas Agrupadas en Intervalos" width="100%"></td>
            <td><img src="./Images/DEMO/Table_Of_Frecuency/Cuantitative_Grouped/Calc_Table_Frecuences_Graph_Box.png" alt="Grafico de Cajas para Variables Cuantitativas Agrupadas en Intervalos" width="100%"></td>
        </tr>
    </table>
    <h3 style="font-size:14px;font-style:italic;">Variables Cuantitativas Sin Agrupar en Intervalos</h3>
    <div style="display:flex; flex-wrap:wrap; gap:15px; justify-content:center; margin-bottom:20px;">
        <img src="./Images/DEMO/Table_Of_Frecuency/Cuantitative_Not_Grouped/Table_Frecuences.png" alt="Calculo con Variables Cuantitativas Sin Agrupar en Intervalos" width="200">
        <img src="./Images/DEMO/Table_Of_Frecuency/Cuantitative_Not_Grouped/Calc_Table_Frecuences_Graph.png" alt="Grafico de las Frecuencias Obtenidas" width="200">
    </div>
    <table style="margin: 0 auto; border-collapse: collapse; width: 80%; text-align: center;">
        <tr>
            <th>Grafico de Barras para fi</th>
            <th>Grafico de Barras para hi</th>
            <th>Grafico de Barras para hi%</th>
            <th>Grafico de Pastel</th>
            <th>Grafico de Cajas</th>
        </tr>
        <tr>
            <td><img src="./Images/DEMO/Table_Of_Frecuency/Cuantitative_Not_Grouped/Calc_Table_Frecuences_Graph_fi.png" alt="Grafico de Barras fi para Variables Cuantitativas Sin Agrupar en Intervalos" width="100%"></td>
            <td><img src="./Images/DEMO/Table_Of_Frecuency/Cuantitative_Not_Grouped/Calc_Table_Frecuences_Graph_hi.png" alt="Grafico de Barras hi para Variables Cuantitativas Sin Agrupar en Intervalos" width="100%"></td>
            <td><img src="./Images/DEMO/Table_Of_Frecuency/Cuantitative_Not_Grouped/Calc_Table_Frecuences_Graph_hi_percent.png" alt="Grafico de Barras hi% para Variables Cuantitativas Sin Agrupar en Intervalos" width="100%"></td>
            <td><img src="./Images/DEMO/Table_Of_Frecuency/Cuantitative_Not_Grouped/Calc_Table_Frecuences_Graph_Pie.png" alt="Grafico de Pastel para Variables Cuantitativas Sin Agrupar en Intervalos" width="100%"></td>
            <td><img src="./Images/DEMO/Table_Of_Frecuency/Cuantitative_Not_Grouped/Calc_Table_Frecuences_Graph_Box.png" alt="Grafico de Cajas para Variables Cuantitativas Sin Agrupar en Intervalos" width="100%"></td>
        </tr>
    </table>
    <h3 style="font-size:14px;font-style:italic;">Variables Cualitativas</h3>
    <div style="display:flex; flex-wrap:wrap; gap:15px; justify-content:center; margin-bottom:20px;">
        <img src="./Images/DEMO/Table_Of_Frecuency/Cualitative/Table_Frecuences.png" alt="Calculo con Variables Cualitativas" width="200">
        <img src="./Images/DEMO/Table_Of_Frecuency/Cualitative/Calc_Table_Frecuences_Graph.png" alt="Grafico de las Frecuencias Obtenidas" width="200">
    </div>
    <table style="margin: 0 auto; border-collapse: collapse; width: 80%; text-align: center;">
        <tr>
            <th>Grafico de Barras para fi</th>
            <th>Grafico de Barras para hi</th>
            <th>Grafico de Barras para hi%</th>
            <th>Grafico de Pastel</th>
        </tr>
        <tr>
            <td><img src="./Images/DEMO/Table_Of_Frecuency/Cualitative/Calc_Table_Frecuences_Graph_fi.png" alt="Grafico de Barras fi para Variables Cualitativas" width="100%"></td>
            <td><img src="./Images/DEMO/Table_Of_Frecuency/Cualitative/Calc_Table_Frecuences_Graph_hi.png" alt="Grafico de Barras hi para Variables Cualitativas" width="100%"></td>
            <td><img src="./Images/DEMO/Table_Of_Frecuency/Cualitative/Calc_Table_Frecuences_Graph_hi_percent.png" alt="Grafico de Barras hi% para Variables Cualitativas" width="100%"></td>
            <td><img src="./Images/DEMO/Table_Of_Frecuency/Cualitative/Calc_Table_Frecuences_Graph_Pie.png" alt="Grafico de Pastel para Variables Cualitativas" width="100%"></td>
        </tr>
    </table>
    <h3 style="font-size:14px;font-style:italic;">Datos Importados de un Excel</h3>
    <img src="./Images/DEMO/Table_Of_Frecuency/Imported_Data_From_Excel/Calc_Table_Frecuences_Window_Import_Excel.png" alt="Ventana de Importacion de Datos de un Excel" style="margin-bottom:20px;">
    <div style="display:flex; flex-wrap:wrap; gap:15px; justify-content:center; margin-bottom:20px;">
        <img src="./Images/DEMO/Table_Of_Frecuency/Imported_Data_From_Excel/Calc_Table_Frecuences_Excel_Prev.png" alt="Previsualizacion de un Excel" width="200">
        <img src="./Images/DEMO/Table_Of_Frecuency/Imported_Data_From_Excel/Calc_Table_Frecuences_Sucess_Import.png" alt="Importar Datos de un Excel" width="200">
        <img src="./Images/DEMO/Table_Of_Frecuency/Imported_Data_From_Excel/Table_Frecuences.png" alt="Tabla Para Multiples Variables de un Excel" width="200">
        <img src="./Images/DEMO/Table_Of_Frecuency/Imported_Data_From_Excel/Calc_Table_Frecuences_Graph.png" alt="Grafico Para Multiples Variables de un Excel" width="200">
    </div>
</div>

---

### ***Crear Diagramas de Venn***
![Ventana Crear Diagramas de Venn](./Images/DEMO/Venn_Diagram/Calc_Venn_Diagram_DEMO_1.png)
---
<table style="margin: 0 auto;">
    <tr>
        <th>Para datos ingresados manualmente</th>
        <th>Para datos importados de un excel</th>
    </tr>
    <tr>
        <td><img src="./Images/DEMO/Venn_Diagram/Calc_Venn_Diagram_DEMO_2_Data_From_Input.png" alt="Crear diagrama de Venn para datos ingresados manualmente"></img></td>
        <td><img src="./Images/DEMO/Venn_Diagram/Calc_Venn_Diagram_DEMO_2_Imported_Data_Diagram.png" alt="Crear diagrama de Venn para datos importados de un excel"></img></td>
    </tr>
</table>

### ***Calcular Tamaño de Muestra***
![Ventana Calcular Tamaño de Muestra](./Images/DEMO/MAS/MAS_Calc_DEMO_1.png)
<table style="margin: 0 auto;">
    <tr>
        <th>Calculo de Tamaño de Muestra para una Poblacion Finita</th>
        <th>Calculo de Tamaño de Muestra para una Poblacion Infinita</th>
    </tr>
    <tr>
        <td><img src="./Images/DEMO/MAS/MAS_Calc_DEMO_2_Finite_Population.png" alt="Calculo de Tamaño de Muestra para una Poblacion Finita"></img></td>
        <td><img src="./Images/DEMO/MAS/MAS_Calc_DEMO_2_Infinite_Population.png" alt="Calculo de Tamaño de Muestra para una Poblacion Infinita"></img></td>
    </tr>
</table>

---

## **Caracteristicas**
Algunas caracteristicas importantes de StatPhi son:
* Interfaz sencilla y amigable.

* Calculo de tablas de frecuencias usando variables cualitativas y cuantitativas, con la posibilidad de agrupar los datos cuantitativos en intervalos.

* Generacion de un archivo Excel con la tabla de frecuencias generada.

* Generacion de graficos para la distribucion de frecuencias en baja o alta calidad (hasta 2000 DPI).

* Carga de datos de un archivo excel externo.

* Calculo de diagramas de Venn.

* Calculo de tamaño de muestra por medio del Muestreo Aleatorio Simple (M.A.S.).

---

## **Caracteristicas proximas**
✅ Posibilidad de importar datos de un Excel.

✅ Calculo de cuantiles.

✅ Visualizacion de grafico de frecuencias.

✅ Creacion de Diagramas de Venn.

⬜ Creacion y exportacion de multiples graficos en una sola imagen.

⬜ Importacion de datos de archivos .csv .txt .sql

⬜ Implementacion de librerias para acelerar la importacion y analisis de miles de datos.


---

## **Estructura del proyecto**
El proyecto tiene la siguiente estructura de carpetas:
```bash
Statphi/
├── Calcs/
│   ├── Imports/
│   │   └── Import_Data_From_Excel.py
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
│   │   ├── Summary_Measures/
│   │   │   ├── Calc_For_Grouped_Data.py
│   │   │   └── Calc_For_Not_Grouped_Data.py
│   │   └── Calc_Values_Tables.py
│   ├── Venn/
│   │   ├── Calc_Venn_Diagram.py
│   │   └── Export_Venn_Diagram.py
│   └── Center_Window.py
├── Exceptions/
│   └── Exception_Warning.py
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
│   │   └── Window_Show_Graph.py
│   ├── Venn_Diagram/
│   │   ├── Window_Create_Venn_Diagram.py
│   │   └── Window_Export_Venn_Diagram.py
│   ├── Main_Window.py
│   ├── Window_Create_Multiple_Graphs.py
│   ├── Window_Import_Excel.py
│   └── Window_Progress_Bar.py
├── Path_Manager.py
├── .gitignore
└── README.md
```

## **Instalacion**

Por el momento, no esta disponible un ejecutable que facilite su instalacion y uso, esto debido a que el proyecto todavia esta en fase de construccion y pruebas.

### ***Requisitos previos***
 Si deseas probar StatPhi en tu ordenador, deberas tener intalado los siguientes programas:
- Un editor de codigo como `VSCode`.
- `Python 3.11.X`
- El sistema de control de versiones de `git`.

### ***Librerias Necesarias***
Ademas, deberas contar con las siguientes librerias de **python**:
1. `tkinter`
2. `pandas 2.2.3`
3. `matplotlib 3.10.0`
4. `openpyxl 3.1.5`
5. `scipy 1.15.1`
6. `seaborn 0.13.2`
7. `venn 0.1.3`

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
    ```

4. Activar el entorno virtual:
    ```bash
    .\venv\Scripts\activate
    ```

5. Instalar las librerias necesarias.
    - Usando `pip`:
        ```bash
        pip install tkinter pandas==2.2.3 matplotlib==3.10.0 openpyxl==3.1.5 scipy==1.15.1 seaborn==0.13.2 venn==0.1.3
        ```
    - Usando `conda`:
        ```bash
        conda install tkinter pandas=2.2.3 matplotlib=3.10.0 openpyxl=3.1.5 scipy=1.15.1 seaborn=0.13.2 venn=0.1.3
        ```
6. Verificar si los paquetes se instalaron correctamente:
    - Usando `pip`:
        ```bash
        pip list
        ```
    - Usando `conda`:
        ```bash
        conda list
        ```

7. Ejecutar el programa:
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
    Aqui puedes ingresar datos de manera manual, para un calculo correcto y sin errores, asegurate de separar cada uno de los datos por un espacio y de usar puntos decimales en lugar de comas. Por favor, use este campo solo para introducir pocos valores, de lo contrario el programa se congelara. Si desea introducir muchos datos es recomendable importarlos de un excel.

- **Precision**:
    Permite ajustar la cantidad de decimales que se mostraran en valores como las Medidas de Resumen , los Quantiles , Deciles , Percentiles , la Frecuencia Relativa (hi) , la Frecuencia Relativa Acumulada (Hi) y sus respectivos valores porcentuales (hi% y Hi%).

- **Importar datos**:
    Permite importar datos de una o varias columnas de un archivo `.xlsx` externo. Para ello, sigue los siguientes pasos:
    
    1. Selecciona la ubicacion de tu archivo Excel con los datos a importar. Posteriormente, se cargara tu archivo en la parte superior de la ventana a modo de previsualizacion.

    2. Una vez cargado tu archivo, selecciona el rango de celdas que contienen tus datos, algunos ejemplos de como seleccionar los datos son:
        - *Para una sola columna de datos*: `A1:A1001`

        - *Para multiples columnas de datos consecutivas*: `A1:C1001`

        - *Para multiples columnas de datos no consecutivas*: `A1:C1001;E1:E1001;G1:H1001`

        - *Para una o multiples columnas de datos de diferente tamaño*: `A1:A300;B1:B500;C1:D100`

    4. Finalmente, si no ocurre ningun error, podras ver los datos seleccionados en el cuadro de previsualizacion y en la ventana de calculo. Si lo deseas puedes salir de la ventana de importacion o corregir la seleccion actual.
> [!WARNING]
> Evite ingresar rangos de celdas como A1:C1001;B1:D1001.

> [!TIP]
> Para evitar errores de importacion, por favor asegurese de que el formato de los datos sea el adecuado, que no existan celdas vacias dentro del rango de celdas a exportar y que todo tu dataset se encuentre en la primera fila del excel.

- **Calcular Tabla**: Una vez que hayas introducido los datos manualmente o que los hayas importado de un excel, podras calcular la tabla de frecuencias junto con las demas medidas de resumen. 

- **Exportar Tabla a Excel**: Esta opcion es util cuando quieres tener algo mas estetico y personalizable que el cuadro que se muestra en el programa. Si tuvieras varias tablas de frecuencias, puedes seleccionar cuales exportar marcando su casilla correspondiente.

- **Mostrar Grafico**:
    Ofrece la posibilidad de ver los graficos para la tabla de frecuencias actual. Los graficos que podras ver son:
    - *Grafico de Barras para la Frecuencia Absoluta Simple*
    - *Grafico de Barras para la Frecuencia Relativa Simple*
    - *Grafico de Barras para la Frecuencia Relativa Simple Porcentual*
    - *Grafico de pastel*
    - *Grafico de Cajas*

    Si anteriormente importaste datos de multiples columnas de un Excel usando la opcion de `Importar datos`,
    podras elegir de que variable ver los graficos.

    Dentro de la ventana de visualizacion de graficos estara disponible la opcion de exportar los graficos como imagenes.

    - ***Exportar Graficos***: Permite exportar los graficos antes vistos en el apartado `Mostrar Grafico` como imagenes a su computadora, para que puedan ser usados en documentos de Word, PDF, entre otros.

        Dentro de esta ventana encontraras los siguientes elementos:
        -  ***Nombre de la Imagen***: Permite colocar un nombre a la imagen a exportar, es opcional, este nombre se aplica a todas las imagenes exportadas.

        - ***Formato***: Es una pequeña caja con 3 opciones de formato posibles .jpg .png y .svg

        - ***Ruta de Exportacion***

        - ***Resolucion (DPI)***: Las resoluciones DPI disponibles son de:

            - *72 DPI*: Baja resolución, se utiliza para borradores o documentos que no requieren alta calidad.

            - *96 DPI*: Es una resolución comúnmente utilizada para mostrar imágenes en pantallas de computadora o en la web.

            - *150 DPI*: Es una resolución adecuada para impresiones de documentos simples, como reportes o borradores. Aunque no es lo ideal para imágenes de alta calidad, es suficiente para texto y gráficos básicos.

            - *300 DPI*: Alta Resolucion, es la resolución estándar para imprimir documentos de buena calidad, como folletos, carteles, libros, y fotografías. Es el estándar para impresiones comerciales y fotográficas de calidad.

            - *600 DPI*: Es una resolución excelente para impresoras que necesitan detalles más finos y mayor precisión en las imágenes.

            - *1200 DPI*: Permite la impresión de texto extremadamente pequeño y detalles en gráficos, lo que resulta útil cuando los informes o diagramas incluyen notas, cifras o ecuaciones que necesitan ser legibles con alta precisión.

            - *2000 DPI*: Ultra Alta Resolucion, para impresión ultra detallada y trabajos artísticos de alta precisión.

            Ten en cuenta que exportar graficos con una resolucion alta toma mas tiempo.

        - ***Seleccion de Graficos a Exportar***: Permite elegir si exportar algunos graficos o todos.

        - ***Nombre de los Graficos***: Permite colocar un titulo que describa mejor el grafico a exportar, dependiendo de que graficos exportes podras colocar un nombre al grafico de barras, de pastel y de cajas.
        Si no colocas ningun nombre, el grafico se exportara sin un titulo.
---

#### ***Calculo de Diagramas de Venn***
Aqui te encontraras con los siguientes elementos:
- **Campos de texto**: Aqui puedes introducir los datos correspondientes a cada conjunto, el nombre de cada conjunto va de A hasta F, solo se pueden ingresar como maximo datos para 6 conjuntos. Si se cuenta con muchos datos es mejor importarlos de un excel y no importarlos manualmente ya que podria congelar el programa.

- **Importar Datos**: Permite importar datos de una o varias columnas de un archivo `.xlsx` externo. Su funcionamiento es similar a la detallada en el apartado `Calculo de Tablas de Frecuencias`, con la unica diferencia de que solo podras importar de 2 a 6 columnas de datos.

- **Generar diagrama**: Una vez que hayas introducido los datos manualmente o que los hayas importado de un excel, podras generar el diagrama de Venn.

- **Exportar grafico**: Permite exportar los graficos a su computadora, para que puedan ser usados en documentos de Word, PDF, entre otros. Dentro de esta ventana encontraras los siguientes elementos:
    - ***Nombre de la imagen***:

    - ***Ruta de exportacion***

    - ***Resolucion (DPI)***: Las resoluciones disponibles son de 72 , 96 , 150 , 300 , 600 , 1200 y 2000 DPI, todas cumpliendo las mismas caracteristicas detalladas en `Exportar Graficos` dentro del apartado de  `Calculo de Tablas de Frecuencias`.

    - ***Titulo para el diagrama de Venn***: Permite colocar un titulo que describa mejor el grafico a exportar. Si no se coloca uno, el grafico se exportara sin un titulo.

---

#### ***Calculo de Tamaño de Muestra por M.A.S.***
Aqui te encontraras con los siguientes elementos:
- **Seleccion de tipo de poblacion**: Permite especificar el tamaño de la poblacion a investigar, si es finita (Cantidad Conocida) o infinita (Cantidad no conocida).

- **Poblacion (N)**: Si la poblacion a añalizar es finita, podras ingresar el tamaño de la poblacion del cual se calculara el tamaño de muestra.

- **Nivel de Confianza (1 - α)**: Corresponde al valor crítico de la distribución normal estándar que se utiliza para calcular el intervalo de confianza.

- **Probabilidad de Exito (p)**: Proporción estimada de la población con una característica específica (si no se conoce, se puede asumir 0.5 para maximizar la muestra).

- **Error (e)**: Margen de error permitido.

- **Muestreo Inicial (n_o)**: Resulta de aplicar la formula de Muestreo Aleatorio Simple (para poblaciones finitas o conocidas), para poblaciones grandes este valor puede ser proporcionalmente grande, brindando un tamaño de muestra aproximado. 

- **Muestreo Final Corregido (n_f)**: Es el resultado de dividir el Muestreo Inicial entre 1 mas el Factor de Correccion el cual es igual al Muestreo Inicial sobre el tamaño de la poblacion. Este valor proporciona un tamaño de poblacion mas razonable comparado con el tamaño del Muestreo Inicial. Este valor solo es calculable con un tamaño de muestra finita o conocida.

---

## **Autor**
Programa desarrollado por [JunixOs](https://github.com/JunixOs)

---

## **Creditos**
- Asesoramiento en temas de Estadistica de `Bremudez Pino, Wilmer Julio`. Contacto: `+51 952 846 248`.

- Asesoramiento en el codigo, estructura del proyecto y uso de gitflow de [paultb3](https://github.com/paultb3).

- Codigos para la importacion de datos de un excel, creacion de graficos de frecuencias y calculo de tamaño de muestra por M.A.S. extraidos y adaptados de los repositorios de [paultb3](https://github.com/paultb3).

---

## **Licencia**

Este proyecto está bajo la Licencia GNU GPLv3 - consulta el archivo [LICENSE](./LICENSE) para más detalles.

---