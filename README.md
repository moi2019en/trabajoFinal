# 📊 Análisis Exploratorio de Datos - Telco Customer Churn

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📋 Descripción del Proyecto

Aplicación interactiva desarrollada en **Streamlit** para realizar un **Análisis Exploratorio de Datos (EDA)** del dataset **TelcoCustomerChurn**. El objetivo es identificar patrones asociados a la fuga de clientes (**Churn**) mediante técnicas de visualización, estadística descriptiva y análisis multivariado.

Este proyecto forma parte del **Caso de Estudio N°2** del curso **Especialización en Python for Analytics** y demuestra la aplicación práctica de conceptos fundamentales de programación, análisis de datos y desarrollo de aplicaciones web interactivas.

> **Nota:** Este proyecto NO busca desarrollar modelos predictivos, sino analizar, limpiar, transformar y visualizar los datos para comprender las causas asociadas a la fuga de clientes.

## 🎯 Objetivos del Proyecto

- ✅ Desarrollar una aplicación ejecutable con Streamlit
- ✅ Aplicar conceptos de Programación Orientada a Objetos (POO)
- ✅ Realizar análisis estadístico descriptivo completo
- ✅ Crear visualizaciones efectivas con Matplotlib y Seaborn
- ✅ Implementar análisis exploratorio estructurado en 10 ítems
- ✅ Generar insights accionables para la toma de decisiones

## 🚨 Contexto de Negocio

Durante el último mes, debido a la coyuntura del COVID-19, la empresa incrementó su ratio de fuga de clientes en **+0.5 puntos porcentuales**, pasando de 2% en promedio a 2.5%.

**Dato clave:** El costo de adquirir un nuevo cliente es entre **6 y 7 veces mayor** que retener uno existente.

Por esto, es vital analizar los datos históricos para detectar patrones de comportamiento y mejorar la retención.

## 📊 Dataset

El dataset **TelcoCustomerChurn.csv** contiene información sobre:

- 👥 **Datos demográficos:** género, edad, dependientes, etc.
- 📞 **Servicios contratados:** teléfono, internet, streaming, soporte técnico
- 💰 **Facturación:** cargos mensuales, cargos totales, método de pago
- 📅 **Antigüedad:** meses de permanencia (tenure)
- ⚠️ **Churn:** estado de abandono (Yes/No)

### Variables Principales

| Variable | Descripción |
|----------|-------------|
| `customerID` | Identificador único del cliente |
| `gender` | Género del cliente |
| `SeniorCitizen` | Si el cliente es adulto mayor (1/0) |
| `Partner` | Si el cliente tiene pareja |
| `Dependents` | Si el cliente tiene dependientes |
| `tenure` | Meses de permanencia |
| `PhoneService` | Servicio telefónico (Yes/No) |
| `InternetService` | Tipo de servicio de internet |
| `Contract` | Tipo de contrato (Month-to-month, One year, Two year) |
| `MonthlyCharges` | Cargo mensual en dólares |
| `TotalCharges` | Cargo total acumulado |
| `Churn` | Si abandonó la empresa (Yes/No) |

## 🛠️ Tecnologías Utilizadas

- 🐍 **Python 3.11 - Lenguaje de programación
- 📊 **Pandas** - Manipulación y análisis de datos
- 🔢 **NumPy** - Cálculos numéricos
- 📈 **Matplotlib** - Visualización de datos
- 🎨 **Seaborn** - Gráficos estadísticos avanzados
- 🚀 **Streamlit** - Framework para aplicaciones web interactivas

## 📁 Estructura del Proyecto

```
telco-customer-churn-eda/
│
├── app.py                          # Aplicación principal de Streamlit
├── requirements.txt                # Dependencias del proyecto
├── README.md                       # Este archivo
├── TelcoCustomerChurn.csv         # Dataset (no incluido en repo)
│
└── .gitignore                     # Archivos ignorados por Git
```

## 🚀 Instalación y Ejecución

### Prerequisitos

- Python 3.11 o superior
- pip (gestor de paquetes de Python)
- Git (opcional, para clonar el repositorio)

### Pasos de Instalación

1. **Clonar el repositorio:**

```bash
git clone https://github.com/moi2019en/trabajoFinal.git
cd telco-customer-churn-eda
```

2. **Crear un entorno virtual (recomendado):**

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Instalar las dependencias:**

```bash
pip install -r requirements.txt
```

4. **Descargar el dataset:**

Coloca el archivo `TelcoCustomerChurn.csv` en el directorio del proyecto.

5. **Ejecutar la aplicación:**

```bash
streamlit run app.py
```

6. **Abrir en el navegador:**

La aplicación se abrirá automáticamente en `http://localhost:8501`

## 📱 Estructura de la Aplicación

La aplicación está organizada en **4 módulos principales** navegables desde el menú lateral:

### 🏠 1. Home (Presentación)

- Título y descripción del proyecto
- Información del autor
- Contexto del dataset
- Tecnologías utilizadas
- Estructura del proyecto

### 📂 2. Carga de Datos

- Upload interactivo del archivo CSV
- Validación del archivo cargado
- Vista previa del dataset
- Información de dimensiones y tipos de datos
- Detalle de columnas y valores nulos

### 🔍 3. Análisis Exploratorio (EDA)

El módulo principal, organizado en **10 ítems de análisis**:

#### ℹ️ Ítem 1: Información General
- Estructura del dataset con `.info()`
- Tipos de datos
- Resumen de valores nulos

#### 📋 Ítem 2: Clasificación de Variables
- Identificación automática de variables numéricas y categóricas
- Uso de función personalizada con POO
- Visualización de la distribución de tipos

#### 📈 Ítem 3: Estadísticas Descriptivas
- Tabla completa con `.describe()`
- Análisis individual de variables (media, mediana, moda)
- Interpretación de asimetrías

#### ❓ Ítem 4: Valores Faltantes
- Conteo y visualización de valores nulos
- Porcentaje de missing values
- Recomendaciones de tratamiento

#### 📊 Ítem 5: Distribución de Variables Numéricas
- Histogramas interactivos
- Control de bins personalizable
- Opción de curva KDE (Kernel Density Estimation)
- Estadísticas por variable

#### 🏷️ Ítem 6: Variables Categóricas
- Gráficos de barras
- Frecuencias y porcentajes
- Tablas de contingencia
- Identificación de categorías dominantes

#### 📉 Ítem 7: Numérico vs Churn
- Boxplots y violinplots comparativos
- Análisis de diferencias entre grupos
- Interpretación estadística automática

#### 📊 Ítem 8: Categórico vs Churn
- Análisis de asociación con Churn
- Tablas cruzadas (crosstabs)
- Tasas de churn por categoría
- Identificación de categorías de riesgo

#### ⚙️ Ítem 9: Análisis Dinámico
- Selección interactiva de variables
- Múltiples opciones de análisis simultáneas
- Filtros personalizables
- Matriz de correlación dinámica

#### 🧠 Ítem 10: Hallazgos Clave
- Resumen ejecutivo de insights
- Visualizaciones de impacto
- Métricas principales de Churn
- Análisis consolidado por tipo de variable

### 📌 4. Conclusiones

- 5 conclusiones principales del análisis
- Implicaciones de negocio
- Oportunidades y riesgos identificados
- Próximos pasos recomendados
- Reflexión final

## 🎨 Características Destacadas

### Programación Orientada a Objetos

```python
class DataAnalyzer:
    """
    Clase para realizar análisis exploratorio de datos
    """
    def __init__(self, df):
        self.df = df
    
    def clasificar_variables(self):
        # Clasificación automática de variables
        
    def estadisticas_descriptivas(self):
        # Estadísticas descriptivas
        
    # ... más métodos
```

### Interfaz Interactiva

- 🎛️ **Widgets dinámicos:** selectbox, multiselect, slider, checkbox
- 📊 **Visualizaciones:** más de 20 gráficos diferentes
- 🎨 **Personalización:** colores, tipos de gráficos, filtros
- 📱 **Responsive:** diseño adaptado con columns y tabs

### Análisis Estadístico

- Media, mediana, moda
- Desviación estándar
- Análisis de distribuciones
- Correlaciones
- Análisis bivariado
- Tablas de contingencia

## 🔍 Hallazgos Principales

### 1️⃣ Antigüedad Crítica
Los primeros 6-12 meses son el período de mayor riesgo de churn. Los clientes que abandonan tienen significativamente menor tenure.

### 2️⃣ Impacto del Precio
Correlación positiva entre cargos mensuales altos y probabilidad de churn. Los clientes con facturas elevadas son más propensos a abandonar.

### 3️⃣ Tipo de Contrato
Los contratos month-to-month presentan tasas de churn dramáticamente superiores vs. contratos anuales o bianuales.

### 4️⃣ Servicios Adicionales
Los clientes con servicios complementarios (seguridad, soporte, backup) muestran menores tasas de churn.

### 5️⃣ Enfoque Data-Driven
El EDA proporciona bases sólidas para estrategias de retención sin necesidad de modelos predictivos complejos.

## 📈 Impacto de Negocio

### Oportunidades
- 📉 Reducción potencial de 0.5-1 punto porcentual en tasa de churn
- 💰 Incremento de 15-20% en Customer Lifetime Value
- 🎯 Focalización eficiente de recursos en segmentos de riesgo

### Recomendaciones
1. **Programa de Onboarding:** Seguimiento intensivo primeros 6 meses
2. **Revisión de Precios:** Optimizar relación valor-precio
3. **Incentivos Contractuales:** Migración a contratos largos
4. **Upselling Estratégico:** Servicios adicionales como factor de retención

## 🌐 Deployment

### Streamlit Cloud

La aplicación puede desplegarse gratuitamente en Streamlit Cloud:

1. Crear cuenta en [share.streamlit.io](https://share.streamlit.io)
2. Conectar repositorio de GitHub
3. Seleccionar rama y archivo principal (`app.py`)
4. Deploy automático

### Otras Opciones

- **Heroku:** Platform as a Service
- **AWS EC2:** Máquina virtual en la nube
- **Google Cloud Run:** Contenedores serverless
- **Docker:** Containerización para cualquier plataforma

## 👨‍💻 Autor

**Moises Tarazona Cochachin**

- 🎓 **Curso:** Especialización en Python for Analytics
- 👨‍🏫 **Docente:** MSc. Carlos Carrillo Villavicencio
- 📅 **Año:** 2026

## 📝 Licencia

Este proyecto fue desarrollado con fines educativos como parte del curso de Especialización en Python for Analytics.

## 🙏 Agradecimientos

- A **Carlos Carrillo Villavicencio** por la guía y enseñanzas durante el curso
- A la comunidad de **Streamlit** por la excelente documentación
- Al equipo de **Pandas** y **Seaborn** por las herramientas de análisis

## 📚 Referencias

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Matplotlib Documentation](https://matplotlib.org/)

---

<div align="center">

**⭐ Si este proyecto te resultó útil, considera darle una estrella en GitHub ⭐**

Desarrollado con ❤️ usando Python y Streamlit

</div>
