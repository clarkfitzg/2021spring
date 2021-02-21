[Hackair](https://www.hackair.eu/)
[WIND](https://www.sciencedirect.com/science/article/pii/S0306261915004237?via%3Dihub/)
[Guidebook on Grid Integration Studies](https://www.nrel.gov/docs/fy20osti/72143.pdf)

# Hackair
* App that lets you access, collect, and improve information about air quality in Europe 
* Users can contribute by building their own sensors, uploading pictures which are processed to estimate air quality
* Geotagged pictures from sources like Instagram are also gathered 
* Data from these unconventional sources are fused with official data (like the data we are looking at) to give estimations of air quality even in places without coverage 

# Wind Integration National Dataset (WIND) Toolkit
* This is a paper on a dataset that is useful for grid integration studies 
* Grid integration studies provide "an analytical framework for evaluating a power system with high levels of variable RE" and "a primary goal of a grid integration study is to address stakeholder concerns that a power system can operate reliably and cost-effectively under high-RE scenarios"
* They would consider things like the reduction in wind speed from other wind farms which is known as the wake effect 
* From the article, "This article describes the creation and validation of a data set that has been especially designed for wind integration studies: the Wind Integration National Dataset, also known as the WIND Toolkit. The WIND Toolkit is a combination of a meteorological data set provided by a mesoscale model, a power data set, and a forecast data set."

# Smokey: Air Quality Bot by Amrit Sharma
* This doesn't seem to be live anymore

# Power from wind: Open data on AWS by Caleb Phillips, Caroline Draxl, John Readey, Jordan Perr-Sauer
* I was able to successfully 

# Wind Visualization by Jordan Perr-Sauer
This tool can be useful during our initial setup of our wind data because it would allow us to view values to ensure it's working. However, beyond that this tool is simply a Javascript visualization of the WIND data but doesn't provide any additional usage.

# Mapping urban air pollution using GIS: a regression-based approach
https://www.tandfonline.com/doi/abs/10.1080/136588197242158
>Traditionally, two general approaches to air pollution mapping can be identified:
spatial interpolation and dispersion modelling (Briggs 1992). The former uses statistical or other methods to model the pollution surface, based upon measurements at
monitoring sites. With the development of GIS and geostatistical techniques in recent
years, a wide range of spatial interpolation methods have now become available.
Burrough (1986) divides these into global methods (e.g., trend surface analysis),
which fit a single surface on the basis of the entire data set, and local methods (e.g.,
moving window methods, kriging, spline interpolation) in which a series of local
estimates are made, based on the nearest data points. Recently, particular attention
has tended to focus on kriging in its various forms (e.g., Oliver and Webster 1990,
Myers 1994). Nevertheless, despite a number of studies comparing this with other
techniques (e.g., Abbass et al. 1990, Dubrule 1984, Laslett et al. 1987, von Kuilenburg
et al. 1982, Weber and Englund 1992, Knotters et al. 1995), there is no clear consensus
to suggest that any one approach is universally optimal. Instead, performance of the
various methods tends to vary depending upon the character of the underlying
spatial variation being modelled, and the speci®c characteristics of the data concerned
(e.g., sampling density, sampling distribution).

In this study they used multiple input variables. For example
* Road network: All access roads within the study area
* Road type: Classifcation of road on basis of population served
* Distance to road: Distance to nearest road serving > 25000 people
* Land cover NO2 concentration Mean NO2 concentration (by survey period, and modelled annual mean)
* Topographical exposure: Mean difference in altitude between each pixel and the eight surrounding pixels