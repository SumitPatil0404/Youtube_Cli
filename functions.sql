DELIMITER //
get_total_dislikes
CREATE FUNCTION (video_id_param INT)
RETURNS INT
BEGIN
  DECLARE total_dislikes INT;
  SELECT COUNT(*) INTO total_dislikes FROM dislike_videos WHERE videos_id = video_id_param;
  RETURN total_dislikes;
END //

DELIMITER ;


DELIMITER //

CREATE FUNCTION get_total_likes(video_id_param INT)
RETURNS INT
BEGIN
  DECLARE total_likes INT;
  SELECT COUNT(*) INTO total_likes FROM liked_videos WHERE videos_id = video_id_param;
  RETURN total_likes;
END //

DELIMITER ;


DELIMITER //

CREATE FUNCTION get_total_views(video_id_param INT)
RETURNS INT
BEGIN
  DECLARE total_views INT;
  SELECT COUNT(*) INTO total_views FROM views WHERE videos_id = video_id_param;
  RETURN total_views;
END //

DELIMITER ;
