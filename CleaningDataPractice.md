```python
import pandas as pd
```


```python
pew = pd.read_csv('C:\\Users\\bly\\Desktop\\pew.csv')
```


```python
pew.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>religion</th>
      <th>&lt;$10k</th>
      <th>$10-20k</th>
      <th>$20-30k</th>
      <th>$30-40k</th>
      <th>$40-50k</th>
      <th>$50-75k</th>
      <th>$75-100k</th>
      <th>$100-150k</th>
      <th>&gt;150k</th>
      <th>Don't know/refused</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Agnostic</td>
      <td>27</td>
      <td>34</td>
      <td>60</td>
      <td>81</td>
      <td>76</td>
      <td>137</td>
      <td>122</td>
      <td>109</td>
      <td>84</td>
      <td>96</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Atheist</td>
      <td>12</td>
      <td>27</td>
      <td>37</td>
      <td>52</td>
      <td>35</td>
      <td>70</td>
      <td>73</td>
      <td>59</td>
      <td>74</td>
      <td>76</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Buddhist</td>
      <td>27</td>
      <td>21</td>
      <td>30</td>
      <td>34</td>
      <td>33</td>
      <td>58</td>
      <td>62</td>
      <td>39</td>
      <td>53</td>
      <td>54</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Catholic</td>
      <td>418</td>
      <td>617</td>
      <td>732</td>
      <td>670</td>
      <td>638</td>
      <td>1116</td>
      <td>949</td>
      <td>792</td>
      <td>633</td>
      <td>1489</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Don’t know/refused</td>
      <td>15</td>
      <td>14</td>
      <td>15</td>
      <td>11</td>
      <td>10</td>
      <td>35</td>
      <td>21</td>
      <td>17</td>
      <td>18</td>
      <td>116</td>
    </tr>
  </tbody>
</table>
</div>




```python
pew.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 18 entries, 0 to 17
    Data columns (total 11 columns):
     #   Column              Non-Null Count  Dtype 
    ---  ------              --------------  ----- 
     0   religion            18 non-null     object
     1   <$10k               18 non-null     int64 
     2   $10-20k             18 non-null     int64 
     3   $20-30k             18 non-null     int64 
     4   $30-40k             18 non-null     int64 
     5   $40-50k             18 non-null     int64 
     6   $50-75k             18 non-null     int64 
     7   $75-100k            18 non-null     int64 
     8   $100-150k           18 non-null     int64 
     9   >150k               18 non-null     int64 
     10  Don't know/refused  18 non-null     int64 
    dtypes: int64(10), object(1)
    memory usage: 1.7+ KB
    


```python
pew.columns
```




    Index(['religion', '<$10k', '$10-20k', '$20-30k', '$30-40k', '$40-50k',
           '$50-75k', '$75-100k', '$100-150k', '>150k', 'Don't know/refused'],
          dtype='object')




```python
pew.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>&lt;$10k</th>
      <th>$10-20k</th>
      <th>$20-30k</th>
      <th>$30-40k</th>
      <th>$40-50k</th>
      <th>$50-75k</th>
      <th>$75-100k</th>
      <th>$100-150k</th>
      <th>&gt;150k</th>
      <th>Don't know/refused</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>18.000000</td>
      <td>18.000000</td>
      <td>18.000000</td>
      <td>18.000000</td>
      <td>18.000000</td>
      <td>18.000000</td>
      <td>18.000000</td>
      <td>18.000000</td>
      <td>18.000000</td>
      <td>18.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>107.222222</td>
      <td>154.500000</td>
      <td>186.500000</td>
      <td>183.444444</td>
      <td>171.388889</td>
      <td>288.055556</td>
      <td>221.666667</td>
      <td>177.611111</td>
      <td>144.888889</td>
      <td>340.055556</td>
    </tr>
    <tr>
      <th>std</th>
      <td>168.931784</td>
      <td>255.172433</td>
      <td>309.891869</td>
      <td>291.470354</td>
      <td>271.144446</td>
      <td>458.442436</td>
      <td>345.078849</td>
      <td>275.679724</td>
      <td>205.224952</td>
      <td>530.523878</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>3.000000</td>
      <td>4.000000</td>
      <td>2.000000</td>
      <td>7.000000</td>
      <td>3.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>8.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>12.250000</td>
      <td>14.750000</td>
      <td>17.000000</td>
      <td>15.750000</td>
      <td>15.000000</td>
      <td>34.250000</td>
      <td>25.250000</td>
      <td>22.500000</td>
      <td>23.750000</td>
      <td>41.250000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>20.000000</td>
      <td>27.000000</td>
      <td>33.500000</td>
      <td>40.000000</td>
      <td>34.000000</td>
      <td>66.500000</td>
      <td>65.500000</td>
      <td>48.500000</td>
      <td>53.500000</td>
      <td>74.500000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>170.000000</td>
      <td>193.000000</td>
      <td>192.000000</td>
      <td>198.750000</td>
      <td>166.750000</td>
      <td>201.500000</td>
      <td>128.750000</td>
      <td>103.500000</td>
      <td>134.250000</td>
      <td>294.750000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>575.000000</td>
      <td>869.000000</td>
      <td>1064.000000</td>
      <td>982.000000</td>
      <td>881.000000</td>
      <td>1486.000000</td>
      <td>949.000000</td>
      <td>792.000000</td>
      <td>634.000000</td>
      <td>1529.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
long_pew = pd.melt(
    pew,
    id_vars='religion', 
    var_name = 'income', 
    value_name = 'count')
```


```python
long_pew.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>religion</th>
      <th>income</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Agnostic</td>
      <td>&lt;$10k</td>
      <td>27</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Atheist</td>
      <td>&lt;$10k</td>
      <td>12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Buddhist</td>
      <td>&lt;$10k</td>
      <td>27</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Catholic</td>
      <td>&lt;$10k</td>
      <td>418</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Don’t know/refused</td>
      <td>&lt;$10k</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
billboard = pd.read_csv('C:\\Users\\bly\\Desktop\\data\\billboard.csv')
```


```python
billboard
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>artist</th>
      <th>track</th>
      <th>time</th>
      <th>date.entered</th>
      <th>wk1</th>
      <th>wk2</th>
      <th>wk3</th>
      <th>wk4</th>
      <th>wk5</th>
      <th>...</th>
      <th>wk67</th>
      <th>wk68</th>
      <th>wk69</th>
      <th>wk70</th>
      <th>wk71</th>
      <th>wk72</th>
      <th>wk73</th>
      <th>wk74</th>
      <th>wk75</th>
      <th>wk76</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>2 Pac</td>
      <td>Baby Don't Cry (Keep...</td>
      <td>4:22</td>
      <td>2000-02-26</td>
      <td>87</td>
      <td>82.0</td>
      <td>72.0</td>
      <td>77.0</td>
      <td>87.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2000</td>
      <td>2Ge+her</td>
      <td>The Hardest Part Of ...</td>
      <td>3:15</td>
      <td>2000-09-02</td>
      <td>91</td>
      <td>87.0</td>
      <td>92.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Kryptonite</td>
      <td>3:53</td>
      <td>2000-04-08</td>
      <td>81</td>
      <td>70.0</td>
      <td>68.0</td>
      <td>67.0</td>
      <td>66.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>76</td>
      <td>76.0</td>
      <td>72.0</td>
      <td>69.0</td>
      <td>67.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2000</td>
      <td>504 Boyz</td>
      <td>Wobble Wobble</td>
      <td>3:35</td>
      <td>2000-04-15</td>
      <td>57</td>
      <td>34.0</td>
      <td>25.0</td>
      <td>17.0</td>
      <td>17.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>312</th>
      <td>2000</td>
      <td>Yankee Grey</td>
      <td>Another Nine Minutes</td>
      <td>3:10</td>
      <td>2000-04-29</td>
      <td>86</td>
      <td>83.0</td>
      <td>77.0</td>
      <td>74.0</td>
      <td>83.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>313</th>
      <td>2000</td>
      <td>Yearwood, Trisha</td>
      <td>Real Live Woman</td>
      <td>3:55</td>
      <td>2000-04-01</td>
      <td>85</td>
      <td>83.0</td>
      <td>83.0</td>
      <td>82.0</td>
      <td>81.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>314</th>
      <td>2000</td>
      <td>Ying Yang Twins</td>
      <td>Whistle While You Tw...</td>
      <td>4:19</td>
      <td>2000-03-18</td>
      <td>95</td>
      <td>94.0</td>
      <td>91.0</td>
      <td>85.0</td>
      <td>84.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>315</th>
      <td>2000</td>
      <td>Zombie Nation</td>
      <td>Kernkraft 400</td>
      <td>3:30</td>
      <td>2000-09-02</td>
      <td>99</td>
      <td>99.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>316</th>
      <td>2000</td>
      <td>matchbox twenty</td>
      <td>Bent</td>
      <td>4:12</td>
      <td>2000-04-29</td>
      <td>60</td>
      <td>37.0</td>
      <td>29.0</td>
      <td>24.0</td>
      <td>22.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>317 rows × 81 columns</p>
</div>




```python
long_billboard = pd.melt(
    billboard,
    id_vars=['year','artist','track','time','date.entered'],
    var_name='week',
    value_name='rating')
```


```python
long_billboard
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>artist</th>
      <th>track</th>
      <th>time</th>
      <th>date.entered</th>
      <th>week</th>
      <th>rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>2 Pac</td>
      <td>Baby Don't Cry (Keep...</td>
      <td>4:22</td>
      <td>2000-02-26</td>
      <td>wk1</td>
      <td>87.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2000</td>
      <td>2Ge+her</td>
      <td>The Hardest Part Of ...</td>
      <td>3:15</td>
      <td>2000-09-02</td>
      <td>wk1</td>
      <td>91.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Kryptonite</td>
      <td>3:53</td>
      <td>2000-04-08</td>
      <td>wk1</td>
      <td>81.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk1</td>
      <td>76.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2000</td>
      <td>504 Boyz</td>
      <td>Wobble Wobble</td>
      <td>3:35</td>
      <td>2000-04-15</td>
      <td>wk1</td>
      <td>57.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>24087</th>
      <td>2000</td>
      <td>Yankee Grey</td>
      <td>Another Nine Minutes</td>
      <td>3:10</td>
      <td>2000-04-29</td>
      <td>wk76</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24088</th>
      <td>2000</td>
      <td>Yearwood, Trisha</td>
      <td>Real Live Woman</td>
      <td>3:55</td>
      <td>2000-04-01</td>
      <td>wk76</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24089</th>
      <td>2000</td>
      <td>Ying Yang Twins</td>
      <td>Whistle While You Tw...</td>
      <td>4:19</td>
      <td>2000-03-18</td>
      <td>wk76</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24090</th>
      <td>2000</td>
      <td>Zombie Nation</td>
      <td>Kernkraft 400</td>
      <td>3:30</td>
      <td>2000-09-02</td>
      <td>wk76</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24091</th>
      <td>2000</td>
      <td>matchbox twenty</td>
      <td>Bent</td>
      <td>4:12</td>
      <td>2000-04-29</td>
      <td>wk76</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>24092 rows × 7 columns</p>
</div>




```python
ebola = pd.read_csv('C:\\Users\\bly\\Desktop\\data\\country_timeseries.csv')
```


```python
ebola
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Day</th>
      <th>Cases_Guinea</th>
      <th>Cases_Liberia</th>
      <th>Cases_SierraLeone</th>
      <th>Cases_Nigeria</th>
      <th>Cases_Senegal</th>
      <th>Cases_UnitedStates</th>
      <th>Cases_Spain</th>
      <th>Cases_Mali</th>
      <th>Deaths_Guinea</th>
      <th>Deaths_Liberia</th>
      <th>Deaths_SierraLeone</th>
      <th>Deaths_Nigeria</th>
      <th>Deaths_Senegal</th>
      <th>Deaths_UnitedStates</th>
      <th>Deaths_Spain</th>
      <th>Deaths_Mali</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/5/2015</td>
      <td>289</td>
      <td>2776.0</td>
      <td>NaN</td>
      <td>10030.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1786.0</td>
      <td>NaN</td>
      <td>2977.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/4/2015</td>
      <td>288</td>
      <td>2775.0</td>
      <td>NaN</td>
      <td>9780.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1781.0</td>
      <td>NaN</td>
      <td>2943.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2015</td>
      <td>287</td>
      <td>2769.0</td>
      <td>8166.0</td>
      <td>9722.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1767.0</td>
      <td>3496.0</td>
      <td>2915.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/2/2015</td>
      <td>286</td>
      <td>NaN</td>
      <td>8157.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3496.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>12/31/2014</td>
      <td>284</td>
      <td>2730.0</td>
      <td>8115.0</td>
      <td>9633.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1739.0</td>
      <td>3471.0</td>
      <td>2827.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>117</th>
      <td>3/27/2014</td>
      <td>5</td>
      <td>103.0</td>
      <td>8.0</td>
      <td>6.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>66.0</td>
      <td>6.0</td>
      <td>5.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>118</th>
      <td>3/26/2014</td>
      <td>4</td>
      <td>86.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>62.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>119</th>
      <td>3/25/2014</td>
      <td>3</td>
      <td>86.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>120</th>
      <td>3/24/2014</td>
      <td>2</td>
      <td>86.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>59.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>121</th>
      <td>3/22/2014</td>
      <td>0</td>
      <td>49.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>29.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>122 rows × 18 columns</p>
</div>




```python
long_ebola = pd.melt(ebola,
                     id_vars=['Date', 'Day'],
                     value_name='Count'
                    )
long_ebola
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Day</th>
      <th>variable</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/5/2015</td>
      <td>289</td>
      <td>Cases_Guinea</td>
      <td>2776.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/4/2015</td>
      <td>288</td>
      <td>Cases_Guinea</td>
      <td>2775.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2015</td>
      <td>287</td>
      <td>Cases_Guinea</td>
      <td>2769.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/2/2015</td>
      <td>286</td>
      <td>Cases_Guinea</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>12/31/2014</td>
      <td>284</td>
      <td>Cases_Guinea</td>
      <td>2730.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1947</th>
      <td>3/27/2014</td>
      <td>5</td>
      <td>Deaths_Mali</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1948</th>
      <td>3/26/2014</td>
      <td>4</td>
      <td>Deaths_Mali</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1949</th>
      <td>3/25/2014</td>
      <td>3</td>
      <td>Deaths_Mali</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1950</th>
      <td>3/24/2014</td>
      <td>2</td>
      <td>Deaths_Mali</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1951</th>
      <td>3/22/2014</td>
      <td>0</td>
      <td>Deaths_Mali</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>1952 rows × 4 columns</p>
</div>




```python
variable_split = long_ebola['variable'].str.split('_')
variable_split
```




    0       [Cases, Guinea]
    1       [Cases, Guinea]
    2       [Cases, Guinea]
    3       [Cases, Guinea]
    4       [Cases, Guinea]
                 ...       
    1947     [Deaths, Mali]
    1948     [Deaths, Mali]
    1949     [Deaths, Mali]
    1950     [Deaths, Mali]
    1951     [Deaths, Mali]
    Name: variable, Length: 1952, dtype: object




```python
long_ebola['Status'] = variable_split.str[0]
long_ebola['Country'] = variable_split.str[1]
```


```python
long_ebola
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Day</th>
      <th>variable</th>
      <th>Count</th>
      <th>Status</th>
      <th>Country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/5/2015</td>
      <td>289</td>
      <td>Cases_Guinea</td>
      <td>2776.0</td>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/4/2015</td>
      <td>288</td>
      <td>Cases_Guinea</td>
      <td>2775.0</td>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2015</td>
      <td>287</td>
      <td>Cases_Guinea</td>
      <td>2769.0</td>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/2/2015</td>
      <td>286</td>
      <td>Cases_Guinea</td>
      <td>NaN</td>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>4</th>
      <td>12/31/2014</td>
      <td>284</td>
      <td>Cases_Guinea</td>
      <td>2730.0</td>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1947</th>
      <td>3/27/2014</td>
      <td>5</td>
      <td>Deaths_Mali</td>
      <td>NaN</td>
      <td>Deaths</td>
      <td>Mali</td>
    </tr>
    <tr>
      <th>1948</th>
      <td>3/26/2014</td>
      <td>4</td>
      <td>Deaths_Mali</td>
      <td>NaN</td>
      <td>Deaths</td>
      <td>Mali</td>
    </tr>
    <tr>
      <th>1949</th>
      <td>3/25/2014</td>
      <td>3</td>
      <td>Deaths_Mali</td>
      <td>NaN</td>
      <td>Deaths</td>
      <td>Mali</td>
    </tr>
    <tr>
      <th>1950</th>
      <td>3/24/2014</td>
      <td>2</td>
      <td>Deaths_Mali</td>
      <td>NaN</td>
      <td>Deaths</td>
      <td>Mali</td>
    </tr>
    <tr>
      <th>1951</th>
      <td>3/22/2014</td>
      <td>0</td>
      <td>Deaths_Mali</td>
      <td>NaN</td>
      <td>Deaths</td>
      <td>Mali</td>
    </tr>
  </tbody>
</table>
<p>1952 rows × 6 columns</p>
</div>




```python
del long_ebola['variable']
```


```python
long_ebola
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Day</th>
      <th>Count</th>
      <th>Status</th>
      <th>Country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/5/2015</td>
      <td>289</td>
      <td>2776.0</td>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/4/2015</td>
      <td>288</td>
      <td>2775.0</td>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2015</td>
      <td>287</td>
      <td>2769.0</td>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/2/2015</td>
      <td>286</td>
      <td>NaN</td>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>4</th>
      <td>12/31/2014</td>
      <td>284</td>
      <td>2730.0</td>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1947</th>
      <td>3/27/2014</td>
      <td>5</td>
      <td>NaN</td>
      <td>Deaths</td>
      <td>Mali</td>
    </tr>
    <tr>
      <th>1948</th>
      <td>3/26/2014</td>
      <td>4</td>
      <td>NaN</td>
      <td>Deaths</td>
      <td>Mali</td>
    </tr>
    <tr>
      <th>1949</th>
      <td>3/25/2014</td>
      <td>3</td>
      <td>NaN</td>
      <td>Deaths</td>
      <td>Mali</td>
    </tr>
    <tr>
      <th>1950</th>
      <td>3/24/2014</td>
      <td>2</td>
      <td>NaN</td>
      <td>Deaths</td>
      <td>Mali</td>
    </tr>
    <tr>
      <th>1951</th>
      <td>3/22/2014</td>
      <td>0</td>
      <td>NaN</td>
      <td>Deaths</td>
      <td>Mali</td>
    </tr>
  </tbody>
</table>
<p>1952 rows × 5 columns</p>
</div>




```python
weather = pd.read_csv('C:\\Users\\bly\\Desktop\\data\\weather.csv')
```


```python
weather
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>year</th>
      <th>month</th>
      <th>element</th>
      <th>d1</th>
      <th>d2</th>
      <th>d3</th>
      <th>d4</th>
      <th>d5</th>
      <th>d6</th>
      <th>...</th>
      <th>d22</th>
      <th>d23</th>
      <th>d24</th>
      <th>d25</th>
      <th>d26</th>
      <th>d27</th>
      <th>d28</th>
      <th>d29</th>
      <th>d30</th>
      <th>d31</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>1</td>
      <td>tmax</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>27.8</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>1</td>
      <td>tmin</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>14.5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>2</td>
      <td>tmax</td>
      <td>NaN</td>
      <td>27.3</td>
      <td>24.1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>29.9</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>2</td>
      <td>tmin</td>
      <td>NaN</td>
      <td>14.4</td>
      <td>14.4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>10.7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>3</td>
      <td>tmax</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>32.1</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>3</td>
      <td>tmin</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>14.2</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>4</td>
      <td>tmax</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>36.3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>4</td>
      <td>tmin</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>16.7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>5</td>
      <td>tmax</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>33.2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>5</td>
      <td>tmin</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>18.2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>6</td>
      <td>tmax</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>30.1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>6</td>
      <td>tmin</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>18.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>7</td>
      <td>tmax</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>28.6</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>7</td>
      <td>tmin</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>17.5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>8</td>
      <td>tmax</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>29.6</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>26.4</td>
      <td>NaN</td>
      <td>29.7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>28.0</td>
      <td>NaN</td>
      <td>25.4</td>
    </tr>
    <tr>
      <th>15</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>8</td>
      <td>tmin</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15.8</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>15.0</td>
      <td>NaN</td>
      <td>15.6</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15.3</td>
      <td>NaN</td>
      <td>15.4</td>
    </tr>
    <tr>
      <th>16</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>10</td>
      <td>tmax</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>27.0</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>31.2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>10</td>
      <td>tmin</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>14.0</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>11</td>
      <td>tmax</td>
      <td>NaN</td>
      <td>31.3</td>
      <td>NaN</td>
      <td>27.2</td>
      <td>26.3</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>28.1</td>
      <td>27.7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>19</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>11</td>
      <td>tmin</td>
      <td>NaN</td>
      <td>16.3</td>
      <td>NaN</td>
      <td>12.0</td>
      <td>7.9</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>12.1</td>
      <td>14.2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>20</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>12</td>
      <td>tmax</td>
      <td>29.9</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>27.8</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>21</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>12</td>
      <td>tmin</td>
      <td>13.8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>10.5</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>22 rows × 35 columns</p>
</div>




```python
long_weather = pd.melt( 
                       weather,
                       id_vars=['id','year','month','element'],
                       var_name='day',
                       value_name='temp'
                      )
```


```python
long_weather
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>year</th>
      <th>month</th>
      <th>element</th>
      <th>day</th>
      <th>temp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>1</td>
      <td>tmax</td>
      <td>d1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>1</td>
      <td>tmin</td>
      <td>d1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>2</td>
      <td>tmax</td>
      <td>d1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>2</td>
      <td>tmin</td>
      <td>d1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>3</td>
      <td>tmax</td>
      <td>d1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>677</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>10</td>
      <td>tmin</td>
      <td>d31</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>678</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>11</td>
      <td>tmax</td>
      <td>d31</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>679</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>11</td>
      <td>tmin</td>
      <td>d31</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>680</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>12</td>
      <td>tmax</td>
      <td>d31</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>681</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>12</td>
      <td>tmin</td>
      <td>d31</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>682 rows × 6 columns</p>
</div>




```python
pivot_weather = pd.pivot_table(
                         long_weather,
                         index=['id','year','month','day'],
                         columns='element',
                         values='temp'      
                        )
```


```python
pivot_weather.reset_index()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>element</th>
      <th>id</th>
      <th>year</th>
      <th>month</th>
      <th>day</th>
      <th>tmax</th>
      <th>tmin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>1</td>
      <td>d30</td>
      <td>27.8</td>
      <td>14.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>2</td>
      <td>d11</td>
      <td>29.7</td>
      <td>13.4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>2</td>
      <td>d2</td>
      <td>27.3</td>
      <td>14.4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>2</td>
      <td>d23</td>
      <td>29.9</td>
      <td>10.7</td>
    </tr>
    <tr>
      <th>4</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>2</td>
      <td>d3</td>
      <td>24.1</td>
      <td>14.4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>3</td>
      <td>d10</td>
      <td>34.5</td>
      <td>16.8</td>
    </tr>
    <tr>
      <th>6</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>3</td>
      <td>d16</td>
      <td>31.1</td>
      <td>17.6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>3</td>
      <td>d5</td>
      <td>32.1</td>
      <td>14.2</td>
    </tr>
    <tr>
      <th>8</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>4</td>
      <td>d27</td>
      <td>36.3</td>
      <td>16.7</td>
    </tr>
    <tr>
      <th>9</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>5</td>
      <td>d27</td>
      <td>33.2</td>
      <td>18.2</td>
    </tr>
    <tr>
      <th>10</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>6</td>
      <td>d17</td>
      <td>28.0</td>
      <td>17.5</td>
    </tr>
    <tr>
      <th>11</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>6</td>
      <td>d29</td>
      <td>30.1</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>7</td>
      <td>d3</td>
      <td>28.6</td>
      <td>17.5</td>
    </tr>
    <tr>
      <th>13</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>7</td>
      <td>d14</td>
      <td>29.9</td>
      <td>16.5</td>
    </tr>
    <tr>
      <th>14</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>8</td>
      <td>d23</td>
      <td>26.4</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>8</td>
      <td>d5</td>
      <td>29.6</td>
      <td>15.8</td>
    </tr>
    <tr>
      <th>16</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>8</td>
      <td>d29</td>
      <td>28.0</td>
      <td>15.3</td>
    </tr>
    <tr>
      <th>17</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>8</td>
      <td>d13</td>
      <td>29.8</td>
      <td>16.5</td>
    </tr>
    <tr>
      <th>18</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>8</td>
      <td>d25</td>
      <td>29.7</td>
      <td>15.6</td>
    </tr>
    <tr>
      <th>19</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>8</td>
      <td>d31</td>
      <td>25.4</td>
      <td>15.4</td>
    </tr>
    <tr>
      <th>20</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>8</td>
      <td>d8</td>
      <td>29.0</td>
      <td>17.3</td>
    </tr>
    <tr>
      <th>21</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>10</td>
      <td>d5</td>
      <td>27.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>10</td>
      <td>d14</td>
      <td>29.5</td>
      <td>13.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>10</td>
      <td>d15</td>
      <td>28.7</td>
      <td>10.5</td>
    </tr>
    <tr>
      <th>24</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>10</td>
      <td>d28</td>
      <td>31.2</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>10</td>
      <td>d7</td>
      <td>28.1</td>
      <td>12.9</td>
    </tr>
    <tr>
      <th>26</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>11</td>
      <td>d2</td>
      <td>31.3</td>
      <td>16.3</td>
    </tr>
    <tr>
      <th>27</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>11</td>
      <td>d5</td>
      <td>26.3</td>
      <td>7.9</td>
    </tr>
    <tr>
      <th>28</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>11</td>
      <td>d27</td>
      <td>27.7</td>
      <td>14.2</td>
    </tr>
    <tr>
      <th>29</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>11</td>
      <td>d26</td>
      <td>28.1</td>
      <td>12.1</td>
    </tr>
    <tr>
      <th>30</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>11</td>
      <td>d4</td>
      <td>27.2</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>31</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>12</td>
      <td>d1</td>
      <td>29.9</td>
      <td>13.8</td>
    </tr>
    <tr>
      <th>32</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>12</td>
      <td>d6</td>
      <td>27.8</td>
      <td>10.5</td>
    </tr>
  </tbody>
</table>
</div>




```python
long_billboard
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>artist</th>
      <th>track</th>
      <th>time</th>
      <th>date.entered</th>
      <th>week</th>
      <th>rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>2 Pac</td>
      <td>Baby Don't Cry (Keep...</td>
      <td>4:22</td>
      <td>2000-02-26</td>
      <td>wk1</td>
      <td>87.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2000</td>
      <td>2Ge+her</td>
      <td>The Hardest Part Of ...</td>
      <td>3:15</td>
      <td>2000-09-02</td>
      <td>wk1</td>
      <td>91.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Kryptonite</td>
      <td>3:53</td>
      <td>2000-04-08</td>
      <td>wk1</td>
      <td>81.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk1</td>
      <td>76.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2000</td>
      <td>504 Boyz</td>
      <td>Wobble Wobble</td>
      <td>3:35</td>
      <td>2000-04-15</td>
      <td>wk1</td>
      <td>57.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>24087</th>
      <td>2000</td>
      <td>Yankee Grey</td>
      <td>Another Nine Minutes</td>
      <td>3:10</td>
      <td>2000-04-29</td>
      <td>wk76</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24088</th>
      <td>2000</td>
      <td>Yearwood, Trisha</td>
      <td>Real Live Woman</td>
      <td>3:55</td>
      <td>2000-04-01</td>
      <td>wk76</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24089</th>
      <td>2000</td>
      <td>Ying Yang Twins</td>
      <td>Whistle While You Tw...</td>
      <td>4:19</td>
      <td>2000-03-18</td>
      <td>wk76</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24090</th>
      <td>2000</td>
      <td>Zombie Nation</td>
      <td>Kernkraft 400</td>
      <td>3:30</td>
      <td>2000-09-02</td>
      <td>wk76</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24091</th>
      <td>2000</td>
      <td>matchbox twenty</td>
      <td>Bent</td>
      <td>4:12</td>
      <td>2000-04-29</td>
      <td>wk76</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>24092 rows × 7 columns</p>
</div>




```python
long_billboard[long_billboard['track']=='Loser']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>artist</th>
      <th>track</th>
      <th>time</th>
      <th>date.entered</th>
      <th>week</th>
      <th>rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk1</td>
      <td>76.0</td>
    </tr>
    <tr>
      <th>320</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk2</td>
      <td>76.0</td>
    </tr>
    <tr>
      <th>637</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk3</td>
      <td>72.0</td>
    </tr>
    <tr>
      <th>954</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk4</td>
      <td>69.0</td>
    </tr>
    <tr>
      <th>1271</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk5</td>
      <td>67.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>22510</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk72</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>22827</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk73</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23144</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk74</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23461</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk75</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23778</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk76</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>76 rows × 7 columns</p>
</div>




```python
billboard_songs = long_billboard[['year','artist','track','time']]
billboard_songs
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>artist</th>
      <th>track</th>
      <th>time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>2 Pac</td>
      <td>Baby Don't Cry (Keep...</td>
      <td>4:22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2000</td>
      <td>2Ge+her</td>
      <td>The Hardest Part Of ...</td>
      <td>3:15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Kryptonite</td>
      <td>3:53</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2000</td>
      <td>504 Boyz</td>
      <td>Wobble Wobble</td>
      <td>3:35</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>24087</th>
      <td>2000</td>
      <td>Yankee Grey</td>
      <td>Another Nine Minutes</td>
      <td>3:10</td>
    </tr>
    <tr>
      <th>24088</th>
      <td>2000</td>
      <td>Yearwood, Trisha</td>
      <td>Real Live Woman</td>
      <td>3:55</td>
    </tr>
    <tr>
      <th>24089</th>
      <td>2000</td>
      <td>Ying Yang Twins</td>
      <td>Whistle While You Tw...</td>
      <td>4:19</td>
    </tr>
    <tr>
      <th>24090</th>
      <td>2000</td>
      <td>Zombie Nation</td>
      <td>Kernkraft 400</td>
      <td>3:30</td>
    </tr>
    <tr>
      <th>24091</th>
      <td>2000</td>
      <td>matchbox twenty</td>
      <td>Bent</td>
      <td>4:12</td>
    </tr>
  </tbody>
</table>
<p>24092 rows × 4 columns</p>
</div>




```python
billboard_songs = billboard_songs.drop_duplicates()
billboard_songs
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>artist</th>
      <th>track</th>
      <th>time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>2 Pac</td>
      <td>Baby Don't Cry (Keep...</td>
      <td>4:22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2000</td>
      <td>2Ge+her</td>
      <td>The Hardest Part Of ...</td>
      <td>3:15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Kryptonite</td>
      <td>3:53</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2000</td>
      <td>504 Boyz</td>
      <td>Wobble Wobble</td>
      <td>3:35</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>312</th>
      <td>2000</td>
      <td>Yankee Grey</td>
      <td>Another Nine Minutes</td>
      <td>3:10</td>
    </tr>
    <tr>
      <th>313</th>
      <td>2000</td>
      <td>Yearwood, Trisha</td>
      <td>Real Live Woman</td>
      <td>3:55</td>
    </tr>
    <tr>
      <th>314</th>
      <td>2000</td>
      <td>Ying Yang Twins</td>
      <td>Whistle While You Tw...</td>
      <td>4:19</td>
    </tr>
    <tr>
      <th>315</th>
      <td>2000</td>
      <td>Zombie Nation</td>
      <td>Kernkraft 400</td>
      <td>3:30</td>
    </tr>
    <tr>
      <th>316</th>
      <td>2000</td>
      <td>matchbox twenty</td>
      <td>Bent</td>
      <td>4:12</td>
    </tr>
  </tbody>
</table>
<p>317 rows × 4 columns</p>
</div>




```python
billboard_songs['id'] = range(len(billboard_songs))
```

    <ipython-input-105-331e5cd62e70>:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      billboard_songs['id'] = range(len(billboard_songs))
    


```python
billboard_songs
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>artist</th>
      <th>track</th>
      <th>time</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>2 Pac</td>
      <td>Baby Don't Cry (Keep...</td>
      <td>4:22</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2000</td>
      <td>2Ge+her</td>
      <td>The Hardest Part Of ...</td>
      <td>3:15</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Kryptonite</td>
      <td>3:53</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2000</td>
      <td>504 Boyz</td>
      <td>Wobble Wobble</td>
      <td>3:35</td>
      <td>4</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>312</th>
      <td>2000</td>
      <td>Yankee Grey</td>
      <td>Another Nine Minutes</td>
      <td>3:10</td>
      <td>312</td>
    </tr>
    <tr>
      <th>313</th>
      <td>2000</td>
      <td>Yearwood, Trisha</td>
      <td>Real Live Woman</td>
      <td>3:55</td>
      <td>313</td>
    </tr>
    <tr>
      <th>314</th>
      <td>2000</td>
      <td>Ying Yang Twins</td>
      <td>Whistle While You Tw...</td>
      <td>4:19</td>
      <td>314</td>
    </tr>
    <tr>
      <th>315</th>
      <td>2000</td>
      <td>Zombie Nation</td>
      <td>Kernkraft 400</td>
      <td>3:30</td>
      <td>315</td>
    </tr>
    <tr>
      <th>316</th>
      <td>2000</td>
      <td>matchbox twenty</td>
      <td>Bent</td>
      <td>4:12</td>
      <td>316</td>
    </tr>
  </tbody>
</table>
<p>317 rows × 5 columns</p>
</div>




```python
billboard_ratings = long_billboard.merge(
    billboard_songs,
    on=['year','artist','track','time']
)
billboard_ratings
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>artist</th>
      <th>track</th>
      <th>time</th>
      <th>date.entered</th>
      <th>week</th>
      <th>rating</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>2 Pac</td>
      <td>Baby Don't Cry (Keep...</td>
      <td>4:22</td>
      <td>2000-02-26</td>
      <td>wk1</td>
      <td>87.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2000</td>
      <td>2 Pac</td>
      <td>Baby Don't Cry (Keep...</td>
      <td>4:22</td>
      <td>2000-02-26</td>
      <td>wk2</td>
      <td>82.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2000</td>
      <td>2 Pac</td>
      <td>Baby Don't Cry (Keep...</td>
      <td>4:22</td>
      <td>2000-02-26</td>
      <td>wk3</td>
      <td>72.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2000</td>
      <td>2 Pac</td>
      <td>Baby Don't Cry (Keep...</td>
      <td>4:22</td>
      <td>2000-02-26</td>
      <td>wk4</td>
      <td>77.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2000</td>
      <td>2 Pac</td>
      <td>Baby Don't Cry (Keep...</td>
      <td>4:22</td>
      <td>2000-02-26</td>
      <td>wk5</td>
      <td>87.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>24087</th>
      <td>2000</td>
      <td>matchbox twenty</td>
      <td>Bent</td>
      <td>4:12</td>
      <td>2000-04-29</td>
      <td>wk72</td>
      <td>NaN</td>
      <td>316</td>
    </tr>
    <tr>
      <th>24088</th>
      <td>2000</td>
      <td>matchbox twenty</td>
      <td>Bent</td>
      <td>4:12</td>
      <td>2000-04-29</td>
      <td>wk73</td>
      <td>NaN</td>
      <td>316</td>
    </tr>
    <tr>
      <th>24089</th>
      <td>2000</td>
      <td>matchbox twenty</td>
      <td>Bent</td>
      <td>4:12</td>
      <td>2000-04-29</td>
      <td>wk74</td>
      <td>NaN</td>
      <td>316</td>
    </tr>
    <tr>
      <th>24090</th>
      <td>2000</td>
      <td>matchbox twenty</td>
      <td>Bent</td>
      <td>4:12</td>
      <td>2000-04-29</td>
      <td>wk75</td>
      <td>NaN</td>
      <td>316</td>
    </tr>
    <tr>
      <th>24091</th>
      <td>2000</td>
      <td>matchbox twenty</td>
      <td>Bent</td>
      <td>4:12</td>
      <td>2000-04-29</td>
      <td>wk76</td>
      <td>NaN</td>
      <td>316</td>
    </tr>
  </tbody>
</table>
<p>24092 rows × 8 columns</p>
</div>




```python
billboard_ratings = billboard_ratings[['id','date.entered','week','rating']]
billboard_ratings
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>date.entered</th>
      <th>week</th>
      <th>rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>2000-02-26</td>
      <td>wk1</td>
      <td>87.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>2000-02-26</td>
      <td>wk2</td>
      <td>82.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>2000-02-26</td>
      <td>wk3</td>
      <td>72.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>2000-02-26</td>
      <td>wk4</td>
      <td>77.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>2000-02-26</td>
      <td>wk5</td>
      <td>87.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>24087</th>
      <td>316</td>
      <td>2000-04-29</td>
      <td>wk72</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24088</th>
      <td>316</td>
      <td>2000-04-29</td>
      <td>wk73</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24089</th>
      <td>316</td>
      <td>2000-04-29</td>
      <td>wk74</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24090</th>
      <td>316</td>
      <td>2000-04-29</td>
      <td>wk75</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24091</th>
      <td>316</td>
      <td>2000-04-29</td>
      <td>wk76</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>24092 rows × 4 columns</p>
</div>




```python
billboard_songs
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>artist</th>
      <th>track</th>
      <th>time</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>2 Pac</td>
      <td>Baby Don't Cry (Keep...</td>
      <td>4:22</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2000</td>
      <td>2Ge+her</td>
      <td>The Hardest Part Of ...</td>
      <td>3:15</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Kryptonite</td>
      <td>3:53</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2000</td>
      <td>504 Boyz</td>
      <td>Wobble Wobble</td>
      <td>3:35</td>
      <td>4</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>312</th>
      <td>2000</td>
      <td>Yankee Grey</td>
      <td>Another Nine Minutes</td>
      <td>3:10</td>
      <td>312</td>
    </tr>
    <tr>
      <th>313</th>
      <td>2000</td>
      <td>Yearwood, Trisha</td>
      <td>Real Live Woman</td>
      <td>3:55</td>
      <td>313</td>
    </tr>
    <tr>
      <th>314</th>
      <td>2000</td>
      <td>Ying Yang Twins</td>
      <td>Whistle While You Tw...</td>
      <td>4:19</td>
      <td>314</td>
    </tr>
    <tr>
      <th>315</th>
      <td>2000</td>
      <td>Zombie Nation</td>
      <td>Kernkraft 400</td>
      <td>3:30</td>
      <td>315</td>
    </tr>
    <tr>
      <th>316</th>
      <td>2000</td>
      <td>matchbox twenty</td>
      <td>Bent</td>
      <td>4:12</td>
      <td>316</td>
    </tr>
  </tbody>
</table>
<p>317 rows × 5 columns</p>
</div>




```python

```
