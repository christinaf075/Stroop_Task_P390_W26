library(jmv)

library(haven)
library(jmvconnect)

data = read.csv("StroopAccuracy.csv", header = TRUE, sep = ",")

names(data) <- trimws(names(data))

jmv::anovaRM(
    data = data,
    
    rm = list(
        list(
            label = "Match vs non-match",
            levels = c("Match", "Non-match")
        ),
        list(
            label = "Trial",
            levels = c("T1", "T2", "T3")
        )
    ),
    rmCells = list(
        list(measure = "T1.Match", cell = c("Match", "T1")),
        list(measure = "T2.Match", cell = c("Match", "T2")),
        list(measure = "T3.Match", cell = c("Match", "T3")),

        list(measure = "T1.Non.match", cell = c("Non.match", "T1")),
        list(measure = "T2.Non.match", cell = c("Non.match", "T2")),
        list(measure = "T3.Non.match", cell = c("Non.match", "T3"))
    ),
    rmTerms = ~ `Match vs non-match` * Trial * `Match vs non-match`:Trial)