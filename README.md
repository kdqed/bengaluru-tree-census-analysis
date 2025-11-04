# Bengaluru Tree Census Analysis - Nov 2025

This is a follow-up to my [previous post](https://kdqed.com/bbmp-tree-census-analysis) analyzing the census trees in Bengaluru. There is newer data now and more importantly 5 newer corporations that have replaced BBMP to constitute the GBA (Greater Bengaluru Authority). In this post, the main goal is to classify the trees into the 5 new corporations based on GPS coordinates and repeat the previous analyses on the latest available dataset.

The dataset I used was obtained from the [OpenCity Portal](https://data.opencity.in/dataset/bengaluru-tree-census-data/resource/bbmp-tree-census-data---july-2025), and it is from July 2025. This dataset consists of about 6.8 lakh trees, of which I couldn't classify about 3000 into any of the 5 corporations. I obtained the map boundaries for the 5 corporations [also from OpenCity](https://data.opencity.in/dataset/greater-bengaluru-authority-corporations-delimitation-2025/resource/greater-bengaluru-authority-five-corporations-map---september-2025).

All the code used in this analysis is in this repository.

## Index

- City Wide Tree Species Frequency
- City Wide Tree Density
- Unidentified Trees
- Central Corporation
- East Corporation
- North Corporation
- South Corporation
- West Corporation
- Conclusion

## City Wide Tree Species Frequency

The top occuring 'Tree Name' in the latest dataset is 'Others' accounting for a quarter of the data. 🤷‍♂️

| TreeName                                                         |   Count |   Percentage |
|:-----------------------------------------------------------------|--------:|-------------:|
| Others                                                           |  170505 |         24.9 |
| Pongamia Pinnata (L.) Pierre                                     |  128831 |         18.8 |
| Swietenia Mahagoni (L.) Jacq.                                    |   34842 |          5.1 |
| Tabebuia Rosea (Bertol) Dc.                                      |   27689 |          4.1 |
| Saraca Asoca (Roxb.) De Wilde                                    |   19007 |          2.8 |
| Ptychosperma Macarthuri Nichols                                  |   17863 |          2.6 |
| Markhamia Lutea (Benth.) K.Schum                                 |   14383 |          2.1 |
| Terminalia Catappa L                                             |   13824 |          2   |

Other than 'Others', the top 7 species each represent more than 2% of the data, which looks pretty diverse. Pongamia Pinnata tops the list at 19% and while the next most frequent species covers about 5%.


## City Wide Tree Density

The density of counted trees within the GBA bounds is shown in the below map with hexagonal bins based on [Uber's H3 Indexing system](https://h3geo.org/) (resolution 7).

![Bengaluru GBA Area: Density Map of Census Trees](https://raw.githubusercontent.com/kdqed/bengaluru-tree-census-analysis/refs/heads/main/results/blr_density_map.png)

The counted trees account for about 962 trees per square kilometer. The corporation-wise density is in the table below:

| Corporation       |   Count | Trees Per Sq. km | % Unidentified |
|:------------------|--------:|-----------------:|---------------:|
| South             |  213982 |             1465 |           29.5 |
| Central           |   87615 |             1125 |           16.4 |
| West              |  165298 |             1016 |           24.9 |
| North             |  131274 |              832 |           24.3 |
| East              |   81915 |              503 |           33.3 |
| Total             |  680084 |              962 |           24.9 |

South tops the tree density followed by Central and West. North isn't bad but East could surely has room for improvement (read Trees).

With respect to identification of trees, Central seems to have done the best with least fraction of unidentified trees. Here too, East is lagging behind, with 1 in 3 trees unidentified (33.3%).

## Central Corporation

Central shows an above average tree density at 1125 trees per sq. km. The proportion of identified trees has been the best among the 5 corporations.

### Tree Density - Central Corporation

The density of counted trees within the Central Corporation bounds is shown in the below map with hexagonal bins based on [Uber's H3 Indexing system](https://h3geo.org/) (resolution 8).

![](https://raw.githubusercontent.com/kdqed/bengaluru-tree-census-analysis/refs/heads/main/results/central_density_map.png)

### Top 5 Species - Central Corporation

| TreeName                                                         |   Count |   Percentage |
|:-----------------------------------------------------------------|--------:|-------------:|
| Pongamia Pinnata (L.) Pierre                                     |    8653 |          9.9 |
| Swietenia Mahagoni (L.) Jacq.                                    |    6392 |          7.3 |
| Saraca Asoca (Roxb.) De Wilde                                    |    5370 |          6.1 |
| Markhamia Lutea (Benth.) K.Schum                                 |    4530 |          5.2 |
| Tabebuia Rosea (Bertol) Dc.                                      |    3450 |          3.9 |

Central shows a well distributed frequency of species with no single species exceeding 10%.

## East Corporation

East shows the least tree density at 503 trees per sq. km. (the city-wide average is 962). It also has the highest percentage of unidentified trees (33.3%).

### Tree Density - East Corporation

The density of counted trees within the East Corporation bounds is shown in the below map with hexagonal bins based on [Uber's H3 Indexing system](https://h3geo.org/) (resolution 8).

![](https://raw.githubusercontent.com/kdqed/bengaluru-tree-census-analysis/refs/heads/main/results/east_density_map.png)

### Top 5 Species - East Corporation

| TreeName                                                         |   Count |   Percentage |
|:-----------------------------------------------------------------|--------:|-------------:|
| Pongamia Pinnata (L.) Pierre                                     |   11782 |         14.4 |
| Swietenia Mahagoni (L.) Jacq.                                    |    5239 |          6.4 |
| Tabebuia Rosea (Bertol) Dc.                                      |    4643 |          5.7 |
| Markhamia Lutea (Benth.) K.Schum                                 |    2220 |          2.7 |
| Thespesia Populnea                                               |    2095 |          2.6 |

Of the top 5 species, Pongamia alone accounts for 14.4% of the trees, which is roughly 1 in 7.


## North Corporation

North does moderately well compared to the city-wide averages in terms of tree density and tree identification. The tree density is 832 trees per sq. km., which is somewhat below the city-wide average of 962. Roughly in 1 in 4 trees haven't been identified (24.3 %).

### Tree Density - North Corporation

The density of counted trees within the North Corporation bounds is shown in the below map with hexagonal bins based on [Uber's H3 Indexing system](https://h3geo.org/) (resolution 8).

![](https://raw.githubusercontent.com/kdqed/bengaluru-tree-census-analysis/refs/heads/main/results/north_density_map.png)

### Top 5 Species - North Corporation

| TreeName                                                         |   Count |   Percentage |
|:-----------------------------------------------------------------|--------:|-------------:|
| Pongamia Pinnata (L.) Pierre                                     |   31963 |         24.3 |
| Swietenia Mahagoni (L.) Jacq.                                    |    9262 |          7.1 |
| Tabebuia Rosea (Bertol) Dc.                                      |    9245 |          7   |
| Markhamia Lutea (Benth.) K.Schum                                 |    4165 |          3.2 |
| Syzygium Cumini (L.) Skeels                                      |    3654 |          2.8 |

Of the top 5 species, Pongamia accounts for roughly 1 in 4 trees. The distribution looks less diverse compared to other corporations.

## South Corporation

South the tops the chart for tree density with 1465 trees per sq. km. compared to the city wide average of 965. However, it could do better with identifying the trees being counted, with 29.5% of the counted trees not having a species name.

### Tree Density - South Corporation

The density of counted trees within the South Corporation bounds is shown in the below map with hexagonal bins based on [Uber's H3 Indexing system](https://h3geo.org/) (resolution 8).

![](https://raw.githubusercontent.com/kdqed/bengaluru-tree-census-analysis/refs/heads/main/results/south_density_map.png)

### Top 5 Species - South Corporation

| TreeName                                                         |   Count |   Percentage |
|:-----------------------------------------------------------------|--------:|-------------:|
| Pongamia Pinnata (L.) Pierre                                     |   41086 |         19.2 |
| Ptychosperma Macarthuri Nichols                                  |   10206 |          4.8 |
| Tabebuia Rosea (Bertol) Dc.                                      |    7268 |          3.4 |
| Swietenia Mahagoni (L.) Jacq.                                    |    6573 |          3.1 |
| Saraca Asoca (Roxb.) De Wilde                                    |    6132 |          2.9 |

Of the top 5 species, Pongamia accounts for roughly 1 in 5 trees. South could work on having a more diverse distribution of trees.

## West Corporation

West Corporation is the closest to the city-wide average both in terms of tree density (1016 trees per sq. km.) as well as percentage of unidentified trees (24.9 %).

### Tree Density - West Corporation

The density of counted trees within the West Corporation bounds is shown in the below map with hexagonal bins based on [Uber's H3 Indexing system](https://h3geo.org/) (resolution 8).

![](https://raw.githubusercontent.com/kdqed/bengaluru-tree-census-analysis/refs/heads/main/results/west_density_map.png)

### Top 5 Species - West Corporation

| TreeName                                                         |   Count |   Percentage |
|:-----------------------------------------------------------------|--------:|-------------:|
| Pongamia Pinnata (L.) Pierre                                     |   34960 |         21.1 |
| Swietenia Mahagoni (L.) Jacq.                                    |    7320 |          4.4 |
| Wrightia Tinctoria (Roxb.) R. Br                                 |    5763 |          3.5 |
| Ptychosperma Macarthuri Nichols                                  |    4619 |          2.8 |
| Acacia Auriculiformis Cunn. Ex Benth                             |    4573 |          2.8 |

Similar to South, Pongamia accounts for roughly 1 in 5 trees. West could also work on having a more diverse distribution of trees.

## Conclusion

With the currently available data, it seems South, West, and Central would be the best corporations to live in if you're looking for tree cover. North could use some more trees and East needs a lot more trees!

In terms of the census going forward, we aren't really sure how the new corporations would handle each of their jurisdictions, but all corporations could do better with identifying all the counted species.
