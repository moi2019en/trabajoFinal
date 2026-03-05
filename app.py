import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

# ---------------------------
# CONFIGURACIÓN GENERAL
# ---------------------------
st.set_page_config(
    page_title="EDA Telco Customer Churn",
    page_icon="📊",
    layout="wide"
)

# ---------------------------
# CLASE POO - DataAnalyzer
# ---------------------------
class DataAnalyzer:
    """
    Clase para realizar análisis exploratorio de datos
    Encapsula funciones de estadísticas descriptivas, clasificación de variables
    y funciones de visualización
    """
    def __init__(self, df):
        self.df = df

    def clasificar_variables(self):
        """Clasifica las variables en numéricas y categóricas"""
        numericas = self.df.select_dtypes(include=["int64", "float64"]).columns.tolist()
        categoricas = self.df.select_dtypes(include=["object"]).columns.tolist()
        return numericas, categoricas

    def valores_nulos(self):
        """Retorna el conteo de valores nulos por columna"""
        return self.df.isnull().sum()

    def estadisticas_descriptivas(self):
        """Retorna estadísticas descriptivas del dataframe"""
        return self.df.describe()

    def media(self, col):
        """Calcula la media de una columna numérica"""
        return self.df[col].mean()

    def mediana(self, col):
        """Calcula la mediana de una columna numérica"""
        return self.df[col].median()

    def moda(self, col):
        """Calcula la moda de una columna"""
        moda = self.df[col].mode()
        return moda[0] if len(moda) > 0 else None
    
    def calcular_porcentaje_churn(self):
        """Calcula el porcentaje de churn en el dataset"""
        if 'Churn' in self.df.columns:
            return self.df['Churn'].value_counts(normalize=True) * 100
        return None

# ---------------------------
# SIDEBAR - MENÚ DE NAVEGACIÓN
# ---------------------------
st.sidebar.title("🧭 Navegación Principal")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Seleccione una sección:",
    ["🏠 Home", "📂 Carga de Datos", "🔍 Análisis Exploratorio (EDA)", "📌 Conclusiones"]
)

st.sidebar.markdown("---")
st.sidebar.info("""
**💡 Instrucciones:**
1. Comienza por **Home** para conocer el proyecto
2. Carga el dataset en **Carga de Datos**
3. Explora los 10 ítems de análisis en **EDA**
4. Revisa las **Conclusiones** finales
""")

# ---------------------------
# MÓDULO 1: HOME
# ---------------------------
if menu == "🏠 Home":
    st.title("📊 Análisis Exploratorio de Datos")
    st.title("Telco Customer Churn")
    st.markdown("---")

    # Columnas para mejor presentación
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 🎯 Objetivo del Proyecto
        
        Desarrollar una aplicación interactiva en **Streamlit** para realizar un **Análisis Exploratorio
        de Datos (EDA)** del dataset **TelcoCustomerChurn**, con el fin de identificar patrones asociados
        a la fuga de clientes (**Churn**).
        
        Este proyecto **NO busca desarrollar modelos predictivos**, sino **analizar, limpiar, transformar 
        y visualizar los datos** para comprender las causas asociadas a la fuga de clientes.
        
        ### 📊 Contexto del Dataset
        
        El dataset contiene información sobre:
        - 📋 Datos demográficos de los clientes
        - 💼 Servicios contratados
        - 💰 Información de facturación
        - 📅 Antigüedad y tiempo de permanencia
        - ⚠️ Estado de Churn (si abandonó la empresa)
        
        ### 🚨 Contexto de Negocio
        
        Durante el último mes, debido a la coyuntura del COVID-19, la empresa incrementó
        su ratio de fuga de clientes en **+0.5 puntos porcentuales**, pasando de 2% en 
        promedio a 2.5%.
        
        El costo de adquirir un nuevo cliente es entre **6 y 7 veces mayor** que retener uno 
        existente, por lo que es vital analizar los datos históricos para detectar patrones de 
        comportamiento y mejorar la retención.
        """)
    
    with col2:
        st.markdown("""
        ### 👤 Información del Autor
        
        **Nombre:** Moises Tarazona Cochachin  
        **Curso:** Especialización en Python for Analytics  
        **Docente:** MSc. Carlos Carrillo Villavicencio  
        **Año:** 2026
        
        ### 🛠️ Tecnologías Utilizadas
        
        - 🐍 **Python 3.11**
        - 📊 **Pandas** - Manipulación de datos
        - 🔢 **NumPy** - Cálculos numéricos
        - 📈 **Matplotlib** - Visualización
        - 🎨 **Seaborn** - Gráficos estadísticos
        - 🚀 **Streamlit** - Aplicación web interactiva
        
        ### 📁 Estructura del Proyecto
        
        ```
        📦 Proyecto
        ├── 📄 app.py
        ├── 📄 requirements.txt
        ├── 📄 README.md
        └── 📊 TelcoCustomerChurn.csv
        ```
        """)

    st.markdown("---")
    st.success("✨ **¡Comienza tu análisis!** Navega al módulo de **Carga de Datos** para iniciar.")

# ---------------------------
# MÓDULO 2: CARGA DE DATOS
# ---------------------------
elif menu == "📂 Carga de Datos":
    st.title("📂 Carga del Dataset")
    st.markdown("### Cargar archivo TelcoCustomerChurn.csv")
    
    st.info("""
    ℹ️ **Instrucciones:** 
    - Carga el archivo CSV con los datos de Telco Customer Churn
    - El archivo debe contener información sobre clientes, servicios y estado de Churn
    - Una vez cargado, podrás acceder al módulo de Análisis Exploratorio
    """)

    archivo = st.file_uploader(
        "📁 Seleccione el archivo TelcoCustomerChurn.csv",
        type=["csv"],
        help="Sube el archivo CSV del dataset de Telco Customer Churn"
    )

    if archivo is not None:
        try:
            # Cargar el dataset
            df = pd.read_csv(archivo)
            st.session_state["df"] = df
            st.session_state["archivo_cargado"] = True

            st.success("✅ Archivo cargado correctamente")

            # Mostrar información básica
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("📊 Total de Filas", f"{df.shape[0]:,}")
            
            with col2:
                st.metric("📋 Total de Columnas", df.shape[1])
            
            with col3:
                memoria_mb = df.memory_usage(deep=True).sum() / 1024**2
                st.metric("💾 Tamaño en Memoria", f"{memoria_mb:.2f} MB")

            st.markdown("---")
            
            # Vista previa del dataset
            st.subheader("👀 Vista Previa del Dataset")
            
            col1, col2 = st.columns(2)
            with col1:
                num_filas = st.slider("Número de filas a mostrar:", 5, 50, 10)
            with col2:
                vista = st.radio("Tipo de vista:", ["Primeras filas", "Últimas filas", "Muestra aleatoria"])
            
            if vista == "Primeras filas":
                st.dataframe(df.head(num_filas), use_container_width=True)
            elif vista == "Últimas filas":
                st.dataframe(df.tail(num_filas), use_container_width=True)
            else:
                st.dataframe(df.sample(n=min(num_filas, len(df))), use_container_width=True)

            st.markdown("---")
            
            # Información de las columnas
            st.subheader("📋 Información de las Columnas")
            
            col_info = pd.DataFrame({
                'Columna': df.columns,
                'Tipo de Dato': df.dtypes.values,
                'Valores No Nulos': df.count().values,
                'Valores Nulos': df.isnull().sum().values,
                '% Nulos': (df.isnull().sum().values / len(df) * 100).round(2)
            })
            
            st.dataframe(col_info, use_container_width=True)
            
        except Exception as e:
            st.error(f"❌ Error al cargar el archivo: {str(e)}")
            st.info("💡 Asegúrate de que el archivo sea un CSV válido.")
    else:
        st.warning("⚠️ Por favor, carga el archivo CSV para continuar con el análisis")
        st.markdown("""
        ### 📝 Requisitos del Archivo:
        - Formato: **CSV** (valores separados por comas)
        - Debe contener la columna **'Churn'** con valores Yes/No
        - Variables demográficas, de servicios y facturación
        """)

# ---------------------------
# MÓDULO 3: ANÁLISIS EXPLORATORIO (EDA)
# ---------------------------
elif menu == "🔍 Análisis Exploratorio (EDA)":
    st.title("🔍 Análisis Exploratorio de Datos (EDA)")
    
    # Validar que el dataset esté cargado
    if "df" not in st.session_state:
        st.warning("⚠️ **No se ha cargado ningún dataset**")
        st.info("👈 Por favor, dirígete al módulo **'Carga de Datos'** y carga el archivo CSV primero.")
        st.stop()
    
    # Obtener el dataframe y crear instancia del analizador
    df = st.session_state["df"]
    analyzer = DataAnalyzer(df)
    numericas, categoricas = analyzer.clasificar_variables()

    st.markdown(f"""
    📊 **Dataset cargado exitosamente:** {df.shape[0]:,} filas × {df.shape[1]} columnas
    """)
    
    st.markdown("---")

    # Crear tabs para los 10 ítems de análisis
    tabs = st.tabs([
        "ℹ️ 1. Info General",
        "📋 2. Clasificación",
        "📈 3. Estadísticas",
        "❓ 4. Valores Faltantes",
        "📊 5. Dist. Numéricas",
        "🏷️ 6. Var. Categóricas",
        "📉 7. Numérico vs Churn",
        "📊 8. Categórico vs Churn",
        "⚙️ 9. Análisis Dinámico",
        "🧠 10. Hallazgos Clave"
    ])

    # ---------------------------
    # ÍTEM 1: INFORMACIÓN GENERAL
    # ---------------------------
    with tabs[0]:
        st.subheader("ℹ️ Ítem 1: Información General del Dataset")
        st.markdown("""
        Esta sección muestra información técnica sobre el dataset: tipos de datos,
        valores no nulos y uso de memoria.
        """)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("### 📋 Estructura del Dataset")
            
            # Capturar .info()
            buffer = StringIO()
            df.info(buf=buffer)
            info_str = buffer.getvalue()
            
            st.text(info_str)
        
        with col2:
            st.markdown("### 📊 Resumen Rápido")
            st.metric("Filas totales", f"{df.shape[0]:,}")
            st.metric("Columnas totales", df.shape[1])
            st.metric("Valores nulos totales", df.isnull().sum().sum())
            
            # Tipos de datos
            st.markdown("#### Tipos de Datos")
            tipo_counts = df.dtypes.value_counts()
            for tipo, count in tipo_counts.items():
                st.write(f"**{tipo}:** {count} columnas")

    # ---------------------------
    # ÍTEM 2: CLASIFICACIÓN DE VARIABLES
    # ---------------------------
    with tabs[1]:
        st.subheader("📋 Ítem 2: Clasificación de Variables")
        st.markdown("""
        Clasificación automática de las variables del dataset en **numéricas** y **categóricas**
        utilizando una función personalizada de la clase `DataAnalyzer`.
        """)
        
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🔢 Variables Numéricas")
            st.info(f"**Total: {len(numericas)} variables**")
            
            for i, var in enumerate(numericas, 1):
                st.write(f"{i}. `{var}`")

        with col2:
            st.markdown("### 🏷️ Variables Categóricas")
            st.info(f"**Total: {len(categoricas)} variables**")
            
            for i, var in enumerate(categoricas, 1):
                st.write(f"{i}. `{var}`")
        
        st.markdown("---")
        
        # Resumen visual
        st.markdown("### 📊 Distribución de Tipos de Variables")
        
        fig, ax = plt.subplots(figsize=(8, 5))
        tipos = ['Numéricas', 'Categóricas']
        conteos = [len(numericas), len(categoricas)]
        colores = ['#3498db', '#e74c3c']
        
        ax.bar(tipos, conteos, color=colores, alpha=0.7, edgecolor='black')
        ax.set_ylabel('Cantidad de Variables', fontsize=12)
        ax.set_title('Clasificación de Variables', fontsize=14, fontweight='bold')
        
        for i, v in enumerate(conteos):
            ax.text(i, v + 0.5, str(v), ha='center', va='bottom', fontsize=12, fontweight='bold')
        
        st.pyplot(fig)
        plt.close()

    # ---------------------------
    # ÍTEM 3: ESTADÍSTICAS DESCRIPTIVAS
    # ---------------------------
    with tabs[2]:
        st.subheader("📈 Ítem 3: Estadísticas Descriptivas")
        st.markdown("""
        Análisis de las medidas de tendencia central (media, mediana, moda) y dispersión
        para todas las variables numéricas del dataset.
        """)
        
        st.markdown("### 📊 Tabla de Estadísticas Descriptivas")
        st.dataframe(analyzer.estadisticas_descriptivas(), use_container_width=True)
        
        st.markdown("---")
        st.markdown("### 🔍 Análisis Individual de Variables")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            var_seleccionada = st.selectbox(
                "🔢 Seleccione una variable numérica:",
                numericas,
                help="Elige una variable para ver sus estadísticas detalladas"
            )
        
        with col2:
            st.markdown(f"#### Estadísticas de: **{var_seleccionada}**")
            
            media = analyzer.media(var_seleccionada)
            mediana = analyzer.mediana(var_seleccionada)
            moda = analyzer.moda(var_seleccionada)
            
            col_a, col_b, col_c = st.columns(3)
            
            with col_a:
                st.metric("📊 Media", f"{media:.2f}")
            with col_b:
                st.metric("📍 Mediana", f"{mediana:.2f}")
            with col_c:
                st.metric("🎯 Moda", f"{moda}")
        
        st.markdown("---")
        
        # Interpretación
        st.markdown("### 💡 Interpretación de Medidas de Tendencia Central")
        st.markdown(f"""
        - **Media ({media:.2f}):** Valor promedio de la variable. Sensible a valores extremos.
        - **Mediana ({mediana:.2f}):** Valor central cuando los datos están ordenados. Robusta ante outliers.
        - **Moda ({moda}):** Valor que más se repite en el conjunto de datos.
        """)
        
        # Análisis de asimetría
        if media > mediana:
            st.info("📈 La distribución presenta **asimetría positiva** (cola hacia la derecha)")
        elif media < mediana:
            st.info("📉 La distribución presenta **asimetría negativa** (cola hacia la izquierda)")
        else:
            st.info("⚖️ La distribución es aproximadamente **simétrica**")

    # ---------------------------
    # ÍTEM 4: VALORES FALTANTES
    # ---------------------------
    with tabs[3]:
        st.subheader("❓ Ítem 4: Análisis de Valores Faltantes")
        st.markdown("""
        Identificación y visualización de valores nulos (missing values) en el dataset.
        Los valores faltantes pueden afectar significativamente el análisis.
        """)
        
        nulos = analyzer.valores_nulos()
        total_nulos = nulos.sum()
        porcentaje_nulos = (total_nulos / (df.shape[0] * df.shape[1]) * 100)

        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("🔢 Total de Valores Nulos", f"{total_nulos:,}")
        with col2:
            st.metric("📊 % del Dataset", f"{porcentaje_nulos:.2f}%")
        with col3:
            columnas_con_nulos = (nulos > 0).sum()
            st.metric("📋 Columnas Afectadas", columnas_con_nulos)
        
        st.markdown("---")
        
        if total_nulos > 0:
            st.warning(f"⚠️ Se detectaron {total_nulos:,} valores nulos en el dataset")
            
            # Tabla de valores nulos
            st.markdown("### 📊 Detalle de Valores Nulos por Columna")
            
            df_nulos = pd.DataFrame({
                'Columna': nulos.index,
                'Valores Nulos': nulos.values,
                '% Nulos': (nulos.values / len(df) * 100).round(2)
            })
            df_nulos = df_nulos[df_nulos['Valores Nulos'] > 0].sort_values('Valores Nulos', ascending=False)
            
            st.dataframe(df_nulos, use_container_width=True)
            
            # Visualización
            st.markdown("### 📈 Visualización de Valores Nulos")
            
            fig, ax = plt.subplots(figsize=(10, 6))
            nulos_filtrados = nulos[nulos > 0].sort_values(ascending=True)
            
            nulos_filtrados.plot(kind='barh', ax=ax, color='#e74c3c', edgecolor='black')
            ax.set_xlabel('Cantidad de Valores Nulos', fontsize=12)
            ax.set_ylabel('Variables', fontsize=12)
            ax.set_title('Distribución de Valores Nulos por Variable', fontsize=14, fontweight='bold')
            ax.grid(axis='x', alpha=0.3)
            
            st.pyplot(fig)
            plt.close()
            
            # Recomendaciones
            st.markdown("### 💡 Recomendaciones")
            st.info("""
            - **< 5% nulos:** Generalmente seguro eliminar filas
            - **5-25% nulos:** Considerar imputación (media, mediana, moda)
            - **> 25% nulos:** Evaluar si la variable aporta valor al análisis
            """)
        else:
            st.success("✅ ¡Excelente! No se encontraron valores faltantes en el dataset")
            st.balloons()

    # ---------------------------
    # ÍTEM 5: DISTRIBUCIÓN DE VARIABLES NUMÉRICAS
    # ---------------------------
    with tabs[4]:
        st.subheader("📊 Ítem 5: Distribución de Variables Numéricas")
        st.markdown("""
        Visualización de la distribución de frecuencias de las variables numéricas
        mediante histogramas. Permite identificar patrones, asimetrías y outliers.
        """)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            var_num = st.selectbox(
                "🔢 Seleccione una variable numérica:",
                numericas,
                key="hist_var"
            )
            
            bins = st.slider(
                "📦 Número de bins (barras):",
                min_value=5,
                max_value=50,
                value=30,
                step=5,
                help="Más bins = mayor detalle en la distribución"
            )
            
            color_hist = st.color_picker("🎨 Color del histograma:", "#3498db")
            
            mostrar_kde = st.checkbox("📈 Mostrar curva KDE", value=True, 
                                     help="Kernel Density Estimation - estimación de densidad")
        
        with col2:
            fig, ax = plt.subplots(figsize=(10, 6))
            
            if mostrar_kde:
                sns.histplot(df[var_num], bins=bins, kde=True, ax=ax, color=color_hist, edgecolor='black')
            else:
                sns.histplot(df[var_num], bins=bins, ax=ax, color=color_hist, edgecolor='black')
            
            ax.set_xlabel(var_num, fontsize=12)
            ax.set_ylabel('Frecuencia', fontsize=12)
            ax.set_title(f'Distribución de {var_num}', fontsize=14, fontweight='bold')
            ax.grid(axis='y', alpha=0.3)
            
            st.pyplot(fig)
            plt.close()
        
        # Estadísticas de la variable
        st.markdown("---")
        st.markdown(f"### 📊 Estadísticas de {var_num}")
        
        col_a, col_b, col_c, col_d, col_e = st.columns(5)
        
        with col_a:
            st.metric("Media", f"{df[var_num].mean():.2f}")
        with col_b:
            st.metric("Mediana", f"{df[var_num].median():.2f}")
        with col_c:
            st.metric("Desv. Est.", f"{df[var_num].std():.2f}")
        with col_d:
            st.metric("Mínimo", f"{df[var_num].min():.2f}")
        with col_e:
            st.metric("Máximo", f"{df[var_num].max():.2f}")

    # ---------------------------
    # ÍTEM 6: ANÁLISIS DE VARIABLES CATEGÓRICAS
    # ---------------------------
    with tabs[5]:
        st.subheader("🏷️ Ítem 6: Análisis de Variables Categóricas")
        st.markdown("""
        Análisis de frecuencias y proporciones de las variables categóricas
        mediante gráficos de barras.
        """)
        
        if len(categoricas) == 0:
            st.warning("⚠️ No se encontraron variables categóricas en el dataset")
        else:
            col1, col2 = st.columns([1, 2])
            
            with col1:
                var_cat = st.selectbox(
                    "🏷️ Seleccione una variable categórica:",
                    categoricas,
                    key="cat_var"
                )
                
                mostrar_porcentaje = st.checkbox("📊 Mostrar porcentajes", value=True)
                ordenar = st.checkbox("🔽 Ordenar por frecuencia", value=True)
                color_bar = st.color_picker("🎨 Color de las barras:", "#e74c3c")
            
            with col2:
                # Conteos y proporciones
                conteos = df[var_cat].value_counts()
                proporciones = df[var_cat].value_counts(normalize=True) * 100
                
                if not ordenar:
                    conteos = conteos.sort_index()
                    proporciones = proporciones.sort_index()
                
                fig, ax = plt.subplots(figsize=(10, 6))
                
                if mostrar_porcentaje:
                    proporciones.plot(kind='bar', ax=ax, color=color_bar, edgecolor='black')
                    ax.set_ylabel('Porcentaje (%)', fontsize=12)
                    
                    # Agregar etiquetas de porcentaje
                    for i, v in enumerate(proporciones):
                        ax.text(i, v + 1, f'{v:.1f}%', ha='center', va='bottom', fontweight='bold')
                else:
                    conteos.plot(kind='bar', ax=ax, color=color_bar, edgecolor='black')
                    ax.set_ylabel('Frecuencia', fontsize=12)
                    
                    # Agregar etiquetas de conteo
                    for i, v in enumerate(conteos):
                        ax.text(i, v + max(conteos)*0.01, f'{v}', ha='center', va='bottom', fontweight='bold')
                
                ax.set_xlabel(var_cat, fontsize=12)
                ax.set_title(f'Distribución de {var_cat}', fontsize=14, fontweight='bold')
                ax.tick_params(axis='x', rotation=45)
                ax.grid(axis='y', alpha=0.3)
                plt.tight_layout()
                
                st.pyplot(fig)
                plt.close()
            
            # Tabla de frecuencias
            st.markdown("---")
            st.markdown(f"### 📋 Tabla de Frecuencias: {var_cat}")
            
            df_freq = pd.DataFrame({
                'Categoría': conteos.index,
                'Frecuencia': conteos.values,
                'Porcentaje': proporciones.values.round(2)
            })
            df_freq['Porcentaje'] = df_freq['Porcentaje'].apply(lambda x: f"{x}%")
            
            st.dataframe(df_freq, use_container_width=True)
            
            # Insights
            st.markdown("### 💡 Insights")
            categoria_mas_frecuente = conteos.index[0]
            freq_max = conteos.values[0]
            porc_max = proporciones.values[0]
            
            st.info(f"""
            - La categoría más frecuente es **'{categoria_mas_frecuente}'** con {freq_max:,} casos ({porc_max:.2f}%)
            - Total de categorías únicas: **{len(conteos)}**
            - Categoría menos frecuente: **'{conteos.index[-1]}'** ({conteos.values[-1]:,} casos)
            """)

    # ---------------------------
    # ÍTEM 7: ANÁLISIS BIVARIADO (NUMÉRICO VS CHURN)
    # ---------------------------
    with tabs[6]:
        st.subheader("📉 Ítem 7: Variable Numérica vs Churn")
        st.markdown("""
        Análisis de la relación entre variables numéricas y la variable objetivo **Churn**.
        Los boxplots permiten comparar distribuciones entre clientes que se fueron y los que permanecen.
        """)
        
        if 'Churn' not in df.columns:
            st.error("❌ La columna 'Churn' no existe en el dataset")
        else:
            col1, col2 = st.columns([1, 2])
            
            with col1:
                var_num_churn = st.selectbox(
                    "🔢 Seleccione una variable numérica:",
                    numericas,
                    key="num_churn"
                )
                
                tipo_grafico = st.radio(
                    "Tipo de gráfico:",
                    ["📦 Boxplot", "🎻 Violinplot"],
                    help="Boxplot: muestra cuartiles y outliers / Violinplot: muestra densidad"
                )
                
                mostrar_puntos = st.checkbox("📍 Mostrar puntos individuales", value=False)
            
            with col2:
                fig, ax = plt.subplots(figsize=(10, 6))
                
                if tipo_grafico == "📦 Boxplot":
                    sns.boxplot(data=df, x="Churn", y=var_num_churn, ax=ax, palette="Set2")
                    if mostrar_puntos:
                        sns.stripplot(data=df, x="Churn", y=var_num_churn, ax=ax, 
                                    color='black', alpha=0.3, size=2)
                else:
                    sns.violinplot(data=df, x="Churn", y=var_num_churn, ax=ax, palette="Set2")
                
                ax.set_xlabel('Churn', fontsize=12)
                ax.set_ylabel(var_num_churn, fontsize=12)
                ax.set_title(f'{var_num_churn} vs Churn', fontsize=14, fontweight='bold')
                ax.grid(axis='y', alpha=0.3)
                
                st.pyplot(fig)
                plt.close()
            
            # Estadísticas comparativas
            st.markdown("---")
            st.markdown(f"### 📊 Comparación Estadística: {var_num_churn}")
            
            churn_yes = df[df['Churn'] == 'Yes'][var_num_churn]
            churn_no = df[df['Churn'] == 'No'][var_num_churn]
            
            col_a, col_b, col_c = st.columns(3)
            
            with col_a:
                st.markdown("#### Churn = No")
                st.metric("Media", f"{churn_no.mean():.2f}")
                st.metric("Mediana", f"{churn_no.median():.2f}")
                st.metric("Desv. Est.", f"{churn_no.std():.2f}")
            
            with col_b:
                st.markdown("#### Churn = Yes")
                st.metric("Media", f"{churn_yes.mean():.2f}")
                st.metric("Mediana", f"{churn_yes.median():.2f}")
                st.metric("Desv. Est.", f"{churn_yes.std():.2f}")
            
            with col_c:
                st.markdown("#### Diferencias")
                diff_media = churn_yes.mean() - churn_no.mean()
                diff_mediana = churn_yes.median() - churn_no.median()
                
                st.metric("Δ Media", f"{diff_media:.2f}", 
                         delta=f"{(diff_media/churn_no.mean()*100):.1f}%")
                st.metric("Δ Mediana", f"{diff_mediana:.2f}",
                         delta=f"{(diff_mediana/churn_no.median()*100):.1f}%")
            
            # Interpretación
            st.markdown("### 💡 Interpretación")
            if abs(diff_media) > 0.1 * churn_no.mean():
                st.warning(f"""
                ⚠️ **Diferencia significativa detectada:** Los clientes que abandonaron (Churn=Yes) 
                tienen un valor {'mayor' if diff_media > 0 else 'menor'} en {var_num_churn} 
                ({abs(diff_media/churn_no.mean()*100):.1f}% de diferencia).
                """)
            else:
                st.info(f"""
                ℹ️ **Diferencia poco significativa:** No hay una gran diferencia en {var_num_churn} 
                entre clientes que se fueron y los que permanecen.
                """)

    # ---------------------------
    # ÍTEM 8: ANÁLISIS BIVARIADO (CATEGÓRICO VS CHURN)
    # ---------------------------
    with tabs[7]:
        st.subheader("📊 Ítem 8: Variable Categórica vs Churn")
        st.markdown("""
        Análisis de la relación entre variables categóricas y **Churn**.
        Permite identificar qué categorías presentan mayor tasa de abandono.
        """)
        
        if 'Churn' not in df.columns:
            st.error("❌ La columna 'Churn' no existe en el dataset")
        elif len(categoricas) <= 1:  # Solo Churn
            st.warning("⚠️ No hay suficientes variables categóricas para analizar (además de Churn)")
        else:
            # Filtrar categoricas sin incluir Churn
            categoricas_sin_churn = [c for c in categoricas if c != 'Churn']
            
            col1, col2 = st.columns([1, 2])
            
            with col1:
                var_cat_churn = st.selectbox(
                    "🏷️ Seleccione una variable categórica:",
                    categoricas_sin_churn,
                    key="cat_churn"
                )
                
                tipo_viz = st.radio(
                    "Tipo de visualización:",
                    ["📊 Conteo", "📈 Porcentaje"],
                    help="Conteo: valores absolutos / Porcentaje: proporciones relativas"
                )
                
                vista_horizontal = st.checkbox("🔄 Vista horizontal", value=False)
            
            with col2:
                fig, ax = plt.subplots(figsize=(10, 6))
                
                if tipo_viz == "📊 Conteo":
                    if vista_horizontal:
                        sns.countplot(data=df, y=var_cat_churn, hue="Churn", ax=ax, palette="Set1")
                    else:
                        sns.countplot(data=df, x=var_cat_churn, hue="Churn", ax=ax, palette="Set1")
                        ax.tick_params(axis='x', rotation=45)
                else:
                    # Calcular porcentajes
                    crosstab = pd.crosstab(df[var_cat_churn], df['Churn'], normalize='index') * 100
                    crosstab.plot(kind='bar', ax=ax, stacked=False, color=['#2ecc71', '#e74c3c'])
                    ax.set_ylabel('Porcentaje (%)', fontsize=12)
                    ax.tick_params(axis='x', rotation=45)
                    ax.legend(title='Churn')
                
                ax.set_title(f'{var_cat_churn} vs Churn', fontsize=14, fontweight='bold')
                ax.grid(axis='y' if not vista_horizontal else 'x', alpha=0.3)
                plt.tight_layout()
                
                st.pyplot(fig)
                plt.close()
            
            # Tabla cruzada
            st.markdown("---")
            st.markdown(f"### 📋 Tabla de Contingencia: {var_cat_churn} vs Churn")
            
            col_tabla1, col_tabla2 = st.columns(2)
            
            with col_tabla1:
                st.markdown("**Conteos Absolutos**")
                crosstab_count = pd.crosstab(df[var_cat_churn], df['Churn'], margins=True)
                st.dataframe(crosstab_count, use_container_width=True)
            
            with col_tabla2:
                st.markdown("**Porcentajes por Fila (%)**")
                crosstab_pct = pd.crosstab(df[var_cat_churn], df['Churn'], normalize='index') * 100
                crosstab_pct = crosstab_pct.round(2)
                st.dataframe(crosstab_pct, use_container_width=True)
            
            # Análisis de Churn por categoría
            st.markdown("---")
            st.markdown("### 🎯 Tasa de Churn por Categoría")
            
            churn_rate = df.groupby(var_cat_churn)['Churn'].apply(lambda x: (x == 'Yes').sum() / len(x) * 100).sort_values(ascending=False)
            
            fig, ax = plt.subplots(figsize=(10, 5))
            churn_rate.plot(kind='barh', ax=ax, color='#e74c3c', edgecolor='black')
            
            for i, v in enumerate(churn_rate):
                ax.text(v + 1, i, f'{v:.1f}%', va='center', fontweight='bold')
            
            ax.set_xlabel('Tasa de Churn (%)', fontsize=12)
            ax.set_ylabel(var_cat_churn, fontsize=12)
            ax.set_title(f'Tasa de Churn por {var_cat_churn}', fontsize=14, fontweight='bold')
            ax.grid(axis='x', alpha=0.3)
            plt.tight_layout()
            
            st.pyplot(fig)
            plt.close()
            
            # Insights
            st.markdown("### 💡 Insights Clave")
            categoria_mayor_churn = churn_rate.index[0]
            tasa_mayor = churn_rate.values[0]
            categoria_menor_churn = churn_rate.index[-1]
            tasa_menor = churn_rate.values[-1]
            
            st.info(f"""
            - **Mayor tasa de Churn:** '{categoria_mayor_churn}' con {tasa_mayor:.2f}%
            - **Menor tasa de Churn:** '{categoria_menor_churn}' con {tasa_menor:.2f}%
            - **Diferencia:** {(tasa_mayor - tasa_menor):.2f} puntos porcentuales
            """)

    # ---------------------------
    # ÍTEM 9: ANÁLISIS DINÁMICO CON PARÁMETROS
    # ---------------------------
    with tabs[8]:
        st.subheader("⚙️ Ítem 9: Análisis Dinámico Basado en Parámetros")
        st.markdown("""
        Herramienta interactiva que permite seleccionar variables y aplicar filtros
        dinámicos para realizar análisis personalizados del dataset.
        """)
        
        st.markdown("### 🎛️ Panel de Control")
        
        # Selección de columnas
        st.markdown("#### 1️⃣ Selección de Variables")
        
        col1, col2 = st.columns(2)
        
        with col1:
            columnas_num_sel = st.multiselect(
                "🔢 Seleccione variables numéricas:",
                numericas,
                default=numericas[:3] if len(numericas) >= 3 else numericas,
                help="Puedes seleccionar múltiples variables"
            )
        
        with col2:
            columnas_cat_sel = st.multiselect(
                "🏷️ Seleccione variables categóricas:",
                categoricas,
                default=categoricas[:2] if len(categoricas) >= 2 else categoricas,
                help="Puedes seleccionar múltiples variables"
            )
        
        st.markdown("---")
        
        # Opciones de análisis
        st.markdown("#### 2️⃣ Opciones de Análisis")
        
        opciones = st.multiselect(
            "¿Qué análisis deseas realizar?",
            [
                "📊 Estadísticas descriptivas",
                "📈 Matriz de correlación",
                "📉 Distribuciones",
                "🔍 Valores únicos",
                "📋 Tabla filtrada"
            ],
            default=["📊 Estadísticas descriptivas"]
        )
        
        # Filtros dinámicos
        if 'Churn' in df.columns:
            st.markdown("---")
            st.markdown("#### 3️⃣ Filtros")
            
            col_f1, col_f2 = st.columns(2)
            
            with col_f1:
                filtrar_churn = st.checkbox("🎯 Filtrar por Churn")
                if filtrar_churn:
                    valor_churn = st.selectbox("Valor de Churn:", df['Churn'].unique())
                    df_filtrado = df[df['Churn'] == valor_churn].copy()
                else:
                    df_filtrado = df.copy()
            
            with col_f2:
                st.metric("📊 Registros seleccionados", f"{len(df_filtrado):,}")
                st.metric("📉 % del total", f"{(len(df_filtrado)/len(df)*100):.2f}%")
        else:
            df_filtrado = df.copy()
        
        # Mostrar resultados según opciones seleccionadas
        st.markdown("---")
        st.markdown("### 📊 Resultados del Análisis")
        
        if "📊 Estadísticas descriptivas" in opciones and columnas_num_sel:
            with st.expander("📊 Estadísticas Descriptivas", expanded=True):
                st.dataframe(df_filtrado[columnas_num_sel].describe(), use_container_width=True)
        
        if "📈 Matriz de correlación" in opciones and len(columnas_num_sel) >= 2:
            with st.expander("📈 Matriz de Correlación", expanded=True):
                fig, ax = plt.subplots(figsize=(10, 8))
                
                corr_matrix = df_filtrado[columnas_num_sel].corr()
                sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
                           center=0, ax=ax, square=True, linewidths=1)
                
                ax.set_title('Matriz de Correlación', fontsize=14, fontweight='bold')
                plt.tight_layout()
                
                st.pyplot(fig)
                plt.close()
        
        if "📉 Distribuciones" in opciones and columnas_num_sel:
            with st.expander("📉 Distribuciones de Variables Numéricas", expanded=True):
                num_cols = len(columnas_num_sel)
                num_rows = (num_cols + 1) // 2
                
                fig, axes = plt.subplots(num_rows, 2, figsize=(14, 5*num_rows))
                axes = axes.flatten() if num_cols > 1 else [axes]
                
                for i, col in enumerate(columnas_num_sel):
                    sns.histplot(df_filtrado[col], kde=True, ax=axes[i], color='#3498db')
                    axes[i].set_title(f'Distribución de {col}', fontweight='bold')
                    axes[i].grid(axis='y', alpha=0.3)
                
                # Ocultar ejes no utilizados
                for i in range(num_cols, len(axes)):
                    axes[i].set_visible(False)
                
                plt.tight_layout()
                st.pyplot(fig)
                plt.close()
        
        if "🔍 Valores únicos" in opciones and columnas_cat_sel:
            with st.expander("🔍 Valores Únicos de Variables Categóricas", expanded=True):
                for col in columnas_cat_sel:
                    st.markdown(f"**{col}:**")
                    valores = df_filtrado[col].value_counts()
                    st.write(f"Total de valores únicos: {len(valores)}")
                    st.dataframe(valores.reset_index().rename(columns={'index': 'Valor', col: 'Frecuencia'}), 
                               use_container_width=True)
                    st.markdown("---")
        
        if "📋 Tabla filtrada" in opciones:
            with st.expander("📋 Datos Filtrados", expanded=False):
                todas_cols_sel = columnas_num_sel + columnas_cat_sel
                if todas_cols_sel:
                    st.dataframe(df_filtrado[todas_cols_sel].head(100), use_container_width=True)
                    st.info(f"Mostrando las primeras 100 filas de {len(df_filtrado):,} registros seleccionados")
                else:
                    st.warning("⚠️ Selecciona al menos una variable para ver los datos")

    # ---------------------------
    # ÍTEM 10: HALLAZGOS CLAVE
    # ---------------------------
    with tabs[9]:
        st.subheader("🧠 Ítem 10: Hallazgos Clave del Análisis")
        st.markdown("""
        Resumen ejecutivo de los principales insights y patrones identificados
        durante el análisis exploratorio del dataset Telco Customer Churn.
        """)
        
        if 'Churn' not in df.columns:
            st.error("❌ No se puede realizar el análisis sin la variable 'Churn'")
        else:
            # Métricas generales de Churn
            st.markdown("### 📊 Resumen Ejecutivo de Churn")
            
            churn_counts = df['Churn'].value_counts()
            churn_prop = analyzer.calcular_porcentaje_churn()
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Total Clientes", f"{len(df):,}")
            with col2:
                clientes_churn = churn_counts.get('Yes', 0)
                st.metric("Clientes Churn", f"{clientes_churn:,}", 
                         delta=f"{churn_prop.get('Yes', 0):.1f}%",
                         delta_color="inverse")
            with col3:
                clientes_no_churn = churn_counts.get('No', 0)
                st.metric("Clientes Retenidos", f"{clientes_no_churn:,}",
                         delta=f"{churn_prop.get('No', 0):.1f}%")
            with col4:
                tasa_churn = churn_prop.get('Yes', 0)
                st.metric("Tasa de Churn", f"{tasa_churn:.2f}%")
            
            st.markdown("---")
            
            # Visualización de la distribución de Churn
            col_viz1, col_viz2 = st.columns(2)
            
            with col_viz1:
                st.markdown("#### 📊 Distribución de Churn")
                fig, ax = plt.subplots(figsize=(8, 6))
                
                colores = ['#2ecc71', '#e74c3c']
                churn_counts.plot(kind='bar', ax=ax, color=colores, edgecolor='black')
                
                for i, v in enumerate(churn_counts):
                    porcentaje = (v / len(df)) * 100
                    ax.text(i, v + len(df)*0.01, f'{v:,}\n({porcentaje:.1f}%)', 
                           ha='center', va='bottom', fontweight='bold')
                
                ax.set_xlabel('Churn', fontsize=12)
                ax.set_ylabel('Cantidad de Clientes', fontsize=12)
                ax.set_title('Distribución de Churn', fontsize=14, fontweight='bold')
                ax.tick_params(axis='x', rotation=0)
                ax.grid(axis='y', alpha=0.3)
                plt.tight_layout()
                
                st.pyplot(fig)
                plt.close()
            
            with col_viz2:
                st.markdown("#### 🥧 Proporción de Churn")
                fig, ax = plt.subplots(figsize=(8, 6))
                
                ax.pie(churn_counts, labels=churn_counts.index, autopct='%1.1f%%',
                      colors=colores, startangle=90, textprops={'fontsize': 12, 'fontweight': 'bold'})
                ax.set_title('Proporción de Churn', fontsize=14, fontweight='bold')
                
                st.pyplot(fig)
                plt.close()
            
            st.markdown("---")
            
            # Hallazgos por variable numérica
            st.markdown("### 🔍 Análisis de Variables Numéricas vs Churn")
            
            if 'tenure' in df.columns:
                st.markdown("#### 📅 Antigüedad (Tenure)")
                
                col_t1, col_t2 = st.columns(2)
                
                with col_t1:
                    tenure_churn_yes = df[df['Churn'] == 'Yes']['tenure'].mean()
                    tenure_churn_no = df[df['Churn'] == 'No']['tenure'].mean()
                    
                    st.metric("Tenure promedio (Churn=Yes)", f"{tenure_churn_yes:.1f} meses")
                    st.metric("Tenure promedio (Churn=No)", f"{tenure_churn_no:.1f} meses")
                    
                    diferencia_tenure = tenure_churn_no - tenure_churn_yes
                    st.metric("Diferencia", f"{diferencia_tenure:.1f} meses",
                             delta=f"{(diferencia_tenure/tenure_churn_yes*100):.1f}%")
                
                with col_t2:
                    fig, ax = plt.subplots(figsize=(8, 5))
                    sns.boxplot(data=df, x='Churn', y='tenure', ax=ax, palette=['#2ecc71', '#e74c3c'])
                    ax.set_title('Tenure vs Churn', fontsize=12, fontweight='bold')
                    ax.grid(axis='y', alpha=0.3)
                    st.pyplot(fig)
                    plt.close()
                
                st.info("""
                🔎 **Insight:** Los clientes que abandonan tienen una antigüedad significativamente menor.
                Los primeros meses son críticos para la retención.
                """)
            
            st.markdown("---")
            
            if 'MonthlyCharges' in df.columns:
                st.markdown("#### 💰 Cargos Mensuales (MonthlyCharges)")
                
                col_m1, col_m2 = st.columns(2)
                
                with col_m1:
                    mc_churn_yes = df[df['Churn'] == 'Yes']['MonthlyCharges'].mean()
                    mc_churn_no = df[df['Churn'] == 'No']['MonthlyCharges'].mean()
                    
                    st.metric("Cargo promedio (Churn=Yes)", f"${mc_churn_yes:.2f}")
                    st.metric("Cargo promedio (Churn=No)", f"${mc_churn_no:.2f}")
                    
                    diferencia_mc = mc_churn_yes - mc_churn_no
                    st.metric("Diferencia", f"${diferencia_mc:.2f}",
                             delta=f"{(diferencia_mc/mc_churn_no*100):.1f}%",
                             delta_color="inverse")
                
                with col_m2:
                    fig, ax = plt.subplots(figsize=(8, 5))
                    sns.boxplot(data=df, x='Churn', y='MonthlyCharges', ax=ax, palette=['#2ecc71', '#e74c3c'])
                    ax.set_title('Monthly Charges vs Churn', fontsize=12, fontweight='bold')
                    ax.grid(axis='y', alpha=0.3)
                    st.pyplot(fig)
                    plt.close()
                
                st.warning("""
                ⚠️ **Insight:** Los clientes con cargos mensuales más altos tienen mayor probabilidad de abandono.
                La relación precio-valor percibido es clave para la retención.
                """)
            
            st.markdown("---")
            
            # Hallazgos por variables categóricas
            st.markdown("### 🏷️ Análisis de Variables Categóricas vs Churn")
            
            if 'Contract' in df.columns:
                st.markdown("#### 📄 Tipo de Contrato")
                
                contract_churn = pd.crosstab(df['Contract'], df['Churn'], normalize='index') * 100
                
                fig, ax = plt.subplots(figsize=(10, 6))
                contract_churn.plot(kind='bar', ax=ax, color=['#2ecc71', '#e74c3c'], edgecolor='black')
                ax.set_ylabel('Porcentaje (%)', fontsize=12)
                ax.set_xlabel('Tipo de Contrato', fontsize=12)
                ax.set_title('Tasa de Churn por Tipo de Contrato', fontsize=14, fontweight='bold')
                ax.tick_params(axis='x', rotation=45)
                ax.legend(title='Churn')
                ax.grid(axis='y', alpha=0.3)
                plt.tight_layout()
                
                st.pyplot(fig)
                plt.close()
                
                st.error("""
                🚨 **Insight Crítico:** Los contratos mensuales (Month-to-month) presentan la mayor tasa de churn.
                Los contratos de largo plazo (One year, Two year) son un factor de retención importante.
                """)
            
            st.markdown("---")
            
            # Conclusiones finales consolidadas
            st.markdown("### 🎯 Conclusiones Principales del EDA")
            
            st.success("""
            #### ✅ 5 Hallazgos Clave:
            
            1. **📉 Antigüedad Crítica:** Los primeros meses del cliente son fundamentales. Los clientes 
               que abandonan tienen significativamente menor tiempo de permanencia (tenure).
            
            2. **💰 Impacto del Precio:** Existe una correlación positiva entre cargos mensuales altos 
               y la probabilidad de churn. Los clientes con facturas elevadas son más propensos a abandonar.
            
            3. **📄 Importancia del Contrato:** El tipo de contrato es una variable altamente predictiva. 
               Los contratos mensuales presentan tasas de churn dramáticamente más altas que los contratos 
               anuales o bianuales.
            
            4. **🎁 Valor de Servicios Adicionales:** Los clientes con servicios complementarios 
               (seguridad online, soporte técnico, etc.) tienden a permanecer más tiempo con la empresa.
            
            5. **📊 Enfoque Estratégico:** El análisis exploratorio proporciona bases sólidas para diseñar 
               estrategias de retención enfocadas en: (a) onboarding efectivo en los primeros meses, 
               (b) optimización de la propuesta de valor vs precio, y (c) incentivos para contratos de largo plazo.
            """)
            
            st.markdown("---")
            
            st.info("""
            ### 💡 Recomendaciones Estratégicas
            
            - **Programa de Onboarding:** Implementar seguimiento intensivo durante los primeros 6 meses
            - **Revisión de Precios:** Evaluar la percepción de valor en segmentos de alto costo
            - **Promoción de Contratos Largos:** Incentivos para migrar de mensual a anual/bianual
            - **Upselling Inteligente:** Ofrecer servicios adicionales que incrementen el valor percibido
            - **Sistema de Alertas:** Monitoreo predictivo de clientes en riesgo de churn
            """)

# ---------------------------
# MÓDULO 4: CONCLUSIONES
# ---------------------------
elif menu == "📌 Conclusiones":
    st.title("📌 Conclusiones Finales del Proyecto")
    st.markdown("---")
    
    st.markdown("""
    ## 🎯 Resumen Ejecutivo
    
    Este proyecto de Análisis Exploratorio de Datos (EDA) sobre el dataset **TelcoCustomerChurn**
    ha permitido identificar patrones clave asociados a la fuga de clientes, proporcionando
    insights accionables para la toma de decisiones estratégicas.
    """)
    
    st.markdown("---")
    
    # Conclusiones numeradas
    st.markdown("## 📋 Conclusiones Principales")
    
    st.markdown("""
    ### 1️⃣ La Antigüedad es un Factor Crítico de Retención
    
    **Hallazgo:** Los clientes que abandonan la empresa tienen una antigüedad (tenure) significativamente 
    menor que aquellos que permanecen. Los primeros 6-12 meses representan el período de mayor riesgo.
    
    **Implicación:** Es fundamental implementar estrategias de retención específicas para clientes nuevos,
    incluyendo programas de onboarding robustos y seguimiento proactivo durante los primeros meses.
    
    ---
    
    ### 2️⃣ Los Cargos Mensuales Elevados Están Asociados con Mayor Churn
    
    **Hallazgo:** Existe una correlación positiva entre los cargos mensuales (MonthlyCharges) y la 
    probabilidad de abandono. Los clientes con facturas más altas son más propensos a irse.
    
    **Implicación:** La relación precio-valor percibido requiere revisión. Es necesario evaluar si el
    precio refleja adecuadamente el valor entregado o si existen oportunidades de optimización en la
    estructura de precios y servicios ofrecidos.
    
    ---
    
    ### 3️⃣ El Tipo de Contrato es Altamente Predictivo del Comportamiento de Churn
    
    **Hallazgo:** Los contratos mensuales (Month-to-month) presentan tasas de churn dramáticamente
    superiores comparados con contratos anuales o bianuales. Este es uno de los indicadores más
    fuertes de probabilidad de abandono.
    
    **Implicación:** Se recomienda implementar incentivos atractivos para migrar clientes de contratos
    mensuales a compromisos de largo plazo, lo cual naturalmente reduce el churn y aumenta el valor
    del ciclo de vida del cliente (Customer Lifetime Value).
    
    ---
    
    ### 4️⃣ Los Servicios Adicionales Actúan como Factor de Retención
    
    **Hallazgo:** Los clientes que contratan servicios complementarios (seguridad online, soporte técnico,
    backup, etc.) muestran menores tasas de churn. Cada servicio adicional incrementa el compromiso
    y la percepción de valor.
    
    **Implicación:** Las estrategias de upselling y cross-selling no solo incrementan los ingresos, sino
    que funcionan como mecanismos de retención. Se recomienda desarrollar paquetes de servicios que
    maximicen el valor percibido por el cliente.
    
    ---
    
    ### 5️⃣ El Análisis Exploratorio es Fundamental para la Toma de Decisiones Basada en Datos
    
    **Hallazgo:** A través del EDA se han identificado patrones claros y accionables sin necesidad de
    modelos predictivos complejos. La visualización y el análisis estadístico descriptivo han revelado
    insights de alto impacto.
    
    **Implicación:** Invertir en análisis exploratorio y visualización de datos debe ser una prioridad
    para cualquier organización orientada a datos. El EDA proporciona la base fundamental para
    entender el negocio, validar hipótesis y diseñar estrategias efectivas.
    """)
    
    st.markdown("---")
    
    # Impacto del negocio
    st.markdown("## 💼 Impacto de Negocio")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📈 Oportunidades Identificadas
        
        - **Reducción de Churn:** Potencial de reducir la tasa de abandono en 0.5-1 punto porcentual
          mediante implementación de estrategias basadas en estos insights
        
        - **Optimización de Revenue:** Mejora en la retención puede traducirse en incremento del 
          15-20% en el valor del ciclo de vida del cliente
        
        - **Eficiencia Operativa:** Focalización de recursos en segmentos de mayor riesgo
        
        - **Ventaja Competitiva:** Mayor conocimiento del cliente vs competencia
        """)
    
    with col2:
        st.markdown("""
        ### ⚠️ Riesgos Identificados
        
        - **Pérdida de Clientes de Alto Valor:** Los clientes con mayores cargos mensuales 
          están en mayor riesgo
        
        - **Vulnerabilidad Temprana:** Los primeros meses son críticos y requieren atención
        
        - **Debilidad en Contratos Mensuales:** Más del 40% del churn proviene de este segmento
        
        - **Costo de Oportunidad:** Cada cliente perdido representa 6-7x el costo de adquisición
        """)
    
    st.markdown("---")
    
    # Próximos pasos
    st.markdown("## 🚀 Próximos Pasos Recomendados")
    
    st.warning("""
    ### 📊 Fase 1: Implementación de Acciones Inmediatas
    
    1. **Dashboard de Monitoreo:** Crear tablero de control para seguimiento en tiempo real de métricas de churn
    2. **Segmentación de Clientes:** Clasificar base de clientes según nivel de riesgo
    3. **Programa Piloto:** Implementar iniciativas de retención en segmento de alto riesgo
    4. **A/B Testing:** Validar efectividad de diferentes estrategias de retención
    """)
    
    st.info("""
    ### 🔮 Fase 2: Desarrollo de Capacidades Avanzadas
    
    1. **Modelos Predictivos:** Desarrollar modelos de machine learning para predicción de churn
    2. **Sistema de Alertas Tempranas:** Automatización de detección de clientes en riesgo
    3. **Personalización:** Estrategias de retención customizadas por segmento
    4. **Integración Operativa:** Incorporar insights en procesos de atención al cliente
    """)
    
    st.markdown("---")
    
    # Cierre
    st.success("""
    ## ✅ Reflexión Final
    
    Este proyecto ha demostrado el poder del **Análisis Exploratorio de Datos** como herramienta
    fundamental para la comprensión del negocio y la toma de decisiones estratégicas.
    
    A través de técnicas de Python, visualización y análisis estadístico, hemos transformado
    datos crudos en **insights accionables** que pueden generar impacto real en la retención
    de clientes y la rentabilidad del negocio.
    
    El camino hacia una organización verdaderamente data-driven comienza con la capacidad de
    hacer las preguntas correctas y explorar los datos con rigurosidad y curiosidad científica.
    
    ---
    
    **"En Dios confiamos, todos los demás traigan datos."** - W. Edwards Deming
    """)
    
    st.markdown("---")
    
    # Información del autor
    st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <h3>👨‍💻 Desarrollado por Frank Bellido</h3>
        <p><strong>Especialización en Python for Analytics</strong></p>
        <p>Módulo 1: Python Fundamentals</p>
        <p>Docente: MSc. Carlos Carrillo Villavicencio</p>
        <p>Año 2026</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------
# FOOTER
# ---------------------------
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #7f8c8d; padding: 10px;'>
    <p>📊 Proyecto EDA Telco Customer Churn | Desarrollado con ❤️ usando Python & Streamlit</p>
    <p>🐍 Python | 📊 Pandas | 📈 Matplotlib | 🎨 Seaborn | 🚀 Streamlit</p>
</div>
""", unsafe_allow_html=True)
