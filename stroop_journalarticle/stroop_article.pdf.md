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
All of the data from the study was included in the results, including outliers such as participants with extremely high reaction times or extremely poor accuracy.


## Reaction Time - Overall vs Congruent vs Incongruent

### Daniella in-line
The overall results including both congruent and incongruent words were analyzed first. The mean reaction time across all trials was about `python mean_rt` seconds. Shown in Figure 1, reaction time decreased sharply between Trial 1 (M = 1.63s) and Trial 2 (M = 1.10s) before evening out in Trial 3 (M = 1.09s). Figure 2 demonstrates the average reaction times of congruent and incongruent words. The mean reaction time for congruent words across all trials was about 1.19 seconds while the mean reaction time for incongruent words across all trials was about 1.28 seconds. Trial 1 went against the hypothesis as the mean reaction time for congruent words (M = 1.63s) was higher than that of incongruent words (M = 1.56s). However, this was not the same for trials 2 and 3. In trial 2, the mean reaction time for congruent words (M = 0.92s) ended up lower than incongruent words (M = 1.16s). Trial 3 followed this same trend with congruent words (M = 1.02) being lower than incongruent words (M = 1.14s). However, unlike the overall results the mean reaction time for congruent words rose slightly from trial 2 to trial 3.


## Accuracy - Overall vs Congruent vs Incongruent

### Daniella in-line
The overall results including both congruent and incongruent words were analyzed first, with the mean accuracy across all trials coming out to about `python mean_accuracy`. Shown in Figure 3, accuracy in Trial 1 starts off fairly low (M = 81.8%) and rises steadily through Trial 2 (M = 87.5%) and reaches a peak at Trial 3 (M = 90.0%). When compared to the average accuracy based on congruency, the trend shifts away from a steady rise. The mean accuracy for congruent words across all trials was about 92.0%, where incongruent words ended up with a mean accuracy of about 81.3%. Figure 4 demonstrates the mean accuracy based on each trial. Trial 1 started with a large gap between congruent words (M = 91.7%) and incongruent words (M = 76.5%). Despite congruent accuracy remaining higher than incongruent accuracy, Trial 2 saw a drop in congruent accuracy (M = 87.5%) and a rise in incongruent accuracy (M = 82.9%). However, Trial 3 saw a rise in both congruent accuracy (M = 96.9%) and incongruent accuracy (M = 84.6%). Although there was a rise in both congruent and incongruent accuracy, congruent words remained higher than incongruent words through all trials.


## Interaction between congruency and trial on reaction time

## Christina anova




In order to analyze the effects of trial and congruency on reaction time, a 2-way repeated measures ANOVA was conducted. Demonstrated in Table 1, the results yielded insignificant effects. There was no significant main effect found of congruency (F(1, 13)=0.07, p =0.799), meaning there was not a noticeable difference of reaction time between congruent and incongruent conditions. Trial came just short of reaching a significant main effect (F(2, 28) = 3.36, p = 0.049). Although trial did not reach statistical significance, this suggests there is a possible trend in reaction time among trials. In addition, the interaction between congruency and trial showed no significance (F(2, 28) = 0.29, p = 0.752), meaning there is no significant effect of congruency on reaction time across time. Despite the potential trend of the trial condition, the results of this ANOVA found no significant main effects of congruency on reaction time.


## Interaction between congruency and trial on accuracy

## hopefully daniella can adapt from above to here if it works
In order to analyze the effect of trial and congruency on accuracy, a 2-way repeated measures ANOVA was conducted. Demonstrated in Table 2, similar to the results of the first ANOVA conducted, the results yielded insignificant effects. There was no significant main effect found of congruency (F(1, 13) = 5.69, p = 0.033), meaning there was no significant difference of accuracy between congruent and incongruent trials. There was no significant main effect found of trial (F(2, 28) = 0.48, p = 0.621), meaning accuracy did not noticeably differ between trials. Unlike the previous ANOVA where trial had a slight trend, this one did not provide a trend of trial. Additionally, the interaction between congruency and trial showed no significance (F(2, 28) = 1.86, p = 0.175), meaning there is no significant effect of congruency on accuracy across time. Like the results of the previous ANOVA, there were no significant main effects of congruency on accuracy.





::: {.cell}
::: {.cell-output-display}
![Changes in Mean Reaction Time Across Trials](stroop_article_files/figure-pdf/fig-rt-overall-1.pdf){#fig-rt-overall}
:::
:::



::: {.cell}
::: {.cell-output .cell-output-stdout}

```
([<matplotlib.axis.XTick object at 0x745ca407b070>, <matplotlib.axis.XTick object at 0x745c9f6bd360>, <matplotlib.axis.XTick object at 0x745c9f6fa4d0>], [Text(0, 0, 'Trial 1'), Text(1, 0, 'Trial 2'), Text(2, 0, 'Trial 3')])
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
([<matplotlib.axis.XTick object at 0x745c9f630430>, <matplotlib.axis.XTick object at 0x745c9f631480>, <matplotlib.axis.XTick object at 0x745c9f5bc460>], [Text(0, 0, 'Trial 1'), Text(1, 0, 'Trial 2'), Text(2, 0, 'Trial 3')])
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

## hopefully daniella can adapt from above to here if it works
In order to analyze the effects of trial and congruency on reaction time, a 2-way repeated measures ANOVA was conducted. Demonstrated in @tbl-rt-anova, the results yielded insignificant effects. There was no significant main effect found of congruency (F(1,15) = 0.200, p = 0.661), meaning there was not a noticeable difference of reaction time between congruent and incongruent conditions. Trial came just short of reaching a significant main effect (F(2,30) = 3.178, p = 0.056). Although trial did not reach statistical significance, this suggests there is a possible trend in reaction time among trials. In addition, the interaction between congruency and trial showed no significance (F(2,30) = 0.280, p = 0.758), meaning there is no significant effect of congruency on reaction time across time. Despite the potential trend of the trial condition, the results of this ANOVA found no significant main effects of congruency on reaction time.

## christina anova table


::: {.cell}
::: {.cell-output .cell-output-stdout}

```
         Effect DFn DFd    F     p
1         Match   1  13 0.07 0.799
2         Trial   2  28 3.36 0.049
3 Match × Trial   2  28 0.29 0.752
```


:::
:::



::: {#tbl-rt-anova .cell tbl-cap='Repeated Measures ANOVA for Reaction Time'}
::: {.cell-output .cell-output-stdout}

```
                Effect  Sum of Squares  df  Mean Square      F      p
0           Congruency           0.204   1        0.204  0.200  0.661
1   Error (Congruency)          15.344  15        1.023    NaN    NaN
2                Trial           6.035   2        3.017  3.178  0.056
3        Error (Trial)          28.486  30        0.950    NaN    NaN
4   Congruency × Trial           0.400   2        0.200  0.280  0.758
5  Error (Interaction)          21.441  30        0.715    NaN    NaN
```


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





::: {#tbl-acc-anova .cell tbl-cap='Repeated Measures ANOVA for Accuracy'}
::: {.cell-output .cell-output-stdout}

```
                Effect  Sum of Squares  df  Mean Square      F      p
0           Congruency           0.275   1        0.275  2.479  0.136
1   Error (Congruency)           1.666  15        0.111    NaN    NaN
2                Trial           0.083   2        0.041  1.128  0.337
3        Error (Trial)           1.099  30        0.037    NaN    NaN
4   Congruency × Trial           0.048   2        0.024  0.488  0.619
5  Error (Interaction)           1.469  30        0.049    NaN    NaN
```


:::
:::


::: {.cell}

```{.python .cell-code}
import pandas as pd

data = pd.DataFrame({
    "reaction_time": [0.681, 0.524, 0.628, 0.769, 0.599, 0.659, 0.610, 0.675, 0.588, 0.678, 0.545, 0.641, 0.576, 0.561, 0.616, 0.580, 0.670, 0.721, 0.801, 0.572, 0.549, 0.743, 0.534, 0.607, 0.603, 0.561, 1.203, 0.577, 0.562, 0.574, 1.231, 1.144, 1.289, 1.160, 1.278, 1.419, 1.241, 2.117, 1.300, 1.519, 1.179, 1.201, 1.641, 1.209, 1.463, 1.917, 1.089, 1.009, 1.075, 1.258, 1.241, 1.302, 1.187, 1.263, 1.493, 1.171, 1.243, 1.349, 2.632, 5.719, 1.430, 13.240, 2.506, 1.480, 13.747, 1.602, 2.473, 0.864, 4.781, 1.184, 1.185, 3.710, 1.517, 1.431, 1.274, 1.523, 1.145, 1.182, 1.794, 1.066, 1.231, 0.970, 0.740, 0.820, 0.906, 0.775, 0.841, 1.447, 0.716, 0.839, 0.992, 0.549, 1.048, 0.718, 0.726, 1.225, 0.915, 0.761, 0.779, 0.705, 0.703, 0.753, 0.763, 0.796, 0.708, 0.870, 1.080, 0.842, 0.847, 1.066, 0.698, 0.787, 0.689, 0.753, 0.716, 0.822, 0.730, 0.770, 0.835, 1.102, 1.015, 0.920, 1.192, 0.839, 0.717, 1.244, 1.029, 1.358, 1.244, 0.976, 0.894, 0.866, 0.842, 0.831, 0.584, 0.688, 1.370, 0.846, 0.611, 0.645, 0.777, 1.001, 0.756, 0.782, 1.039, 1.008, 0.845, 0.918, 0.764, 0.664, 0.803, 0.839, 0.664, 0.645, 0.831, 0.624, 0.727, 0.684, 0.704, 0.593, 0.557, 0.583, 0.632, 0.603, 0.563, 0.766, 9.214, 0.751, 0.613, 0.643, 1.820, 1.196, 1.316, 1.128, 1.015, 1.010, 0.785, 0.900, 0.712, 0.898, 1.037, 1.427, 0.807, 0.725, 1.742, 0.847, 0.807, 0.925, 0.770, 1.284, 0.932, 1.032, 0.742, 1.179, 0.952, 0.792, 0.835, 0.900, 0.849, 0.810, 0.819, 0.737, 0.685, 0.642, 0.522, 0.543, 0.699, 0.706, 1.548, 0.965, 1.521, 1.206, 1.081, 2.590, 1.021, 0.972, 0.990, 0.856, 0.996, 1.090, 0.922, 0.780, 0.933, 1.015, 1.193, 0.937, 0.817, 0.984, 0.965, 0.862, 0.757, 0.835, 0.759, 0.799, 1.019, 0.768, 1.190, 1.112, 0.937, 0.963, 1.677, 1.377, 1.346, 1.572, 1.425, 1.448, 1.450, 1.309, 1.679, 1.736, 1.175, 0.966, 1.016, 1.118, 1.731, 1.463, 1.233, 1.458, 1.445, 1.135, 1.015, 1.430, 1.540, 0.863, 0.991, 0.784, 1.070, 1.125, 0.968, 1.594, 1.088, 1.069, 0.690, 19.209, 0.988, 0.756, 1.378, 0.922, 0.707, 0.799, 0.762, 0.750, 0.904, 3.663, 0.750, 0.886, 0.595, 0.859, 0.605, 1.037, 0.785, 0.743, 0.690, 0.805, 0.606, 0.603, 0.902, 0.736, 0.624, 0.837, 1.656, 1.607, 1.953, 1.445, 3.871, 1.588, 1.754, 1.168, 1.771, 1.876, 1.014, 1.068, 1.180, 0.967, 1.034, 1.223, 2.154, 3.485, 1.761, 3.024, 1.033, 2.738, 1.085, 1.052, 1.168, 1.092, 1.421, 1.584, 2.055, 1.491, 0.734, 0.843, 0.874, 0.914, 0.945, 0.826, 0.833, 0.782, 0.850, 0.789, 0.737, 0.878, 0.849, 0.777, 0.839, 0.987, 0.853, 0.866, 0.920, 0.758, 0.796, 0.807, 0.728, 0.825, 0.704, 0.842, 0.705, 0.770, 0.758, 1.340, 1.681, 1.149, 1.278, 1.258, 1.391, 0.935, 1.428, 1.039, 0.984, 0.922, 1.211, 1.053, 0.801, 0.854, 1.041, 1.058, 0.912, 1.001, 1.121, 1.018, 1.025, 15.257, 0.936, 0.697, 0.692, 0.899, 0.814, 1.139, 0.928, 1.116, 14.691, 3.276, 0.880, 1.964, 1.139, 1.466, 1.089, 1.024, 1.294, 1.288, 1.008, 1.695, 0.951, 1.016, 1.389, 1.136, 0.932, 1.171, 0.966, 1.368, 1.036, 0.996, 0.822, 0.934, 0.834, 1.292, 0.909, 0.963, 0.991, 1.116, 1.358, 1.409, 1.787, 1.685, 1.220, 1.561, 1.367, 0.711, 1.464, 1.970, 1.108, 1.161, 1.117, 1.229, 1.031, 1.377, 2.021, 1.394, 1.232, 0.595, 0.905, 1.505, 0.858, 0.789, 1.917, 0.686, 0.804, 0.761, 0.733, 1.614, 1.102, 1.099, 0.864, 1.180, 17.071, 0.743, 0.674, 0.535, 0.805, 0.755, 0.705, 2.476, 0.663, 0.549, 0.536, 0.546, 0.757, 0.678, 0.699, 0.543, 2.352, 0.566, 1.946, 0.526, 0.745, 0.658, 0.608, 2.898, 0.514, 0.569]
})

mean_rt = data["reaction_time"].mean()
print(mean_rt)
```

::: {.cell-output .cell-output-stdout}

```
1.2776375000000002
```


:::
:::



::: {.cell}

```{.python .cell-code}
import pandas as pd

data = pd.DataFrame({
    "accuracy": [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
})

mean_accuracy = data["accuracy"].mean()
print(mean_accuracy)
```

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
