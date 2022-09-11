# Assignment 1: Visualizing government debt in 2020

## Part 1- Examining 2020 data 
### During 2020, Greece's debts (as a % of GDP) were 2x the average among OECD member-states in the European Union 

<iframe 
        src="https://data.oecd.org/chart/6Obi" 
        width="860" height="645" 
        style="border: 0" 
        mozallowfullscreen="true" 
        webkitallowfullscreen="true" 
        allowfullscreen="true"
        ><a 
            href="https://data.oecd.org/chart/6Obi" 
            target="_blank">OECD Chart: General government debt, Total, % of GDP, Annual, 2020
        </a
></iframe>

## Part 2- Taking a look at historical context
<div class="flourish-embed flourish-chart" data-src="visualisation/11148552"><script src="https://public.flourish.studio/resources/embed.js"></script></div>

## Part 3- Taking a look at the geographic distribution
<div class="flourish-embed flourish-map" data-src="visualisation/11152264"><script src="https://public.flourish.studio/resources/embed.js"></script></div>

## Part 4- Examining these visualizations and their source
The data displayed on this page track "general government debt ratios" (see source (here)[https://data.oecd.org/gga/general-government-debt.htm] ) which measure the gross debt a government possesses as a percentage of GDP. It is broadly considered an indicator of how sustainable a government's finances are: high debt-to-GDP ratios are considered unsustainable. It is calculated as:

![equation](https://latex.codecogs.com/svg.image?\frac{\textup{Currency&space;and&space;Deposits}&space;&plus;&space;\textup{Debt&space;Securities&space;and&space;Loans}&space;&plus;&space;\textup{Insurance,&space;Pensions,&space;and&space;Standardized&space;Guarantees}&space;&plus;&space;\textup{Other&space;Accounts&space;Payable}}{\textup{Gross&space;Domestic&space;Product})

Since GDP is so widely collected across nations, it makes for a convenient denominator. The central idea to the ratio above is that governments with high liabilities cannot remain financially solvent if their productivity is relatively low. Though the comparability of debt-to-GDP ratios across nations is common, (some analysts)[https://carnegieendowment.org/chinafinancialmarkets/86397] believe that comparing different financial systems with such a simplistic measure falls short. This is one of the reasons I constrained the data to EU nations, because by design EU nations have more intrinsically linked economies and many share currency systems. This hopefully improves the comparability of the data. Keeping all of this in mind, I will now explore the results in greater detail. The data explored here span from 2007-2020, as OECD averages started being calculated in 2007 and Romania joined the EU in 2007. Incomplete data are available in 2021.

The bar chart tells the audience one basic piece of information: that Greece had unusually high debt-to-GDP ratios in 2020 as compared to the OECD average. The sparkline chart substantiates this observation with trends of the past 13 years. It also shows that the top 5 countries with relatively high debt loads as a % of GDP have similar histories and that they consistently, as a group, are more endebted than other OECD nations on average. This is a useful development because 2020 was a chaotic year and it stands to reason that the single-year data are not reflective of broader trends. Not only did this chart reveal that Greece is consistently above the OECD average, but also that debts spiked in 2020. Then, I chose to map the nations with high debt loads to see if there was a consistent geographic trend. The resulting map (which I generated using colorblind-aware palettes via (Colorbrewer2)[Colorbrewer2.org] ) showed that many of these nations were in Southern Europe and further clarifies that many nations are missing from my evaluations.



