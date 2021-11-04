
# B. APPLICATION

### I. SETTING UP OUR DEVELOPMENT ENVIRONMENT


#pip install mysql-connector-python==8.0.11 #for python 3.8
#pip install pymysql


import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd
from sqlalchemy import create_engine
import pymysql

### II. HOW TO CONNECT GOOGLE COLAB DEVELOPMENT ENVIRONMENT TO THE LOCAL MYSQL DATABASE:
"""
If you are running this script from your local IDE, the connection with MySQL database can be easily established using these codes:"""

try:

    db  = mysql.connect(
                        host = "localhost",
                        user = "Lan_Trinh", #<your user name>
                        passwd = "MarieCurie1691!") #<your password>
    if db.is_connected():
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE AnimeDB")
        print("AnimeDB database is created")
        
except Error as e:

    print("Error while connecting to MySQL",e)

"""
For your local MySQL to be reachable by the Internet, you must host it in a third party server, in this case I am using ngrok. The step is as follow:
1. Download the program from https://ngrok.com/download then you will need to unzip the file and open the program.
2. To begin, connect your account using the Authtoken provided by this link https://dashboard.ngrok.com/get-started/your-authtoken. You will be asked to login or sign up.
`ngrok authtoken <your_auth_token>`
3. Then for MySQL, use the command `ngrok tcp 3306`, which will display the hostname.
4. For example, from the image below, host is given by `"0.tcp.ngrok.io"`, port number is `"14892"`. Bear in mind that everytime you run ngrok, your host address and port number will change
![ngrok.png](data:image/png;base64,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)
5. We will connect to our MySQL database using mysql.connector which require you to specify the host, port (as specified above) user and password as in your set up.


#ESTABLISHING CONNECTION BETWEEN THE Python IDE and MySQL database
#CREATING A NEW DATABASE IF SUCCESSFUL.
try:
    db  = mysql.connect(
                        host = "6.tcp.ngrok.io",
                        port ="18052",
                        user = "Lan_Trinh",
                        passwd = "MarieCurie1691!"
                        )
    if db.is_connected():
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE AnimeDB")
        print("AnimeDB database is created")
        
except Error as e:
    print("Error while connecting to MySQL",e)

"""

### III. READ AND INSERT DATA


#List of all animes and their related information
#Reading the csv file before adding the table in our database   
anime = pd.read_csv("anime.csv")
print(anime)

synopsis = pd.read_csv("anime_with_synopsis.csv")
print(synopsis)

#FOR A BIG TABLE WITH 35 COLUMNS, I DECIDED NOT TO CREATE THE TABLE
#AND DECLARE EACH VARIABLES ONE BY ONE BUT TO INSERT MY DATAFRAME IN TO
#THE DATABASE USING pandas to_sql() FUNCTION

#!!!YOU MUST ADAPT YOUR HOST ADDRESS AND PORT NUMBER EVERYTIME YOU NGROK
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}:{port}/{db}"
                       .format(host="6.tcp.ngrok.io", port="18052", user="Lan_Trinh",pw="MarieCurie1691!", db="AnimeDB"))

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                       .format(host="localhost", user="Lan_Trinh",pw="MarieCurie1691!", db="AnimeDB"))


#!!!YOU SHOULD ONLY RUN THIS CELL ONCE
anime.to_sql("anime", con = engine, if_exists = "append")
synopsis.to_sql("synopsis", con = engine, if_exists = "append")

"""What is happening?


*   `"anime"` is the name of the table in which we want to insert out pandas Dataframe.
*   `con = engine` provides the connection details (recall that we created engine using our authentication details in the step prior).
*  `if_exists = 'append'` checks whether the table we specified already exists or not, and then append the new data (if it does exist) or creates new table(if it doesn't).

### IV. DATA CLEANING & EXPLORATION
***1. CHECK FOR DUPLICATE***
"""

#reconnect
db = mysql.connect(host="localhost",
                   user="Lan_Trinh",
                   passwd = "MarieCurie1691!",
                   database = "animedb")

cursor = db.cursor()

#%load_ext google.colab.data_table

#WE FIRST TAKE A LOOK AT OUR COMPLETE TABLE
name = """SELECT *
          FROM anime
          """
#read_sql function return the result of our query as a dataframe
print(pd.read_sql(name,db))


#CHECK FOR DUPLICATE
#We know that MAL_ID has unique values and is our PRIMARY KEY
#So now we will inspect all the anime name similar and why is that
#the query return Name, Score,
#duplicate: number as duplicate per anime name
#tot: cummulative sum of number of anime

distinct = """WITH dup
              AS(SELECT Name, Score, COUNT(*) AS duplicate
                  FROM anime
                  GROUP BY Name
                  ORDER BY duplicate DESC)
              SELECT *,
                    SUM(duplicate) OVER(
                                      ORDER BY duplicate DESC
                                      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
                                      ) AS tot 
              FROM dup"""          

print(pd.read_sql(distinct,db))

result = pd.read_sql(distinct,db)

#For bettew view of the table, the output dataframe
#is converted to a csv file
#which will appear on the left hand side after refreshing
#when clicking on it, a window containing view of the data will open.
result.to_csv("distinct.csv")

#INSPECTING DUPLICATE
with_dup = """SELECT *
              FROM anime
              WHERE Name IN ('Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e',
                             'Hinamatsuri',
                              'Youkoso! Ecolo Shima')"""

result = pd.read_sql(with_dup,db)
result.to_csv("with_dup.csv")

query = """SELECT Name, Type, Source
           FROM anime
           WHERE Name IN ('Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e',
                             'Hinamatsuri',
                              'Youkoso! Ecolo Shima')"""
print(pd.read_sql(query,db)) 

clean = "DELETE FROM anime WHERE MAL_ID IN (48417,48418,39143)"
cursor.execute(clean)

print ("FINISH DATA CLEANING")

#query return the number of rows with unknown score
unknown = """SELECT COUNT(*) as score_unknown
             FROM anime
             WHERE Score = "Unknown" """

print(pd.read_sql(unknown, db))
       
#we inspect why the value is unknown
unknown_row = """SELECT *
                 FROM anime
                 WHERE Score = "Unknown"
                 """
unknown = pd.read_sql(unknown_row,db)
unknown.to_csv("unknown_row.csv")

#INSPECTING SOURCE OF UNKNOW SCORE

year = pd.read_csv("unknown_row.csv")
Premiered = year.loc[:,"Premiered"]

l=[]
for r in Premiered:
  if r != "Unknown":
    a = r.split()
    l.append(a[-1])

from collections import Counter
print(Counter(l))


#for anime with unknown score,
#the query count the number of anime with a given number
#of user who like it
fav = """SELECT Favorites, COUNT(*) AS with_fav
       FROM anime
       WHERE Score = "Unknown"
       GROUP BY Favorites
       ORDER BY with_fav DESC
       """
print(pd.read_sql(fav,db))

#the average number of favourite users per all anime
avg = """SELECT AVG(Favorites) as avg_fav
         FROM anime"""
print(pd.read_sql(avg,db))

#new releases or not yet in 2021, without available score
a2021 = """SELECT Name, Score, Favorites, Premiered
           FROM anime
           WHERE Premiered LIKE '%2021'
           ORDER BY Favorites DESC """

print(pd.read_sql(a2021,db))
result = pd.read_sql(a2021,db)
result.to_csv("a2021.csv")

"""
***3. DATA EXPLORATION***
"""


#TOP 10 BEST ANIME OF ALL TIME BEFORE 2021
#ordered by scores
best = """SELECT *
          FROM anime
          WHERE Score != "Unknown" AND Premiered NOT LIKE "%2021"
          ORDER BY Score DESC
          LIMIT 50
       """

print(pd.read_sql(best,db))
pd.read_sql(best,db).to_csv("top50.csv")

#ordered by favourites
pop = """SELECT Name, Score, Favorites
         FROM anime
         WHERE Score != "unknown"
         AND Premiered != "unknown"
         AND Premiered NOT LIKE '%2021'
         ORDER BY Favorites DESC
         LIMIT 10"""

print(pd.read_sql(pop,db))

#TOP 10 WORST ANIME OF ALL TIME BEFORE 2021
#ordered by score
worst = """SELECT Name, Score, Favorites
          FROM anime
          WHERE Score != "Unknown" AND Premiered NOT LIKE "%2021"
          ORDER BY Score
          LIMIT 10
        """

print(pd.read_sql(worst,db))

#ordered by favourite
hate = """SELECT Name, Score, Favorites
         FROM anime
         WHERE Score != "unknown"
         AND Premiered != "unknown"
         AND Premiered NOT LIKE '%2021'
         ORDER BY Favorites
         LIMIT 10"""

print(pd.read_sql(hate,db))


"""The outputs for the best anime given by ranking with attribute Favourites closely resemble that of score but perform poorly when choosing the worst animes. 

We will now take at quick looks at other attributes:

**3.1 Type of anime**

"""

#DISTRIBUTION OF ANIME TYPE
atype = """WITH numtype AS(
                          SELECT type,COUNT(*) as num_anime
                          FROM anime
                          GROUP BY type
                          ORDER BY num_anime DESC)
           SELECT *,
                  SUM(num_anime) OVER(
                                      ORDER BY num_anime DESC
                                      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
                                      ) AS cum_tot,
                  ROUND(((num_anime/17562)*100),2) AS percent
           FROM numtype
           """
print(pd.read_sql(atype,db))
print("------------------------------------")

#Is this also the case for the TOP 50 BEST ANIME?
best_type = """
            WITH 
               best AS(
                            SELECT *
                            FROM anime
                            WHERE Premiered NOT LIKE "%2021"
                            AND Score != "Unknown"
                            ORDER BY Score DESC
                            LIMIT 50),
               numtype AS(
                          SELECT type,COUNT(*) as num_anime
                          FROM best
                          GROUP BY type
                          ORDER BY num_anime DESC)
               SELECT *,
                      SUM(num_anime) OVER(
                                          ORDER BY num_anime DESC
                                          ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
                                          ) AS cum_tot,
                      ROUND(((num_anime/50)*100),2) AS percent
           FROM numtype
           """
print(pd.read_sql(best_type ,db))

"""
**3.2 Source of Content**
"""

#DISTRIBUTION OF ANIME TYPE
source = """WITH numsource AS(
                          SELECT source,COUNT(*) as num_anime
                          FROM anime
                          GROUP BY source
                          ORDER BY num_anime DESC)
           SELECT *,
                  SUM(num_anime) OVER(
                                      ORDER BY num_anime DESC
                                      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
                                      ) AS cum_tot,
                  ROUND(((num_anime/17562)*100),2) AS percent
           FROM numsource
           """
print(pd.read_sql(source,db))
print("------------------------------------")

#Is this also the case for the TOP 50 BEST ANIME?
best_source = """
            WITH 
               best AS(
                            SELECT *
                            FROM anime
                            WHERE Premiered NOT LIKE "%2021"
                            AND Score != "Unknown"
                            ORDER BY Score DESC
                            LIMIT 50),
               numsource AS(
                          SELECT source,COUNT(*) as num_anime
                          FROM best
                          GROUP BY source
                          ORDER BY num_anime DESC)
               SELECT *,
                      SUM(num_anime) OVER(
                                          ORDER BY num_anime DESC
                                          ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
                                          ) AS cum_tot,
                      ROUND(((num_anime/50)*100),2) AS percent
           FROM numsource
           """
print(pd.read_sql(best_source ,db))

"""**3.3 Production Studios**"""

#DISTRIBUTION OF ANIME TYPE
Studios = """WITH numStudios AS(
                          SELECT Studios,COUNT(*) as num_anime
                          FROM anime
                          GROUP BY Studios
                          ORDER BY num_anime DESC)
           SELECT *,
                  SUM(num_anime) OVER(
                                      ORDER BY num_anime DESC
                                      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
                                      ) AS cum_tot,
                  ROUND(((num_anime/17562)*100),2) AS percent
           FROM numStudios
           """
print(pd.read_sql(Studios,db))
print("------------------------------------")

#Is this also the case for the TOP 50 BEST ANIME?
best_Studios = """
            WITH 
               best AS(
                            SELECT *
                            FROM anime
                            WHERE Premiered NOT LIKE "%2021"
                            AND Score != "Unknown"
                            ORDER BY Score DESC
                            LIMIT 50),
               numStudios AS(
                          SELECT Studios,COUNT(*) as num_anime
                          FROM best
                          GROUP BY Studios
                          ORDER BY num_anime DESC)
               SELECT *,
                      SUM(num_anime) OVER(
                                          ORDER BY num_anime DESC
                                          ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
                                          ) AS cum_tot,
                      ROUND(((num_anime/50)*100),2) AS percent
           FROM numStudios
           """
print(pd.read_sql(best_Studios ,db))

"""**3.4 Age Rating**"""


#DISTRIBUTION OF ANIME TYPE
Rating = """WITH numRating AS(
                          SELECT Rating,COUNT(*) as num_anime
                          FROM anime
                          GROUP BY Rating
                          ORDER BY num_anime DESC)
           SELECT *,
                  SUM(num_anime) OVER(
                                      ORDER BY num_anime DESC
                                      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
                                      ) AS cum_tot,
                  ROUND(((num_anime/17562)*100),2) AS percent
           FROM numRating
           """
print(pd.read_sql(Rating,db))
print("------------------------------------")

#Is this also the case for the TOP 50 BEST ANIME?
best_R = """
            WITH 
               best AS(
                            SELECT *
                            FROM anime
                            WHERE Premiered NOT LIKE "%2021"
                            AND Score != "Unknown"
                            ORDER BY Score DESC
                            LIMIT 50),
               numRating AS(
                          SELECT Rating,COUNT(*) as num_anime
                          FROM best
                          GROUP BY Rating
                          ORDER BY num_anime DESC)
               SELECT *,
                      SUM(num_anime) OVER(
                                          ORDER BY num_anime DESC
                                          ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
                                          ) AS cum_tot,
                      ROUND(((num_anime/50)*100),2) AS percent
           FROM numRating
           """
print(pd.read_sql(best_R ,db))

"""**3.5 Anime Genres of the TOP 50**

Anime Genres is saved as Text Datatype in our database and is presented as a list of genres separated by a comma.

Since MySQL doesn't support the command UNNEST, we must once a gain use the help of Python to unpack our lists, and count the number of occurence of each genre. 

Note that the sum of genre occurences will not be equal to the number of anime we have, since each anime consists of several genres, so the data is repetitive.
"""

def Count(colname,tablename):
  input = tablename.loc[:,colname]
  output = []
  for row in input:
    out  = row.split(", ")
    for word in out:
      output.append(word)
  counter = Counter(output)
  i = 0
  for val,count in counter.most_common():
    print(val,count)
    i += 1
  print("The number of genres is:{}".format(i))

print("ANIME GENRES RANKED BY MOST COMMON:")
Count("Genres",anime)
print("-------------------------------------")

print("MOST COMMON GENRES OF TOP 50 ANIME:")
top = pd.read_csv("top50.csv")
Count("Genres",top)

"""### V. MAKING RECOMMENDATION - Relevant queries

***1.ANIMES TO LOOK FORWARD TO IN 2021***

The query will return all names of anime that will premiere in 2021, ranked by popularity among user and their synopsis

"""

#since the table synopsis contain less observations than anime, we will check for the anime missing

cursor = db.cursor()

to2021 = """SELECT a.MAL_ID,a.Name, a.Premiered, s.sypnopsis
            FROM anime AS a LEFT JOIN synopsis AS s
              ON a.MAL_ID = s.MAL_ID AND a.Name = s.Name
            WHERE a.Premiered LIKE '%2021'
            ORDER BY a.Popularity"""

print(pd.read_sql(to2021,db))
pd.read_sql(to2021,db).to_csv("to2021.csv")

"""***2. ANIME WITH SEVERAL SEASONS***

Usually for TV and OVA, there are multiple seasons instead of 1 because many of which are based on an ongoing Manga. To confirm this, we generate a query which return the name of TV or OVA anime series in order of alphabetical and their sources. 

Given that it is true, we will now look at a few CLASSIC animes with multiple season. With some of these famous anime, they not only come as TV show, but also movies and others. These anime are some of the names we got from the Top 50 best anime:


*   Fullmetal Alchemist
*   Steins:Gate
*   Hunter x Hunter
*   Gintaima
*   Shingeki no Kyojin
*   Code Geass
*   Haikyuu

"""

season = """SELECT Name, Source
            FROM anime
            WHERE Type IN ('TV','OVA')
            ORDER BY Name
            LIMIT 20"""

print(pd.read_sql(season,db))
print("-------------------------------")

#Lets inspect Shingeki no Kyojin
 
AOT = """WITH AOT AS(SELECT *
                      FROM anime
                      WHERE Name LIKE '%Shingeki no Kyojin%')
         SELECT COUNT(DISTINCT(Name)) as num_release,
                COUNT(DISTINCT(Type)) as num_type,
                COUNT(DISTINCT(Studios)) as num_studio,
                AVG(Score) as Avg_Score,
                MIN(Score) as lowest,
                MAX(Score) as highest
         FROM AOT"""

rating = """SELECT DISTINCT(Rating), COUNT(*) AS count
            FROM Anime
            WHERE Name LIKE '%Shingeki no Kyojin%'
            GROUP BY Rating"""

genre = """SELECT Genres
           FROM Anime
           WHERE Name Like '%Shingeki no Kyojin%'
           AND Score = 9.17"""

print(pd.read_sql(AOT,db))
print(pd.read_sql(rating,db))
print(pd.read_sql(genre,db))
#pd.read_sql(AOT,db).to_csv("AOT.csv")

"""Now, we shall make a recommendation for someone who enjoys Shingeki no Kyojin. We will write a query which return a list of anime names,scores, and sypnosis. 
Given that these animes have the same rating, share at least two similar genres with grades greater or equal to the average score 7.7. 
"""


cursor = db.cursor()

recommend = """WITH joined AS(
                              SELECT a.Name, a.Score, s.sypnopsis
                              FROM anime AS a LEFT JOIN synopsis AS s
                              ON a.MAL_ID = s.MAL_ID AND a.Name = s.Name
                              WHERE a.Name NOT LIKE '%Shingeki no Kyojin%'
                                    AND a.Rating LIKE "%violence & profanity%" 
                                    AND a.Score > 7.7 
                                    AND a.Genres LIKE '%Super Power%'
                                    AND a.Genres LIKE '%Drama%'
                              ORDER BY a.Score DESC)
               SELECT *
               FROM joined"""

print(pd.read_sql(recommend,db))
#pd.read_sql(recommend,db).to_csv("AOT_rec.csv")

"""***3.ANIME MOVIE RECOMMENDATION***

For people living a busy life style, finishing several seasons or just one might be impossible but fear not.

Most people learned about anime through movies coming from studio Ghibli and so we will try to make recommendation 

based on 10 of their best works according to users, making it an easy and gentle introduction to anime. 

"""


ghibli = """
            SELECT *
            FROM anime as a
            WHERE a.Studios = 'Studio Ghibli'
            AND a.type = 'Movie'
            ORDER BY a.Score DESC
            LIMIT 10
                          """

info = """WITH ghibli AS(SELECT *
                        FROM anime
                        WHERE Studios = "Studio Ghibli")
         SELECT COUNT(DISTINCT(Name)) as num_release,
                COUNT(DISTINCT(Source)) as num_source,
                COUNT(DISTINCT(Rating)) as num_rating,
                AVG(Score) as Avg_Score,
                MIN(Score) as lowest,
                MAX(Score) as highest
         FROM ghibli"""

rating = """SELECT DISTINCT(Rating), COUNT(*) AS count
            FROM Anime
            WHERE Studios LIKE 'Studio Ghibli'
            GROUP BY Rating
            """

genre = """SELECT Genres
           FROM Anime
           WHERE Studios Like 'Studio Ghibli'
           AND Score = 8.83"""

print(pd.read_sql(ghibli,db))
pd.read_sql(ghibli,db).to_csv("ghibli.csv")
print(pd.read_sql(info,db))
print(pd.read_sql(rating,db))
print(pd.read_sql(genre,db))

"""Now we shall make a recommendation for anime movies (other Ghibli movies included) that share some characteristics with Ghibli movies in general and Spirited Away.

Write a query which results in a list with anime names, their scores and the sypnopsis. Given that they have the rating for all ages, share at least 1 similar genres and has score greater or equal to 6.8
"""


movie = """WITH rec AS(
                        SELECT a.Name, a.Score, s.sypnopsis
                        FROM anime AS a LEFT JOIN synopsis AS s
                          ON a.MAL_ID = s.MAL_ID AND a.Name = s. Name
                        WHERE a.Type = "Movie"
                        AND a.Rating LIKE "%All Ages%"
                        AND a.Genres LIKE "%Adventure%"
                        AND a.Genres LIKE "%Drama%"
                        AND a.Score >= 6.8
                        ORDER BY a.Score DESC)
            SELECT *
            FROM rec """

print(pd.read_sql(movie,db))
#pd.read_sql(movie,db).to_csv("Ghibli_rec.csv")
