create table Languages (
  id integer primary KEY,
  language varchar(15),
  answer varchar(100),
  answered bool,
  guide varchar(500)
  );

alter table Languages
  add column rating;

insert into Languages VALUES
  (1, "Python", "google", 0, "A folder named Python was created. Go there and fight with program.py!", 6),
  (2, "Go", "200 OK", 0, "A folder named Go was created. Go there and try to make Google Go run.", 4),
  (3, "Java", "object oriented programming", 0, "A folder named Java was created. Can you handle the class?", 8),
  (4, "Haskell", "Lambda", 0, "Something pure has landed. Go to Haskell folder and see it!", 7),
  (5, "C#", "NDI=", 0, "Do you see sharp? Go to the C# folder and check out.", 2),
  (6, "Ruby", "https://www.ruby-lang.org/bg/", 0, "Ruby, ruby, rubyyy, aaahaaaahaa! (music). Go to Ruby folder!", 9),
  (7, "C++", "header files", 0, "Here be dragons! It's C++ time. Go to the C++ folder.", 7),
  (8, "JavaScript", "Douglas Crockford", 0, "NodeJS time. Go to JavaScript folder and Node your way!", 3)

update Languages
  set answered = 1
  where id < 3;

select * from Languages
  where answer like "200 OK" or answer like "Lambda";