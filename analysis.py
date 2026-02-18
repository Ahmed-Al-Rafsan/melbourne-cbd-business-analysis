import pandas as pd 
project_file=pd.read_csv(r"A:\\Data\\business-establishments-with-address-and-industry-classification.csv")
print(project_file)
print(project_file.info())
print(project_file.isna().sum().sort_values(ascending=False))
#creating a copy of the main file
project_file_work=project_file.copy()
print(project_file_work.groupby("census_year").size().reset_index(name="establishment_count"))
print(project_file_work.columns)
# Which Melbourne areas have the highest number of business establishments overall?
print(project_file_work.groupby("clue_small_area").size().sort_values(ascending=False))
# How has the number of establishments changed over time (2002–2023)?
print(project_file_work.groupby('census_year').size().sort_index(ascending=True))
# Which industries dominate each area and how does this differ by location?
print(project_file_work.groupby("industry_anzsic4_description").size().sort_values(ascending=False))
# Are there industries that are growing or declining significantly over time?
business_year=project_file_work.groupby(["census_year","industry_anzsic4_description"]).size().reset_index(name="business_establishment")
pivot=business_year.pivot(index="industry_anzsic4_description",columns="census_year",values="business_establishment")
change=pivot["change"]=pivot[2023]-pivot[2002]
print(pivot.sort_values("change",ascending=False).head(5))
#Which areas show the most diversification versus concentration of industries?
print(project_file_work.columns)
print(project_file_work.groupby("industry_anzsic4_description").size().sort_values(ascending=False))