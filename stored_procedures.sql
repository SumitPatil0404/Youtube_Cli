



-- Stored Procedure for User Signup
DELIMITER //

CREATE PROCEDURE users(IN p_Name VARCHAR(255), IN p_Gender VARCHAR(10), IN p_Age INT)
BEGIN
  INSERT INTO Users (Name, Gender, Age) VALUES (p_Name, p_Gender, p_Age);
  SELECT LAST_INSERT_ID() AS user_id;
END //

DELIMITER ;


-- Stored Procedure for User Login
DELIMITER //

CREATE PROCEDURE login1(IN p_Email_ID VARCHAR(255), IN p_Password VARCHAR(255))
BEGIN
  SELECT user_id FROM login WHERE Email_ID = p_Email_ID AND Password = p_Password;
END //

DELIMITER ;



-- Stored Procedure for User Signup



-- Stored Procedure for Login
DELIMITER //

CREATE PROCEDURE login(IN p_Email_ID VARCHAR(255), IN p_Password VARCHAR(255), IN p_user_id INT)
BEGIN
  INSERT INTO Login(Email_ID, Password, user_id) VALUES (p_Email_ID, p_Password, p_user_id);
END //

DELIMITER ;


-- Stored Procedure for Video Upload
DELIMITER //

CREATE PROCEDURE video_upload(IN p_Title VARCHAR(255), IN p_Description TEXT, IN p_user_id INT)
BEGIN
  INSERT INTO Videos(Title, Description, user_id) VALUES (p_Title, p_Description, p_user_id);
END //

DELIMITER ;



-- Stored Procedure for Retrieving All Videos
DELIMITER //

CREATE PROCEDURE videos_to_watch()
BEGIN
  SELECT * FROM videos;
END //

DELIMITER ;


-- Stored Procedure for Retrieving All Users
DELIMITER //

CREATE PROCEDURE allusers()
BEGIN
  SELECT * FROM users;
END //

DELIMITER ;



-- Stored Procedure for Counting Views
DELIMITER //

CREATE PROCEDURE views(IN video_id_param INT)
BEGIN
  SELECT COUNT(*) AS Count FROM views
  WHERE videos_id = video_id_param;
END //

DELIMITER ;


-- Stored Procedure for Counting Likes
DELIMITER //

CREATE PROCEDURE liked_videos(IN video_id_param INT)
BEGIN
  SELECT COUNT(*) AS Count FROM liked_videos
  WHERE videos_id = video_id_param;
END //

DELIMITER ;



-- Stored Procedure for Counting Dislikes
DELIMITER //

CREATE PROCEDURE dislike_videos(IN video_id_param INT)
BEGIN
  SELECT COUNT(*) AS Count FROM dislike_videos
  WHERE videos_id = video_id_param;
END //

DELIMITER ;



-- Stored Procedure for Counting Subscribers
DELIMITER //

CREATE PROCEDURE subscriber(IN video_id_param INT)
BEGIN
  SELECT COUNT(*) AS Count FROM subscriptions
  WHERE user_id IN (SELECT user_id FROM videos WHERE id = video_id_param);
END //

DELIMITER ;



-- Stored Procedure for Adding Comments
DELIMITER //

CREATE PROCEDURE comment(IN text_param VARCHAR(255), IN user_id_param INT, IN video_id_param INT)
BEGIN
  INSERT INTO comments (text, user_id, videos_id)
  VALUES (text_param, user_id_param, video_id_param);
END //

DELIMITER ;



-- Stored Procedure for Checking Subscriptions
DELIMITER //

CREATE PROCEDURE check_subscription(IN subscriber_id_param INT, IN video_id_param INT)
BEGIN
  SELECT user_id
  FROM subscriptions
  WHERE subscriber_id = subscriber_id_param
    AND user_id IN (SELECT user_id FROM videos WHERE id = video_id_param);
END //

DELIMITER ;


-- Stored Procedure for Subscribing to a Channel
DELIMITER //

CREATE PROCEDURE subscribing_channel(IN subscriber_id_param INT, IN video_id_param INT)
BEGIN
  DECLARE user_id_value INT;

  -- Get the user_id from the videos table based on the provided video_id_param
  SELECT user_id INTO user_id_value
  FROM videos
  WHERE id = video_id_param;

  -- Insert into subscriptions using the retrieved user_id
  INSERT INTO subscriptions (subscriber_id, user_id)
  VALUES (subscriber_id_param, user_id_value);
END //

DELIMITER ;



-- Stored Procedure for Fetching Comments
DELIMITER //

CREATE PROCEDURE comments(IN video_id_param INT)
BEGIN
  SELECT Text, Name
  FROM users, comments
  WHERE users.id = user_id AND videos_id = video_id_param;
END //

DELIMITER ;




-- Stored Procedure for Fetching User Videos
DELIMITER //

CREATE PROCEDURE your_videos(IN user_id_param INT)
BEGIN
  SELECT *
  FROM videos
  WHERE user_id = user_id_param;
END //

DELIMITER ;


-- Stored Procedure for Fetching History Videos
DELIMITER //

CREATE PROCEDURE your_history_videos(IN user_id_param INT)
BEGIN
  SELECT *
  FROM videos
  WHERE id IN (SELECT videos_id FROM history WHERE user_id = user_id_param);
END //

DELIMITER ;




-- Stored Procedure for Fetching Liked Videos
DELIMITER //

CREATE PROCEDURE your_liked_videos(IN user_id_param INT)
BEGIN
  SELECT *
  FROM videos
  WHERE id IN (SELECT videos_id FROM liked_videos WHERE user_id = user_id_param);
END //

DELIMITER ;


-- Stored Procedure for Fetching Subscriptions
DELIMITER //

CREATE PROCEDURE your_subscriptions(IN user_id_param INT)
BEGIN
  SELECT id, Name
  FROM users
  WHERE id IN (SELECT user_id FROM subscriptions WHERE subscriber_id = user_id_param);
END //

DELIMITER ;


-- Stored Procedure for Fetching Subscribers
DELIMITER //

CREATE PROCEDURE your_subscribers(IN user_id_param INT)
BEGIN
  SELECT id, Name
  FROM users
  WHERE id IN (SELECT subscriber_id FROM subscriptions WHERE user_id = user_id_param);
END //

DELIMITER ;


-- Stored Procedure for Payment Analytics
DELIMITER //

CREATE PROCEDURE payment_analytics(IN user_id_param INT)
BEGIN
  SELECT v.id AS id, v.Title AS Title, COUNT(*) AS views_count
  FROM videos v
  JOIN views view ON v.id = view.videos_id
  WHERE v.user_id = user_id_param
  GROUP BY v.id;
END //

DELIMITER ;




-- Stored Procedure to Check History
DELIMITER //


CREATE PROCEDURE check_update_hist(IN user_id_param INT, IN videos_id_param INT)
BEGIN
  SELECT * FROM history WHERE user_id = user_id_param AND videos_id = videos_id_param;
END //

DELIMITER ;



-- Stored Procedure to Update History
DELIMITER //

CREATE PROCEDURE check_update_history(IN user_id_param INT, IN videos_id_param INT)
BEGIN
  DECLARE record_count INT;

  SELECT COUNT(*) INTO record_count FROM history WHERE user_id = user_id_param AND videos_id = videos_id_param;

  IF record_count = 0 THEN
    INSERT INTO history (user_id, videos_id) VALUES (user_id_param, videos_id_param);
  END IF;
END //

DELIMITER ;


-- Stored Procedure to Check Views
DELIMITER //

CREATE PROCEDURE CheckViews(IN user_id_param INT, IN videos_id_param INT)
BEGIN
  SELECT * FROM views WHERE user_id = user_id_param AND videos_id = videos_id_param;
END //

DELIMITER ;

-- Stored Procedure to Update Views
DELIMITER //

CREATE PROCEDURE check_update_views(IN user_id_param INT, IN videos_id_param INT)
BEGIN
  DECLARE record_count INT;

  SELECT COUNT(*) INTO record_count FROM views WHERE user_id = user_id_param AND videos_id = videos_id_param;

  IF record_count = 0 THEN
    INSERT INTO views (user_id, videos_id) VALUES (user_id_param, videos_id_param);
  END IF;
END //

DELIMITER ;


-- Stored Procedure to Check Liked Videos
DELIMITER //

CREATE PROCEDURE CheckLikedVideos(IN user_id_param INT, IN videos_id_param INT)
BEGIN
  SELECT * FROM liked_videos WHERE user_id = user_id_param AND videos_id = videos_id_param;
END //

DELIMITER ;


-- Stored Procedure to Update Liked Videos
DELIMITER //

CREATE PROCEDURE check_update_liked_videos(IN user_id_param INT, IN videos_id_param INT)
BEGIN
  DECLARE record_count INT;

  SELECT COUNT(*) INTO record_count FROM liked_videos WHERE user_id = user_id_param AND videos_id = videos_id_param;

  IF record_count = 0 THEN
    INSERT INTO liked_videos (user_id, videos_id) VALUES (user_id_param, videos_id_param);
  END IF;
END //

DELIMITER ;


-- Stored Procedure to Check Dislike Videos
DELIMITER //

CREATE PROCEDURE CheckDislikeVideos(IN user_id_param INT, IN videos_id_param INT)
BEGIN
  SELECT * FROM dislike_videos WHERE user_id = user_id_param AND videos_id = videos_id_param;
END //

DELIMITER ;



-- Stored Procedure to Update Dislike Videos
DELIMITER //

CREATE PROCEDURE check_update_dislike_videos(IN user_id_param INT, IN videos_id_param INT)
BEGIN
  DECLARE record_count INT;

  SELECT COUNT(*) INTO record_count FROM dislike_videos WHERE user_id = user_id_param AND videos_id = videos_id_param;

  IF record_count = 0 THEN
    INSERT INTO dislike_videos (user_id, videos_id) VALUES (user_id_param, videos_id_param);
  END IF;
END //

DELIMITER ;








-- Stored Procedure to Delete a User Account
DELIMITER //

CREATE PROCEDURE Delete_Account(IN user_id_param INT)
BEGIN
  DELETE FROM users WHERE id = user_id_param;
END //

DELIMITER ;



-- Stored Procedure to Delete a Video
DELIMITER //

CREATE PROCEDURE Delete_Videos(IN video_id_param INT)
BEGIN
  DELETE FROM videos WHERE id = video_id_param;
END //

DELIMITER ;
