

CREATE DATABASE IF NOT EXISTS longze;
use longze;
DROP TABLE IF EXISTS job_details;
CREATE TABLE IF NOT EXISTS job_details(
	id INT NOT NULL AUTO_INCREMENT,
    department VARCHAR(30) NOT NULL  COMMENT '所属部门',
    title VARCHAR(30) NOT NULL COMMENT '岗位名称',
    salary INT NOT NULL COMMENT '薪资待遇',
    location VARCHAR(30) NOT NULL  COMMENT '工作地点',
    if_part_time TINYINT NOT NULL COMMENT '是否可兼职，1:可以，0:不可以',
    education_requirement VARCHAR(50) NOT NULL COMMENT '教育要求',
    experience_requirement VARCHAR(100) NOT NULL COMMENT '经验要求',
    skill_requirement VARCHAR(100) NOT NULL COMMENT '技能要求',
    job_description  VARCHAR(500) NOT NULL COMMENT '工作描述',
    job_pic_url  VARCHAR(50) NOT NULL COMMENT '岗位图片',
	created_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
	updated_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (id)
);


CREATE DATABASE IF NOT EXISTS longze;
use longze;
DROP TABLE IF EXISTS job_apply_details;
CREATE TABLE IF NOT EXISTS job_apply_details(
	id INT NOT NULL AUTO_INCREMENT COMMENT '申请人ID',
    name VARCHAR(30) NOT NULL COMMENT '申请人姓名',
    age INT NOT NULL COMMENT '申请人年龄',
    gender VARCHAR(30) NOT NULL COMMENT '申请人性别',
    phone VARCHAR(30) NOT NULL COMMENT '申请人电话',
    email VARCHAR(30) NOT NULL COMMENT '申请人邮箱',
    comment VARCHAR(30) NOT NULL COMMENT '申请人留言',
    job_id INT NOT NULL COMMENT '申请岗位ID',
    job_title VARCHAR(30) NOT NULL COMMENT '申请岗位名称',
    department VARCHAR(30) NOT NULL  COMMENT '申请岗位所属部门',
    location VARCHAR(30) NOT NULL  COMMENT '申请岗位工作地点',
    resume_url VARCHAR(100) NOT NULL  COMMENT '申请岗位简历地址',
	created_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '申请时间',
	updated_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '申请时间',
    PRIMARY KEY (id)
);



INSERT INTO job_details
    (department,title,salary,location,if_part_time,education_requirement,experience_requirement,skill_requirement,job_description,job_pic_url)
VALUES
    ('审计部','高级项目经理',3000,'福田,深圳',1,'大专以上','至少三年以上工作经验','注册会计师','在上级领导下，根据审计计划和审计范围，拟订审计计划方案;负责做好有关审计资料的原始调查的收集、整理、建档工作，按规定保守秘密和保护当事人合法权益;选择适当的审计方法进行现场审计，收集相关事实依据，形成审计工作底稿;提出相关审计意见 ;按照适当的审计程序和审计方法，收集相关事实依据，获取充分的审计证据，支持审计发现，形成审计 工作底稿; 提出相关审计发现和建议，为公司运营提供增值服务;编写相关审计小结或审计报告，确保审计证据支持审计目的;参与公司实施专项审计任务（包括但不限于采购审计、离任审计等）; 8、跟踪审计发现问题的整改落实情况;审计资料的档案整理;领导安排的其他工作;','../static/images/testmonials/author-01.png'),
    ('审计部','审计项目经理',2434,'福田,深圳',1,'本科以上','至少2年以上工作经验','注册会计师','在上级领导下，根据审计计划和审计范围，拟订审计计划方案;负责做好有关审计资料的原始调查的收集、整理、建档工作，按规定保守秘密和保护当事人合法权益;选择适当的审计方法进行现场审计，收集相关事实依据，形成审计工作底稿;提出相关审计意见 ;按照适当的审计程序和审计方法，收集相关事实依据，获取充分的审计证据，支持审计发现，形成审计 工作底稿; 提出相关审计发现和建议，为公司运营提供增值服务;编写相关审计小结或审计报告，确保审计证据支持审计目的;参与公司实施专项审计任务（包括但不限于采购审计、离任审计等）; 8、跟踪审计发现问题的整改落实情况;审计资料的档案整理;领导安排的其他工作;','../static/images/testmonials/author-01.png'),
    ('审计部','审计专员',2009,'福田,深圳',0,'本科以上','至少三年以上工作经验','注册会计师','在上级领导下，根据审计计划和审计范围，拟订审计计划方案;负责做好有关审计资料的原始调查的收集、整理、建档工作，按规定保守秘密和保护当事人合法权益;选择适当的审计方法进行现场审计，收集相关事实依据，形成审计工作底稿;提出相关审计意见 ;按照适当的审计程序和审计方法，收集相关事实依据，获取充分的审计证据，支持审计发现，形成审计 工作底稿; 提出相关审计发现和建议，为公司运营提供增值服务;编写相关审计小结或审计报告，确保审计证据支持审计目的;参与公司实施专项审计任务（包括但不限于采购审计、离任审计等）; 8、跟踪审计发现问题的整改落实情况;审计资料的档案整理;领导安排的其他工作;','../static/images/testmonials/author-01.png'),
    ('市场部','项目助理',9382,'福田,深圳',1,'本科以上','至少5年以上工作经验','注册会计师','在上级领导下，根据审计计划和审计范围，拟订审计计划方案;负责做好有关审计资料的原始调查的收集、整理、建档工作，按规定保守秘密和保护当事人合法权益;选择适当的审计方法进行现场审计，收集相关事实依据，形成审计工作底稿;提出相关审计意见 ;按照适当的审计程序和审计方法，收集相关事实依据，获取充分的审计证据，支持审计发现，形成审计 工作底稿; 提出相关审计发现和建议，为公司运营提供增值服务;编写相关审计小结或审计报告，确保审计证据支持审计目的;参与公司实施专项审计任务（包括但不限于采购审计、离任审计等）; 8、跟踪审计发现问题的整改落实情况;审计资料的档案整理;领导安排的其他工作;','../static/images/testmonials/author-01.png'),
    ('审计部','审计师',14000,'福田,深圳',0,'本科以上','至少三年以上工作经验','注册会计师','在上级领导下，根据审计计划和审计范围，拟订审计计划方案;负责做好有关审计资料的原始调查的收集、整理、建档工作，按规定保守秘密和保护当事人合法权益;选择适当的审计方法进行现场审计，收集相关事实依据，形成审计工作底稿;提出相关审计意见 ;按照适当的审计程序和审计方法，收集相关事实依据，获取充分的审计证据，支持审计发现，形成审计 工作底稿; 提出相关审计发现和建议，为公司运营提供增值服务;编写相关审计小结或审计报告，确保审计证据支持审计目的;参与公司实施专项审计任务（包括但不限于采购审计、离任审计等）; 8、跟踪审计发现问题的整改落实情况;审计资料的档案整理;领导安排的其他工作;','../static/images/testmonials/author-01.png')
;

select * from job_details;


