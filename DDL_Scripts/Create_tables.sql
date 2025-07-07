-- Sample SQL: Create dimension and fact tables
CREATE TABLE DimProduct (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Category VARCHAR(50)
);

CREATE TABLE FactSales (
    SaleID INT PRIMARY KEY,
    ProductID INT,
    SaleDate DATE,
    Quantity INT,
    Revenue DECIMAL(10,2),
    FOREIGN KEY (ProductID) REFERENCES DimProduct(ProductID)
);
