# DjangoChart

Bases on [Django][0] + [Pandas][1] and [Echarts][2] + [Fancytree][3], and provides customizable data visualization charts (Candlestick chart / Line chart).

--

[0]: https://github.com/django/django
[1]: https://github.com/pandas-dev/pandas
[2]: https://github.com/ecomfe/echarts
[3]: https://github.com/mar10/fancytree

#### What's New
- Add document trees of memory state in the sidebar
- Add legend, multi-panels
- Add another Y-axis in the panels
- Improve robustness in django
- change UI to fit the document trees
- set black as the default color of the first line in the chart

#### Some Tricks
- Press ctrl and click the file in the sidebar, if you want to view a specified chart in other tab
- Now, you can open any files as chart in your disks, just specify the path. *http://your-host/show/?path=xxxx*

#### CSV Storage Path
`/static/csv/`



#### CSV Format:
#####1.Single Panel Chart :

*Without y-axis*

| dates | openp | closep | lowp | highp |
| :------| ------: | :------: | :------:|:------:|
|01/01/1990|0.789|0.789|0.789|0.789|
|02/01/1990|0.7903|0.7865|0.7844|0.7903|
|03/01/1990|0.7862|0.7837|0.7827|0.7862|

*With another y-axis*

| dates | openp | closep | lowp | highp | test_y1 |
| :------| ------: | :------: | :------:|:------:|:------:|
|01/01/1990|0.789|0.789|0.789|0.789|1.23|
|02/01/1990|0.7903|0.7865|0.7844|0.7903|3.45|
|03/01/1990|0.7862|0.7837|0.7827|0.7862|4.56|



#####2.Two Panels Chart:

*Have P0(the top panel), P1(the second panel), With y-axis in P0 *

| dates | cft01_y0 | cftf01 | cfif01_y1_p0 | DLAY01_p1 |
| --- | --- | --- | --- | --- |
| 2015/3/20 | 97.09 | 98.17 | 3919 | 4174 |
| 2015/3/23 | 97.02 | 97.99 | 3994.2 | 4164 |
| 2015/3/24 | 96.92 | 97.94 | 3963.6 | 4161  |

*Have P0 and P1, With y-axis in P0 and P1*

| dates | cft01_y0 | cftf01 | cfif01_y1_p0 | DLAY01_p1 | DLAY01_y1_p1 |
| --- | --- | --- | --- | --- | --- |
| 2015/3/20 | 97.09 | 98.17 | 3919 | 4174 | 1234 |
| 2015/3/23 | 97.02 | 97.99 | 3994.2 | 4164 | 5678 |
| 2015/3/24 | 96.92 | 97.94 | 3963.6 | 4161  | 9123 |

#####3.Three Panels Chart:

*Have P0, P1 and P2*

| dates | openp | closep | highp | lowp | ub_y0_p0 | lb_y0 | mv_p0 | bw_p1 | pctb_y0_p2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2015/3/20 | 97.09 | 98.17 | 3919 | 4174 | 1234 |3919 | 4174 | 1234 | 6542 |
| 2015/3/23 | 97.02 | 97.99 | 3994.2 | 4164 | 5678 |3919 | 4174 | 1234 | 6542 |
| 2015/3/24 | 96.92 | 97.94 | 3963.6 | 4161  | 9123 |3919 | 4174 | 1234 | 6542 |


#### Preview:

![](http://ooatlgonu.bkt.clouddn.com/single_panel.png)
![](http://ooatlgonu.bkt.clouddn.com/three_panels.png)
![](http://ooatlgonu.bkt.clouddn.com/two_panels.png)

