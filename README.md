# Project README

## Project Objective
The objective of this project is to find best possible path to regulate the velib network.

## Data
The data used in this project is the Velib data from Paris. The data is available in the `data/` directory.


## Running the Code
To run the code and reproduce the results, follow these steps:

1. Create a virtual environment:
   ```shell
   python -m venv venv
    ```
2. Activate the virtual environment:
    - On Windows:
      ```shell
      venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```shell
      source venv/bin/activate
      ```
3. Install the required packages:
    ```shell
    pip install -r requirements.txt
    ```
4. Run the main script:
    ```shell
    python main.py
    ```


## Results
You can find the results of this project in the `logs/` directory.



### an example of log
```
2024-07-31 18:35:40,194 - Loading data from data/velib-emplacement-des-stations.csv
2024-07-31 18:35:40,198 - Data loaded
2024-07-31 18:35:40,198 - Loading pre-initialized graph (it might take 35s)
2024-07-31 18:36:02,592 - Graph loaded
2024-07-31 18:36:02,592 - Start iteration 1
2024-07-31 18:36:02,593 - Start station chosen: 15028 with imbalance 35
2024-07-31 18:36:02,593 - End station chosen: 15019 with imbalance -18
2024-07-31 18:36:02,593 - Distance: 1.5414439111275084
2024-07-31 18:36:02,593 - Starting A* algorithm from station 15028 to station 15019
2024-07-31 18:36:03,207 - Explored 1000 nodes so far
2024-07-31 18:36:03,523 - Optimal path found: 15028 -> 15019
2024-07-31 18:36:03,523 - Number of bikes to move: 15
2024-07-31 18:36:03,523 - Iteration 1: Optimal path found:
2024-07-31 18:36:03,524 - Path: 15028 -> 15019
2024-07-31 18:36:03,524 - Moved 15 bikes from station 15028 to station 15019
2024-07-31 18:36:03,524 - Start iteration 2
2024-07-31 18:36:03,524 - Start station chosen: 13055 with imbalance 29
2024-07-31 18:36:03,524 - End station chosen: 12106 with imbalance -34
2024-07-31 18:36:03,524 - Distance: 1.7101895066410635
2024-07-31 18:36:03,524 - Starting A* algorithm from station 13055 to station 12106
2024-07-31 18:36:04,179 - Explored 1000 nodes so far
2024-07-31 18:36:04,783 - Optimal path found: 13055 -> 12106
2024-07-31 18:36:04,783 - Number of bikes to move: 15
2024-07-31 18:36:04,784 - Iteration 2: Optimal path found:
2024-07-31 18:36:04,784 - Path: 13055 -> 12106
2024-07-31 18:36:04,784 - Moved 15 bikes from station 13055 to station 12106
2024-07-31 18:36:04,784 - Start iteration 3
2024-07-31 18:36:04,784 - Start station chosen: 15030 with imbalance 36
2024-07-31 18:36:04,784 - End station chosen: 16039 with imbalance -20
2024-07-31 18:36:04,784 - Distance: 1.6489694323012574
2024-07-31 18:36:04,784 - Starting A* algorithm from station 15030 to station 16039
2024-07-31 18:36:05,516 - Explored 1000 nodes so far
2024-07-31 18:36:06,788 - Explored 2000 nodes so far
2024-07-31 18:36:08,329 - Explored 3000 nodes so far
2024-07-31 18:36:09,942 - Explored 4000 nodes so far
2024-07-31 18:36:11,402 - Explored 5000 nodes so far
2024-07-31 18:36:12,766 - Explored 6000 nodes so far
2024-07-31 18:36:14,215 - Explored 7000 nodes so far
2024-07-31 18:36:15,509 - Explored 8000 nodes so far
2024-07-31 18:36:16,985 - Explored 9000 nodes so far
2024-07-31 18:36:19,244 - Explored 10000 nodes so far
2024-07-31 18:36:20,718 - Explored 11000 nodes so far
2024-07-31 18:36:22,198 - Explored 12000 nodes so far
2024-07-31 18:36:23,699 - Explored 13000 nodes so far
2024-07-31 18:36:25,092 - Explored 14000 nodes so far
2024-07-31 18:36:26,423 - Explored 15000 nodes so far
2024-07-31 18:36:27,713 - Explored 16000 nodes so far
2024-07-31 18:36:29,006 - Explored 17000 nodes so far
2024-07-31 18:36:30,255 - Explored 18000 nodes so far
2024-07-31 18:36:31,504 - Explored 19000 nodes so far
2024-07-31 18:36:32,858 - Explored 20000 nodes so far
2024-07-31 18:36:32,860 - A* algorithm reached the maximum number of explored nodes (20000)
2024-07-31 18:36:34,772 - Iteration 3: No path found.
2024-07-31 18:36:34,773 - Start iteration 4
2024-07-31 18:36:34,773 - Start station chosen: 15008 with imbalance 29
2024-07-31 18:36:34,774 - End station chosen: 15053 with imbalance -21
2024-07-31 18:36:34,774 - Distance: 1.5533330723994443
2024-07-31 18:36:34,774 - Starting A* algorithm from station 15008 to station 15053
2024-07-31 18:36:35,632 - Explored 1000 nodes so far
2024-07-31 18:36:36,881 - Explored 2000 nodes so far
2024-07-31 18:36:38,318 - Explored 3000 nodes so far
2024-07-31 18:36:39,667 - Explored 4000 nodes so far
2024-07-31 18:36:41,017 - Explored 5000 nodes so far
2024-07-31 18:36:42,483 - Explored 6000 nodes so far
2024-07-31 18:36:43,843 - Explored 7000 nodes so far
2024-07-31 18:36:45,070 - Explored 8000 nodes so far
2024-07-31 18:36:46,740 - Explored 9000 nodes so far
2024-07-31 18:36:48,168 - Explored 10000 nodes so far
2024-07-31 18:36:49,593 - Explored 11000 nodes so far
2024-07-31 18:36:50,970 - Explored 12000 nodes so far
2024-07-31 18:36:52,371 - Explored 13000 nodes so far
2024-07-31 18:36:54,247 - Explored 14000 nodes so far
2024-07-31 18:36:55,719 - Explored 15000 nodes so far
2024-07-31 18:36:57,174 - Explored 16000 nodes so far
2024-07-31 18:36:58,563 - Explored 17000 nodes so far
2024-07-31 18:36:59,844 - Explored 18000 nodes so far
2024-07-31 18:37:01,726 - Explored 19000 nodes so far
2024-07-31 18:37:03,437 - Explored 20000 nodes so far
2024-07-31 18:37:03,439 - A* algorithm reached the maximum number of explored nodes (20000)
2024-07-31 18:37:05,060 - Iteration 4: No path found.
2024-07-31 18:37:05,060 - Start iteration 5
2024-07-31 18:37:05,061 - Start station chosen: 7010 with imbalance 30
2024-07-31 18:37:05,061 - End station chosen: 8017 with imbalance -19
2024-07-31 18:37:05,061 - Distance: 1.7854253164965599
2024-07-31 18:37:05,061 - Starting A* algorithm from station 7010 to station 8017
2024-07-31 18:37:05,892 - Explored 1000 nodes so far
2024-07-31 18:37:07,860 - Explored 2000 nodes so far
2024-07-31 18:37:09,313 - Explored 3000 nodes so far
2024-07-31 18:37:10,763 - Explored 4000 nodes so far
2024-07-31 18:37:12,464 - Explored 5000 nodes so far
2024-07-31 18:37:14,290 - Explored 6000 nodes so far
2024-07-31 18:37:15,988 - Explored 7000 nodes so far
2024-07-31 18:37:17,786 - Explored 8000 nodes so far
2024-07-31 18:37:19,343 - Explored 9000 nodes so far
2024-07-31 18:37:20,820 - Explored 10000 nodes so far
2024-07-31 18:37:22,406 - Explored 11000 nodes so far
2024-07-31 18:37:24,231 - Explored 12000 nodes so far
2024-07-31 18:37:26,020 - Explored 13000 nodes so far
2024-07-31 18:37:28,016 - Explored 14000 nodes so far
2024-07-31 18:37:29,689 - Explored 15000 nodes so far
2024-07-31 18:37:31,279 - Explored 16000 nodes so far
2024-07-31 18:37:33,429 - Explored 17000 nodes so far
2024-07-31 18:37:35,361 - Explored 18000 nodes so far
2024-07-31 18:37:37,009 - Explored 19000 nodes so far
2024-07-31 18:37:38,713 - Explored 20000 nodes so far
2024-07-31 18:37:38,714 - A* algorithm reached the maximum number of explored nodes (20000)
2024-07-31 18:37:40,427 - Iteration 5: No path found.
2024-07-31 18:37:40,427 - Start iteration 6
2024-07-31 18:37:40,428 - Start station chosen: 11102 with imbalance 30
2024-07-31 18:37:40,428 - End station chosen: 12108 with imbalance -18
2024-07-31 18:37:40,428 - Distance: 1.6220114686969942
2024-07-31 18:37:40,428 - Starting A* algorithm from station 11102 to station 12108
2024-07-31 18:37:42,193 - Explored 1000 nodes so far
2024-07-31 18:37:44,429 - Explored 2000 nodes so far
2024-07-31 18:37:46,424 - Explored 3000 nodes so far
2024-07-31 18:37:48,599 - Explored 4000 nodes so far
2024-07-31 18:37:50,358 - Explored 5000 nodes so far
2024-07-31 18:37:52,334 - Explored 6000 nodes so far
2024-07-31 18:37:54,391 - Explored 7000 nodes so far
2024-07-31 18:37:56,291 - Explored 8000 nodes so far
2024-07-31 18:37:58,047 - Explored 9000 nodes so far
2024-07-31 18:37:59,977 - Explored 10000 nodes so far
2024-07-31 18:38:01,845 - Explored 11000 nodes so far
2024-07-31 18:38:03,668 - Explored 12000 nodes so far
2024-07-31 18:38:05,192 - Explored 13000 nodes so far
2024-07-31 18:38:06,674 - Explored 14000 nodes so far
2024-07-31 18:38:08,274 - Explored 15000 nodes so far
2024-07-31 18:38:09,807 - Explored 16000 nodes so far
2024-07-31 18:38:11,313 - Explored 17000 nodes so far
2024-07-31 18:38:12,905 - Explored 18000 nodes so far
2024-07-31 18:38:14,444 - Explored 19000 nodes so far
2024-07-31 18:38:16,025 - Explored 20000 nodes so far
2024-07-31 18:38:16,027 - A* algorithm reached the maximum number of explored nodes (20000)
2024-07-31 18:38:17,720 - Iteration 6: No path found.
2024-07-31 18:38:17,720 - Start iteration 7
2024-07-31 18:38:17,721 - Start station chosen: 15008 with imbalance 29
2024-07-31 18:38:17,721 - End station chosen: 15053 with imbalance -21
2024-07-31 18:38:17,721 - Distance: 1.5533330723994443
2024-07-31 18:38:17,721 - Starting A* algorithm from station 15008 to station 15053
2024-07-31 18:38:18,547 - Explored 1000 nodes so far
2024-07-31 18:38:20,097 - Explored 2000 nodes so far
2024-07-31 18:38:21,875 - Explored 3000 nodes so far
2024-07-31 18:38:23,738 - Explored 4000 nodes so far
2024-07-31 18:38:25,240 - Explored 5000 nodes so far
2024-07-31 18:38:26,759 - Explored 6000 nodes so far
2024-07-31 18:38:28,512 - Explored 7000 nodes so far
2024-07-31 18:38:30,202 - Explored 8000 nodes so far
2024-07-31 18:38:31,856 - Explored 9000 nodes so far
2024-07-31 18:38:33,565 - Explored 10000 nodes so far
2024-07-31 18:38:35,087 - Explored 11000 nodes so far
2024-07-31 18:38:36,486 - Explored 12000 nodes so far
2024-07-31 18:38:37,965 - Explored 13000 nodes so far
2024-07-31 18:38:39,370 - Explored 14000 nodes so far
2024-07-31 18:38:40,776 - Explored 15000 nodes so far
2024-07-31 18:38:42,276 - Explored 16000 nodes so far
2024-07-31 18:38:44,051 - Explored 17000 nodes so far
2024-07-31 18:38:45,665 - Explored 18000 nodes so far
2024-07-31 18:38:47,150 - Explored 19000 nodes so far
2024-07-31 18:38:48,682 - Explored 20000 nodes so far
2024-07-31 18:38:48,684 - A* algorithm reached the maximum number of explored nodes (20000)
2024-07-31 18:38:50,231 - Iteration 7: No path found.
2024-07-31 18:38:50,231 - Start iteration 8
2024-07-31 18:38:50,232 - Start station chosen: 7010 with imbalance 30
2024-07-31 18:38:50,232 - End station chosen: 8017 with imbalance -19
2024-07-31 18:38:50,232 - Distance: 1.7854253164965599
2024-07-31 18:38:50,232 - Starting A* algorithm from station 7010 to station 8017
2024-07-31 18:38:50,964 - Explored 1000 nodes so far
2024-07-31 18:38:52,373 - Explored 2000 nodes so far
2024-07-31 18:38:53,774 - Explored 3000 nodes so far
2024-07-31 18:38:55,151 - Explored 4000 nodes so far
2024-07-31 18:38:56,598 - Explored 5000 nodes so far
2024-07-31 18:38:58,190 - Explored 6000 nodes so far
2024-07-31 18:38:59,819 - Explored 7000 nodes so far
2024-07-31 18:39:01,292 - Explored 8000 nodes so far
2024-07-31 18:39:02,790 - Explored 9000 nodes so far
2024-07-31 18:39:04,391 - Explored 10000 nodes so far
2024-07-31 18:39:06,075 - Explored 11000 nodes so far
2024-07-31 18:39:07,649 - Explored 12000 nodes so far
2024-07-31 18:39:09,131 - Explored 13000 nodes so far
2024-07-31 18:39:10,688 - Explored 14000 nodes so far
2024-07-31 18:39:12,186 - Explored 15000 nodes so far
2024-07-31 18:39:13,689 - Explored 16000 nodes so far
2024-07-31 18:39:15,047 - Explored 17000 nodes so far
2024-07-31 18:39:16,363 - Explored 18000 nodes so far
2024-07-31 18:39:17,854 - Explored 19000 nodes so far
2024-07-31 18:39:19,372 - Explored 20000 nodes so far
2024-07-31 18:39:19,373 - A* algorithm reached the maximum number of explored nodes (20000)
2024-07-31 18:39:20,909 - Iteration 8: No path found.
2024-07-31 18:39:20,910 - Start iteration 9
2024-07-31 18:39:20,910 - Start station chosen: 15030 with imbalance 36
2024-07-31 18:39:20,910 - End station chosen: 16039 with imbalance -20
2024-07-31 18:39:20,910 - Distance: 1.6489694323012574
2024-07-31 18:39:20,911 - Starting A* algorithm from station 15030 to station 16039
2024-07-31 18:39:21,636 - Explored 1000 nodes so far
2024-07-31 18:39:23,254 - Explored 2000 nodes so far
2024-07-31 18:39:24,734 - Explored 3000 nodes so far
2024-07-31 18:39:26,247 - Explored 4000 nodes so far
2024-07-31 18:39:27,815 - Explored 5000 nodes so far
2024-07-31 18:39:29,333 - Explored 6000 nodes so far
2024-07-31 18:39:30,758 - Explored 7000 nodes so far
2024-07-31 18:39:32,245 - Explored 8000 nodes so far
2024-07-31 18:39:33,762 - Explored 9000 nodes so far
2024-07-31 18:39:35,162 - Explored 10000 nodes so far
2024-07-31 18:39:36,530 - Explored 11000 nodes so far
2024-07-31 18:39:38,059 - Explored 12000 nodes so far
2024-07-31 18:39:39,492 - Explored 13000 nodes so far
2024-07-31 18:39:40,853 - Explored 14000 nodes so far
2024-07-31 18:39:42,357 - Explored 15000 nodes so far
2024-07-31 18:39:43,873 - Explored 16000 nodes so far
2024-07-31 18:39:45,310 - Explored 17000 nodes so far
2024-07-31 18:39:46,718 - Explored 18000 nodes so far
2024-07-31 18:39:48,361 - Explored 19000 nodes so far
2024-07-31 18:39:49,983 - Explored 20000 nodes so far
2024-07-31 18:39:49,984 - A* algorithm reached the maximum number of explored nodes (20000)
2024-07-31 18:39:52,459 - Iteration 9: No path found.
2024-07-31 18:39:52,459 - Start iteration 10
2024-07-31 18:39:52,460 - Start station chosen: 7010 with imbalance 30
2024-07-31 18:39:52,460 - End station chosen: 8017 with imbalance -19
2024-07-31 18:39:52,460 - Distance: 1.7854253164965599
2024-07-31 18:39:52,460 - Starting A* algorithm from station 7010 to station 8017
2024-07-31 18:39:53,452 - Explored 1000 nodes so far
2024-07-31 18:39:55,091 - Explored 2000 nodes so far
2024-07-31 18:39:56,738 - Explored 3000 nodes so far
2024-07-31 18:39:58,624 - Explored 4000 nodes so far
2024-07-31 18:40:00,175 - Explored 5000 nodes so far
2024-07-31 18:40:01,865 - Explored 6000 nodes so far
2024-07-31 18:40:04,001 - Explored 7000 nodes so far
2024-07-31 18:40:05,998 - Explored 8000 nodes so far
2024-07-31 18:40:07,868 - Explored 9000 nodes so far
2024-07-31 18:40:09,547 - Explored 10000 nodes so far
2024-07-31 18:40:11,536 - Explored 11000 nodes so far
2024-07-31 18:40:13,456 - Explored 12000 nodes so far
2024-07-31 18:40:15,081 - Explored 13000 nodes so far
2024-07-31 18:40:16,753 - Explored 14000 nodes so far
2024-07-31 18:40:18,590 - Explored 15000 nodes so far
2024-07-31 18:40:20,235 - Explored 16000 nodes so far
2024-07-31 18:40:21,663 - Explored 17000 nodes so far
2024-07-31 18:40:23,282 - Explored 18000 nodes so far
2024-07-31 18:40:24,897 - Explored 19000 nodes so far
2024-07-31 18:40:26,486 - Explored 20000 nodes so far
2024-07-31 18:40:26,488 - A* algorithm reached the maximum number of explored nodes (20000)
2024-07-31 18:40:28,401 - Iteration 10: No path found.
```