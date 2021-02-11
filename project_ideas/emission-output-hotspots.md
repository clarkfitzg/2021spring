[NREL Wind Data](https://registry.opendata.aws/nrel-pds-wtk/)

[OpenAQ PM2.5 Data](https://registry.opendata.aws/openaq/)

An idea of what we could build would be a tool that can cross analyze historical data from these two data sets to identify high polluter areas. 

# NREL Wind data
The WIND Toolkit includes instantaneous meteorological conditions from computer model output and calculated turbine power for more than 126,000 sites in the continental United States for the years 2007–2013. It features three data sets:

- The meteorological data set includes basic information on the weather conditions in each 2-km x 2-km grid cell. The meteorological data set also includes parameters such as wind profiles, atmospheric stability, and solar radiation data in those cells. This complete data set is not yet publicly available, though some of the data is made available with the power data set.

- The power data set was created using the wind data at 100-meter hub height and site-appropriate turbine power curves to estimate the power produced at each of the turbine sites.

- The forecast data set includes forecasts for 1-hour, 4-hour, 6-hour, and 24-hour forecast horizons.

# OpenAQ
The data here is less concrete since the sensors have to be setup and so covered can't be guarenteed. Additionally, because each sensor is it's own device the history from this varies from area to area and sensor to sensor. We would need to analyze the map to determine whether it has enough locations to make a prediction. From my spot checking there are 6 sensors where I live in Cameron Park, 15 in Folsom and 18 in the combined East Sacramento and downtown area.

# Challenges
- OpenAQ inconsistent data
- NREL low resolution wind maps
