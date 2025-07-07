# 📈 Data Warehouse Project Enhancement Roadmap

This checklist outlines enhancements to showcase enterprise-grade SQL Server Data Warehouse design, ETL flow, performance, and BI integration.

---

## 🔗 Data Sources & Staging
- [ ] Simulate multiple raw data feeds: CRM, Sales, HR
- [ ] Create staging tables for each source
- [ ] Implement incremental loading logic (MERGE or upsert strategy)

## 📐 Schema Design
- [ ] Create star schema: FactSales, DimCustomer, DimProduct, DimDate
- [ ] Add surrogate keys for all dimension tables
- [ ] Handle Slowly Changing Dimensions (SCD Type 1 and 2)

## 🧰 T-SQL Optimization
- [ ] Use indexes on Fact and Dim tables
- [ ] Partition Fact tables (by date or product)
- [ ] Create views and indexed views for reporting
- [ ] Use stored procedures for repeatable transformations

## 🔁 ETL Strategy
- [ ] Design full and incremental ETL procedures
- [ ] Simulate or outline SSIS equivalent flow
- [ ] Add error logging and auditing mechanism (ETL log table)

## 📊 BI & Reporting Layer
- [ ] Create Power BI dashboards (Sales, Customer trends)
- [ ] Export .pbix files and screenshots to `Reports/`
- [ ] Include basic KPIs: revenue, AOV, churn, etc.

## 🧪 Testing and QA
- [ ] Data quality validation scripts (check nulls, keys, duplicates)
- [ ] Sample test data included in `Sample_Data/`
- [ ] Document transformation logic and test cases

## 📄 Documentation
- [ ] Add ER diagrams and flowcharts to `Diagrams/`
- [ ] Write data dictionary (Fact and Dim descriptions)
- [ ] Update README with updated architecture and usage details

---

## ✅ Optional Advanced Additions
- [ ] Docker setup with SQL Server Express
- [ ] CI/CD using GitHub Actions to test scripts
- [ ] Role-based access modeling (views per team role)
