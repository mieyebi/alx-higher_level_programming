-- A script that lists all shows contained in hbtn_0d_tvshows without genre linked
SELECT tv_show.title, tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
