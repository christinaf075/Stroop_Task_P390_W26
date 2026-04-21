library(jmv)
library(haven)
library(jmvReadWrite)
library(jmvconnect)

getwd()

data <- read.csv("StroopAccuracy.csv", header=TRUE, sep=",", stringsAsFactors=FALSE)

print(dim(data))
print(names(data))
head(data)

names(data) <- trimws(names(data))

jmv::anovaRM(
    data = data,
    rm = list(
        list(
            label="Match vs non-match",
            levels=c("Match", "Non-match")),
        list(
            label="Trial",
            levels=c("Trial 1", "Trial 2", "Trial 3"))
    ),
    rmCells = list(
        list(measure="T1 Match", cell=c("Match", "Trial 1")),
        list(measure="T2 Match", cell=c("Match", "Trial 2")),
        list(measure="T3 Match", cell=c("Match", "Trial 3")),
        list(measure="T1 Non-match", cell=c("Non-match", "Trial 1")),
        list(measure="T2 Non-match", cell=c("Non-match", "Trial 2")),
        list(measure="T3 Non-match", cell=c("Non-match", "Trial 3"))
    ),
    rmTerms = ~ `Match vs non-match` + Trial + `Match vs non-match`:Trial
)