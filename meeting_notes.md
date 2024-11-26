## 11-26
**Organizing model output**
- Danny is working on a script that could auto-update figures, most have been updated in the /src/figures folder. Good that the model is performing relatively well (with the exception of Stevens Pass)!
**Flowchart of data inputs/outputs**
See /docs/dataputs.png. Output is currently for the entire snowpack
- Figures take 7-8s to generate (for every new thing that is made), so we could have the code directly in to the server, or just have a separate set of code grab the figure (but this can't be manipulated since it's just a photo file)
  - Size is ~50 mb?
  - Text box highlights from point-click feature: instead of ennumerating number of concerning layers, just mention if there is presence of sandwich layers and what depth they might be at. (Keep it simple. But prioritize former over the latter.)
- Tradeoffs are with customizability from the user. No huge downside to waiting for things to load, unless fast response is the priority. Scraping where it's hosted elsewhere would be the most efficient (but least information dense). Also requires a dependency (or recreate a separate function)
- From a learning perspective, probably better to work with the real data and deal with the time lag. We can practice test-driven development.
**Next steps**
- Bow: integrate with Streamlit, play around with sample data and figures.
- Danny: get all the data set up to be piped into Streamlit. Put sample figures up as Output. Put example data as well + processing code. 
- Jane: Refit repo to project structure specifications.
-   Documentation? Brainstorm ideas for tests.
-   Make sure we have tests set up for receiving/processing valid output. What errors are raised? Exceptions to start off since it does take a while to run Streamlit.
-   Drop in tech review slide deck.
- Tuesday: We'll walk through the entire structure and provide insights into what has been done
- Thursday: Refine other features and work on tests

## 11-21
**Group-work during class**
- Note from Bryna: can be helpful to start high-level and work downwards to identify/specify the bit-sized components
- Focused on creating and merging changes to the *new* `component_specifications` file in /docs

## 11-19
**Brainstorming site infrastructure**
- SUMMA is pulling weather data, but it can also be fed directly into the site (eg, weather, humidity) for users to access
- Front-end should only really have spatial data: color/shape can be determined by specific attributes
- Clicking on the location -> give access to the file where all the data are pulled from, so this wouldn't require a complete re-run when each feature layer is processed
- Feature layers/added components (?):
-   Forecast
-   Real observations (instead of smoothed lines)
- The general view is L-shaped, with a larger bottom rung:
-   Sidebar for map feature layers / model features that want to be shown on the bottom panel
-   Map in the center that has points for stations ("At site X, snow is expected to be Y deep, watch out for [instability at Z-depth], point out layers for concern. Check out NWAC for safety guidelines.) in a type of tl;dr caption

## 11-05 
**Component design**
Note: starting next week Dave will look into our repos and assess progress towards completing component specification for each user
See slides for template on how to specify components
At minimum, should include: 
- Name
- What it does
- Inputs
- Outputs
- Components used
- Side effects

## 10-31 
**Use cases**
[] Identify 30 user stories, iterate throughout the next month. Can all be “similar” (10 different kinds of graduate students)
[] Describe relevant use cases
[] Develop component specifications

