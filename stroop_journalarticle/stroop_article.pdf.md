---
title: Stroop Task Replication Study
author:
  - name: Christina Fan
    affiliations:
        - id: p390
          department: Department of Psychology
          name: University of Waterloo
  - name: Daniella Christina Pereira Cisorio
    affiliations:
        - ref: p390
  - name: Alexia Nijgorodov
    affiliations:
        - ref: p390
  - name: Diya Renjan
    affiliations:
        - ref: p390
abstract: |
  This study aimed to replicate the Stroop effect, which predicts slower reaction times and lower accuracy for incongruent compared to congruent colour-word stimuli. Fifteen undergraduate participants completed a computerized Stroop task, and reaction time and accuracy were analyzed using two-way repeated measures ANOVAs. Contrary to our hypothesis, no significant main effect of congruency was found on reaction time or accuracy. The lack of significant findings may be due to methodological limitations, including a small sample size, fewer trials, and the presence of extreme outliers. Future research should increase statistical power by using a larger number of trials and participants, and apply stricter data screening procedures.
keywords:
  - Stroop task
  - cognitive interference
  - cognitive control
  - automaticity
  - congruency
  - reaction time
  - accuracy
  - replication
bibliography: bibliography.bib 
format:
  elsevier-pdf:
    keep-tex: true
    keep-md: true
    fig-pos: "H" 
    journal:
      name: Journal Name
      formatting: preprint
      cite-style: authoryear
---

# Introduction

The Stroop effect is one of the most well-known phenomena in cognitive psychology. First demonstrated by John Ridley Stroop in 1935, the effect refers to the cognitive interference that occurs when the brain is presented with two conflicting pieces of information at the same time. In the conventional Stroop task, participants are shown colour words printed in different ink colours and are asked to name the colour of the word, ignoring the word itself. The task consists of two conditions. In congruent trials, the word and ink colour match (e.g the word “RED” written in red). In incongruent trials, the word and ink colour do not match (e.g. the word “RED” written in blue). The task measures reaction time and accuracy as objective indicators of cognitive interference experienced during incongruent trials. The Stroop task is often used to measure attention, processing speed, and cognitive control. 

@Stroop1935 originally found that participants were significantly slower and less accurate when naming colours on incongruent trials compared to congruent ones. This effect has been replicated across hundreds of studies, making it a very reliable finding [@MacLeod1991]. It was also found that with practice, interference decreases over time, though it never fully disappears, suggesting the effect reflects automatic reading and limits in cognitive control. Several theories have been proposed to explain why the Stroop effect occurs. The relative speed of processing theory suggests that the brain processes written words faster than colours, so the word meaning reaches the response stage first and interferes with the colour naming [@MacLeod1991]. The automaticity theory proposes that reading is such a highly practiced process that it occurs automatically, which interferes with the slower, more deliberate process of colour naming which draws more heavily on attentional resources [@MacLeod1991]. While these theories explain parts of the effect, there is no single universally accepted explanation for the Stroop effect. 

This present study aimed to replicate the Stroop effect. Based on previous research, we hypothesized that participants would show slower reaction times and lower accuracy on incongruent trials compared to congruent trials.

# Methods
This study replicated the Stroop Effect by implementing the word-color visualizations on a computer screen. We wrote an experimental program in PsychoPy, an open-source software library written in Python, that delievered the experiment.

## Participants
Fifteen participants in the age range of 19-25 were recruited from an undergraduate upper-year psychology seminar course at the University of Waterloo. Each participant completed the Stroop Task on one of the researcher's computer. 

## Experimental Task Design
Participants are introduced to the experiment with instructions describing the experiment protocol. After reading, participants are instructed to press the spacebar to proceed to the first trial of the experiment. There are a total of 3 trials, with 10 words being shown to participants in each trial. Each word is shown on the screen for 500 ms before disappearing, and participants are required to press a key to indicate the color of the word. The next word will not appear until participants give a response to the current word. @fig-experiment_visual shows an illustration of the experiment protocol.

![Experiment Protocol Flowchart](article_images/task_flowchart.png){#fig-experiment_visual width="60%"}

The program randomly generates color words from the list: red, green, blue, yellow and the color of those words are also randomly selected among those colors. Thus, the chances of a word presentation being congruent or incongruent are random. The keys "r", "g","b","y" are assigned to the respective colors red, green, blue, yellow for participants to give their response when reporting the color of the word. Participants are able to exit the experiment at any time by pressing the "Esc" key.

## Data Processing and Analysis
During the experiment, the congruency of each word is recorded, and the participant's reaction time (the time in between stimulus presentation and keyboard response), and accuracy of response are recorded. These results are stored in a CSV file generated for each participant.

Two 2-way repeated measures ANOVA tests were performed examining the main effects of trial and congruency on reaction time and accuracy. Interactions effects between trial and congruency were considered on reaction time and accuracy as well.

# Results
Two participants were excluded due to the random occurence of having trials where words were either all congruent or incongruent (no differences in congruency).


## Reaction Time - Overall vs Congruent vs Incongruent

### Daniella in-line
The overall results including both congruent and incongruent words were analyzed first. The mean reaction time across all trials was about `python mean_rt` seconds. Shown in Figure 1, reaction time decreased sharply between Trial 1 (M = 1.63s) and Trial 2 (M = 1.10s) before evening out in Trial 3 (M = 1.09s). Figure 2 demonstrates the average reaction times of congruent and incongruent words. The mean reaction time for congruent words across all trials was about 1.19 seconds while the mean reaction time for incongruent words across all trials was about 1.28 seconds. Trial 1 went against the hypothesis as the mean reaction time for congruent words (M = 1.63s) was higher than that of incongruent words (M = 1.56s). However, this was not the same for trials 2 and 3. In trial 2, the mean reaction time for congruent words (M = 0.92s) ended up lower than incongruent words (M = 1.16s). Trial 3 followed this same trend with congruent words (M = 1.02) being lower than incongruent words (M = 1.14s). However, unlike the overall results the mean reaction time for congruent words rose slightly from trial 2 to trial 3.


## Accuracy - Overall vs Congruent vs Incongruent

### Daniella in-line
The overall results including both congruent and incongruent words were analyzed first, with the mean accuracy across all trials coming out to about `python mean_accuracy`. Shown in Figure 3, accuracy in Trial 1 starts off fairly low (M = 81.8%) and rises steadily through Trial 2 (M = 87.5%) and reaches a peak at Trial 3 (M = 90.0%). When compared to the average accuracy based on congruency, the trend shifts away from a steady rise. The mean accuracy for congruent words across all trials was about 92.0%, where incongruent words ended up with a mean accuracy of about 81.3%. Figure 4 demonstrates the mean accuracy based on each trial. Trial 1 started with a large gap between congruent words (M = 91.7%) and incongruent words (M = 76.5%). Despite congruent accuracy remaining higher than incongruent accuracy, Trial 2 saw a drop in congruent accuracy (M = 87.5%) and a rise in incongruent accuracy (M = 82.9%). However, Trial 3 saw a rise in both congruent accuracy (M = 96.9%) and incongruent accuracy (M = 84.6%). Although there was a rise in both congruent and incongruent accuracy, congruent words remained higher than incongruent words through all trials.


## Interaction between congruency and trial on reaction time

## Christina anova




In order to analyze the effects of trial and congruency on reaction time, a 2-way repeated measures ANOVA was conducted. Demonstrated in Table 1, the results yielded insignificant effects. There was no significant main effect found of congruency (F(1, 13)=0.07, p =0.799), meaning there was not a noticeable difference of reaction time between congruent and incongruent conditions. Trial had a significant main effect (F(2, 28) = 3.36, p = 0.049). This suggests there is a significant change in reaction time among trials. In addition, the interaction between congruency and trial showed no significance (F(2, 28) = 0.29, p = 0.752), meaning there is no significant effect of congruency on reaction time across time. 


## Interaction between congruency and trial on accuracy

In order to analyze the effect of trial and congruency on accuracy, a 2-way repeated measures ANOVA was conducted. Demonstrated in Table 2, there was a significant main effect found of congruency (F(1, 13) = 5.69, p = 0.033), meaning there was a significant difference of accuracy between congruent and incongruent trials. There was no significant main effect found of trial (F(2, 28) = 0.48, p = 0.621), meaning accuracy did not noticeably differ between trials. Unlike the previous ANOVA where trial had a slight trend, this one did not provide a trend of trial. Additionally, the interaction between congruency and trial showed no significance (F(2, 28) = 1.86, p = 0.175), meaning there is no significant effect of congruency on accuracy across time. 



::: {.cell}
::: {.cell-output-display}
![Changes in Mean Reaction Time Across Trials](stroop_article_files/figure-pdf/fig-rt-overall-1.pdf){#fig-rt-overall}
:::
:::



::: {.cell}
::: {.cell-output .cell-output-stdout}

```
([<matplotlib.axis.XTick object at 0x7df1cf67b070>, <matplotlib.axis.XTick object at 0x7df1cacb5360>, <matplotlib.axis.XTick object at 0x7df1cacfe4d0>], [Text(0, 0, 'Trial 1'), Text(1, 0, 'Trial 2'), Text(2, 0, 'Trial 3')])
```


:::

::: {.cell-output-display}
![Effects of Congruency on Reaction Time](stroop_article_files/figure-pdf/fig-rt-congruency-3.pdf){#fig-rt-congruency}
:::
:::


## Accuracy - Overall vs Congruent vs Incongruent

## Daniella in-line
The overall results including both congruent and incongruent words were analyzed first, with the mean accuracy across all trials coming out to about 86.4%. Shown in @fig-acc-overall, accuracy in Trial 1 starts off fairly low (M = 81.8%) and rises steadily through Trial 2 (M = 87.5%) and reaches a peak at Trial 3 (M = 90.0%). When compared to the average accuracy based on congruency, the trend shifts away from a steady rise. The mean accuracy for congruent words across all trials was about 92.0%, where incongruent words ended up with a mean accuracy of about 81.3%. @fig-acc-congruency demonstrates the mean accuracy based on each trial. Trial 1 started with a large gap between congruent words (M = 91.7%) and incongruent words (M = 76.5%). Despite congruent accuracy remaining higher than incongruent accuracy, Trial 2 saw a drop in congruent accuracy (M = 87.5%) and a rise in incongruent accuracy (M = 82.9%). However, Trial 3 saw a rise in both congruent accuracy (M = 96.9%) and incongruent accuracy (M = 84.6%). Although there was a rise in both congruent and incongruent accuracy, congruent words remained higher than incongruent words through all trials.


::: {.cell}
::: {.cell-output-display}
![Changes in Mean Accuracy Rates Across Trials](stroop_article_files/figure-pdf/fig-acc-overall-5.pdf){#fig-acc-overall}
:::
:::



::: {.cell}
::: {.cell-output .cell-output-stdout}

```
([<matplotlib.axis.XTick object at 0x7df1cac30430>, <matplotlib.axis.XTick object at 0x7df1cac31480>, <matplotlib.axis.XTick object at 0x7df1cabc0460>], [Text(0, 0, 'Trial 1'), Text(1, 0, 'Trial 2'), Text(2, 0, 'Trial 3')])
```


:::

::: {.cell-output .cell-output-stdout}

```
(0.0, 1.3)
```


:::

::: {.cell-output-display}
![Effects of Congruency on Accuracy](stroop_article_files/figure-pdf/fig-acc-congruency-7.pdf){#fig-acc-congruency}
:::
:::


## Interaction between congruency and trial on reaction time

In order to analyze the effects of trial and congruency on reaction time, a 2-way repeated measures ANOVA was conducted. Demonstrated in @setup1, the results yielded insignificant effects. There was no significant main effect found of congruency (F(1, 13)=0.07, p =0.799), meaning there was not a noticeable difference of reaction time between congruent and incongruent conditions. Trial had a significant main effect (F(2, 28) = 0.48, p = 0.621),suggesting there is a possible trend in reaction time among trials. In addition, the interaction between congruency and trial showed no significance (F(2, 28) = 1.86, p = 0.175), meaning there is no significant effect of congruency on reaction time across time. Despite the potential trend of the trial condition, the results of this ANOVA found no significant main effects of congruency on reaction time.


::: {.cell}
::: {.cell-output-display}


Table: Repeated Measures ANOVA for Reaction Time

|Effect        | DFn| DFd|    F|p     |
|:-------------|---:|---:|----:|:-----|
|Match         |   1|  13| 0.07|0.799 |
|Trial         |   2|  28| 3.36|0.049 |
|Match × Trial |   2|  28| 0.29|0.752 |


:::
:::


## Interaction between congruency and trial on accuracy

## hopefully daniella can adapt from above TABLE to here if it works
In order to analyze the effect of trial and congruency on accuracy, a 2-way repeated measures ANOVA was conducted. Demonstrated in @tbl-acc-anova, similar to the results of the first ANOVA conducted, the results yielded insignificant effects. There was no significant main effect found of congruency (F(1,15) = 2.479, p = 0.136), meaning there was no significant difference of accuracy between congruent and incongruent trials. There was no significant main effect found of trial (F(2,30) = 1.128, p = 0.337), meaning accuracy did not noticeably differ between trials. Unlike the previous ANOVA where trial had a slight trend, this one did not provide a trend of trial. Additionally, the interaction between congruency and trial showed no significance (F(2,30) = 0.488, p = 0.619), meaning there is no significant effect of congruency on accuracy across time. Like the results of the previous ANOVA, there were no significant main effects of congruency on accuracy.


::: {.cell}
::: {.cell-output .cell-output-stdout}

```
         Effect DFn DFd    F     p
1         Match   1  13 5.69 0.033
2         Trial   2  28 0.48 0.621
3 Match × Trial   2  28 1.86 0.175
```


:::
:::



::: {.cell}
::: {.cell-output .cell-output-stdout}

```
1.2776375000000002
```


:::
:::



::: {.cell}
::: {.cell-output .cell-output-stdout}

```
0.8645833333333334
```


:::
:::


# Discussion

To reiterate, the goal of this experiment was to replicate the classic Stroop effect, which predicts that participants will exhibit slower reaction times and lower accuracy when presented with incongruent stimuli compared to congruent ones. 

Our results, however, speak otherwise. The results of the Repeated Measures ANOVA indicate that the main effect of word-colour matching, congruency, on reaction time was not statistically significant, **F(1,15)=0.200, p=0.661**. This finding contradicts the established literature which states that the automaticity of reading typically interferes with the more deliberate task of colour naming. In our sample, the mean reaction time across all conditions was approximately **1277.69 ms**, with an overall accuracy of **86.4%**. While the Stroop effect was not significant, there was a marginal effect of trial on reaction time, p=0.056. The mean reaction time decreased notably from trial 1 **(1633.85 ms) to trial 2 (1100.98 ms)** and remained stable in trial 3 **(1098.26 ms)**. Similarly, mean accuracy improved from **0.819 in Trial 1 to 0.900 in Trial 3**. These trends suggest a practice effect, where participants became more efficient at the task as the experiment progressed.

Moreover, a reason for the failure in statistical significance could be attributed to extreme outliers in the raw data, which significantly inflated the variance within the ANOVA. Several participants recorded reaction times that exceeded 10 seconds, which is typically uncharacteristic for a standard Stroop task; Participant 10 recorded a reaction time of **19,209 ms during trial 1, Participant 16 recorded 17,071 ms in trial 1, and Participant 3 exceeded 13,000 ms in trial 1**. This may have been caused by participants losing focus, being overwhelmed by a new task, looking for the key locations, or talking to the proctor.  Because the ANOVA uses the "Sum of Squares" to calculate the F-statistic, these massive deviations likely masked the smaller, millisecond-level differences typically associated with cognitive interference. Furthermore, as stated before, the automaticity theory suggests that reading is a highly practiced task that occurs without conscious effort, hence interfering with the slower process of colour naming. While our data did not show a significant difference between the match and non-match conditions, the overall high accuracy of **86.4%** suggests that the participants did successfully engage in cognitive control to ignore the word's meaning, even though the distraction of the words didn't significantly change the reaction times for this group. 

Two major limitations of this study were the small count of 10 words per Trial, for a total of 3 trials, and the small sample size. Furthermore, since we had randomized the congruent and incongruent words, some participants got more, and some got fewer, creating an uneven balance of conditions, which could have still worked if we had more words per trial. Additionally, since we did not exclude outliers in our data analysis, that means those data points definitely impacted the data analysis. Therefore, future replications should include a larger number of trials to increase statistical power, a larger pool of participants, and an outlier removal protocol to ensure that the final analysis accurately reflects cognitive processing speed rather than behavioural distractions.


# References {-}

::: {#refs}
:::
