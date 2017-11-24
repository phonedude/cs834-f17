query1 <- read.csv("Query1.csv", header = TRUE)
query2 <- read.csv("Query2.csv", header = TRUE)
query1$Recall
plot(query1$Recall,query1$Precision,type = "o",col = "red", xlab = "Recall", ylab = "Precision", 
     main = "Recall vs Precision Graph",  ylim=c(0,1))
lines(query2$Recall,query2$Precision, type = "o", pch=22, lty=2, col = "blue")
legend("bottomright", c("Query1","Query2"), col=c("red","blue"),pch=21:22, lty=1:2)