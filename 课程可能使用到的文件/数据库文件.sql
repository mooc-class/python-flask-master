CREATE DATABASE `movie_cat` DEFAULT CHARACTER SET = `utf8mb4`;


CREATE TABLE `user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `nickname` varchar(30) NOT NULL DEFAULT '' COMMENT '昵称',
  `login_name` varchar(20) NOT NULL DEFAULT '' COMMENT '登录用户名',
  `login_pwd` varchar(32) NOT NULL DEFAULT '' COMMENT '登录用户密码',
  `login_salt` varchar(32) NOT NULL DEFAULT '' COMMENT '登录密码随机字符串',
  `status` tinyint(3) NOT NULL DEFAULT '1' COMMENT '状态 0：无效 1：有效',
  `updated_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_login_name` (`login_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户表';





CREATE TABLE `movie` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL DEFAULT '' COMMENT '电影名称',
  `classify` varchar(100) NOT NULL DEFAULT '' COMMENT '类别',
  `actor` varchar(500) NOT NULL DEFAULT '' COMMENT '主演',
  `cover_pic` varchar(300) NOT NULL DEFAULT '' COMMENT '封面图',
  `pics` varchar(1000) NOT NULL DEFAULT '' COMMENT '图片地址json',
  `url` varchar(300) NOT NULL DEFAULT '' COMMENT '电影详情地址',
  `desc` text NOT NULL COMMENT '电影描述',
  `magnet_url` varchar(5000) NOT NULL DEFAULT '' COMMENT '磁力下载地址',
  `hash` varchar(32) NOT NULL DEFAULT '' COMMENT '唯一值',
  `pub_date` datetime NOT NULL COMMENT '来源网址发布日期',
  `source` varchar(20) NOT NULL DEFAULT '' COMMENT '来源',
  `view_counter` int(11) NOT NULL DEFAULT '0' COMMENT '阅读数',
  `updated_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间',
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_hash` (`hash`),
  KEY `idx_pu_date` (`pub_date`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 COMMENT='影视数据表';

