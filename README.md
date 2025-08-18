# Spotify Data Analytics Project

This project analyzes a random user’s Spotify listening history to uncover patterns in listening habits, platform usage, skipped tracks, and top artists/albums. The project includes **data cleaning, exploratory data analysis (EDA), visualizations in Python, and Tableau dashboards**.

---

## 📂 Project Structure

### **Data Files**

* **`data/spotify_data_dictionary Description.csv`**
  Dictionary file that explains each column in the dataset.

* **`data/spotify_history.csv`**
  Raw dataset containing the user’s Spotify listening history.

* **`data/clean data/clean_Spotify_data.xlsx`**
  Cleaned version of `spotify_history.csv` after preprocessing in Jupyter Notebook.

---

### **Jupyter Notebook**

* **`jupyter_notebook/Spotify_history.ipynb`**
  Python notebook that includes:

  * Importing libraries and loading the dataset
  * Data cleaning: handling missing values, converting timestamps, removing short plays (<15 seconds), etc.
  * Feature engineering: extracting year, month, day, hour
  * Converting `ms_played` to minutes/seconds
  * Exploratory Data Analysis (EDA):

    * Top artists and tracks by total listening time
    * Listening habits by hour
    * Platform usage (Android, iOS, Web, etc.)
    * Skipping behavior (songs/artists skipped most)
    * Album listening trends
  * Data visualizations in Python:

    * **Bar chart:** Top 10 artists
    * **Heatmap:** Listening by day of week & hour
    * **Pie chart:** Platform usage
    * **Bar chart:** Most skipped songs
    * **Line graph:** Album listening trends
  * Exporting cleaned data

---

### **Tableau Visualizations**

* **`visuals/Tableau_visual/Spotify_History_Project.twb`**
  Tableau workbook containing:

  * Heatmap of listening trends
  * Treemap of top artists & songs

* **[Tableau Public Link](https://public.tableau.com/app/profile/ameer.sulyans2376/viz/Spotify_History_Project/Dashboard)**
  Published interactive dashboard.

* ![image alt]([image_url](https://github.com/Ameer-Sulyans/Spotify-Listening-Analysis/blob/a9981588a490202cee76f965b6f46bed00476b89/visuals/Tableau_visual/Tableau_Spotify_data_visualization.png))
  Static image of the Tableau project (partial treemap view of top artists & songs).

📌 **Key Tableau Insight**: The most played song was *Ode to the Mets* by **The Strokes**.

---

### **Python Visualizations (PNG)**

All visuals generated in Jupyter Notebook, with key insights:

1.  ![image alt]([image_url](https://github.com/Ameer-Sulyans/Spotify-Listening-Analysis/blob/a9981588a490202cee76f965b6f46bed00476b89/visuals/python_visuals/Listening_Time_by_Hour_Heatmap.png))
   
   * 🔑 *Insight*: User listens most around **6:00 PM**, with a peak of **1,378,579 seconds** played.

2. ![image alt]([image_url](https://github.com/Ameer-Sulyans/Spotify-Listening-Analysis/blob/a9981588a490202cee76f965b6f46bed00476b89/visuals/python_visuals/Most_skip_artist.png))

   * 🔑 *Insight*: **The Beatles** were the most skipped artist.

3. ![image alt]([image_url](https://github.com/Ameer-Sulyans/Spotify-Listening-Analysis/blob/a9981588a490202cee76f965b6f46bed00476b89/visuals/python_visuals/Platform_Usage.png))

   * 🔑 *Insight*: **Android** was used significantly more than Windows, Web Player, iOS, or Cast to Device.

4.  ![image alt]([image_url](https://github.com/Ameer-Sulyans/Spotify-Listening-Analysis/blob/a9981588a490202cee76f965b6f46bed00476b89/visuals/python_visuals/Top_10_Albums_by_listening_time.png))

   * 🔑 *Insight*: *The New Abnormal* was the most listened album, followed by albums from **The Beatles**.

5.  ![image alt]([image_url](https://github.com/Ameer-Sulyans/Spotify-Listening-Analysis/blob/a9981588a490202cee76f965b6f46bed00476b89/visuals/python_visuals/Top_Artists.png))

   * 🔑 *Insight*: **The Beatles** were the top artist, followed by **The Killers**.

---

## 🚀 Key Insights

* The user’s peak listening time was **6:00 PM**.
* **Android** dominated platform usage.
* **The Beatles** were both the **most listened** and **most skipped** artist.
* **The New Abnormal** was the top album.
* Tableau confirmed *Ode to the Mets* by **The Strokes** as the most played track.

---

## 🛠️ Tools & Technologies

* **Python (Pandas, Matplotlib, Seaborn)** – Data cleaning, analysis, and visualizations
* **Jupyter Notebook** – Analysis workflow
* **Excel** – Cleaned data export
* **Tableau** – Interactive dashboards
