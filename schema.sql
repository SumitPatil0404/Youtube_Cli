Create Table users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    Name Varchar(50),
    Age INT,
    Gender Varchar(50)
);


Create Table videos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    Title Varchar(50),
    Description Varchar(1000),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

Create Table comments(
    id INT PRIMARY KEY AUTO_INCREMENT,
    text Varchar(500),
    user_id INT,
    videos_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (videos_id) REFERENCES videos(id) ON DELETE CASCADE
);

Create Table dislike_videos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    videos_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (videos_id) REFERENCES videos(id) ON DELETE CASCADE
);

Create Table liked_videos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    videos_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (videos_id) REFERENCES videos(id) ON DELETE CASCADE
);

Create Table login(
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    Email_ID Varchar(50),
    Password Varchar(50),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

Create Table payment_analytics(
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    Amount INT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

Create Table subscriptions(
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    subscriber_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (subscriber_id) REFERENCES users(id) ON DELETE CASCADE
);
Create Table views(
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    videos_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (videos_id) REFERENCES videos(id) ON DELETE CASCADE
);


Create Table history(
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    videos_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (videos_id) REFERENCES videos(id) ON DELETE CASCADE
);