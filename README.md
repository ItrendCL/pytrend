# pytrend

La librería Python for Itrend (pytrend) permite acceder a los distintos conjuntos de datos de la Plataforma de Datos de Itrend. La librería es completamente abierta, pero para acceder a los datos se requieren credenciales de acceso administradas por Itrend propiamente tal.

![itrend logo](https://itrend.cl/wp-content/uploads/2019/11/logo-color.svg "Itrend")

- **Autor**: [Sebastián Castro](https://github.com/sebacastroh)
- **Version**: 1.0.0
- **Fecha**: 02 de Mayo de 2022

## Requisitos

- Python 3.7+
- [urllib](https://docs.python.org/3/library/urllib.html "urllib")
- [requests](https://requests.readthedocs.io/en/latest/ "requests")

Para acceder a la descarga de datos y metadatos se requieren credenciales de acceso, las cuales se obtienen a través de la [Plataforma de Datos](https://www.plataformadedatos.cl/user/developer "Plataforma de Datos").

## Ejemplos

### Configuración de credenciales
```python
import pytrend

session = pytrend.itrend_developer_tools()

session.set_credentials(
    access_key_id = '',    # Ingresa tu access_key_id
    secret_access_key = '' # Ingresa tu secret_access_key
)
```

### Obtener formatos disponibles de un conjunto de datos
```python
dataset_id = '492F65B350AAF9D1' # Base de datos histórica de cicatrices de incendios chilenos - 1. Resumen
formats = session.get_dataset_formats(dataset_id)
```

### Obtener formatos disponibles de los elementos de una colección
```python
dataset_id = 'ZW5TFERBT8B0GMQ' # Registro de eventos sísmicos significativos
element_formats = session.get_element_formats(dataset_id)
```

### Descargar un conjunto de datos
```python
dataset_id = '40JUKMAQLGUV53P' # División Política Administrativa a nivel comunal
fmt = 'shp'
response = session.download_file(dataset_id, fmt)
filename = response.get('filename')
delimiter = response.get('delimiter') # Útil cuando se descarga un csv
```

### Descargar un elemento de una colección
```python
dataset_id = '472AE6E9AD343E6'
collection_id = 'ID'
fmt = 'csv'

# Descargamos y leemos la tabla
response = session.download_file(dataset_id, fmt)
filename = response.get('filename')
delimiter = response.get('delimiter')
df = pd.read_csv(filename, delimiter)

# Descargamos un elemento
element_formats = session.get_element_formats(dataset_id)
efmt = element_formats[0] # Escoger el formato que más le acomode

for r, row in df.iterrows():
    element_id = str(row[collection_id])
    element_response = session.download_file(dataset_id, efmt, element_id)
    break
```
