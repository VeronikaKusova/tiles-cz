## Sada matic dlaždic

Pro správné fungování dlaždicových služeb je třeba předem ustanovit 

1. Počátek celého systému (souřadnice levého-horního rohu v daném
   souřadnicovém systému)
2. Velikost dlaždice (preferovaná varianta 512px nebo akceptovatelná 256px)
3. Řadu měřítek, ve kterých budou definovány jednotlivé matice

### Souřadnicový systém Web Mercator EPSG:3857

Jedná se o globální souřadnicový systém a v současnosti se jedná o de-facto
technologický standard pro publikaci mapových děl v prostředí WWW. Jeho podoba
byla původně kodifikována firmou Google a převzata konsorciem OGC.

Země je reprezentovaná pomocí projekce Mercator ([EPSG:3857](https://epsg.io/3857)) a pokrývá oblast -180.0, -85.06, 180.0, 85.06 v souřadnicích WGS84 nebo -20026376.39, -20048966.10, 20026376.39, 20048966.10 v souřadnicích EPSG:3857.

Měřítková řada a její charakteristiky:

| Úroveň přiblížení | Rozlišení [m/px] | Měřítko mapy (při 90.7 dpi) | Šířka a výška mapy (px) |
|-------------------|------------------|-----------------------------|-------------------------|
| 0                 | 156543.033       | 1 : 559 082 264.03          | 256                     |
| 1                 | 78271.5169       | 1 : 279 541 132.01          | 512                     |
| 2                 | 39135.7584       | 1 : 139 770 566.01          | 1 024                   |
| 3                 | 19567.8792       | 1 : 69 885 283.00           | 2 048                   |
| 4                 | 9783.93962       | 1 : 34 942 641.50           | 4 096                   |
| 5                 | 4891.96981       | 1 : 17 471 320.75           | 8 192                   |
| 6                 | 2445.98490       | 1 : 8 735 660.38            | 16 384                  |
| 7                 | 1222.99245       | 1 : 4 367 830.19            | 32 768                  |
| 8                 | 611.496226       | 1 : 2 183 915.09            | 65 536                  |
| 9                 | 305.748113       | 1 : 1 091 957.55            | 131 072                 |
| 10                | 152.874056       | 1 : 545 978.77              | 262 144                 |
| 11                | 76.4370282       | 1 : 272 989.39              | 524 288                 |
| 12                | 38.2185141       | 1 : 136 494.69              | 1 048 576               |
| 13                | 19.1092570       | 1 : 68 247.35               | 2 097 152               |
| 14                | 9.55462853       | 1 : 34 123.67               | 4 194 304               |
| 15                | 4.77731426       | 1 : 17 061.84               | 8 388 608               |
| 16                | 2.38865713       | 1 : 8 530.92                | 16 777 216              |
| 17                | 1.19432856       | 1 : 4 265.46                | 33 554 432              |
| 18                | 0.59716428       | 1 : 2 132.73                | 67 108 864              |
| 19                | 0.29858214       | 1 : 1 066.36                | 134 217 728             |
| 20                | 0.14929107       | 1 : 533.18                  | 268 435 456             |
| 21                | 0.07464553       | 1 : 266.59                  | 536 870 912             |
| 22                | 0.03732276       | 1 : 133.30                  | 1 073 741 824           |
| 23                | 0.01866138       | 1 : 66.65                   | 2 147 483 648           |


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

| Úroveň přiblížení | Rozlišení [m/px] | Měřítko mapy (při 90.7 dpi) | Šířka a výška mapy (px) |
|-------------------|------------------|-----------------------------|-------------------------|
| 0                 | 2048.25600       | 1 : 7 315 200.00            | 256                     |
| 1                 | 1024.12800       | 1 : 3 657 600.00            | 512                     |
| 2                 | 512.064000       | 1 : 1 828 800.00            | 1 024                   |
| 3                 | 256.032000       | 1 : 914 400.00              | 2 048                   |
| 4                 | 128.016000       | 1 : 457 200.00              | 4 096                   |
| 5                 | 64.0080000       | 1 : 228 600.00              | 8 192                   |
| 6                 | 32.0040000       | 1 : 114 300.00              | 16 384                  |
| 7                 | 16.0020000       | 1 : 57 150.00               | 32 768                  |
| 8                 | 8.00100000       | 1 : 28 575.00               | 65 536                  |
| 9                 | 4.00050000       | 1 : 14 287.50               | 131 072                 |
| 10                | 2.00025000       | 1 : 7 143.75                | 262 144                 |
| 11                | 1.00012500       | 1 : 3 571.88                | 524 288                 |
| 12                | 0.50006250       | 1 : 1 785.94                | 1 048 576               |
| 13                | 0.25003125       | 1 : 892.97                  | 2 097 152               |
| 14                | 0.12501562       | 1 : 446.48                  | 4 194 304               |
| 15                | 0.06250781       | 1 : 223.24                  | 8 388 608               |
| 16                | 0.03125390       | 1 : 111.62                  | 16 777 216              |
| 17                | 0.01562695       | 1 : 55.81                   | 33 554 432              |
| 18                | 0.00781347       | 1 : 27.91                   | 67 108 864              |
| 19                | 0.00390673       | 1 : 13.95                   | 134 217 728             |



### Rozlišení pro tisk

*TODO* Dospecifikovat tiskovou HiDPI službu a její rozlišení.

Všechny měřítkové řady musí podporovat větší rozlišení pro tisk (např. 300dpi). To lze zajistit generováním dlaždic za běhu nebo předgenerováním větších dlaždic.
