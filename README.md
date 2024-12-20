# MoSnoPro-US 🏔️❄️
MoSnoPro-US stands for Modeling Snow Properties - Using SUMMA, a modeling and visualization tool for snow pack properties using real-time (and possibly forecasted) observations in Washington State, USA. This repository contains the code necessary to locally host an interactive tool for visualizing SUMMA output at some key locations in Western Washington State to convey possible instabilities within the snowpack.

Check out the deployed app [here](https://mosnopro-us.streamlit.app/)!

### **Key directory structure**
- `examples/`: This contains an example of running the project. It also contains example visualizations of snowpack density and temperature that are key features for avalanche forecasting.
- `data/`: This directory holds the multi-source data files used in the project. It also contains a folder of outdated data that can be accessible without secret Dropbox access codes.
- `docs/`: This directory contains our component and functional specification documents, presentation files, as well as project-planning materials for internal management.
- `src/`: This directory houses the visualization tool (`app.py`) and all the components needed to run it.
	- `src/mosnopro_us`: This directory holds all the components needed to run the app.
	- `src/mosnopro_us/test/`: This directory holds all files needed to run tests.

### **Getting started:**
This is all executed via the command line.
1. Clone the repo using `git clone [insert SSH link]`.
2. Set MoSnoPro-US/ as your working directory.
3. Set up the environment using `conda env create -f zenvironment.yml`. 
	- *Note*: the odd name (`zenvironment.yml`) is used because Streamlit does not have enough host memory to run conda. It instead uses `pip` to install packages using the `requirments.txt` file.
4. Initialization of the project will be built-in to the `pyproject.toml` file. No explicit step needed to execute here.
5. To run the Streamlit app, use `streamlit run src/app.py`.
6. Happy mapping! _For users interested in building on top of this project, please contact the authors to access raw SUMMA data._

### **Team:**
Danny Hogan, Civil and Environmental Engineering (lead)  
Bow Sruangsaeng Chaikasetsin, Civil and Environmental Engineering  
Xinya Tang, iSchool  
Jane Dai, School of Public Health  

#### Contribution Taxonomy (initials)
- Wrote python functions (DH, BS)
- Wrote tests (DH, BS, XT, JD)
- Human centered design (JD, BS)
- Wrote documentation (JD)
- Set up packaging (DH, BS)
- Set up CI (DH, BS)
- Code review (XT)
