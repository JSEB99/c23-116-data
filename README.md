<H1>Fraud Eye</H1>
</BR>
<H3>¡Somos el Equipo C23-116-Data y les presentamos nuestro MVP!</H3>
</BR>
<H2>Análisis Descriptivo y Predictivo de Transacciones para Detección de Fraudes</H2>

## **Descripción y objetivo del proyecto:**

### Situación inicial

Nuestro cliente, una plataforma de **e-commerce**, identificó un problema creciente: **fraudes con tarjetas de crédito** en transacciones realizadas en su plataforma. Aunque el número de fraudes no era extremadamente alto, el impacto financiero y la reputación de la empresa estaban en juego. Para abordar este desafío, nos pidieron analizar los datos de transacciones recopilados, con dos objetivos claros:

1. **Entender el comportamiento de las transacciones y los fraudes**.
2. **Desarrollar un modelo predictivo** que permitiera identificar transacciones potencialmente fraudulentas en tiempo real.

</BR>

## **Análisis y hallazgos clave**

Para resolver el problema, realizamos un **análisis descriptivo y exploratorio** de los datos, centrándonos en identificar patrones y tendencias que pudieran indicar fraudes. Estos fueron los insights más relevantes:

### 1. **Temporalidad de los fraudes**

- Analizamos las transacciones por mes, día y hora, y descubrimos que los fraudes ocurrían con mayor frecuencia en **horarios específicos** (especialmente en la madrugada) y durante **ciertos días de la semana**.
- Los gráficos de transacciones totales vs. transacciones fraudulentas mostraron picos significativos en estos períodos, lo que nos permitió identificar momentos críticos para monitorear.

### 2. **Geografía y demografía**

- Al visualizar la localización geográfica de las transacciones, identificamos **estados con mayor concentración de fraudes por cada mil habitantes**. Esto sugirió que ciertas regiones podrían ser focos de actividad fraudulenta.
- En cuanto a correlación entre densidad de población y fraudes, según se demuestra, aumentan los fraudes en cuanto a **cantidad de habitantes**.
- Además, al cruzar datos de edad y género, encontramos que **ciertos grupos demográficos** tenían una mayor incidencia de fraudes, lo que nos permitió segmentar y enfocar mejor las estrategias de prevención.

### 3. **Categorías de negocio**

- Los gráficos de fraudes por categoría de negocio revelaron que **algunos tipos de comercios** eran más propensos a sufrir fraudes. Este hallazgo fue crucial para recomendar medidas específicas en esos sectores.

</BR>

## **Solución predictiva**

Con estos insights, no solo logramos entender el comportamiento de los fraudes, sino que también desarrollamos un **modelo predictivo** utilizando **GradientBoost XGBoost**. Este modelo permite:

- **Evaluar en tiempo real** si una transacción tiene características que podrían indicar un fraude.
- **Priorizar la revisión** de transacciones sospechosas, reduciendo el riesgo y optimizando los recursos del equipo de seguridad.

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
