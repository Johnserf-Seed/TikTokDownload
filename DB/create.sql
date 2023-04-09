--
-- SQLiteStudio v3.4.3 生成的文件，周一 2月 13 23:47:22 2023
--
-- 所用的文本编码：UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- 表：aweme
CREATE TABLE IF NOT EXISTS aweme (
    id                  INTEGER     PRIMARY KEY AUTOINCREMENT,
    aweme_collect_count TEXT        NOT NULL,
    aweme_comment_count TEXT        NOT NULL,
    aweme_creat_time    TEXT (10)   NOT NULL,
    aweme_desc          TEXT        NOT NULL,
    aweme_digg_count    TEXT        NOT NULL,
    aweme_nickname      TEXT        NOT NULL,
    aweme_music_uri     TEXT (19)   NOT NULL,
    aweme_play_count    TEXT        NOT NULL,
    aweme_sec_uid       TEXT (19)   NOT NULL,
    aweme_share_count   TEXT        NOT NULL,
    aweme_type          INTEGER (3) NOT NULL,
    aweme_unique_id     TEXT        NOT NULL,
    aweme_user_age      INTEGER (3) NOT NULL
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
