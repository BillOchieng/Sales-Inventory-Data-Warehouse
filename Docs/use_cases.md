Sales-Inventory-Data-Warehouse/
├── DDL_Scripts/
│   ├── create_tables.sql             # Star schema: fact & dimension tables
│   └── create_indexes.sql            # Indexes for performance tuning
│
├── ETL_Scripts/
│   ├── load_staging.sql              # Load CSVs to staging tables
│   ├── transform_dw.sql              # Populate DW from staging
│   └── scd_type2_handler.sql         # Handle SCD Type 2 changes
│
├── Sample_Data/
│   ├── sales.csv
│   ├── inventory.csv
│   └── customers.csv
│
├── Diagrams/
│   ├── erd.png                       # Entity Relationship Diagram
│   └── etl_flow.png                  # ETL pipeline visual
│
├── Reports/
│   ├── sales_dashboard.pbix         # Power BI report file
│   └── screenshots/
│       ├── sales_kpis.png
│       └── inventory_trends.png
│
├── Metadata/
│   ├── data_dictionary.md            # Table & column descriptions
│   └── etl_log_structure.sql         # Schema for ETL audit logging
│
├── docs/
│   ├── architecture.md               # DW layers and system components
│   └── use_cases.md                  # Business scenarios and benefits
│
├── enhancements.md                  # Enhancement checklist
├── references.md                    # Reference sources
├── futureplans.txt                  # Ideas and next steps
├── README.md                        # Project overview
└── .gitignore                       # Exclude temp/log/BI files
