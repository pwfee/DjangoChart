# DjangoChart

Base on Django + [Pandas][1] and [Echarts][2] + [bootstrap-layout][3]



[1]: https://github.com/pandas-dev/pandas
[2]: https://github.com/ecomfe/echarts
[3]: https://github.com/themekit/bootstrap-layout

### CSV Storage Path
`/static/csv/`



### CSV Format:
1.OHLC-Chart :

| dates | openp | closep | lowp | highp |
| :------| ------: | :------: | :------:|:------:|
|01/01/1990|0.789|0.789|0.789|0.789|
|02/01/1990|0.7903|0.7865|0.7844|0.7903|
|03/01/1990|0.7862|0.7837|0.7827|0.7862|
|04/01/1990|0.7905|0.7894|0.7825|0.7905|


2.Line-Chart:

| dates | closep |
| :------| ------: | 
|01/01/1990|1.6125|
|02/01/1990|1.61|
|03/01/1990|1.6125|
|04/01/1990|1.6355|


