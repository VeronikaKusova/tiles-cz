## Sada matic dlaždic

Pro správné fungování dlaždicových služeb je třeba předem ustanovit 

1. Počátek celého systému (souřadnice levého-horního rohu v daném
   souřadnicovém systému)
2. Velikost dlaždice (obvykle 256 nebo 512px)
3. Řadu měřítek, ve kterých budou definovány jednotlivé matice

### Souřadnicový systém Web Mercator EPSG:3857

Jedná se o globální souřadnicový systém a v současnosti se jedná o de-facto
technologický standard pro publikaci mapových děl v prostředí WWW. Jeho podoba
byla původně kodifikována firmou Google a převzata konsorciem OGC.

Země je reprezentovaná pomocí projekce Mercator ([EPSG:3857](https://epsg.io/3857)) a pokrývá oblast -180.0, -85.06, 180.0, 85.06 v souřadnicích WGS84 nebo -20026376.39, -20048966.10, 20026376.39, 20048966.10 v souřadnicích EPSG:3857.

Měřítková řada a její charakteristiky:

| Úroveň přiblížení | Rozlišení [m/px] | Měřítko mapy (při 96 dpi) | Šířka a výška mapy (px) |
| ----------------- | --------------- | ------------------------- | ----------------------- |
| 0                 | 156 543.0339    | 1 : 591 658 710.90        | 256                     |
| 1                 | 78 271.51696    | 1 : 295 829 355.45        | 512                     |
| 2                 | 39 135.75848    | 1 : 147 914 677.73        | 1 024                   |
| 3                 | 19 567.87924    | 1 : 73 957 338.86         | 2 048                   |
| 4                 | 9 783.939620    | 1 : 36 978 669.43         | 4 096                   |
| 5                 | 4 891.969810    | 1 : 18 489 334.72         | 8 192                   |
| 6                 | 2 445.984905    | 1 : 9 244 667.36          | 16 384                  |
| 7                 | 1 222.992452    | 1 : 4 622 333.68          | 32 768                  |
| 8                 | 611.4962263     | 1 : 2 311 166.84          | 65 536                  |
| 9                 | 305.7481131     | 1 : 1 155 583.42          | 131 072                 |
| 10                | 152.8740566     | 1 : 577 791.71            | 262 144                 |
| 11                | 76.43702829     | 1 : 288 895.85            | 524 288                 |
| 12                | 38.21851414     | 1 : 144 447.93            | 1 048 576               |
| 13                | 19.10925707     | 1 : 72 223.96             | 2 097 152               |
| 14                | 9.554728536     | 1 : 36 111.98             | 4 194 304               |
| 15                | 4.777314268     | 1 : 18 055.99             | 8 388 608               |
| 16                | 2.388657133     | 1 : 9 028.00              | 16 777 216              |
| 17                | 1.194328566     | 1 : 4 514.00              | 33 554 432              |
| 18                | 0.597164263     | 1 : 2 257.00              | 67 108 864              |
| 19                | 0.298582142     | 1 : 1 128.50              | 134 217 728             |
| 20                | 0.149291071     | 1 : 564.25                | 268 435 456             |
| 21                | 0.074645535     | 1 : 282.12                | 536 870 912             |
| 22                | 0.037322768     | 1 : 141.06                | 1 073 741 824           |
| 23                | 0.018661384     | 1 : 70.53                 | 2 147 483 648           |


### Souřadnicový systém S-JTSK EPSG:5514

Jedná se o lokální souřadnicový systém používaný na území České a Slovenské
republiky, přičemž v tomto dokumentu se zabýváme pouze územím České republiky.

Oblast pokrytí je 12.09, 48.58, 18.86, 51.06 v souřadnicích WGS84 nebo
-935747.74, -1183037.28, -418641.09, -969106.24 v souřadnicích EPSG:5514.

Pro účely sady dlaždic stanovujeme počátek (levý-horní roh) systému do bodu

x: -925000, y: -920000

Sada měřítek je odvozena od základního principu: dlaždice na úrovni 0 pokrývá
celé území a v každé další úrovni se každá dlaždice "rozpadá" na 4 další.

Měřítková řada a její charakteristiky:

| Úroveň přiblížení | Rozlišní [m/px]   | Měřítko mapy (při 96 dpi) | Šířka a výška mapy (px) |
| ----------------- | ----------------- | ------------------------- | ----------------------- |
| 0                 | 2064.512          | 1 : 7315200               | 256                     |
| 1                 | 1032.256          | 1 : 3657600               | 512                     |
| 2                 | 516.128           | 1 : 1828800               | 1 024                   |
| 3                 | 258.064           | 1 : 914400                | 2 048                   |
| 4                 | 129.032           | 1 : 457200                | 4 096                   |
| 5                 | 64.516            | 1 : 228600                | 8 192                   |
| 6                 | 32.258            | 1 : 114300                | 16 384                  |
| 7                 | 16.129            | 1 : 57150                 | 32 768                  |
| 8                 | 8.0645            | 1 : 28575                 | 65 536                  |
| 9                 | 4.03225           | 1 : 14287.5               | 131 072                 |
| 10                | 2.016125          | 1 : 7143.75               | 262 144                 |
| 11                | 1.0080625         | 1 : 3571.875              | 524 288                 |
| 12                | 0.50403125        | 1 : 1785.9375             | 1 048 576               |
| 13                | 0.252015625       | 1 : 892.96875             | 2 097 152               |
| 14                | 0.1260078125      | 1 : 446.484375            | 4 194 304               |
| 15                | 0.06300390625     | 1 : 223.2421875           | 8 388 608               |
| 16                | 0.031501953125    | 1 : 111.62109375          | 16 777 216              |
| 17                | 0.0157509765625   | 1 : 55.810546875          | 33 554 432              |
| 18                | 0.00787548828125  | 1 : 27.9052734375         | 67 108 864              |
| 19                | 0.003937744140625 | 1 : 13.95263671875        | 134 217 728             |


### Souřadnicový systém S-JTSK EPSG:5514 - dekadická měřítková sada

Jedná se o lokální souřadnicový systém používaný na území České a Slovenské
republiky, přičemž v tomto dokumentu se zabýváme pouze územím České republiky.

Oblast pokrytí je 12.09, 48.58, 18.86, 51.06 v souřadnicích WGS84 nebo
-935747.74, -1183037.28, -418641.09, -969106.24 v souřadnicích EPSG:5514.

Pro účely sady dlaždic stanovujeme počátek (levý-horní roh) systému do bodu

x: -925000, y: -920000

Měřítková řada je odvozena podle dekadického měřítkového principu - jednotlivé
úrovně na sebe nijak nenavazují a celý systém je podřízen přirozeným měřítkům
používaným v tištěných mapách.

Měřítková řada a její charakteristiky:

**TODO** Tohle musíme dospecifikovat

| Úroveň přiblížení | Rozlišní [m/px]   | Měřítko mapy (při 96 dpi) | Šířka a výška mapy (px) |
| ----------------- | ----------------- | ------------------------- | ----------------------- |
| 0                 |                   | 1 : 10 000 000            |                         |
| 1                 |                   | 1 : 5 000 000             |                         |
| 2                 |                   | 1 : 2 500 000             |                         |
| 3                 |                   | 1 : 1 000 000             |                         |
| 4                 |                   | 1 : 500 000               |                         |
| 5                 |                   | 1 : 200 000               |                         |
| 6                 |                   | 1 : 100 000               |                         |
| 7                 |                   | 1 : 50 000                |                         |
| 8                 |                   | 1 : 25 000                |                         |
| 9                 |                   | 1 : 10 000                |                         |
| 10                |                   | 1 : 5 000                 |                         |
| 11                |                   | 1 : 2 000                 |                         |
| 12                |                   | 1 : 1 000                 |                         |
| 13                |                   | 1 : 500                   |                         |
| 14                |                   | 1 : 200                   |                         |
| 15                |                   | 1 : 100                   |                         |
| 16                |                   | 1 : 50                    |                         |
| 17                |                   | 1 : 20                    |                         |
| 18                |                   | 1 : 10                    |                         |
| 19                |                   | 1 : 5                     |                         |
| 20                |                   | 1 : 2                     |                         |
| 21                |                   | 1 : 1                     |                         |

2880 ?
https://www.natur.cuni.cz/geografie/geoinformatika-kartografie/ke-stazeni/vyuka/seminar-z-geoinformatiky/literatura/kartografie/

co zvolit nad  1mil a pod 10 000
https://www.zakonyprolidi.cz/cs/2006-430
