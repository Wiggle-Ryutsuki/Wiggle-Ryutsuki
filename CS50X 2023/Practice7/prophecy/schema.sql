CREATE TABLE students(
    id INTEGER NOT NULL,
    name TEXT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE houses(
    id INTEGER NOT NULL,
    house TEXT NOT NULL,
    head TEXT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE assign(
    student_id INTEGER NOT NULL,
    house_id INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (house_id) REFERENCES houses(id)
);