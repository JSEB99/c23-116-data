--- trimestre con más transacciones
SELECT
    DATE_PART('quarter', trans_date_trans_time) AS trimestre,
    COUNT(*) AS total_transacciones
FROM transactions
GROUP BY trimestre
ORDER BY total_transacciones DESC;

--- mes con más transacciones -- 
SELECT
    DATE_PART('month', trans_date_trans_time) AS mes,
    COUNT(*) AS total_transacciones
FROM transactions
GROUP BY mes
ORDER BY total_transacciones DESC;

--- día de la semana con más transacciones
SELECT
    CASE
        WHEN DATE_PART('dow', trans_date_trans_time) = 0 THEN 'Domingo'
        WHEN DATE_PART('dow', trans_date_trans_time) = 1 THEN 'Lunes'
        WHEN DATE_PART('dow', trans_date_trans_time) = 2 THEN 'Martes'
        WHEN DATE_PART('dow', trans_date_trans_time) = 3 THEN 'Miércoles'
        WHEN DATE_PART('dow', trans_date_trans_time) = 4 THEN 'Jueves'
        WHEN DATE_PART('dow', trans_date_trans_time) = 5 THEN 'Viernes'
        WHEN DATE_PART('dow', trans_date_trans_time) = 6 THEN 'Sábado'
    END AS dia_semana,
    COUNT(*) AS total_transacciones
FROM transactions
GROUP BY DATE_PART('dow', trans_date_trans_time)
ORDER BY total_transacciones DESC;

--- transaciones más comunes por segmnento
SELECT
    category,
    COUNT(*) AS total_transacciones
FROM transactions
GROUP BY category
ORDER BY total_transacciones DESC
LIMIT 10;

--- transaciones más comunes por segmento y cuantas son fraude y cuantos no
WITH top_categories AS (
    SELECT
        category,
        COUNT(*) AS total_transacciones
    FROM transactions
    GROUP BY category
    ORDER BY total_transacciones DESC
    LIMIT 10
)
SELECT
    t.category,
    COUNT(*) AS total_transacciones,
    SUM(CASE WHEN is_fraud THEN 1 ELSE 0 END) AS transacciones_fraudulentas,
    SUM(CASE WHEN NOT is_fraud THEN 1 ELSE 0 END) AS transacciones_no_fraudulentas,
    ROUND(100.0 * SUM(CASE WHEN is_fraud THEN 1 ELSE 0 END) / COUNT(*), 2) AS porcentaje_fraudulentas,
    ROUND(100.0 * SUM(CASE WHEN NOT is_fraud THEN 1 ELSE 0 END) / COUNT(*), 2) AS porcentaje_no_fraudulentas
FROM transactions t
WHERE category IN (SELECT category FROM top_categories)
GROUP BY t.category
ORDER BY total_transacciones DESC;

SELECT
    job,
    COUNT(*) AS transaction_count
FROM
    transactions
GROUP BY
    job
ORDER BY
    transaction_count DESC;
--- categorias y trabajos con más transacciones

SELECT
    category,
    COUNT(DISTINCT job) AS job_count,
    STRING_AGG(DISTINCT job, ', ') AS jobs
FROM
    transactions
GROUP BY
    category
ORDER BY
    category;
--- Dias con mas transacciones
SELECT
    CAST(trans_date_trans_time AS DATE) AS transaction_date,
    COUNT(*) AS transaction_count
FROM
    transactions
GROUP BY
    CAST(trans_date_trans_time AS DATE)
ORDER BY
    transaction_date;
-------------------------------------
SELECT
    TO_CHAR(trans_date_trans_time, 'YYYY-MM') AS transaction_month,
    COUNT(*) AS transaction_count
FROM
    transactions
GROUP BY
    TO_CHAR(trans_date_trans_time, 'YYYY-MM')
ORDER BY
    transaction_month;
______________________________________
SELECT
    is_fraud,
    COUNT(*) AS transaction_count
FROM
    transactions
GROUP BY
    is_fraud
ORDER BY
    is_fraud;
---------------------------------
SELECT
    TO_CHAR(trans_date_trans_time, 'YYYY-MM') AS transaction_month,
    is_fraud,
    COUNT(*) AS transaction_count
FROM
    transactions
GROUP BY
    transaction_month, is_fraud
ORDER BY
    transaction_month, is_fraud;

---------------------------------------
consulta aparte
SELECT
    DATE_TRUNC('quarter', trans_date_trans_time) AS transaction_quarter,
    category,
    job,
    is_fraud,
    COUNT(*) AS transaction_count
FROM
    transactions
GROUP BY
    transaction_quarter, category, job, is_fraud
ORDER BY
    transaction_quarter, transaction_count DESC;
--------------------------------
SELECT
    DATE_TRUNC('quarter', trans_date_trans_time) AS transaction_quarter,
    category,
    is_fraud,
    COUNT(*) AS transaction_count
FROM
    transactions
GROUP BY
    transaction_quarter, category, is_fraud
ORDER BY
    transaction_quarter, transaction_count DESC;
----------------------------------------
SELECT
    COUNT(*) AS total_rows
FROM
    transactions;
-----------------------------------------
SELECT
    gender,
    is_fraud,
    COUNT(*) AS total_rows
FROM
    transactions
GROUP BY
    gender, is_fraud
ORDER BY
    gender, is_fraud;
------------------------------------------
SELECT
    CONCAT('Q', EXTRACT(QUARTER FROM trans_date_trans_time), '-', EXTRACT(YEAR FROM trans_date_trans_time)) AS transaction_quarter,
    category,
    is_fraud,
    COUNT(*) AS transaction_count
FROM
    transactions
GROUP BY
    transaction_quarter, category, is_fraud
ORDER BY
    transaction_quarter, transaction_count DESC;