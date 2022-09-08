<h1>Project: Data Pipelines</h1>


<h3>Introduction</h3>
A music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.

They have decided to bring you into the project and expect you to create high grade data pipelines that are dynamic and built from reusable tasks, can be monitored, and allow easy backfills. They have also noted that the data quality plays a big part when analyses are executed on top the data warehouse and want to run tests against their datasets after the ETL steps have been executed to catch any discrepancies in the datasets.

The source data resides in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source datasets consist of JSON logs that tell about user activity in the application and JSON metadata about the songs the users listen to.



<h3>How to run</h3>

 - Create Redshift cluster on your AWS account
 - Turn on Airflow by running Airflow/start.sh
 - Create AWS and Redshift connections on Airflow Web UI
 - Run create_table_dag DAG to create tables on Redshift
 - Run udac_example_dag DAG to trigger ETL data pipeline


<h3>Dag</h3>
<img width="801" alt="Captura de Tela 2022-09-08 às 16 23 54" src="https://user-images.githubusercontent.com/92527247/189209747-a08c0d0d-4899-4ddb-8a5f-fc6118b5c6c4.png">


<h3>Database</h3>

<img width="723" alt="Captura de Tela 2022-09-08 às 10 49 25" src="https://user-images.githubusercontent.com/92527247/189140276-7e6634a3-b500-4db0-8aab-4bee0378d55d.png">



 
