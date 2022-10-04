# Premier League 22/23 Forwards Stats

A dynamic RMarkdown project aiming to visualize the statistical performance of Premier League Forwards 2022/23.

## Prerequisites

Install Python, R, and RStudio to use the files.

To run the setup.py, install these libraries.

```
pip install time
pip install pandas
pip install numpy
pip install tqdm
```
## Running the Scripts

To run the program go through the following steps.

### Clonning theRepository
First clone the repository.
```
https://github.com/pparthiv/Premier-League-22-23-Forwards-Stats.git
```

### setup.py
Run the setup.py to update the player table to the latest version. The downloading time depends on the internet speed and may take longer on slower speeds.
You can use the software without updating the tables as well.

![setup.py](./Assets/setup.png)

After updating the table, you may run the .Rmd file to see the visualizations.

### PremierLeagueFWsStats.Rmd
This is the RMarkdown file which is responsible for projecting the visuals.

Before running the .Rmd file, install the following libraries in RStudio.

```
install.packages(c("tidyverse","dplyr","fmsb","shiny","DT","ggplot2","plotly"))
```

After doing so, open the .Rmd file with RStudio and run the document.

![PremierLeagueFWsStats.Rmd](./Assets/document.png)

And that is it. Now you can view the visualizations and see the statisical performances of Premier League 2022/23 Forwards. 

![PremierLeagueFWsStats.Rmd](./Assets/final.png)

## Source

All the data has been made available by [FBRef](https://fbref.com) (provided by [StatsBomb](https://statsbomb.com/)).
