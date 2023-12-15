.read data.sql


CREATE TABLE bluedog AS
    select color, pet from students where color='blue' and pet='dog';

CREATE TABLE bluedog_songs AS
    select color, pet , song from students where color='blue' and pet='dog';

CREATE TABLE matchmaker AS
  select a.pet, a.song, a.color, b.color
    from students as a, students AS b
    where a.pet = b.pet and a.song = b.song and a.time < b.time;

CREATE TABLE sevens AS
    select s.seven
        from students as s, numbers as num
        where s.time = num.time and s.number = 7 and num.'7' = 'True';

CREATE TABLE favpets AS
    select pet, count(pet) as favpet
        from students group by pet order by favpet desc limit 10;

CREATE TABLE dog AS
    select pet, count(pet)
        from students where pet='dog';

CREATE TABLE bluedog_agg AS
    select song, count(pet) as favpet
        from bluedog_songs group by song order by favpet desc;

CREATE TABLE instructor_obedience AS
    select seven, instructor, count(*)
        from students
        where seven='7' group by instructor;
