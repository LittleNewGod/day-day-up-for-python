/*
 Navicat Premium Data Transfer

 Source Server         : mysqltest
 Source Server Type    : MySQL
 Source Server Version : 50722
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 50722
 File Encoding         : 65001

 Date: 21/02/2019 21:28:07
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for app01_detail
-- ----------------------------
DROP TABLE IF EXISTS `app01_detail`;
CREATE TABLE `app01_detail`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Asin_detail` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Total_reviews_detail` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Total_score_detail` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Asin_tag` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Reviewer` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Stars` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Title` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Review_content` varchar(5000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Date_str` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of app01_detail
-- ----------------------------
INSERT INTO `app01_detail` VALUES (1, 'B07GRSY8RG', '10', '4', 'Color: Black', 'deefree', '5', 'Extremely cool', 'Great costume', '2019/1/7');
INSERT INTO `app01_detail` VALUES (2, 'B07GRSY8RG', '10', '4', 'Color: Black', 'Amazon Customer', '4', 'Fire made flesh', 'I luv the material n the look', '2018/12/28');
INSERT INTO `app01_detail` VALUES (3, 'B07GRSY8RG', '10', '4', 'Color: Black', 'Daniel F.', '5', '8 yr old daughter loves the wings and tail', 'She didn\'t use the mask， but instead used a makeup tutorial online to create a mermaid/dragon look.', '2018/12/27');
INSERT INTO `app01_detail` VALUES (4, 'B07GRSY8RG', '10', '4', 'Color: Black', 'Crystal', '3', 'Beware!', 'What i was recieved was damaged and peeling! i paid too much for this quality. I ordered a replacement but we\'ll see what i get. UPDATE I put in for a replacement and received a new one within a few days and still in time for xmas the quality was greatly improved!', '2018/12/18');
INSERT INTO `app01_detail` VALUES (5, 'B07GRSY8RG', '10', '4', 'Color: Black', 'Stella B', '1', 'Child size', 'Child size. Does not fit adults.', '2018/12/1');
INSERT INTO `app01_detail` VALUES (6, 'B07GRSY8RG', '10', '4', 'Color: Black', 'monica woo', '4', 'Meh', 'This was a big hit for me and my sons， khaleesi and drogon costume. The costume was fierce. However， the tail wouldnt stay on and the metal piece ended up breaking off and we had to use nail glue to put the piece back on. And a bit over priced.', '2018/12/1');
INSERT INTO `app01_detail` VALUES (7, 'B07GRSY8RG', '10', '4', 'Color: Black', 'Amazon Customer', '5', 'Five Stars', 'So much better than we expected! The detail and construction is above average.', '2018/11/15');
INSERT INTO `app01_detail` VALUES (8, 'B07GRSY8RG', '10', '4', 'Color: Black', 'Lynsie Rukgaber', '5', 'Definitely need to wear something to hook the tail too.', 'My 8 year olf loved this costume and the wings and mask fit perfect. We didn\'t end up using the tail for trick or treating because it kept falling off.', '2018/11/2');
INSERT INTO `app01_detail` VALUES (9, 'B07GRSY8RG', '10', '4', 'Color: Black', 'ragedyanna', '1', 'Disappointed', 'This came so bent up it wasn’t wearable...my 10 year old son was deeply disappointed.', '2018/10/27');
INSERT INTO `app01_detail` VALUES (10, 'B07GRSY8RG', '10', '4', 'Color: Black', 'Lester Knockercot', '5', 'Well crafted， high quality & sturdy.', 'Despite the relative high cost， this set is extremely well made and should hold up to the rigors of outdoor costume-play for several years.  Would have probably been cheaper purchasing not so close to Halloween， but despite that we\'re very satisfied customers.', '2018/10/23');

SET FOREIGN_KEY_CHECKS = 1;
