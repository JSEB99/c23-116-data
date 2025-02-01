<H1>Fraud Eye</H1>
</BR>
<H3>¡Somos el Equipo C23-116-Data y les presentamos nuestro MVP!</H3>
</BR>
<H2>Análisis Descriptivo y Predictivo de Transacciones para Detección de Fraudes</H2>

## **Descripción y objetivo del proyecto:**

### Situación inicial

Nuestro cliente, una plataforma de **e-commerce**, identificó un problema creciente: **fraudes con tarjetas de crédito** en transacciones realizadas en su plataforma. Aunque el número de fraudes no era extremadamente alto, el impacto financiero y la reputación de la empresa estaban en juego. Para abordar este desafío, nos pidieron analizar los datos de transacciones recopilados, con dos objetivos claros:

1️⃣ **Entender el comportamiento de las transacciones y los fraudes**.

2️⃣ **Desarrollar un modelo predictivo** que permitiera identificar transacciones potencialmente fraudulentas en tiempo real.

> [!NOTE]
> Fuente del proyecto: [Kaggle dataset](https://www.kaggle.com/datasets/kartik2112/fraud-detection?select=fraudTrain.csv)

> [!IMPORTANT]
> Los datos que se usaron no son exactamente los mismos, se editaron, limpiaron y transformaron para subirse a la base de datos. Como tal ocupan *todo el año 2019*

</BR>

## **Diccionario de datos**

| Nombre de la columna         | Tipo de dato          | Descripción |
|-----------------------------|----------------------|-------------|
| `id`                        | `INT`                | Identificador único de la transacción. |
| `trans_date_trans_time`     | `DATETIME`           | Fecha y hora en la que ocurrió la transacción. |
| `cc_num`                    | `BIGINT`             | Número de la tarjeta de crédito utilizada en la transacción. |
| `merchant`                  | `VARCHAR(255)`       | Nombre del comerciante donde se realizó la transacción. |
| `category`                  | `VARCHAR(50)`        | Categoría del comercio donde se realizó la transacción. |
| `trans_amount`              | `DECIMAL(10,2)`      | Monto de la transacción en dólares. |
| `first_name`                | `VARCHAR(50)`        | Nombre del titular de la tarjeta. |
| `last_name`                 | `VARCHAR(50)`        | Apellido del titular de la tarjeta. |
| `gender`                    | `CHAR(1)`            | Género del titular de la tarjeta (`M` = Masculino, `F` = Femenino). |
| `street`                    | `VARCHAR(255)`       | Dirección del titular de la tarjeta. |
| `city`                      | `VARCHAR(100)`       | Ciudad de residencia del titular de la tarjeta. |
| `state_code`                | `CHAR(2)`            | Código del estado en el que reside el titular de la tarjeta. |
| `zip`                       | `VARCHAR(10)`        | Código postal del titular de la tarjeta. |
| `latitude`                  | `DECIMAL(9,6)`       | Latitud de la ubicación de residencia del titular. |
| `longitude`                 | `DECIMAL(9,6)`       | Longitud de la ubicación de residencia del titular. |
| `city_population`           | `INT`                | Población de la ciudad donde reside el titular de la tarjeta. |
| `job`                       | `VARCHAR(100)`       | Profesión del titular de la tarjeta. |
| `dob`                       | `DATE`               | Fecha de nacimiento del titular de la tarjeta. |
| `trans_num`                 | `VARCHAR(50)`        | Identificador único de la transacción. |
| `unix_time`                 | `BIGINT`             | Timestamp de la transacción en formato UNIX. |
| `merch_lat`                 | `DECIMAL(9,6)`       | Latitud de la ubicación del comerciante. |
| `merch_long`                | `DECIMAL(9,6)`       | Longitud de la ubicación del comerciante. |
| `is_fraud`                  | `BOOLEAN`            | Indica si la transacción es fraudulenta (`true` = fraude, `false` = no fraude). |

## **Análisis y hallazgos clave**

Para resolver el problema, realizamos un **análisis descriptivo y exploratorio** de los datos, centrándonos en identificar patrones y tendencias que pudieran indicar fraudes. Estos fueron los insights más relevantes:

### 1️⃣ **Temporalidad de los fraudes**

- Analizamos las transacciones por mes, día y hora, y descubrimos que los fraudes ocurrían con mayor frecuencia en **horarios específicos** (especialmente en la madrugada) y durante **ciertos días de la semana**.
- Los gráficos de transacciones totales vs. transacciones fraudulentas mostraron picos significativos en estos períodos, lo que nos permitió identificar momentos críticos para monitorear.

### 2️⃣ **Geografía y demografía**

- Al visualizar la localización geográfica de las transacciones, identificamos **estados con mayor concentración de fraudes por cada mil habitantes**. Esto sugirió que ciertas regiones podrían ser focos de actividad fraudulenta.
- En cuanto a correlación entre densidad de población y fraudes, según se demuestra, aumentan los fraudes en cuanto a **cantidad de habitantes**.
- Además, al cruzar datos de edad y género, encontramos que **ciertos grupos demográficos** tenían una mayor incidencia de fraudes, lo que nos permitió segmentar y enfocar mejor las estrategias de prevención.

### 3️⃣ **Categorías de negocio**

- Los gráficos de fraudes por categoría de negocio revelaron que **algunos tipos de comercios** eran más propensos a sufrir fraudes. Este hallazgo fue crucial para recomendar medidas específicas en esos sectores.

### 4️⃣ **Perfil del cliente**

- Los gráficos de fraudes por perfil del cliente, revelaron una paridad entre hombres y mujeres, con una mayoría de fraudes efectuados con personas **mayores de 60 años**, separandose de la media, haciendo notable el peso de cuentas con edades avanzadas.

</BR>

## **Solución predictiva**

Con estos insights, no solo logramos entender el comportamiento de los fraudes, sino que también desarrollamos un **modelo predictivo** utilizando **GradientBoost XGBoost**. Este modelo permite:

- **Evaluar en tiempo real** si una transacción tiene características que podrían indicar un fraude.
- **Priorizar la revisión** de transacciones sospechosas, reduciendo el riesgo y optimizando los recursos del equipo de seguridad.

> [!NOTE]
> El modelo funciona en base a los datos entrenados, mas no se re-entrena con datos nuevos

> [!CAUTION]
> El modelo esta establecido según unos criterios y datos recomendados, estos se revelan en el formulario, por lo cual se sugiere seguirlos para un correcto funcionamiento

Además, el informe incluyó gráficos clave como:

- **Transacciones totales vs. fraudulentas** por mes y día de la semana.
- **Fraudes por cada mil transacciones**, segmentados por categoría de negocio y ubicación geográfica.
- **Montos máximos y mínimos** de transacciones fraudulentas.

Estos elementos no solo brindaron claridad sobre el problema, sino que también proporcionaron una **hoja de ruta accionable** para prevenir fraudes en el futuro.

</BR>

## **Conclusión**

Este análisis no solo ayudó al cliente a comprender mejor los patrones de fraude en su plataforma, sino que también le proporcionó una herramienta poderosa para **anticiparse y mitigar riesgos**. Con el modelo predictivo y las recomendaciones basadas en datos, la plataforma está ahora mejor equipada para proteger sus transacciones y mantener la confianza de sus usuarios.

</BR>

## Integrantes

- Juan Sebastian Mora Tibamoso: [GitHub](https://github.com/JSEB99)
- Georgina Máscolo: [GitHub](https://github.com/GeoArg)
- Jairo Ordoñez: [GitHub](https://github.com/jairodpac)

## Tecnologías

<img align="left" alt="Python" width="50px" style="padding-right:10px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"/>
<img align="left" alt="Pandas" width="50px" style="padding-right:10px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pandas/pandas-original-wordmark.svg"/>
<img align="left" alt="Numpy" width="50px" style="padding-right:10px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/numpy/numpy-plain.svg"/>
<img align="left" alt="Scikit-learn" width="50px" style="padding-right:10px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg"/>
<img align="left" alt="SQLAlchemy" width="50px" style="padding-right:10px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlalchemy/sqlalchemy-original-wordmark.svg"/>
<img align="left" alt="PostgreSQL" width="50px" style="padding-right:10px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg"/>
<img align="left" alt="Supabase" width="50px" style="padding-right:10px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/supabase/supabase-original.svg"/>
<img align="left" alt="FastAPI" width="50px" style="padding-right:10px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original.svg"/>
<img align="left" alt="Jupyter" width="50px" style="padding-right:10px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jupyter/jupyter-original.svg"/>
<img align="left" alt="Streamlit" width="50px" style="padding-right:10px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/streamlit/streamlit-plain-wordmark.svg"/>

<br clear="left">

## Arquitectura

<div style="display: flex; justify-content: center; align-items: center; width: 100%;">
    <img style="width: 95%;" src="/images/architecture.png" />
</div>

## Instrucciones

> [!TIP]
> El proyecto esta estructurado en directorios con las tareas especificas, todo esto para evitar conflictos entre las tareas:
> - frontend: interfaz de usuario del proyecto, interactua internamente con el API y Base de Datos
> - app: desarrollo de la API, de manera local sería otra tarea a ejecutar para el funcionamiento general
> - sql: contiene el esquema de la base de datos, de manera local estaría presente en la creación y almacenamiento de la información
> - notebooks: desarrollo del análisis para el desarrollo del modelo predictivo
> - scripts: funcionalidades de python de apoyo
> - models: empaquetados para ejecución del modelo predictivo
> - images: imagenes utilizadas
> - data: directorio para almacenamiento de archivos csv (no se suben a github para no sobrecargar el proyecto)

- Para poder ejecutar correctamente este proyecto de manera `local` se deben seguir los siguientes pasos:

1️⃣ Crear y cargar la información a una base de datos:
- Se trabajo con `PostgreSQL`, si se usa otro motor se recomienda revisar la documentación del motor seleccionado ya que puede cambiar el modo de conectarse
- Modificar las conexiones de la base de datos con las credenciales que obtengas de tu base de datos

2️⃣ En el directorio `app/` para el uso de la **API**:
- Crear ambiente virtual, ejemplo con Windows y en *powershell*: `python -m venv .env`
- Activar ambiente virtual, ejemplo con Windows y en *powershell*: `.\.env\Scripts\Activate.ps1`
- Instalar librerias del archivo `requirements.txt`, ejemplo con Windows y en *powershell*: `pip install -r requirements.txt`
- Ejecutar *API*, Existen dos formas de ejecutarlo esta forma es una de ellas y es la mas actual según la documentación en [FastAPI](https://fastapi.tiangolo.com/tutorial/), ejemplo con Windows y en *powershell*: `fastapi dev main.py`

3️⃣ En el directorio `frontend/` para el uso de la **Interfaz UI**:
- Crear ambiente virtual, ejemplo con Windows y en *powershell*: `python -m venv .env`
- Activar ambiente virtual, ejemplo con Windows y en *powershell*: `.\.env\Scripts\Activate.ps1`
- Instalar librerias del archivo `requirements.txt`, ejemplo con Windows y en *powershell*: `pip install -r requirements.txt`
> [!IMPORTANT]
> Si es de manera local, se deben modificar las conexiones a la base de datos y api para que streamlit se pueda conectar correctamente a las fuentes deseadas.
- Ejecutar *streamlit*, ejemplo con Windows y en *powershell*: `streamlit run 0_🏡_home.py`

> [!WARNING]
> Se pueden presentar inconvenientes debido a que ambos usan `localhost` para desplegarse y si el puerto llega a ser el mismo. Se debe revisar la documentación de cada servicio para que se despliegue localmente con un puerto deseado.

> [!TIP]
> Si se quiere ejecutar en algun servidor se recomienda:
> - Para la base de datos usamos supabase, en este caso si subes la data a este servidor, deberias modificar las credenciales que te ofrecen de tu base de datos.
> - Para la API se uso render, en este caso puedes tener la **API** en un repositorio de *GitHub*, y mediante *GitHub* conectarla a [Render](https://render.com/) para desplegar el **API**, en este caso sería editar en el código la url del api que tengas desplegada
> - Para streamlit, en este caso sería subir a *GitHub* el proyecto y de ahi conectarla streamlit cloud platform. Se deben añadir los **secretos de streamlit**, que en este caso serían las credenciales que usara la base de datos y la API, si quieres mantener el esquema del código que obtenga los datos de este medio y no plasmarlos textualmente en el código.
