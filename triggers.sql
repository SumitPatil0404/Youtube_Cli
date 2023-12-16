DELIMITER //

CREATE TRIGGER after_insert_views
AFTER INSERT ON views
FOR EACH ROW
BEGIN
  -- Increment the view count in the Videos table when a new view is inserted
  UPDATE videos SET ViewsCount = ViewsCount + 1 WHERE id = NEW.videos_id;
END //

DELIMITER ;


DELIMITER //

CREATE TRIGGER after_insert_liked_videos
AFTER INSERT ON liked_videos
FOR EACH ROW
BEGIN
  -- Increment the liked count in the Videos table when a new like is inserted
  UPDATE videos SET LikesCount = LikesCount + 1 WHERE id = NEW.videos_id;
END //

DELIMITER ;


DELIMITER //

CREATE TRIGGER after_insert_dislike_videos
AFTER INSERT ON dislike_videos
FOR EACH ROW
BEGIN
  -- Increment the dislike count in the Videos table when a new dislike is inserted
  UPDATE videos SET DislikesCount = DislikesCount + 1 WHERE id = NEW.videos_id;
END //

DELIMITER ;



