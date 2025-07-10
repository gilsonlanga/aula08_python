from etl import pipeline_calcular_kpi_de_vendas_consolidado

pasta = 'data'
formato_de_saida: list = ["csv"] #["csv", "parquet"]

pipeline_calcular_kpi_de_vendas_consolidado(pasta, formato_de_saida)