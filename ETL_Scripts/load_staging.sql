-- Sample ETL SQL to load staging data
BULK INSERT StagingSales
FROM 'C:\\data\\sales.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);