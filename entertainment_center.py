import fresh_tomatoes
import media
toy_story1=media.Movie("Toy Story", r"A boy with his toys"\
, "http://m.midiario.com/sites/default/files/styles/md_uhora_image_node_slideshow/public/ava.jpg?itok=Xi_ix-L9",\
"https://www.youtube.com/watch?v=KYz2wyBy3kc")
toy_story2=media.Movie("Toy Story", r"A boy with his toys",\
"http://m.midiario.com/sites/default/files/styles/md_uhora_image_node_slideshow/public/ava.jpg?itok=Xi_ix-L9",\
"https://www.youtube.com/watch?v=KYz2wyBy3kc")
toy_story3=media.Movie("Toy Story",\
r"A boy with his toys", "http://m.midiario.com/sites/default/files/styles/md_uhora_image_node_slideshow/public/ava.jpg?itok=Xi_ix-L9", \
"https://www.youtube.com/watch?v=KYz2wyBy3kc")
toy_story5=media.Movie("Toy Story",\
"A boy with his toys",\
"http://m.midiario.com/sites/default/files/styles/md_uhora_image_node_slideshow/public/ava.jpg?itok=Xi_ix-L9",\
"https://www.youtube.com/watch?v=KYz2wyBy3kc")
movies=[toy_story5, toy_story1, toy_story2, toy_story3]
fresh_tomatoes.open_movies_page(movies)