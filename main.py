import pandas as pd
import matplotlib.pyplot as plt


# Using xlsx file from Climate Watch (Updated on March 23rd, 2021), do some calculations,
# then graph the data using matplotlib via bar graph.


#Data retevied from [Climate Watch 2021. Washington, DC: World Resources Institute. Available online at: https://www.climatewatchdata.org.]
df = pd.read_excel("climatewatch-usemissions.xlsx")
stateDict = {}   

#Getts all the states and puts them into a dictionary for later use
def getStateData():
    statesData = df["Climate Watch - U.S States Greenhouse Gas Emissions"]

    for i in statesData[3:]:
        if i not in stateDict.keys():
            stateDict[i] = 0

#Since we're using 28 YEARS of data, we add all the data from each state for each year to get the total for EACH state then save it to the prior dict.
def addGHGEmissions():
    #Total green house gasses EXCLUDING land-use change and forestry
    totalGHGMinLUCF = df["Unnamed: 2"][3:]
    count=3
    while count < len(totalGHGMinLUCF):
        for states in stateDict.keys():
            stateDict[states] += totalGHGMinLUCF[count]
            count += 1

    #Remove this line if you want to see total of all states   
    stateDict.pop("United States")

#using mlp to visualize the data from the dict above.
def graphIt(stateDict):
    plt.rcParams.update(plt.rcParamsDefault)
    plt.style.use('dark_background')

    _, ax = plt.subplots()
    ax.bar(list(stateDict.keys()), list(stateDict.values()))
    ax.set_xticklabels(list(stateDict.keys()), rotation=60, horizontalalignment="right", fontsize="10")
    ax.set_title(f"Total GHG Emissions By State (Exclusing LUCF) [1990-2018]", fontsize=15)
    ax.set_ylabel("Metric Tons Of Carbon Dioxide Equivalent")
    ax.set_xlabel("States")


if __name__ == '__main__':
    getStateData()
    addGHGEmissions()
    graphIt(stateDict)

    plt.show()
