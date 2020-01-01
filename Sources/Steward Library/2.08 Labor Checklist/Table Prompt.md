


Please, extract the tables from the document and transcribe them to markdown here is a guide.


### Table Formatting Guide

**1. Summary Workload Table**

**Structure:**

- **Header Rows:**
  - The first row contains column titles related to the operational maintenance estimate and total servicing operation.
  
- **Data Rows:**
  - Each row represents a different number of operational days (e.g., 5 Days, 6 Days, 7 Days) and stacker configurations (e.g., 110, 126, 142).

**Example:**

| Operation Days | Servicing (Hrs/Yr) | Routine Repair (Hrs/Yr) | Total Servicing (Hrs/Yr) | Non-Productive Time (Hrs/Yr) | Total (Hrs/Yr) | 1 Tour HRS/Year OpM x 1 | 2 Tours HRS/Year OpM x 2 | 3 Tours HRS/Year OpM x 3 |
|----------------|--------------------|-------------------------|--------------------------|-----------------------------|----------------|-------------------------|-------------------------|-------------------------|
| 5 Days         | 638.92             | 191.68                  | 830.60                   | 83.06                       | 913.66         | 1138.99                 | 1364.33                 | 1589.66                 |
| 6 Days         | 731.65             | 219.50                  | 951.15                   | 95.11                       | 1046.26        | 1316.67                 | 1587.07                 | 1857.47                 |
| 7 Days         | 824.38             | 247.31                  | 1071.69                  | 107.17                      | 1178.86        | 1494.33                 | 1809.79                 | 2125.26                 |


**2. Operational Maintenance Table**

**Structure:**

- **Header Rows:**
  - Contains column titles indicating operation days and the corresponding operational maintenance times for different tours.
  
- **Data Rows:**
  - Each row represents a different number of operational days and includes maintenance times for one, two, and three tours.

**Example:**

| Operation Days | One Tour (Hrs/Yr) | Two Tours (Hrs/Yr) | Three Tours (Hrs/Yr) |
|----------------|-------------------|--------------------|----------------------|
| 5 Days         | 225.33            | 450.67             | 676.00               |
| 6 Days         | 270.40            | 540.80             | 811.20               |
| 7 Days         | 315.47            | 630.93             | 946.40               |


**3. Machine Operating # Days/Week Table**

**Structure:**

- **Header Rows:**
  - Contains column titles indicating stacker configurations and the corresponding routine repair time, non-productive time, total servicing, and operational maintenance times.
  
- **Data Rows:**
  - Each row represents a different stacker configuration and includes times for one, two, and three tours.

**Example:**

### Table 3: Machine Operating 5 Days/Week
| # of Stackers | Routine Servicing per Machine (Hrs/yr) | Repair Time per Machine (Hrs/yr) | Routine Servicing + Repair Time (Hrs/yr) | Non-Productive Time Per Machine (Hrs/yr) | Total Servicing per Machine (Hrs/yr) | 1 Tour OpM (Hrs/Yr) | 2 Tours OpM (Hrs/Yr) | 3 Tours OpM (Hrs/Yr) |
|---------------|------------------------------|--------------------------------------|----------------|---------------------|----------------------|----------------------|----------------------|----------------------|
| 110           | 191.68                       | 83.06                                | 913.66         | 1138.99             | 1364.33              | 1589.66              |1689.66               |1789.66               |
| 126           | 193.16                       | 83.70                                | 920.71         | 1146.04             | 1371.38              | 1796.71              |1889.66               |1989.66               |
| 142           | 197.85                       | 85.74                                | 943.10         | 1168.43             | 1393.77              | 1919.10              |2089.66               |2189.66               |



**4. Power Off and Power On Tasks Tables**

**Structure:**

- **Header Rows:**
  - The first row contains thresholds, indicating the conditions or frequencies (e.g., 3K, 1.1M, 4.4M, 1 Month, 1K, 14.3M).
  - The second row contains item numbers corresponding to specific tasks (e.g., 5, 8, 9, 28, 25, 34).

- **Data Rows:**
  - The first column specifies the number of stackers (e.g., 110, 126, 142).
  - Subsequent columns under each threshold-item header pair indicate the estimated minutes required for each maintenance task.

**Example:**

| Threshold | 3K | 1.1M | 1.1M | 4.4M | 4.4M | 57.2M |
|-----------|----|------|------|------|------|-------|
| Item #    | 5  | 8    | 9    | 10   | 23   | 24    |
| # Stackers|    |      |      |      |      |       |
| 110       | 9  | 35   | 37   | 139  | 21   | 70    |
| 126       | 1  | 5    | 3    | 10   | 3    | 10    |



| Threshold | 1 Month | 1K  | 1.1M | 14.3M | 14.3M | 20M  |
|-----------|---------|-----|------|-------|-------|------|
| Item #    | 28      | 25  | 34   | 35    | 36    | 29   |
| # Stackers|         |     |      |       |       |      |
| 110       | 18      | 5   | 7    | 14    | 20    | 219  |
| 126       | 2       | 1   | 1    | 2     | 2     | 10   |


Use this structure to accurately describe the formatting and content of these tables, ensuring clear representation of maintenance tasks and their corresponding times for different stacker configurations.

Thresholds and PM Time Summary example:

| Threshold    | Hrs/Yr |
|--------------|--------|
| Daily        | 527.80 |
| Monthly      | 8.20   |
| 1,100,000    | 97.58  |
| 2,200,000    | 15.68  |
| 4,400,000    | 33.76  |
| 14,300,000   | 3.28   |
| 20,000,000   | 10.49  |
| 57,200,000   | 2.14   |

---
