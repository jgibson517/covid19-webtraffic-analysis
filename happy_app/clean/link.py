from .clean_analytics import TrafficData, LanguageData
from .clean_covid_data import CovidData

# # load data for test run
# covid = pd.read_csv("data/cleaned_covid_data.csv")
# # make sure your api key is set for this function to run
# fetch_analytics = get_analytics_by_agency(
#     AGENCY_NAME["HHS"], ("2021-01-01", "2021-12-31"), REPORT_NAME["SITE"]
# )

# analytics_test_data = clean_and_sum(fetch_analytics)


# def merge_data(analytics_data, aux_data, save_locally=False):
#     """
#     Merge cleaned Analytics.gov dataset with COVID-19 dataset

#     - Work out how this should be automated.
#     """
#     merged_data = pd.merge(analytics_data, aux_data, on="date", how="inner")
#     merged_data.date = pd.to_datetime(merged_data.date, yearfirst=True)

#     if save_locally:
#         merged_data.to_csv("data/merged_test_dataset.csv")

#     return merged_data

# Add optional argument to pass in periods to analyze traffic source
def collect_analytics_data(agency, years, report_type, sites):
    """
    Collects and cleans data on website visits, browser langague,
    and traffic source for use in visualizations

    """
    all_visits = TrafficData(agency, years, report_type)

    # Fetch data from the API
    all_visits.fetch_data()

    # Divide into yearly dataframes
    all_visits.split_by_year()

    # Collect visits by year
    all_visits.sum_by("week")

    # Count visits to all sites by week
    all_visits.sum_by("week", aggregate=True)

    # Subsets weekly data by key sites to track
    all_visits.find_sites(sites)

    all_visits.export()

    language = LanguageData(agency, years)

def collect_covid_data():
    '''
    Collects and clean COVID-19 data
    '''
    covid = CovidData()

    