library(tidyverse)
library(dplyr)
library(fmsb)
library(DT)
library(ggplot2)
library(plotly)
library(shinydashboard)

path <- 'Leagues/Premier League/prem_fw_py.csv'
prem <- read.csv(path)
prem <- prem[,-1]
rownames(prem) <- prem[,1]
prem <- prem[,-1]

tmp <- data.frame(prem[21,])

prem <- prem[-21,]

prem <- mutate_all(prem, function(x) as.numeric(as.character(x)))

for (i in rownames(prem[-21,])) {
  prem[i,'Max'] <- max(prem[c(i),2:98])
}

for (i in rownames(prem[-21,])) {
  prem[i,'Min'] <- min(prem[c(i),2:98])
}

prem['Team',] <- tmp

radar_chart <- function(name1, name2, name3, name4, name5){
  st1 <- gsub("\\ ", ".", name1)
  st2 <- gsub("\\ ", ".", name2)
  st3 <- gsub("\\ ", ".", name3)
  st4 <- gsub("\\ ", ".", name4)
  st5 <- gsub("\\ ", ".", name5)
  
  v_label <- rownames(prem)
  
  df <- prem[,c('Max', 'Min', st1, st2, st3, st4, st5)]
  df <- t(df)
  df <- data.frame(df)
  df <- mutate_all(df, function(x) as.numeric(as.character(x)))
  
  colr <- c(rgb(0.8, 0, 0, 1),rgb(0, 0.8, 0.8, 1),rgb(1, 1, 0, 1),rgb(1, 0.4, 0, 1),rgb(0, 1, 0.2, 1))
  colr_f <- c(rgb(0.8, 0, 0, 0.5),rgb(0, 0.8, 0.8, 0.5),rgb(1, 1, 0, 0.5),rgb(1, 0.4, 0, 0.5),rgb(0, 1, 0.2, 0.5))
  
  radarchart(df, cglty = 1, pcol = colr, pfcol = colr_f, plwd = 2, plty = 1, vlabels = v_label, vlcex = 0.75)
}

scatter_fw <- function(value1, value2, df){
  df <- df[-c(99:100)]
  df <- t(df)
  df <- data.frame(df)
  df[,-21] <- mutate_all(df[,-21], function(x) as.numeric(as.character(x)))
  df$Name <- gsub("\\.", " ", rownames(df))
  p <- ggplot(df, aes_string(x = value1, y = value2, label = 'Name')) +
    geom_point(aes(color = Team)) +
    geom_smooth(method=lm , se=TRUE) +
    theme(panel.background = element_blank(), panel.grid.major = element_blank(),panel.grid.minor = element_blank(),axis.line = element_line(colour = "black"),panel.border = element_rect(colour = "black", fill=NA, size=0.5)) +
    scale_x_continuous(name = NULL) + scale_y_continuous(name = NULL)
  ggplotly(p, height = 550, width = 1000)
}

avg_comp <- function(value1){
  name <- gsub("\\ ", ".", value1)
  temp <- data.frame(prem[-21,])
  temp <- temp[-c(98:99)]
  temp <- mutate_all(temp, function(x) as.numeric(as.character(x)))
  for (i in rownames(temp)) {
    temp[c(i),] <- rank(temp[c(i),])
  }
  temp <- mutate_all(temp, function(x) as.numeric(as.character(x)))
  
  player <- data.frame(temp[,c(name)])
  player <- mutate_all(player, function(x) as.numeric(as.character(x)))
  colnames(player) <- c(name)
  player$Categories <- rownames(temp)
  
  p <- ggplot(player, aes_string(x=name, y='Categories')) +
    geom_segment(aes_string(x=50.0, xend=name, y='Categories', yend='Categories'), color = "#7aa9ff") +
    geom_point(color = "#faa039", size=3) +
    theme_light() +
    theme(panel.background = element_blank(),axis.line = element_line(colour = "black"),panel.border = element_rect(colour = "black", fill=NA, size=0.5)) +
    scale_x_continuous(name = value1)
  ggplotly(p, height = 550, width = 1000)
}


prem_op <- function(df){
  df <- df[-c(99:100)]
  df <- t(df)
  rownames(df) <- gsub("\\.", " ", rownames(df))
  df <- data.frame(df[-1,])
  DT::datatable(df, options = list(scrollX = TRUE))
}

players <- gsub("\\.", " ", colnames(prem))

ui <- dashboardPage(
  dashboardHeader(
    title = 'Premier League 2022-23 Forwards',
    titleWidth = 400
  ),
  dashboardSidebar(
    sidebarMenu(menuItem("Compare Players", tabName = "comp", icon = icon("person")),
                menuItem("Plot Players by Categories", tabName = "plots", icon = icon("chart-simple")),
                menuItem("Player Performance", tabName = "50th", icon = icon("sliders")),
                menuItem("Data from FBRef", tabName = "table", icon = icon("table")),
                menuItem("github.com/pparthiv", icon = icon("github"))
    )
  ),
  dashboardBody(
    tabItems(
      tabItem("comp",
        box(title = "Radar Plot Comparison",
            status = "success",
            plotOutput("radarPlot"), width = 6, height = 820),
        box(title = "Select Players",
            status = "info",
            selectInput(
              label = 'Player Red',
              'player1',
              choices = players[-c(99:100)]
            ),
            selectInput(
              label = 'Player Blue',
              'player2',
              choices = players[-c(99:100)]
            ),
            selectInput(
              label = 'Player Yellow',
              'player3',
              choices = players[-c(99:100)]
            ),
            selectInput(
              label = 'Player Orange',
              'player4',
              choices = players[-c(99:100)]
            ),
            selectInput(
              label = 'Player Green',
              'player5',
              choices = players[-c(99:100)]
            )
        )
      ),
      tabItem("plots",
              box(title = "Scatter Plot Comparison",
                  status = "success",
                  plotlyOutput("scatter"), width = 8, height = 650),
              box(title = "Select Categories",
                  status = "primary",
                  selectInput(
                    label = "Category (X-axis): ",
                    'cat1',
                    choices = c(
                      "Non-Penalty Goals" = "Non.Penalty.Goals",
                      "Non-Penalty xG" = "Non.Penalty.xG",
                      "Shots Total" = "Shots.Total",
                      "Assists" = "Assists",
                      "xG Assisted" = "xG.Assisted",
                      "Non-Penalty xG + xG Assisted" = "npxG...xA",
                      "Shot Creating Actions" = "Shot.Creating.Actions",
                      "Pass Completion (in %)" = "Pass.Completion..",
                      "Progressive Passes" = "Progressive.Passes",
                      "Progressive Carries" = "Progressive.Carries",
                      "Dribbles Completed" = "Dribbles.Completed",
                      "Touches in Attacking Penalty Area" = "Touches..Att.Pen.",
                      "Progressive Passes Received" = "Progressive.Passes.Rec",
                      "Pressures" = "Pressures",
                      "Tackles" = "Tackles",
                      "Interceptions" = "Interceptions",
                      "Blocks" = "Blocks",
                      "Clearances" = "Clearances",
                      "Aerials Won" = "Aerials.won"
                    )
                  ),
                  selectInput(
                    label = "Category (Y-axis): ",
                    'cat2',
                    choices = c(
                      "Non-Penalty Goals" = "Non.Penalty.Goals",
                      "Non-Penalty xG" = "Non.Penalty.xG",
                      "Shots Total" = "Shots.Total",
                      "Assists" = "Assists",
                      "xG Assisted" = "xG.Assisted",
                      "Non-Penalty xG + xG Assisted" = "npxG...xA",
                      "Shot Creating Actions" = "Shot.Creating.Actions",
                      "Pass Completion (in %)" = "Pass.Completion..",
                      "Progressive Passes" = "Progressive.Passes",
                      "Progressive Carries" = "Progressive.Carries",
                      "Dribbles Completed" = "Dribbles.Completed",
                      "Touches in Attacking Penalty Area" = "Touches..Att.Pen.",
                      "Progressive Passes Received" = "Progressive.Passes.Rec",
                      "Pressures" = "Pressures",
                      "Tackles" = "Tackles",
                      "Interceptions" = "Interceptions",
                      "Blocks" = "Blocks",
                      "Clearances" = "Clearances",
                      "Aerials Won" = "Aerials.won"
                    )
                  ),
                width = 4
              ),
      ),
      tabItem(
        "50th",
        box(
          title = "Compared to League's 50th Percentile",
          status = "success",
          plotlyOutput("Compw50"),
          width = 8, height = 650),
        box(
          title = "Select Player",
          status = "primary",
          selectInput(
            label = "Forwards: ",
            'stats',
            choices = players[-c(99:100)],
          ),
          width = 3
        )
      ),
      tabItem("table",
              fluidPage(
                h3("Forwards 2022-23"),
                DT::dataTableOutput("prem_forwards")
              )
      )
    )
  )
)

server <- function(input, output){
  output$radarPlot <- renderPlot({
    radar_chart(input$player1, input$player2, input$player3, input$player4, input$player5)
  }, height = 750, width = 750)
  
  output$prem_forwards <- DT::renderDataTable(prem_op(prem))
  
  output$scatter <- renderPlotly({
    scatter_fw(input$cat1, input$cat2, prem)
  })
  
  output$Compw50 <- renderPlotly({
    avg_comp(input$stats)
  })
}

shinyApp(ui = ui, server = server)
