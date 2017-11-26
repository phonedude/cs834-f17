recall <- read.csv("Recall.csv", header = TRUE)
precision <- read.csv("Precision.csv", header = TRUE)

plot(recall$Recall,recall$Value,type = "o",col = "red", xlab = "Recall", ylab = "Precision", 
     main = "Recall vs Precision for CACM Query Set",  ylim=c(0,1), xlim = c(0,1))