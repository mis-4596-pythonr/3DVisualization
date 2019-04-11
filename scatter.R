install.packages("scatterplot3d")
require("scatterplot3d")

MyData <- read.csv(file="C:/Users/matth/Documents/python/csv/playerstatsNEW.csv", header=TRUE, sep=",")

colors <- c("#999999", "#E69F00", "#56B4E9", "#DC143C", "#3CD371")
colors<- colors[as.numeric(MyData$Pos)]
s3d <- scatterplot3d(MyData[,3:5],xlab= "Points",ylab= "Rebounds", zlab = "Assists", pch = 16, color=colors, angle =55)
legend(s3d$xyz.convert(7.5,10,4.5), legend = levels(MyData$Pos), col = c("#999999", "#E69F00", "#56B4E9", "#DC143C", "#3CD371"), pch =16)