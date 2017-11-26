recall <- read.csv("Recall.csv", header = TRUE)

plot(recall$Query,recall$Recall,type = "o",col = "red", xlab = "Query Index", ylab = "Recall", 
     main = "Recall for CACM Query Set",  ylim=c(0,1))