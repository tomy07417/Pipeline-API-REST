# 🚀 Pipeline ETL - Consumo de API REST

Pipeline de datos profesional que consume una API REST de e-commerce con Python, implementando manejo robusto de errores, logging profesional y almacenamiento en formato Parquet con particionamiento por fecha.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Status](https://img.shields.io/badge/Status-Completado-success.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [Tecnologías](#-tecnologías)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Uso](#-uso)
- [Tablas Procesadas](#-tablas-procesadas)
- [Características Principales](#-características-principales)
- [Manejo de Errores](#-manejo-de-errores)
- [Outputs](#-outputs)
- [Lecciones Aprendidas](#-lecciones-aprendidas)
- [Autor](#-autor)

---

## 📝 Descripción

Este proyecto implementa un pipeline ETL completo que:

- **EXTRACT**: Consume datos de una API REST de e-commerce con autenticación y reintentos automáticos
- **TRANSFORM**: Procesa y limpia 11 tablas diferentes, optimizando tipos de datos y manejando valores nulos
- **LOAD**: Guarda los datos en formato Parquet, con órdenes particionadas por año/mes

### 🎯 Objetivos de Aprendizaje

- ✅ Consumir APIs REST con Python
- ✅ Manejar errores de red (timeouts, reintentos con exponential backoff)
- ✅ Implementar logging profesional
- ✅ Usar variables de entorno para secrets
- ✅ Guardar datos en formato Parquet particionado

---

## 🛠 Tecnologías

| Tecnología | Uso |
|------------|-----|
| **Python 3.9+** | Lenguaje principal |
| **Requests** | Consumo de APIs HTTP |
| **Pandas** | Procesamiento y transformación de datos |
| **PyArrow** | Escritura de archivos Parquet |
| **Python-dotenv** | Manejo de variables de entorno |
| **Logging** | Registro de eventos y debugging |

---

## 📂 Estructura del Proyecto

```
Pipeline-API-REST/
├── config.py               # Configuración y variables de entorno
├── ingest.py               # Extracción de datos con retry
├── transform.py            # Transformaciones para cada tabla
├── etl-API.py              # Orquestador principal del pipeline
├── exploracion.ipynb       # Notebook de exploración de datos
├── output/                 # Datos procesados
│   ├── categories.parquet
│   ├── brands.parquet
│   ├── suppliers.parquet
│   ├── warehouses.parquet
│   ├── products.parquet
│   ├── inventory.parquet
│   ├── customers.parquet
│   ├── promotions.parquet
│   ├── orders.parquet
│   ├── order_items.parquet
│   ├── reviews.parquet
│   └── orders/             # Órdenes particionadas
│       └── {year}/{month}/
├── .env                    # Variables de entorno (no versionado)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/Pipeline-API-REST.git
cd Pipeline-API-REST
```

### 2. Crear entorno virtual

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuración

### Variables de Entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
EMAIL=tu_email@ejemplo.com
API_TOKEN=tu_token_aqui
API_BASE_URL=https://iansaura.com/api
```

> ⚠️ **IMPORTANTE**: Nunca subas el archivo `.env` a git. Está incluido en `.gitignore`.

---

## 🚀 Uso

### Ejecutar el pipeline completo

```bash
python etl-API.py
```

### Explorar los datos

Abrir `exploracion.ipynb` en Jupyter o VS Code para analizar la estructura de cada tabla.

---

## 📊 Tablas Procesadas

El pipeline procesa 11 tablas de un sistema de e-commerce:

| Tabla | Descripción | Transformaciones Principales |
|-------|-------------|------------------------------|
| `categories` | Categorías de productos | Manejo de nulls, tipos category |
| `brands` | Marcas | Optimización a category |
| `suppliers` | Proveedores | Normalización de email, rating a float32 |
| `warehouses` | Depósitos | Optimización de enteros a int32 |
| `products` | Productos | Conversión de fechas, precios a float32 |
| `inventory` | Inventario | Fechas de restock, niveles de stock |
| `customers` | Clientes | 3 columnas de fecha, segmentos |
| `promotions` | Promociones | Fechas inicio/fin, tipos de descuento |
| `orders` | Órdenes | Fecha, status, métodos de pago |
| `order_items` | Items de órdenes | IDs nullable, precios optimizados |
| `reviews` | Reseñas | Rating a float16, fechas |

---

## ✨ Características Principales

### 🔄 Retry Automático con Exponential Backoff

El pipeline implementa reintentos inteligentes en `ingest.py`:

```
Intento 1 falla → Esperar 2 segundos
Intento 2 falla → Esperar 4 segundos
Intento 3 falla → Esperar 8 segundos
```

### 📊 Logging Profesional

Logging estructurado con diferentes niveles:

```
2026-01-10 20:43:32,037 - INFO - Fetching 1000 rows of ecommerce data...
2026-01-10 20:43:32,690 - INFO - Table: categories
2026-01-10 20:43:32,693 - INFO - Transforming data...
```

### 🔒 Manejo Seguro de Secrets

- Variables de entorno via `.env` y `python-dotenv`
- Validación de configuración en `config.py`
- `.gitignore` configurado correctamente

### 📁 Almacenamiento en Parquet

- Formato columnar eficiente para analytics
- Compresión automática
- Órdenes particionadas por `year/month` para queries eficientes

---

## ⚠️ Manejo de Errores

| Código | Causa | Acción |
|--------|-------|--------|
| `Timeout` | Red lenta | Reintentar con backoff |
| `429` | Rate limit | Esperar y reintentar |
| `500` | Error del servidor | Reintentar con backoff |
| `401` | Token inválido | ❌ NO reintentar - revisar token |
| `404` | Endpoint no existe | ❌ NO reintentar - revisar URL |

### Errores Comunes a Evitar

- ❌ Hardcodear tokens en el código
- ❌ No manejar errores de conexión
- ❌ No implementar reintentos
- ❌ Olvidar timeouts en requests

---

## 📊 Outputs

```
output/
├── categories.parquet      (10 registros)
├── brands.parquet
├── suppliers.parquet       (8 registros)
├── warehouses.parquet      (5 registros)
├── products.parquet        (100 registros)
├── inventory.parquet       (195 registros)
├── customers.parquet       (334 registros)
├── promotions.parquet      (10 registros)
├── orders.parquet          (1000 registros)
├── order_items.parquet     (3031 registros)
├── reviews.parquet         (200 registros)
└── orders/
    ├── 2023/
    ├── 2024/
    ├── 2025/
    └── 2026/
```

---

## 💡 Lecciones Aprendidas

> *"El manejo de errores es el 80% del código de producción - el happy path es solo el 20%"*

### Principales Aprendizajes

1. **Exponential Backoff es esencial**: Sin él, saturás la API cuando hay problemas
2. **Logging estructurado**: Hace debugging 10x más fácil que print statements
3. **Variables de entorno**: Nunca, NUNCA hardcodear secrets
4. **Parquet > CSV**: Mejor compresión, tipos de datos preservados, más rápido
5. **Particionamiento**: Facilita queries y organiza datos históricos

---

## 👤 Autor

**Tomás** - Data Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue.svg)](https://linkedin.com/in/tomasamundarain)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black.svg)](https://github.com/tomy07417)

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

⭐ Si este proyecto te fue útil, ¡dejá una estrella!
