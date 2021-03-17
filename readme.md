# Zoom Recording Parser 

Zoom does not have a complete recording size by person section. I built the script to aid in finding who is consuming all the zoom storage.



---

Go to your domains recordings management page (Admin only)

```
 https://<ZOOMDOMAIN>/recording/management
```

Select two dates to search between. Export and Download the search results. Put the csv in the same folder as the zoomrec.py script or pass the full path of the csv to the script.

```
python3 zoomrec.py <pathtoexportedcsv> <outfile.csv>
```

Example of exported csv

| Email        | Size in GB |
| ------------ | ---------- |
| foo@bar.com  | 13         |
| jdoe@bar.com | 0.2        |

---

Warning: Zoom will only export upto 5000 entries and a time.

