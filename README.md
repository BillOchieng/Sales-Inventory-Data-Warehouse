# Enterprise Data Warehouse for Sales & Inventory Analytics
---

## 🎯 Project Objective
To design a modern, extensible data warehouse system that can:
- Consolidate data from multiple operational sources
- Provide a clean schema for BI tools and analysts
- Enable efficient ETL and reporting processes

---

## 🧱 Architecture Overview
- **Staging Layer**: Raw ingestion tables for initial data loads
- **Data Warehouse Layer**: Star schema with fact and dimension tables
- **ETL Process**: Manual or automated SQL-based transformation scripts
- **BI Layer**: Ready for integration with Power BI, Tableau, or Excel

---

## 🗂️ Project Components
```
Data-Warehouse-with-SQL-Server/
├── DDL_Scripts/         -- SQL scripts for creating schema and tables
├── ETL_Scripts/         -- SQL procedures/functions for data transformations
├── Sample_Data/         -- Mock CSV or SQL data loads
├── Diagrams/            -- ERDs, schema visuals, architecture flows
├── Reports/             -- Sample queries, Power BI screenshots
├── Futureplans.txt      -- Expansion ideas, automation goals
├── README.md
└── References.md
```

---

## 🧠 Key Skills Demonstrated
- Data warehousing best practices (Inmon vs Kimball)
- Dimensional modeling (fact/dimension design)
- SQL optimization for large datasets
- T-SQL stored procedures and views
- Data cleansing and normalization
- BI-ready structuring and report sourcing

---

## 🚀 Implementation Checklist
- [x] Simulated multiple raw data feeds: CRM, Sales, HR
- [x] Staging tables for each source
- [x] Incremental loading logic using `MERGE`
- [x] Star schema design with surrogate keys
- [x] Slowly Changing Dimensions (SCD Type 1 and 2)
- [x] T-SQL stored procedures and transformations
- [x] Views and indexed views for BI
- [x] Fact table partitioning and indexing
- [x] Power BI dashboards (.pbix and screenshots)
- [x] ETL error logging and auditing table
- [x] Data validation scripts (nulls, keys, duplicates)
- [x] ER diagrams and data dictionary

---

## 💼 Use Case Spotlight

### Sales and Inventory Analytics
This data warehouse supports comprehensive business analysis by combining sales performance tracking with inventory monitoring:
- Track daily, monthly, quarterly sales trends
- Analyze revenue by region, product, and customer
- Monitor stock levels, product turnover, and warehouse performance

**Schema Components**:
- `FactSales`, `FactInventory`
- `DimProduct`, `DimCustomer`, `DimRegion`, `DimWarehouse`, `DimDate`

These combined metrics help organizations align supply with demand, optimize product availability, and enhance revenue insights.

---

## 📚 References
- Inmon, W. H. (2005). *Building the Data Warehouse* (4th ed.). Wiley.
- Kimball, R., & Ross, M. (2013). *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling* (3rd ed.). Wiley.
- Microsoft Docs. (n.d.). *SQL Server Data Warehouse Architecture*. https://docs.microsoft.com/sql/analytics-platform-system/data-warehouse-architecture
- TDWI. (2020). *Modern Data Warehouse Best Practices*. https://www.tdwi.org/research/2020/06/rs-modern-data-warehouse.aspx

---

## 📬 Contact
Created by [Bill Ochieng](https://github.com/BillOchieng). Let’s connect on [LinkedIn](https://linkedin.com/in/) or discuss improvements via GitHub Issues.
