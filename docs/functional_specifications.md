# Functional Specificaiton
## Background
Avalanche forecasts rely on an accurate understanding of internal snowpack properties (temperature, density, etc.) to effectively communicate hazards to transportation and recreation in mountain environments. However, observations of internal snowpack properties are relatively few and far between since they require avalanche professionals to go into the field to take measurements. MoSnoPro-US offers a solution by providing estimates important snowpack properties in an accessible format. The tool provides near-real time model results from a physically-based 1-D snow model driven by remote weather observations. This provides a way to remotely "see" into the snowpack to track internal snowpack changes that are difficult to capture across a broad area. 

## User Profiles

### 1. Data Analyst

**Alex** is a data analyst at a transportation agency. He uses data on snowfall and its impact on road conditions to generate reports for decision-makers. Alex wants an application that simplifies filtering, visualizing, and extracting key patterns from large datasets, such as snowplow performance and accident trends. He has moderate programming skills and prefers an interface with intuitive controls and minimal setup. His primary need is interactive dashboards that help him explore correlations and export visuals for reports.

---

### 2. Graduate Student in Transportation Engineering

**Maria** is a graduate student researching the impact of snowstorms on road safety and traffic flow. She works with datasets from sensors and weather reports to develop insights for winter road maintenance strategies. Maria has basic programming experience and needs a tool that allows her to upload and analyze datasets quickly. She values interactive visualizations, such as time-series data of road conditions, and would like features that suggest possible interventions for safer winter roads.

---

### 3. Traffic Engineer

**James** is a traffic engineer responsible for ensuring road safety and maintaining traffic flow during snow events. He uses weather and traffic data to evaluate snowplow schedules, salt usage, and accident hotspots. James is not familiar with programming and relies on user-friendly software to analyze data. He needs an application that provides clear, actionable insights into road conditions, such as snowplow activity and accident trends, and allows for easy report generation to communicate with decision-makers.

---

### 4. Software Developer

**Priya** is a software developer maintaining a suite of tools for transportation analytics. She integrates weather and traffic data to create applications for snow management systems. Priya is proficient in Python and APIs, but she’s not an expert in transportation engineering. She needs a tool with a well-documented programming interface, allowing her to customize and integrate the MoSnoPro-US features into existing systems. She values flexibility, scalability, and ease of debugging when working with large datasets, such as traffic incidents during snowstorms.

---

### 5. Decision Maker/Manager

**Ethan** is a senior manager at a state department of transportation. He oversees resource allocation for snowplow operations and winter road maintenance. Ethan is not technical and relies on summary dashboards and visualizations to guide his decisions. He needs an application that provides key insights, such as snowplow coverage, road condition trends, and cost-efficiency metrics. The ability to quickly export visuals to presentation-ready formats like PDF or Excel is crucial for communicating with stakeholders and securing funding.

### 6. Avalanche Forecaster

**Dallas** is an avalanche forecaster at the Northwest Avalanche Center. He wants to remotely access snowpack information daily to better understand how the snowpack responds to overlying weather conditions. Dallas is very proficient in snow and meteorology but has little time to sift through large datasets. His primary need is a concise, high-quality interface that provides critical snowpack updates.

---

### 7. Snowboarder

**Cassie** is an avid snowboarder new to the region with prior experience in Colorado. She wants an application to better understand the local snowpack and how it changes over the winter, helping her decide when conditions are optimal for skiing. Cassie has experience interacting with snow but lacks technical knowledge in snow science. She prefers an easy-to-use tool with intuitive visuals.

---

### 8. Ski Resort Manager

**Jay** manages a ski resort and wants a simple, up-to-date interface for forecasting snow accumulation to optimize snowcat deployment for grooming trails. He prioritizes accuracy and real-time updates to ensure efficient resource management.

---

### 9. Hydrologist

**Logan** is a hydrologist for the Washington Department of Ecology. He monitors snowpack water content across multiple basins to forecast spring runoff and manage reservoirs. Logan needs precise data and visualizations that summarize basin-scale snowpack conditions, delivered through a professional and user-friendly platform.

---

### 10. Climate Researcher

**Emma** studies climate change impacts on snowpack in the Cascades. She needs access to historical snow model outputs to analyze trends in snow accumulation and melt patterns over past decades. While comfortable with technical data, Emma prefers an interface that overlays trends on maps intuitively.

---

### 11. Backcountry Skier

**Tyler** enjoys backcountry skiing and wants to plan trips based on snow stability and depth. He needs an interactive map that provides forecasted snow depth and stability metrics for specific locations. Tyler values clear, non-technical explanations of avalanche risks linked to the data.

## Data Sources
- Weather data acquired from select remote snow telemetry (SnoTel) stations throughout Washington located near major recreational areas. 
- Snow model output from pySUMMA, a physically-based 1-D snow model which provides output of internal snowpack properties.

## Use Cases


