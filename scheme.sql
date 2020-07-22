/*GUIA*/

CREATE TABLE users (
    userName TEXT NOT NULL PRIMARY KEY,
    passWord TEXT NOT NULL,
    uID INT AUTO_INCREMENT
);

CREATE TABLE posts (
    tweetTitle TEXT NOT NULL,
    tweetContent TEXT NOT NULL
);